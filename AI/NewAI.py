import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

class NeuroneConvolutionnel:
    def __init__(self, input_shape, num_classes):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.InputLayer(input_shape=self.input_shape),
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(self.num_classes, activation='softmax')
        ])
        model.compile(optimizer='adam',
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                      metrics=['accuracy'])
        return model

    def apprentissage(self, train_generator, epochs=5):
        self.model.fit(train_generator, epochs=epochs)

    def tester(self, test_generator):
        test_loss, test_acc = self.model.evaluate(test_generator, verbose=2)
        print(f"Pourcentage de réussite : {test_acc * 100}%")

    def sauvegarder_modele(self, chemin):
        self.model.save(chemin)

    def predire(self, image_path):
        # Charger et prétraiter l'image
        image = load_img(image_path, target_size=(self.input_shape[0], self.input_shape[1]))
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0) / 255.0

        # Effectuer la prédiction
        predictions = self.model.predict(image)
        predicted_class = np.argmax(predictions, axis=1)

        return predicted_class[0]

def main():
    save_file = './GreenGuardiansGW/AI/Model.keras'
    train_dir = './GreenGuardiansGW/AI/Dataset/Train'
    test_dir = './GreenGuardiansGW/AI/Dataset/Validation'

    # Paramètres pour le traitement des images
    batch_size = 32
    img_height, img_width = 28, 28  # Redimensionnement des images
    num_classes = 10  # Nombre de classes à prédire

    # Utilisation de ImageDataGenerator pour charger et prétraiter les images
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True
    )

    test_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='sparse'
    )

    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='sparse'
    )

    if os.path.exists(save_file):
        modele_charge = tf.keras.models.load_model(save_file)
        modele_charge.summary()
        n = NeuroneConvolutionnel(input_shape=(img_height, img_width, 3), num_classes=num_classes)
        n.model = modele_charge
    else:
        n = NeuroneConvolutionnel(input_shape=(img_height, img_width, 3), num_classes=num_classes)
        print("Apprentissage...")
        n.apprentissage(train_generator, epochs=5)
        # Sauvegarde du modèle après l'apprentissage
        n.sauvegarder_modele(save_file)
        print(f"Modèle sauvegardé dans {save_file}")

    print("Test...")
    n.tester(test_generator)

    # Exécution d'une prédiction sur une image d'exemple
    image_path = './GreenGuardiansGW/AI/Dataset/Train/carton/carton.jpg'  # Remplacez par le chemin de votre image
    predicted_class = n.predire(image_path)
    print(f"Classe prédite pour l'image {image_path} : {predicted_class}")
    return predicted_class


def startAI() :
    return main()
