#!/usr/bin/python3
# -*-coding:Latin-1 -*

from flask import Flask, jsonify, request, jsonify, render_template
import json
import pickle
import pandas as pd
import numpy as np
from catboost import CatBoostClassifier
from functions import function_cost
from pandas import DataFrame
import shap
import dill


app = Flask(__name__)


# reading the data in the csv file
df = pd.read_csv('/Users/hananemaghlazi/Projet7/Back_end/data_pred.csv')
df_display=pd.read_csv('/Users/hananemaghlazi/Projet7/Back_end/display.csv')


# model
def load_model():
	with open('/Users/hananemaghlazi/Projet7/Back_end/model_catboost_w.pkl','rb') as file:
		model=pickle.load(file)
	return model

model=load_model()  
  
# index
@app.route('/')
def loaded():
	
	return "API de prédiction"



# On crée la liste des ID clients qui nous servira dans l'API
Identifiant = df_display["SK_ID_CURR"].astype('int')


# Chargement des données pour la selection de l'ID client
@app.route("/load_data", methods=["GET"])
def load_data():
	
	return Identifiant.to_json(orient="values")

# Afficher tous les clients

@app.route("/display_data_all", methods=["GET"])
def display_data_all():

	data_display = df_display[df_display['SK_ID_CURR']==(Identifiant)]
	output=data_display.to_json(orient="index")

	return output


# Afficher les données relatives à un client

@app.route("/display_data", methods=["GET"])
def display_data():

	
	Identifiant_clt=(request.args.get("Identifiant"))
	data = df_display[df_display["SK_ID_CURR"]== int(Identifiant_clt)]
	data=data.values.tolist()
	return jsonify(data)

# Prediction
@app.route("/predict", methods=["GET"])
def predict():
	
	
	Identifiant_clt=(request.args.get("Identifiant"))
	data_pred = df[df["SK_ID_CURR"]== int(Identifiant_clt)]
	prediction = model.predict_proba(data_pred.iloc[:,0:788])[:, 1]
	prediction = prediction.tolist()


	return jsonify(prediction)

# shap


# shap values
def load_shap():
	with open('/Users/hananemaghlazi/Projet7/Back_end/shap_values_df.pkl', 'rb') as f:
		shap_values = dill.load(f)
		
	return shap_values



@app.route("/shaploan", methods=["GET"])
def shaploan():

	shap_values=load_shap()
	Identifiant_clt=(request.args.get("Identifiant"))
	shap_values = shap_values[shap_values.SK_ID_CURR == int(Identifiant_clt)]
	
	return shap_values.to_json(orient="values")

if __name__ == "__main__":
	#app.run(debug=True) local
	app.run(host='0.0.0.0', port=9192 , debug=True)

