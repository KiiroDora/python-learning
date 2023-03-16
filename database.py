import sqlite3

veriler = [("volkan TAŞÇI","python kitabü"), ("Yaşar Kemal","ince memüd")]

db = sqlite3.connect("kitaplar.sqlite")

imlec = db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS 'kitaplik tablosu' (yazar, kitap)")

for veri in veriler:
    imlec.execute("INSERT INTO 'kitaplik tablosu' VALUES (?,?)",veri)

db.commit()

db.close()