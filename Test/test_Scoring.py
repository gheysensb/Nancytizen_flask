import pytest
import Scoring
import sqlite3

def test_score():
    connecteur = sqlite3.connect("databasetest.db")
    cursor = connecteur.cursor()
    dtable3 = cursor.execute("DROP TABLE IF EXISTS ideabox")
    table3 = cursor.execute("CREATE TABLE ideabox(ididea int PRIMARY KEY,title varchar,content varchar,fav int ,unfav int,dateheure smalldatetime not null)")
    cursor.execute("INSERT INTO ideabox values (1,'inser 1 ','content 1 ',150,2,'18-12-2021/20:21')")
    cursor.execute("INSERT INTO ideabox values (2,'inser 2','content 2 ',20,1,'17-1-2021/10:21')")
    cursor.execute("INSERT INTO ideabox values (3,'inser 3','content 3',1,2000,'18-12-2021/20:21')")
    r = (cursor.execute('SELECT title, content,dateheure, fav, unfav ,ididea FROM ideabox ORDER BY dateheure DESC ')).fetchall()
    s = Scoring.score(r)
    for i in range(1,len(s)):
        assert (s[i][3]-s[i][4])<=(s[i-1][3]-s[i-1][4])

def test_score2():
    connecteur = sqlite3.connect("databasetest.db")
    cursor = connecteur.cursor()
    dtable3 = cursor.execute("DROP TABLE IF EXISTS ideabox")
    table3 = cursor.execute("CREATE TABLE ideabox(ididea int PRIMARY KEY,title varchar,content varchar,fav int ,unfav int,dateheure smalldatetime not null)")
    cursor.execute("INSERT INTO ideabox values (1,'inser 1 ','content 1 ',1,1,'18-12-2021/20:21')")
    cursor.execute("INSERT INTO ideabox values (2,'inser 2','content 2 ',1,1,'17-1-2021/10:21')")
    cursor.execute("INSERT INTO ideabox values (3,'inser 3','content 3',1,1,'18-12-2021/20:21')")
    r = (cursor.execute('SELECT title, content,dateheure, fav, unfav ,ididea FROM ideabox ORDER BY dateheure DESC ')).fetchall()
    s = Scoring.score(r)
    for i in range(1,len(s)):
        assert (s[i][3]-s[i][4])<=(s[i-1][3]-s[i-1][4])

def test_score3():
    connecteur = sqlite3.connect("databasetest.db")
    cursor = connecteur.cursor()
    dtable3 = cursor.execute("DROP TABLE IF EXISTS ideabox")
    table3 = cursor.execute("CREATE TABLE ideabox(ididea int PRIMARY KEY,title varchar,content varchar,fav int ,unfav int,dateheure smalldatetime not null)")
    cursor.execute("INSERT INTO ideabox values (1,'inser 1 ','content 1 ',150121212121212,2121212121121,'18-12-2021/20:21')")
    cursor.execute("INSERT INTO ideabox values (2,'inser 2','content 2 ',2001212121221210,1121212121221,'17-1-2021/10:21')")
    cursor.execute("INSERT INTO ideabox values (3,'inser 3','content 3',11212121112112,2001212121210,'18-12-2021/20:21')")
    r = (cursor.execute('SELECT title, content,dateheure, fav, unfav ,ididea FROM ideabox ORDER BY dateheure DESC ')).fetchall()
    s = Scoring.score(r)
    for i in range(1,len(s)):
        assert (s[i][3]-s[i][4])<=(s[i-1][3]-s[i-1][4])