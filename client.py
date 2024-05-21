#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Librairie(s)
import socket

# Adresse IP et port TCP d'écoute du serveur
HOST = "10.229.253.8"
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