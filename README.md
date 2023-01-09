# P7_Scoring :  Implémentez un modèle de scoring


L’entreprise souhaite mettre en
œuvre un outil de “scoring crédit”
pour calculer la probabilité qu’un
client rembourse son crédit, puis
classifie la demande en crédit accordé
ou refusé. Elle souhaite donc
développer un algorithme de
classification en s’appuyant sur des
sources de données variées (données
comportementales, données provenant
d'autres institutions financières, etc.)

Prêt à dépenser décide donc de développer un dashboard interactif pour que les
chargés de relation client puissent à la fois expliquer de façon la plus transparente
possible les décisions d’octroi de crédit, mais également permettre à leurs clients de
disposer de leurs informations personnelles et de les explorer facilement.

Le dashboard permet de :
Visualiser le score et l’interprétation de ce score pour chaque client de
façon intelligible pour une personne non experte en data science.
Visualiser des informations descriptives relatives à un client (via un
système de filtre).
Comparer les informations descriptives relatives à un client à
l’ensemble des clients ou à un groupe de clients similaires.

Le projet a été réalisé en local sur google colab, Python 3.8 et les packages necessaires ( NumPy, Pandas, MatPlotLib, Seaborn, Scikit-Learn, catboostclassifier,shap).

- La réalisation de ce projet a été faite en 3 étapes : analyse de données,modélisation et la réalisation du dashboard.
- Le projet a été réalisé en local et puis déployé dans le cloud.
## Préparation des  données : 

Le feature engineering a été faite avec le kernel fourni de kaggle : 
https://www.kaggle.com/code/jsaguiar/lightgbm-with-simple-features/script

## Modélisation des  données :

Pour ce projet plusieurs algorithmes ont été testés : Regression logistique,RandomForest,GradientBoosting,Xgboost et Catboostclassifier.

Le Catboostclassifier a donné les meilleures performances et sera donc le modèle retenu.
L’entreprise Prêt à dépenser est une société financière qui propose des crédits et donc essayera de lutter contre les défauts de paiement et diminuer les pertes financières.Pour ceci nous créons une fonction coût métier implémenté par une matrice de confusion, mais au lieu de mettre les quantités prévues, nous allons mettre des pondérations pour chaque élément de la matrice.


## Réalisation du dashboard :

Le dashbord a été réalisé en deux parties:

Front-End : Streamlit
Back-End : Flask

## Déploiement dans le cloud:

Front-End : Streamlit cloud
Back-End : AWS

### Lien du dashboard interactif : 

https://hananemaghlazi-p7-scoring-dashboardprediction-juf752.streamlit.app/


