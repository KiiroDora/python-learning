import sqlite3
db = sqlite3.connect("kitaplar.sqlite")
imlec = db.cursor()

imlec.execute("SELECT * FROM 'kitaplik tablosu' WHERE yazar = 'volkan TAŞÇI' ")

veriler = imlec.fetchall()

for veri in veriler:
    print(veri)

db.close()