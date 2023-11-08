import os
import face_recognition
import pickle

# === LECTURE DES IMAGES === #

# Obtenez le répertoire courant
dossier_courant = os.path.dirname(__file__)  # Si vous exécutez le script depuis le dossier contenant les images

# Chemin relatif vers le dossier contenant les images
dossier_images = "images/"

# Créez le chemin complet en joignant le répertoire courant et le chemin relatif
chemin_complet_dossier_images = os.path.join(dossier_courant, dossier_images)

nombre_images = 0

# Parcourez le dossier et lisez les images
for nom_fichier in os.listdir(chemin_complet_dossier_images):
    chemin_complet = os.path.join(chemin_complet_dossier_images, nom_fichier)

    # Vérifiez si le fichier est une image (vous pouvez ajuster les extensions selon vos besoins)
    if nom_fichier.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        try:
            nombre_images = nombre_images + 1
        except Exception as e:
            print(f"Erreur lors de la lecture de {chemin_complet}: {str(e)}")

# Affichez le nombre d'images chargées
print(f"Nombre d'images disponibles : {nombre_images}")

# Liste pour stocker les images
images = []
images_names = []

index = 1
for nom_fichier in os.listdir(chemin_complet_dossier_images):
    chemin_complet = os.path.join(chemin_complet_dossier_images, nom_fichier)

    # Vérifiez si le fichier est une image (vous pouvez ajuster les extensions selon vos besoins)
    if nom_fichier.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        try:
            image = face_recognition.load_image_file(chemin_complet)
            faceLocation = face_recognition.face_locations(image)
            images.extend(face_recognition.face_encodings(image, faceLocation, model="large"))

            name = nom_fichier.split('.')[0]
            images_names.append(name)

            print(f"{nom_fichier} {index}/{nombre_images}")

            index = index + 1
        except Exception as e:
            print(f"Erreur lors de la lecture de {chemin_complet}: {str(e)}")

# === CREATION DE DOSSIER === #

dossier = "saves"

if not os.path.exists(dossier):
    os.makedirs(dossier)
    print(f"Le dossier '{dossier}' a été créé.")
else:
    print(f"Le dossier '{dossier}' existe déjà.")

# === SAUVEGARDE DES IMAGES === #

# Sauvegarde des images
with open(f"{dossier}/images.pkl", "wb") as fichier:
    pickle.dump(images, fichier)

# Sauvegarde des noms d'images
with open(f"{dossier}/images_names.pkl", "wb") as fichier:
    pickle.dump(images_names, fichier)
