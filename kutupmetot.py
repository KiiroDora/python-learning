sozluk = {"book":"kitap", "computer":"bilgisayar", "mobile":"telefon", "pen":"kalem"}
sozluk2 = sozluk.copy()

for i in sozluk.items():
    print(i)

s = input("Sorgu:" )
print(sozluk.get(s,"Aratılan kelime bulunamadı"))

for i in sozluk.keys():
    print (i)

for i in sozluk.values():
    print (i)

