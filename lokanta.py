masalar = dict()
for i in range(10):
    masalar[i] = 0

def hesapEkle():
    masaNo = int(input("Masa No: "))
    gec = masalar[masaNo]
    eklenecek = float(input("Eklenecek ücret: "))
    toplam = gec + eklenecek
    masalar[masaNo] = toplam 

def hesapSil():
    masaNo = int(input("Masa No: "))
    gec = masalar[masaNo]
    eksilecek = float(input("Eksilecek ücret: "))
    cik = gec - eksilecek
    if cik < 0:
        print("mal")
    else:
        masalar[masaNo] = cik 

def hesapKontrol(dosyaadi):
    try:
        dosya = open(dosyaadi)
        veriler = dosya.read()
        veriler = veriler.split("\n")
        veriler.pop()
        flag = True

    except FileNotFoundError:
        dosya = open(dosyaadi, "w")
        dosya.close()
        flag = False
    if flag:
        for i in enumerate(veriler):
            masalar[i[0]] = float(i[1])
    else:
        pass

def kayitGuncelle():
    dosya = open("lokkayıt.txt", "w")
    for i in range(10):
        ucret = masalar[i]
        ucret = str(ucret)
        dosya.write(ucret + "\n")
    dosya.close()

def main():
    hesapKontrol("lokkayıt.txt")
    print("""
    1-Masaları Görüntüle
    2-Hesap Ekle
    3-Hesap Sil
    4-Çıkış

    """)

    secim = input("işlemin:")

    if secim == "1":
        for i in range(10):
            print("Masa {} için hesap: {}".format(i, masalar[i]))
        main()
    elif secim == "2":
        hesapEkle()
        kayitGuncelle()
        main()
    elif secim == "3":
        hesapSil()
        kayitGuncelle()
        main()
    elif secim == "4":
        quit()
    else:
        print("yo")
        main()
main()
