import sqlite3

def test_insertion_databse():
    connecteur = sqlite3.connect("database.db")
    cursor = connecteur.cursor()

    cursor.execute("INSERT INTO signalements values (100,'Cagnon','Thibaut','1955-12-13 12:43:10','Test titre', 'Route', 'test description', '48.685526', '6.168815', 'Non traité')")
    connecteur.commit()
    
    r = (cursor.execute('SELECT * FROM signalements WHERE identifiant = 100')).fetchall()
    assert(r[0][0]==100),"ce n'est pas le bon nombre" 
    assert(type(r[0][0])==int),"ce n'est pas un entier"
    assert(r[0][1]=="Cagnon"),"ce n'est pas le  bon nom"
    assert(type(r[0][2])==str),"ce n'est pas une chaîne de caractère"
    assert(r[0][3]=="1955-12-13 12:43:10"),"ce n'est pas la bonne date" 
    assert(type(r[0][3])==str),"ce n'est pas une chaîne de caractère"
    assert(r[0][4]=="Test titre"),"ce n'est pas le bon titre" 
    assert(type(r[0][4])==str),"ce n'est pas une chaîne de caractère"
    assert(r[0][5]=="Route"),"ce n'est pas la bonne catégorie" 
    assert(type(r[0][5])==str),"ce n'est pas une chaîne de caractère"
    assert(r[0][6]=="test description"),"ce n'est pas la bonne description" 
    assert(type(r[0][6])==str),"ce n'est pas une chaîne de caractère"
    assert(r[0][7]==48.685526),"ce n'est pas la bonne longitude" 
    assert(type(r[0][7])==float),"ce n'est pas un flottant"
    assert(r[0][8]==6.168815),"ce n'est pas la bonne latitude" 
    assert(type(r[0][8])==float),"ce n'est pas un flottant"
    assert(r[0][9]=="Non traité"),"ce n'est pas le bon statut" 
    assert(type(r[0][9])==str),"ce n'est pas une chaîne de caractère"


    cursor.execute('DELETE FROM signalements WHERE identifiant = 100')
    connecteur.commit()
    connecteur.close()

test_insertion_databse()
