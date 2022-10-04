import Scoring
import sqlite3
import random
import time
import matplotlib.pyplot as plt
N = []
D = []
connecteur = sqlite3.connect("databasetest2.db")
cursor = connecteur.cursor()
dtable3 = cursor.execute("DROP TABLE IF EXISTS ideabox")
table3 = cursor.execute("CREATE TABLE ideabox(ididea int PRIMARY KEY,title varchar,content varchar,fav int ,unfav int,dateheure smalldatetime not null)")
for i in range(1,1500):
    cursor.execute("INSERT INTO ideabox values (?,'inser 1 ','content 1 ',?,?,'18-12-2021/20:21')",(i,random.randint(1,1000),random.randint(1,1000)))
    r = (cursor.execute('SELECT title, content,dateheure, fav, unfav ,ididea FROM ideabox ORDER BY dateheure DESC ')).fetchall()
    start = time.time()
    Scoring.score(r)
    end = time.time()
    duree = end - start
    N.append(i)
    D.append(duree)
plt.plot(N,D)
plt.show()
