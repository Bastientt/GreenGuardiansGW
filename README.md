# GreenGuardiansGW  

## Smart Bin : Ne réfléchissez plus, laissez Smart Bin le faire pour vous !

### La "Smart Bin" est une poubelle intelligente qui trie les déchets pour vous ! Le principe est simple : mettez un déchet dans le conteneur, et l'IA analyse le déchet pour le diriger vers le bon bac de tri.

## Lancement du programme
Pour exécuter le programme, suivez les étapes ci-dessous :

1. **Connexion de la Raspberry Pi** :
   - Connectez votre Raspberry Pi à votre réseau.

2. **Exécution du script principal** :
   - Lancez `Socket.py`.
   - Appuyez sur le bouton poussoir pour initier la détection et le tri des déchets.

## Arborescence
Voici la structure du projet pour vous aider à comprendre l'organisation des fichiers :



## Arborescence : 
### GreenGuardiansGW/
### │
### ├── AI/
### │   ├── Dataset/
### │   │   ├── Train/
### │   │   └── Validation/
### │   ├── Model.keras
### │   ├── NewAI.py
### │   └── OldAI.py
### │
### ├── Hardware/
### │   ├── sensor.py
### │   ├── actuator.py
### │   └── camera.py
### │
### ├── Socket.py
### ├── README.md
### └── requirements.txt

- **AI/** : Contient tout ce qui est relatif à l'intelligence artificielle.
  - **Dataset/** : Contient les sous-dossiers pour l'entraînement et la validation des images.
  - **Model.keras** : Le modèle entraîné de l'IA.
  - **NewAI.py** : Le script principal pour l'entraînement et le test de l'IA.
  - **OldAI.py** : Ancienne version ou autre version de l'IA.

- **Hardware/** : Contient les scripts relatifs au matériel (capteurs, actionneurs, caméra).
  - **sensor.py** : Script pour gérer les capteurs.
  - **actuator.py** : Script pour gérer les actionneurs.
  - **camera.py** : Script pour gérer la caméra.

- **Socket.py** : Le script principal pour lancer le programme.
- **README.md** : Ce fichier d'instructions.
- **requirements.txt** : Liste des dépendances nécessaires pour exécuter le projet.

## Installation des dépendances
Assurez-vous d'avoir toutes les dépendances installées en utilisant le fichier `requirements.txt`.

```bash
pip install -r requirements.txt
