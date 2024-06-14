# GreenGuardiansGW

## Smart Bin : Ne réfléchissez plus, laissez Smart Bin le faire pour vous !

La "Smart Bin", une poubelle intelligente qui trie les déchets pour nous ! Le but est simple, mettre un déchet dans le conteneur, le déchet est traité par une IA qui après analyse, dirige le déchet vers le bon bac de tri.

## Lancement du programme :

Pour exécuter le programme, lancez `Socket.py` et laissez la Raspberry Pi se connecter à votre réseau. Appuyez sur le bouton poussoir pour que la détection se fasse.
```bash
python3 ./Raspberrypi/Socket.py
```
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


### Description des répertoires et fichiers :

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

## Auteurs :

- Leroux Théo, Morroni Alexandre, Bouhaben Sean, Schneider Bastien et Montanari Charlotte
- GreenGuardians
- 2024


## Installation des dépendances
Assurez-vous d'avoir toutes les dépendances installées en utilisant le fichier `requirements.txt`.

```bash
pip install -r requirements.txt
