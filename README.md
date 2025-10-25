# 🧠 Application de détection d'objets YOLOv5

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-DNN-green?logo=opencv)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-pink)](https://github.com/adrien-ldg)

---

## 📸 Aperçu

Cette application **Streamlit** permet de détecter automatiquement des objets sur des images ou des flux vidéo en direct.
Elle propose une interface web prête à l'emploi, reposant sur un modèle **YOLOv5 exporté au format ONNX** et capable de reconnaître vingt catégories d'objets courantes, comme les personnes, les véhicules, les animaux ou encore le mobilier domestique.
L'exécution s'appuie sur l'API **DNN d'OpenCV**, garantissant des performances rapides même sur CPU, sans besoin de GPU.

---

## ⚙️ Fonctionnalités principales

L'utilisateur peut téléverser une image au format **PNG ou JPEG** et obtenir en un clic les détections et cadres englobants générés par le modèle.
Il est également possible d'activer une **analyse vidéo en direct via la webcam**, grâce à une intégration WebRTC fluide, permettant de visualiser en temps réel les prédictions effectuées image par image.

Le modèle utilisé a été entraîné pour reconnaître vingt classes d'objets parmi les plus fréquentes :
**person, car, chair, bottle, pottedplant, bird, dog, sofa, bicycle, horse, boat, motorbike, cat, tvmonitor, cow, sheep, aeroplane, train, diningtable et bus**.

---

## 🏠 Architecture de l'application

L'application est structurée autour d'une interface **multi-pages Streamlit**.
Le fichier `Home.py` présente la page d'accueil et les classes reconnues par le modèle.
Les scripts `pages/1_YOLO_for_image.py` et `pages/2_YOLO_webrtc.py` gèrent respectivement l'analyse d'images et la diffusion vidéo via WebRTC.
Une page `3_About.py` peut être ajoutée pour détailler davantage le projet.

Le back-end d'inférence repose sur la classe `YOLO_Pred` définie dans `yolo_predictions.py`.
Cette classe charge le modèle ONNX, applique les étapes de prétraitement (redimensionnement à **640×640**), effectue la prédiction, applique la suppression non maximale (**NMS**) et renvoie l'image annotée avec les détections.

Les ressources du modèle sont regroupées dans l'archive `models.zip`, qui contient le fichier `best.onnx` (poids du modèle) ainsi que `data.yaml` (métadonnées des classes).

---

## 💻 Prérequis

L'application nécessite **Python 3.9 ou une version ultérieure**, ainsi qu'un gestionnaire de paquets comme **Pip** ou **Conda**.
Une webcam compatible est facultative mais recommandée pour tester la page WebRTC.

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/adrien-ldg/image-analyzer-app.git
cd image-analyzer-app
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
source .venv/bin/activate  # Sous Windows : .venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Extraire le modèle

```bash
cd app
unzip models.zip
cd ..
```

Cette opération crée le dossier `app/models/` contenant les fichiers `best.onnx` et `data.yaml` indispensables à l'exécution du modèle.

---

## 🧩 Lancer l'application

Depuis la racine du projet (ou le dossier `app/`), exécutez :

```bash
streamlit run app/Home.py
```

Streamlit ouvrira automatiquement l'application dans votre navigateur par défaut.
Vous pourrez ensuite naviguer entre les pages **« YOLO for image »** et **« YOLO WebRTC »** via le menu latéral.

---

## 🎯 Utilisation

Sur la page **YOLO for image**, téléversez une image au format `.png` ou `.jpg/.jpeg`.
L'application affichera un aperçu, puis vous pourrez lancer la détection pour obtenir l'image annotée et les métadonnées correspondantes.

Sur la page **YOLO WebRTC**, activez votre caméra lorsque le navigateur le demande.
L'application effectuera alors les prédictions en continu sur le flux vidéo, avec un affichage instantané dans la page.

---

## 🧬 Détails du modèle

Le modèle utilisé est une architecture **YOLOv5** exportée en **ONNX** pour une exécution optimisée sur CPU via OpenCV.
Les images sont redimensionnées à **640×640 pixels** avant traitement.
Le post-traitement applique un **seuil de confiance à 0.4**, un **score minimal à 0.25** et une **suppression non maximale (IoU = 0.45)** afin de filtrer les doublons et d'obtenir des détections précises.

---

## 🧩 Personnalisation

L'application peut être adaptée facilement.
Pour ajouter de nouvelles classes, il suffit de réentraîner un modèle YOLOv5 sur vos propres données, de l'exporter en ONNX et de remplacer les fichiers `best.onnx` et `data.yaml` dans le dossier `app/models/`.

Les seuils de confiance et de score peuvent être ajustés directement dans la méthode `predictions` de la classe `YOLO_Pred`, afin d'adapter la sensibilité du modèle.
Vous pouvez également modifier les fichiers Streamlit (`Home.py` et `pages/*.py`) pour personnaliser l'apparence, les textes et les icônes.

---

## 🛠️ Dépannage

Si une erreur indique que le fichier `best.onnx` est introuvable, vérifiez que vous avez bien extrait `app/models.zip` et que le dossier `models` contient les fichiers nécessaires.

En cas d'indisponibilité du flux WebRTC, assurez-vous que votre navigateur autorise l'accès à la caméra et qu'aucune autre application ne l'utilise simultanément.

Pour améliorer les performances, vous pouvez réduire la taille des images en entrée ou exécuter le projet sur une machine plus puissante.

---

## 📚 Ressources supplémentaires

Deux notebooks, `01_extract_text_from_xml.ipynb` et `yolo_training.ipynb`, illustrent respectivement la préparation des données et l'entraînement d'un modèle YOLOv5.

Pour plus de détails techniques, consultez la [documentation Streamlit](https://docs.streamlit.io/) et la [documentation officielle de YOLOv5](https://github.com/ultralytics/yolov5).


Projet personnel — Application de détection d'objets basée sur YOLOv5 et Streamlit.
[GitHub @adrien-ldg](https://github.com/adrien-ldg)
