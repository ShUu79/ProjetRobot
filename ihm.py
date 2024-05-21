import tkinter as tk
import socket

# Adresse et port du serveur
ADRESSE = "10.229.253.8"
PORT = 1664

# Fonction pour envoyer les commandes au serveur
def envoyer_commande(commande):
    try:
        client_socket.sendall(commande.encode())
    except Exception as e:
        print(f"Erreur d'envoi: {e}")

# Connexion au serveur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((ADRESSE, PORT))
except Exception as e:
    print(f"Erreur de connexion: {e}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Contrôleur Robot EV3")

# Gestion des événements de touche
def on_key_press(event):
    if event.char == 'z':
        envoyer_commande("avancer")
    elif event.char == 's':
        envoyer_commande("reculer")
    elif event.char == 'q':
        envoyer_commande("gauche")
    elif event.char == 'd':
        envoyer_commande("droite")

root.bind('<KeyPress>', on_key_press)

# Fonction pour gérer la fermeture de la fenêtre
def on_close():
    envoyer_commande("quitter")
    client_socket.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# Boucle principale de l'application
root.mainloop()
