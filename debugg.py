bolunen = float(input("Bölünen: "))

bolen = float(input("Bölen: "))

try:
    print("Sonuç",bolunen/bolen)
except ZeroDivisionError as hata:
    print("0'a bölüm tanımsızdır!")
    print("Gerçek hata:")
    print(hata)

except TypeError:
    print("Veri tipi desteklenmiyor!")

finally:
    print("Bu hep var lol")
    
"""
sadece except = tüm hatalar
"""

