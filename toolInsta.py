import requests
import json
from instagram_private_api import (
    Client, 
    ClientCompatPatch
)

# Votre clé d'API Instagram
access_token = "210586311.102d5a1.ddb30951563aa43c64c266bc"

# Nom d'utilisateur du compte Instagram dont vous voulez récupérer les informations publiques
username = "ced.bglne"

# Les champs que vous voulez récupérer pour le compte Instagram
fields = "username,followers_count,follows_count,media_count,profile_picture_url"

# Construire l'URL de l'API Instagram pour récupérer les informations du compte
api_url = f"https://graph.instagram.com/{username}?fields={fields}&access_token={access_token}"

# Envoyer la requête GET à l'API Instagram
response = requests.get(api_url)

# Vérifier que la requête s'est bien passée
if response.status_code == 200:
    # Convertir la réponse JSON en un objet Python
    data = json.loads(response.text)
    # Afficher les informations récupérées
    print("Informations pour le compte Instagram :", username)
    print("Nombre d'abonnés :", data["followers_count"])
    print("Nombre de personnes suivies :", data["follows_count"])
    print("Nombre de publications :", data["media_count"])
    print("Photo de profil :", data["profile_picture_url"])
else:
    print("Erreur lors de la récupération des informations du compte Instagram.")
