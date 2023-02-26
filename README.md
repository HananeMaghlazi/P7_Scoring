# P7_Scoring :  Implémentez un modèle de scoring

#### Enoncé : 

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

#### Mission:

• Construire un modèle de scoring qui donnera une prédiction sur la probabilité de faillite d'un client de façon automatique.
• Construire un Dashboard interactif à destination des gestionnaires de la relation client permettant d'interpréter les prédictions faites par le modèle, et d’améliorer la connaissance client des chargés de relation client.
• Mettre en production le modèle de scoring de prédiction à l’aide d’une API, ainsi que le Dashboard interactif qui appelle l’API pour les prédictions

#### Préparation des  données : 

Le feature engineering a été faite avec le kernel fourni de kaggle : 
https://www.kaggle.com/code/jsaguiar/lightgbm-with-simple-features/script

#### Livrables :

- L’application de dashboard interactif répondant aux spécifications ci-dessus et l’API de prédiction du score, déployées chacunes sur le cloud.
- Un dossier, géré via un outil de versioning de code contenant :
- Le notebook ou code de la modélisation (du prétraitement à la prédiction), intégrant via MLFlow le tracking d’expérimentations et le stockage centralisé des modèles
- Le code générant le dashboard
- Le code permettant de déployer le modèle sous forme d'API
- Pour les applications dashboard et API, un fichier introductif permettant de comprendre l'objectif du projet et le découpage des dossiers, et un fichier listant les packages utilisés seront présents dans les dossiers
- Une note méthodologique décrivant :

  La méthodologie d'entraînement du modèle (2 pages maximum)
  
  Le traitement du déséquilibre des classes (1 page maximum)
  
  La fonction coût métier, l'algorithme d'optimisation et la métrique d'évaluation (1 page maximum)
  
  Un tableau de synthèse des résultats (1 page maximum)
  
  L’interprétabilité globale et locale du modèle (1 page maximum)
  
  Les limites et les améliorations possibles (1 page maximum)
  
- Un support de présentation

#### Compétences évaluées : 

Réaliser un dashboard pour présenter son travail de modélisation

Évaluer les performances des modèles d’apprentissage supervisé selon différents critères

Utiliser un logiciel de version de code pour assurer l’intégration du modèle

Définir et mettre en œuvre un pipeline d’entraînement des modèles

Définir la stratégie d’élaboration d’un modèle d’apprentissage supervisé

Déployer un modèle via une API dans le Web

Définir et mettre en œuvre une stratégie de suivi de la performance d’un modèle

Rédiger une note méthodologique afin de communiquer sa démarche de modélisation

#### Réalisation du dashboard :

Le dashbord a été réalisé en deux parties:

- Front-End : Streamlit
- Back-End : Flask

#### Déploiement dans le cloud:

- Front-End : Streamlit cloud
- Back-End : AWS (EC2)

#### Lien du dashboard interactif : 

https://hananemaghlazi-p7-scoring-dashboardprediction-juf752.streamlit.app/


