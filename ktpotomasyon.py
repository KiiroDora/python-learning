import os

buklist = list()
menu = """
1 - Kitak Ekle
2 - Kitap Al
3 - Tümünü Listele
4 - Çıkış
"""
kitap = ("a", "b")

def kitapEkle(kitap:tuple, liste:list):
    liste.append(kitap)
    print("girdi, ana menüye dön = enter")
    input()

def kontrol(kitap:tuple, liste:list):
    if kitap in liste:
        return True

    else:
        return False

def kitapCikar(kitap:tuple, liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("çıktı, ana menüye dön = enter")
        input()
    else:
        print("öle bi kitap yok mal ana menüye dön hemen = enter")
        input()

def listele(liste:list):
    for i in liste:
        print("Kitpadı: {} -> Yazradı: {}".format(i[0], i[1]))

secim = input("işlem seç")
if secim == "1":
    kitapname = input("Kitap Adı:")
    kitapwrit = input("Yazarın Adı:")
    kitap = (kitapname, kitapwrit)
    kitapEkle(kitap,buklist)
elif secim == "2":
    kitapname = input("Kitap Adı:")
    kitap = kitapname
    kitapCikar (kitap, buklist)
elif secim == "3":
    listele(buklist)
elif secim == "4":
    quit()
else:
    print("hatalı")
