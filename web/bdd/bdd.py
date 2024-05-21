# 4. Stockage
import sqlite3

# Connectez-vous à la base de données
conn = sqlite3.connect('votre_base_de_données.db')
cursor = conn.cursor()

# Insérez des données dans la base de données
def inserer_donnees(taux_nsium, distance_obstacle, position_robot):
    cursor.execute("INSERT INTO Tnisum (taux_nsium, distance_obstacle, position_robot) VALUES (?, ?, ?)", (taux_nsium, distance_obstacle, position_robot))
    conn.commit()

def time():
    cursor.execute()
