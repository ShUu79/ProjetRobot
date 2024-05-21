#!/usr/bin/env pybricks-micropython
"""
NSI :: serveur.py
"""

# Librairie(s)
import socket

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Interface réseau et port TCP d'acoute
ADRESSE = "10.229.253.8"
PORT = 1664

# Création d'une socket
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuration de la socket pour pouvoir la réutiliser
serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# On demande à l'OS d'attacher notre programme au port TCP demandé
serveur.bind(("10.229.253.8", 1664))
serveur.listen(10)

# Boucle de gestion des connexions des clients
fin = False
while fin == False:
    # Attente qu'un client se connecte
    client, adresse = serveur.accept()
    print(f"Connexion de {adresse}")

    # Réception de la requete du client sous forme de bytes et transformation en string
    requete = client.recv(1024)
    print(f"Réception de {requete.decode()}")
    if requete.decode() == "FIN":
        fin = True

    # Préparation et envoi de la réponse
    reponse = "OK"
    client.send(reponse.encode())

    # Déconnexion avec le client
    print("Fermeture de la connexion avec le client.")
    client.close()

# Arrêt du serveur    
print("Arret du serveur.")
serveur.close()