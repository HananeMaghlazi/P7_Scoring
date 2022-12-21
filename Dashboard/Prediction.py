import streamlit as st
import pickle
import dill
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import json
from pandas import DataFrame
import shap
from PIL import Image

# Configuration de la page

st.set_page_config(
	page_title="Loan Prediction App",
	page_icon="loan.png"
)

st.set_option('deprecation.showPyplotGlobalUse', False)

######################
#main page layout
######################
#title and subheader to the page
st.title("Loan Default Prediction")
st.subheader("Cette application d'apprentissage automatique vous aidera à faire une prédiction pour vous aider dans votre décision ")

# split the main page into two columns (col1 and col2)
col1, col2 = st.columns([1, 1])


with col1:
	logo = Image.open("https://raw.githubusercontent.com/HananeMaghlazi/P7_Scoring/main/Dashboard/loan.png")
	st.image(logo)
	#st.image("loan.png")

with col2: 
	st.write("""Pour emprunter de l'argent, une analyse de crédit est effectuée. L'analyse de crédit implique la mesure d'enquêter sur la probabilité que le demandeur rembourse le prêt à temps et de prédire son défaut/non-remboursement.
Ces défis se compliquent à mesure que le nombre de demandes qui sont examinées par les agents de crédit augmente.""")

#URL_local = "http://localhost:5000/"
URL="http://ec2-63-35-250-122.eu-west-1.compute.amazonaws.com:9192/"

#Récupération de la liste des identifiants de l'API Flask

data_json = requests.get(URL+"load_data")
data = data_json.json()

Identifiant = st.sidebar.selectbox("Selectionner un identifiant client: ", data)


######################
#sidebar layout
######################

st.sidebar.title("Loan Applicant Info")
im = Image.open("./ab.png") 

st.sidebar.image(im, width=200)


# Test radio
data = requests.get(URL+"display_data", params={"Identifiant": Identifiant}).json()
action = st.sidebar.radio(
	"Choisissez ce que vous voulez faire",
	('Home','Informations du client', 'Autre informations', 'Informations de tous les clients'))

if action=='Home':

	st.subheader("Pour afficher les informations du client, vous devez suivre les étapes ci-dessous :")
	st.markdown("""
1. Entrez l'identifiant du client;
2. Sélectionnez  "Informations client" et attendez le résultat.
""")
	st.subheader("Pour prévoir le statut de défaut/échec de remboursement, vous devez suivre les étapes ci-dessous :")
	st.markdown("""
1. Entrez l'identifiant du client;
2. Sélectionnez "Prédiction" et attendez le résultat.
""")
	st.markdown("""Si vous voulez plus d'informations sur le client vous pouvez sélectionner "Autre informations" """)
	st.subheader("Ci-dessous, vous pouvez trouver le résultat de la prédiction ")

if action == 'Informations du client':

	st.write("**L'identifiant du client :** " , data[0][0])
	st.write("**Le genre du client :**" , data[0][1])
	st.write("**Le statut familial du client :** " , data[0][2])
	st.write("**L'âge du client :**", int(data[0][3]),"ans")
	st.write("**Nombre d'enfants du client:**" , data[0][4])
	st.write("**Type du prêt du client:**" , data[0][5])
	st.write("**Revenu du client:**" , data[0][6])
	st.write("**Montant du crédit de l'emprunt :**" , data[0][7])
	st.write("**Annuité du prêt :** " , data[0][8])
	st.write("**Expérience du client :**" , int(data[0][12]))
	
if action =='Autre informations' :
	st.write("**L'identifiant du client :** " , data[0][0])
	st.write("**Le genre du client :**" , data[0][1])
	st.write("**Le statut familial du client :** " , data[0][2])
	st.write("**L'âge du client :**", int(data[0][3]),"ans")
	st.write("**Nombre d'enfants du client:**" , data[0][4])
	st.write("**Type du prêt du client:**" , data[0][5])
	st.write("**Revenu du client:**" , data[0][6])
	st.write("**Montant du crédit de l'emprunt :**" , data[0][7])
	st.write("**Annuité du prêt :** " , data[0][8])
	st.write("**Type de revenu du client :**" , data[0][9])
	st.write("**Niveau d'éducation le plus élevé du client :**" , data[0][10])
	st.write("**Expérience du client :**" , int(data[0][12]),"ans")
	st.write("**La Profession du client :** " , data[0][13])
	st.write("**Type d'organisation où le client travaille :**" , data[0][14])

if action =='Informations de tous les clients' :
	display_json=requests.get("http://ec2-63-35-250-122.eu-west-1.compute.amazonaws.com:9192/display_data_all")
	content = json.loads(display_json.content.decode('utf-8'))
	infos_client = pd.DataFrame(content).transpose()
	st.write(infos_client)
	

