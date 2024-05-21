from flask import Flask, render_template, request, send_file
import sqlite3
import csv
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('rechercher_campagne.html')

@app.route('/rechercher_campagne', methods=['POST'])
def rechercher_campagne():
    nom_campagne = request.form['nom_campagne']
    date_campagne = request.form['date_campagne']
    
    # Connect to the database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Search for campaigns based on the form input
    query = "SELECT * FROM Campagnes WHERE Nom LIKE ? AND Date LIKE ?"
    cursor.execute(query, (f"%{nom_campagne}%", f"%{date_campagne}%"))
    results = cursor.fetchall()
    
    conn.close()

    # Render results (you can create a new HTML template to show the results)
    return render_template('rechercher_campagne.html', results=results)

@app.route('/download_csv')
def download_csv():
    # Connect to the database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Retrieve all data from the tables
    cursor.execute("SELECT * FROM Campagnes")
    campagnes = cursor.fetchall()
    
    cursor.execute("SELECT * FROM Obstacles")
    obstacles = cursor.fetchall()
    
    cursor.execute("SELECT * FROM Tnisum")
    tnisum = cursor.fetchall()

    # Create a CSV file in memory
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write data from Campagnes table
    writer.writerow(['Campagnes'])
    writer.writerow(['id_campagnes', 'Nom', 'Date', 'Pilote', 'Action'])
    writer.writerows(campagnes)
    
    # Write data from Obstacles table
    writer.writerow([])
    writer.writerow(['Obstacles'])
    writer.writerow(['id_campagnes', 'id_obstacles', 'Date', 'Latitude', 'Longitude'])
    writer.writerows(obstacles)
    
    # Write data from Tnisum table
    writer.writerow([])
    writer.writerow(['Tnisum'])
    writer.writerow(['id_campagnes', 'id_Tnisum', 'Date', 'Taux_nsium', 'Latitude', 'Longitude'])
    writer.writerows(tnisum)
    
    # Move to the beginning of the StringIO object
    output.seek(0)
    
    conn.close()

    return send_file(output, mimetype='text/csv', attachment_filename='data.csv', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)