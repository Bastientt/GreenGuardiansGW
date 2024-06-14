import tensorflow as tf
import numpy as np
import cv2
import os


def startSearch(image_path) :
    # Désactiver les messages de journalisation de TensorFlow
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

    # Charger le modèle pré-entraîné MobileNetV2 avec des poids entraînés sur ImageNet
    model = tf.keras.applications.MobileNetV2(weights="imagenet")

    # Charger l'image à analyser
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Image non trouvée au chemin: {image_path}")
    except Exception as e:
        print(f"Erreur lors du chargement de l'image: {e}")
        exit(1)

    # Prétraiter l'image
    try:
        resized = cv2.resize(image, (224, 224))
        resized = tf.keras.preprocessing.image.img_to_array(resized)
        resized = tf.keras.applications.mobilenet_v2.preprocess_input(resized)
        resized = np.expand_dims(resized, axis=0)
    except Exception as e:
        print(f"Erreur lors du prétraitement de l'image: {e}")
        exit(1)

    # Faire une prédiction
    try:
        predictions = model.predict(resized)
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)
    except Exception as e:
        print(f"Erreur lors de la prédiction: {e}")
        exit(1)

    # Définir les labels cibles
    target_labels = {
        "cannette": ["can", "beer_glass", "soda_can", "crushed_can", "scrap"],
        "bouteille en verre": ["wine_bottle", "beer_bottle", "glass_bottle"],
        "carton": ["carton", "cardboard", "box", "packet", "mailbag"],
    }

    # Vérifier les prédictions et déterminer le type d'objet
    detected_type = "inconnu"
    for _, label, score in decoded_predictions[0]:
        for object_type, labels in target_labels.items():
            if label in labels:
                detected_type = object_type
                break
        if detected_type != "inconnu":
            break

    # Afficher le résultat
    if detected_type == "cannette":
        return 0
    elif detected_type == "bouteille en verre":
        return 1
    elif detected_type == "carton":
        return 2
    else : 
        return -1
    