# prediction
@st.cache
def load_prediction():
	# Récupérer la prédiction
	prediction = requests.get(URL+"predict",params={"Identifiant": Identifiant}).json()

	return prediction

# shap
@st.cache
def load_shap():
	# Récupérer shap values
	shap_values = requests.get(URL+"shaploan",params={"Identifiant": Identifiant}).json() 
	shap_values_df = pd.DataFrame(shap_values)
	return shap_values_df
	

# shap explainer
@st.cache
def load_explainer():
	with open('./explainer_w.pkl', 'rb') as f:
		explainer = dill.load(f)
		
	return explainer

explainer=load_explainer()

X_test_sample = pd.read_csv('./X_test_sample.csv',index_col="SK_ID_CURR")

#predict button and shap individuel

btn_predict = st.sidebar.button("Prediction")
if btn_predict:
	
	st.subheader("Le résultat de la prédiction est : ")
	prediction=load_prediction()
	st.write(" **La probabilité est :** {:.0%} ".format(round(float(prediction[0]), 2))) 
	st.write("**Le résultat indique la probalité du défaut de paiement** ")

	# Shap client
	shap.initjs()

	shap_values_df=load_shap()

	st.subheader('Interprétabilité des résultats - Niveau client')
	
	fig, ax = plt.subplots(nrows=1, ncols=1)   
	
	shap.plots._waterfall.waterfall_legacy(explainer.expected_value, shap_values_df.iloc[0,:788],feature_names = X_test_sample.columns,max_display=10) 

	st.pyplot(fig)

# Graphiques
sample = pd.read_csv('./sample.csv')

def plot_var(data, var, title) : 
	ax, fig = plt.subplots(figsize=(20,8)) 
	ax = sns.countplot(y=var, data=data, order=data[var].value_counts(ascending=False).index)
	ax.set_title(title)

	for p in ax.patches:
				percentage = '{:.1f}%'.format(100 * p.get_width()/len(data[var]))
				x = p.get_x() + p.get_width()
				y = p.get_y() + p.get_height()/2
				ax.annotate(percentage, (x, y), fontsize=20, fontweight='bold')
#               
check =st.sidebar.checkbox("Visualisation des variables")
check_clt =st.sidebar.checkbox("Comparaison avec d'autres clients ")

df_display=pd.read_csv('./display.csv',index_col="SK_ID_CURR")
if check:
	st.write("#### Select column to visualize: ")
	df_display=df_display.iloc[:,0:10]
	columns = df_display.columns.tolist()
	
	column_name = st.selectbox("",columns)
	
	if column_name=="CODE_GENDER":
		plot_var(df_display, "CODE_GENDER", "Distribution du genre")
		st.pyplot()
		st.write("**Le client est :**",data[0][1])
		
	if column_name=="NAME_FAMILY_STATUS":
		plot_var(df_display, "NAME_FAMILY_STATUS", "Statut familial")
		st.pyplot()
		st.write("**Le client est :**",data[0][2])
	if column_name=="NAME_CONTRACT_TYPE":
		plot_var(df_display, "NAME_CONTRACT_TYPE", "Type de contrat")
		st.pyplot() 
		st.write("**Le client est :**",data[0][5])
	if column_name=="NAME_INCOME_TYPE":
		plot_var(df_display, "NAME_INCOME_TYPE", "Revenu client")
		st.pyplot()     
		st.write("**Le client est :**",data[0][9])
	if column_name=="NAME_EDUCATION_TYPE":
		plot_var(df_display, "NAME_EDUCATION_TYPE", "Niveau études")
		st.pyplot()  
		st.write("**Le client est :**",data[0][10])
	if column_name=="DAYS_BIRTH":
		sns.histplot(data=df_display, x=df_display["DAYS_BIRTH"])
		plt.axvline(data[0][3], color="k", linestyle="--")
		st.pyplot()
	if column_name=="CNT_CHILDREN":
		plot_var(df_display, "CNT_CHILDREN", "Nombre d'enfants")
		st.pyplot()
		st.write("**Le client est :**",data[0][4])
	if column_name=="AMT_INCOME_TOTAL":
		sns.histplot(data=df_display, x=df_display["AMT_INCOME_TOTAL"])
		plt.axvline(data[0][6], color="k", linestyle="--")
		st.pyplot()
	if column_name=="AMT_CREDIT":
		sns.histplot(data=df_display, x=df_display["AMT_CREDIT"])
		plt.axvline(data[0][7], color="k", linestyle="--")
		st.pyplot()
	if column_name=="AMT_ANNUITY":
		sns.histplot(data=df_display, x=df_display["AMT_ANNUITY"])
		plt.axvline(data[0][8], color="k", linestyle="--")
		st.pyplot()
			
if check_clt:
   
	if st.button("Generate"):
		for col in sample.iloc[:,2:8]:
			st.write(sns.histplot(data=sample, x=sample[col], hue="TARGET", multiple="stack"))
			
			st.pyplot()

