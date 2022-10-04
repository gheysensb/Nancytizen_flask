import sqlite3

connecteur = sqlite3.connect("database.db")

cursor = connecteur.cursor()

dtable1 = cursor.execute("DROP TABLE IF EXISTS signalements")
table1 = cursor.execute("CREATE TABLE signalements(identifiant int PRIMARY KEY, Nom varchar not null, Prenom varchar not null, dateheure smalldatetime not null, Titre varchar not null, Categorie varchar not null, Signal_description varchar not null, Longitude float not null, Latitude float not null, statut varchar not null)")

dtable2 = cursor.execute("DROP TABLE IF EXISTS categorie_sign")
table2 = cursor.execute("CREATE TABLE categorie_sign(Type_de_signalement varchar PRIMARY KEY)")

dtable3 = cursor.execute("DROP TABLE IF EXISTS ideabox")
table3 = cursor.execute("CREATE TABLE ideabox(ididea int PRIMARY KEY,title varchar,content varchar,fav int ,unfav int,dateheure smalldatetime not null)")

cursor.execute("INSERT INTO categorie_sign values('Route')")
cursor.execute("INSERT INTO categorie_sign values('Commerce')")
cursor.execute("INSERT INTO categorie_sign values('Ecole')")
cursor.execute("INSERT INTO categorie_sign values('Espace public')")


cursor.execute("INSERT INTO signalements values (1,'Garcia-Forest','Nicolas','2021-12-13 12:43:10','Ecole taguée', 'Ecole', 'Tout le mur de l extérieur de l école a été tagué !', '48.69461366173126' , '6.175055091935587', 'Non Traité')")
cursor.execute("INSERT INTO signalements values (2,'Gheysens','Baptiste','2021-10-24 15:29:11','Route abimée', 'Route', 'Il y a un trou en plein millieu de la route', '48.66907018711965', '6.1950536445228055', 'En cours de traitement')")
cursor.execute("INSERT INTO signalements values (3,'Bouveron','Armand','2022-01-01 08:47:12','Panneau disparu', 'Route', 'Le panneau du rond-poind a disparu', '48.66649457838934', '6.166230626649068', 'Traité')")

cursor.execute("INSERT INTO ideabox values (1,'construction école','L idée serait de construire une école à vandoeuvre les nancy',24,6,'18-12-2021 20:21:34')")
cursor.execute("INSERT INTO ideabox values (2,'Horaire tram et bus','Il serait utile que les bus et tram aient des horaires plus large la nuit. Par exemple, 2h00 du matin',38,2,'14-08-2021 01:45:21')")
cursor.execute("INSERT INTO ideabox values (3,'Sentier GR','Indiquer par des panneaux les sentiers de grande randonnée (GR)',54,4,'23-09-2021 15:20:45')")


connecteur.commit()
connecteur.close()