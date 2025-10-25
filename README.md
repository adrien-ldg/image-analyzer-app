# Application de détection d'objets YOLOv5

## Aperçu
Cette application Streamlit démontre comment utiliser un modèle YOLOv5 exporté au format ONNX pour détecter automatiquement des objets sur des images ou des flux vidéo en direct. Elle met à disposition une interface Web prête à l'emploi qui exploite un modèle pré-entraîné capable de reconnaître 20 catégories d'objets courantes (personnes, véhicules, animaux, mobilier, etc.).

## Fonctionnalités principales
- **Détection d'objets sur images** : téléchargez une image au format PNG ou JPEG et obtenez en un clic les détections et les cadres englobants générés par YOLOv5.
- **Analyse vidéo en direct** : activez votre webcam (ou toute autre source vidéo WebRTC) pour visualiser en direct les détections effectuées image par image.
- **20 classes prêtes à l'emploi** : le modèle est entraîné pour reconnaître les classes suivantes : `person`, `car`, `chair`, `bottle`, `pottedplant`, `bird`, `dog`, `sofa`, `bicycle`, `horse`, `boat`, `motorbike`, `cat`, `tvmonitor`, `cow`, `sheep`, `aeroplane`, `train`, `diningtable`, `bus`.
- **Inférence rapide sur CPU** : le modèle ONNX est exécuté via l'API DNN d'OpenCV, ce qui permet d'obtenir de bonnes performances sans GPU.

## Architecture de l'application
- **Interface multi-pages Streamlit** :
  - `app/Home.py` présente l'application et la liste des classes prises en charge.
  - `app/pages/1_YOLO_for_image.py` gère le téléversement et le traitement d'images.
  - `app/pages/2_YOLO_webrtc.py` met à disposition la diffusion WebRTC pour les flux vidéo.
  - `app/pages/3_About.py` (si présent) peut être adapté pour détailler votre projet.
- **Back-end d'inférence** : la classe `YOLO_Pred` de `app/yolo_predictions.py` charge le modèle ONNX, applique le pré-traitement (mise à l'échelle à 640×640), réalise la suppression non maximale (NMS) et renvoie l'image annotée avec les détections.
- **Ressources du modèle** : `app/models.zip` contient `models/best.onnx` (poids du modèle) et `models/data.yaml` (métadonnées des classes).

## Prérequis
- Python 3.9 ou supérieur (recommandé).
- Pip ou Conda pour gérer les dépendances Python.
- (Optionnel) Une webcam compatible pour tester la page WebRTC.

## Installation
1. **Cloner le dépôt** :
   ```bash
   git clone <URL-DU-DEPOT>
   cd image-analyzer-app
   ```
2. **Créer un environnement virtuel** (fortement recommandé) :
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sous Windows : .venv\Scripts\activate
   ```
3. **Installer les dépendances** :
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. **Extraire le modèle** :
   ```bash
   cd app
   unzip models.zip
   cd ..
   ```
   Cette étape crée le dossier `app/models/` contenant `best.onnx` et `data.yaml`, fichiers requis par les scripts Streamlit.

## Lancer l'application
Depuis la racine du projet (ou depuis le dossier `app/`), exécutez :
```bash
streamlit run app/Home.py
```
Streamlit ouvrira automatiquement l'application dans votre navigateur. Utilisez le menu latéral pour naviguer entre les pages « YOLO for image » et « YOLO WebRTC ».

## Utilisation
### 1. Détection sur image
1. Accédez à la page **YOLO for image**.
2. Téléversez une image `.png` ou `.jpg/.jpeg`. L'application vérifie le type MIME et affiche un aperçu.
3. Cliquez sur **Get Detection from YOLO** pour lancer l'inférence.
4. Les résultats s'affichent sous forme d'image annotée, accompagnés d'un récapitulatif des métadonnées du fichier.

### 2. Détection vidéo (WebRTC)
1. Accédez à la page **YOLO WebRTC**.
2. Autorisez l'accès à votre caméra si votre navigateur vous le demande.
3. Les prédictions sont effectuées en continu sur chaque image issue du flux vidéo, avec affichage direct dans la page.

## Détails du modèle
- **Architecture** : YOLOv5, exportée en ONNX pour une exécution légère via OpenCV.
- **Entrée** : images redimensionnées à 640×640 pixels.
- **Post-traitement** : seuil de confiance à 0,4, score de classe minimum à 0,25 et suppression non maximale (IoU 0,45) pour filtrer les doublons.
- **Classes** : voir la section « Fonctionnalités principales » ou `app/data.yaml`.

## Personnalisation
- **Ajouter de nouvelles classes** : ré-entraînez un modèle YOLOv5 avec vos données, exportez-le en ONNX et remplacez `app/models/best.onnx` ainsi que `app/models/data.yaml` par vos fichiers.
- **Modifier les seuils** : ajustez les valeurs de confiance (`0.4`) et de score (`0.25`) dans `YOLO_Pred.predictions` pour adapter la sensibilité.
- **Changer l'apparence** : éditez les fichiers Streamlit (`Home.py`, `pages/*.py`) pour personnaliser les textes, les icônes et la mise en page.

## Dépannage
- **Erreur « fichier introuvable » pour `best.onnx`** : assurez-vous d'avoir extrait `app/models.zip` et que le dossier `app/models/` contient bien les fichiers nécessaires.
- **Flux WebRTC indisponible** : vérifiez que votre navigateur autorise l'accès à la caméra et que votre appareil n'est pas déjà utilisé par une autre application.
- **Performances lentes** : réduisez la taille des images en entrée ou exécutez l'application sur une machine plus puissante.

## Ressources supplémentaires
- Notebooks `01_extract_text_from_xml.ipynb` et `yolo_training.ipynb` : exemples de préparation de données et d'entraînement YOLOv5.
- Documentation Streamlit : <https://docs.streamlit.io/>
- Documentation YOLOv5 : <https://github.com/ultralytics/yolov5>

Bonnes détections !
