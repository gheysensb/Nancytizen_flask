import sqlite3

def fetchDys():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor() 
    return((cursor.execute('SELECT Titre, Categorie, dateheure, statut, identifiant FROM signalements ORDER BY dateheure DESC')).fetchall())

DATABASE = 'database.db'

def test_fetch():
    assert fetchDys()[-1]==('Test titre', 'Route', '1955-12-13 12:43:10', 'Non Traité', 1)