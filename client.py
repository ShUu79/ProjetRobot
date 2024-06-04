"""
NSI :: Client TCP
"""

# Librairie(s)
import socket

# Adresse IP et port TCP d'écoute du serveur
HOST = "127.0.0.1"
PORT = 1664

# Création de la socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client.connect((HOST, PORT))
print(f"Connexion vers {HOST}:{PORT} reussie.")

# Envoi d'un message texte qu'il faut transformer en octets avant envoi
requete = "Hello world"
print(f"Envoi de : {requete}")
client.send(requete.encode())

# Réception de la réponse du serveur
print("Reception...")
reponse = client.recv(1024)
print(f"Recu : {reponse.decode()}")

# Déconnexion
print("Deconnexion.")
client.close()