import tkinter as tk
from tkinter import messagebox
import socket

# Adresse et port du serveur
ADRESSE = "10.229.253.8"
PORT = 1664

# Fonction pour envoyer les commandes au serveur
def envoyer_commande(commande):
    try:
        client_socket.sendall(commande.encode())
        label_status.config(text=f"Commande envoyée : {commande}")
    except Exception as e:
        print(f"Erreur d'envoi: {e}")
        label_status.config(text=f"Erreur d'envoi : {commande}")

# Connexion au serveur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((ADRESSE, PORT))
except Exception as e:
    print(f"Erreur de connexion: {e}")
    messagebox.showerror("Erreur de connexion", f"Impossible de se connecter au serveur : {e}")
    exit()

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

# Création des boutons pour les commandes
frame = tk.Frame(root)
frame.pack(pady=20)

btn_avancer = tk.Button(frame, text="Avancer", command=lambda: envoyer_commande("avancer"), width=10)
btn_avancer.grid(row=0, column=1, padx=5, pady=5)

btn_gauche = tk.Button(frame, text="Gauche", command=lambda: envoyer_commande("gauche"), width=10)
btn_gauche.grid(row=1, column=0, padx=5, pady=5)

btn_droite = tk.Button(frame, text="Droite", command=lambda: envoyer_commande("droite"), width=10)
btn_droite.grid(row=1, column=2, padx=5, pady=5)

btn_reculer = tk.Button(frame, text="Reculer", command=lambda: envoyer_commande("reculer"), width=10)
btn_reculer.grid(row=2, column=1, padx=5, pady=5)

btn_lever = tk.Button(frame, text="Lever Barre", command=lambda: envoyer_commande("lever"), width=10)
btn_lever.grid(row=3, column=0, padx=5, pady=5)

btn_baisser = tk.Button(frame, text="Baisser Barre", command=lambda: envoyer_commande("baisser"), width=10)
btn_baisser.grid(row=3, column=2, padx=5, pady=5)

# Label pour afficher le statut
label_status = tk.Label(root, text="En attente de commande...")
label_status.pack(pady=10)

# Boucle principale de l'application
root.mainloop()
