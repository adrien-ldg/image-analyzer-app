# Classification de la gravité des accidents routiers (Kaggle)

## 🎯 Contexte
Projet mené lors d'une compétition Kaggle visant à prédire la gravité d'accidents en France. Le jeu de données comportait plus de quarante variables hétérogènes (météo, contexte routier, véhicule, usager, etc.) qu'il a fallu rendre exploitables avant d'entraîner plusieurs modèles de Machine Learning et Deep Learning.

## 🚀 Comment rejouer le projet
Téléchargez le jeu de données Kaggle « Gravité des accidents » (mêmes fichiers utilisés pour la compétition) et placez-le à la racine du projet ou adaptez les chemins dans les notebooks. Créez ensuite un environnement virtuel et installez les dépendances à partir du `requirements.txt`, qui inclut Jupyter, pandas, scikit-learn et les bibliothèques nécessaires à la reproduction des notebooks :
```bash
python -m venv .venv
source .venv/bin/activate  # Sous Windows : .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```
Lancez Jupyter puis ouvrez les notebooks :
```bash
jupyter notebook
```
Ouvrez `notebook_feature_adrien_lindeberg.ipynb` pour le pipeline de feature engineering, puis `notebook_remis.ipynb` ou `notebook_model_adrien_lindeberg.ipynb` pour l'entraînement et la comparaison des modèles de prédiction.

## 🛠️ Étapes de feature engineering (notebook_feature_adrien_lindeberg.ipynb)
La préparation des données commence par un nettoyage et un typage rigoureux : les formats de dates, de catégories et de variables numériques sont harmonisés, et les valeurs manquantes sont traitées pour éliminer les incohérences. Les variables catégorielles sont ensuite encodées en représentations numériques (one-hot ou binaires) afin de rendre les attributs qualitatifs directement exploitables par les modèles. Les variables continues sont standardisées pour équilibrer l'influence de chaque feature dans les algorithmes sensibles aux échelles. Une phase de réduction de dimensionnalité suit : colonnes redondantes, à faible variance ou fortement corrélées sont supprimées ou regroupées, ce qui permet de passer d'un peu plus de quarante colonnes à une vingtaine de variables pertinentes. Enfin, un découpage train/validation est appliqué pour évaluer la généralisation avant l'entraînement définitif.

## 🤖 Modèles de prédiction (notebook_remis.ipynb ou notebook_model_adrien_lindeberg.ipynb)
La phase de modélisation explore plusieurs familles d'algorithmes supervisés. Des arbres de décision et des approches de bagging servent de premiers repères grâce à leur interprétabilité. Des forêts aléatoires et d'autres méthodes d'ensemble sont ensuite évaluées pour mesurer le gain en robustesse. Les méthodes de boosting (Gradient Boosting/XGBoost) sont testées pour leur capacité à capturer des interactions fines, tandis que des réseaux de neurones simples offrent un point de comparaison avec des architectures plus flexibles. Au terme des essais, le modèle de **boosting** fournit la meilleure performance sur l'ensemble de validation et constitue le résultat final retenu.

## ✅ Résultat final et conclusion
Le pipeline complet (feature engineering + boosting) délivre les prédictions les plus stables et performantes parmi les modèles testés. La réduction de dimensionnalité a simplifié l'espace de recherche sans perte notable d'information, aboutissant à des résultats concluants pour la compétition.
