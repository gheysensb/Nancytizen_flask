from datetime import datetime
from flask import Flask , render_template ,request,g,redirect
import folium
import sqlite3
from geopy.geocoders import Nominatim
from CarteCreator import Create, CreateFiltré
from Scoring import score

DATABASE = 'database.db'
app = Flask(__name__)
DL_PHOTO_FOLDER = 'static/photoidea'
ALLOWED_EXTENSIONS = {  'png', 'jpg', 'jpeg', 'gif'}

def fetchDys():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor() 
    return((cursor.execute('SELECT Titre, Categorie, dateheure, statut, identifiant FROM signalements ORDER BY dateheure DESC')).fetchall())

def get_db():  # cette fonction permet de créer une connexion à la db
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):  # pour fermer la connexion proprement
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/ajouter_dysfonctionnement") # charge la page qui permet d'ajouter un dysfonctionnement
def ajouter_dysfonctionnement():
    conn=sqlite3.connect("database.db")
    cursor = conn.cursor()
    categorie = (cursor.execute("SELECT * FROM categorie_sign")).fetchall()
    liste_type_dys = [i[0] for i in categorie]
    return render_template("page_dysfonctionnement.html", list = liste_type_dys)

@app.route("/add_dys", methods=['POST']) # récupère les données du form après remplissage sur la page d'ajout d'un dysfonctionnement
def add_dys():
    curseur = get_db()
    categorie=request.form.get('dys_cat')
    nom=request.form.get('nom')
    title=request.form.get('title')
    description=request.form.get('description')
    prenom=request.form.get('prenom')
    adresses=request.form.get('adresse')
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(adresses)
    dateheure = str(datetime.now())[:-7]
    status = 'Non Traité'
    max_id=(curseur.execute('SELECT max(identifiant) FROM signalements')).fetchall() # récupère l'id du dernier dysfonctionnement 
    id=int(str(max_id[0]).strip('(').strip(')').strip(','))+1 # pour en attribuer un différent (+1) au nouveau dysfonctionnement
    curseur.execute("INSERT INTO signalements VALUES(?,?,?,?,?,?,?,?,?,?)", (id, nom, prenom, dateheure, title, categorie, description, location.latitude, location.longitude, status))
    curseur.commit()
    return redirect("/voir_dysfonctionnements")

@app.route("/voir_dysfonctionnements")
def listeDys():
    r = fetchDys()
    return render_template('affichage.html',curs = r)

@app.route("/details_dysfonctionnement/<int:id>",methods=['POST'])
def detailsDys_post(id):
    print(id)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    r = (cursor.execute('SELECT Prenom, Nom, Titre, Categorie, Signal_description, dateheure, statut, identifiant FROM signalements WHERE identifiant=%s' % id)).fetchall()
    a = (cursor.execute('SELECT titre, longitude, latitude FROM signalements WHERE identifiant =%s' % id)).fetchall()
    b = (cursor.execute('SELECT titre, longitude, latitude , statut FROM signalements WHERE identifiant !=%s' % id)).fetchall()
    inf1 = request.form.get('Traité')
    inf2 = request.form.get('Non Traité')
    inf3 = request.form.get('En cours de traitement')
    Linf = [inf1, inf2, inf3]
    for tpl in a:
        CreateFiltré([tpl[1], tpl[2]], b,Linf, tpl)

    return render_template('affichage_details.html',curs = r,iden=id)

@app.route("/details_dysfonctionnement/<int:id>")
def detailsDys(id):
    print(id)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    r = (cursor.execute('SELECT Prenom, Nom, Titre, Categorie, Signal_description, dateheure, statut, identifiant FROM signalements WHERE identifiant=%s' % id)).fetchall()
    a = (cursor.execute('SELECT titre, longitude, latitude FROM signalements WHERE identifiant =%s' % id)).fetchall()
    b = (cursor.execute('SELECT titre, longitude, latitude , statut FROM signalements WHERE identifiant !=%s' % id)).fetchall()
    for tpl in a:
        Create([tpl[1],tpl[2]],b,tpl)

    return render_template('affichage_details.html',curs = r,iden=id)

@app.route("/change_statut/<int:id>", methods=['POST'])
def changeStatut(id):
    curseur = get_db()
    status=request.form.get('status')
    curseur.execute('UPDATE signalements SET statut = ? WHERE identifiant = ?', (status, id))
    curseur.commit()
    return redirect("/details_dysfonctionnement/%s" %id)

@app.route("/") # charge la page d'accueil
def index():
    return render_template("index.html")

@app.route('/signal',methods=['POST'])
def creaCarte_post():  #Créer la carte en faisant appel a la fonction CreateFiltré
    inf1=request.form.get('Traité')
    inf2 = request.form.get('Non Traité')
    inf3 = request.form.get('En cours de traitement')
    Linf = [inf1,inf2,inf3]
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    r = (cursor.execute('SELECT titre, longitude, latitude, statut FROM signalements ')).fetchall()
    CreateFiltré([48.688164, 6.189513],r,Linf,[])
    return render_template('carte.html')

@app.route('/signal')
def creaCarte(): #Créer la carte en faisant appel a la fonction Create
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    r = (cursor.execute('SELECT titre, longitude, latitude, statut FROM signalements ')).fetchall()
    Create([48.688164, 6.189513],r,[])
    return render_template('carte.html')

@app.route('/ideaBox/<page>') #Fonction de création de la boîte à idée
def ideaBox(page):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    r = (cursor.execute('SELECT title, content,dateheure, fav, unfav ,ididea FROM ideabox ORDER BY dateheure DESC ')).fetchall()
    page = int(page)
    if page == 1:

        r = score(r)
    return render_template('ideabox.html',idea = r,page=page)

@app.route('/ideaBox/fav/<iden>') #Ajout d'un j'aime
def addFav(iden):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE ideabox SET fav = fav +1 WHERE ididea=?',(iden))
    conn.commit()
    conn.close()
    return redirect('/ideaBox/0')

@app.route('/ideaBox/unfav/<iden>') #Ajout d'un je n'aime pas
def dissFav(iden):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE ideabox SET unfav = unfav +1 WHERE ididea=?',(iden))
    conn.commit()
    conn.close()
    return redirect('/ideaBox/0')

@app.route('/ideaBox/createIdea/') #page de création d'une idée
def cIdea():
    return render_template('createidea.html')

@app.route('/ideaBox/createIdea/',methods =['POST']) #Création et enregistrement de l'idée dans la base de donnée
def cIdea_post():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    titre = request.form['titre']
    contenu = request.form['Description']
    s = (cursor.execute('SELECT max(ididea) FROM ideabox')).fetchall()
    s = s[0]
    s = s[0]
    dateheure = str(datetime.now())[:-7]
    cursor.execute('INSERT into ideabox VALUES(?,?,?,0,0,?)', (s+1,titre,contenu,dateheure))
    conn.commit()
    conn.close()
    return redirect('/ideaBox/0')


if __name__ == '__main__':
    app.run()