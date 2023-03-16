from os import system as komut

class Musteri():
    def __init__(self, ID:str, parola:str, isim:str):
        self.isim = isim
        self.ID = ID
        self.parola = parola
        self.bakiye = 0

class Banka():
    def __init__(self):
        self.musteriler = list()

    def musteri_ol(self, ID, parola, isim):
        self.musteriler.append(Musteri(ID, parola, isim))
        print("bamka kayıt arigato")

def main():
    banka = Banka()

        print("""
        1 - Müşteriyim
        2- Kayıt olmak istiyom
        """)
        secim = input("Seçiminz: ")

        if secim == "2":
            ID = input("ID: ")
            isim = input("isim: ")
            parola = input("parola: ")
            banka.musteri_ol(ID, parola, isim)

        elif secim == "1":
            ids = [i.ID for i in banka.musteriler]
            IDs = input("ID: ")
            if IDs in ids:
                for musteri in banka.musteriler:
                    if IDs == musteri.id:
                        print("selam {}".format(musteri.isim))
                        if parola == musteri.parola:
                            while True:
                                komut("cls")
                                print("""
                                1 - Bakiye Sorgula
                                2 - Para Yatır (Kendine)
                                3 - Para Yatır (Başkasına)
                                4 - Para Çek
                                5 - Çık
                                """)

                            secim2 = input("işlemin: ")

                            if secim2 == "1":
                                print("Bakyeniz: {}".format(musteri.bakiye))
                                input("ana menu içn enter")
                            
                            elif secim2 == "2":
                                miktar = int(input("Miktar: "))
                                onay = input("kENDİ HESABINIZA {} Tl para yattır")
                                if onay == "E" or onay == "e":
                                    musteri.bakiye += miktar
                                    print("para yat")
                                    input("ana menu içn enter")

                                elif onay == "h" or onay == "H":
                                    print("İşlem iptal edil")
                                    input("ana menu içn enter")

                                else: 
                                    print("hatalkı")
                                    input("ana menu içn enter")
                            elif secim2 == "3":
                                arananID = input("Müsşt ID: ")
                                if arananID in ids:
                                    for digerMusteri in banka.musteriler:
                                        if arananID == digerMusteri.id:
                                            miktar = int(input("Miktar: "))
                                            if miktar <= musteri.bakiye:
                                                onay = input("yollandı")
                                                if onay == "e" or onay == "E":
                                                    digerMusteri.bakiye += miktar
                                                    musteri.bakiye -= miktar
                                                elif onay == "h" or onay == "H":
                                                    print("iptal")
                                                    input("ana menu içn enter")
                                                else:
                                                    print("yo")
                                                    input("ana menu içn enter")
                                            else:
                                                print("fakir")
                                                input("ana menu içn enter")
                                else:
                                    print("öle biri yok")
                                    input("ana menu içn enter")
                            elif secim2 == "4":
                                miktar = int(input("Mikater:"))
                                if miktar <= musteri.bakiye:
                                    musteri.bakiye -= miktar
                                    print("done")
                                else:
                                    print("fakir")
                            elif secim2 == "q":
                                break
        


if __name__ == "__main__":
    main()