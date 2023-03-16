

print("""
[1] Topla
[2] Çıkar
[3] Çarp
[4] Böl
[5] Üs
[6] Çık
""") 

def hesap(x, y, a):

    if (x.isdigit() == True and y.isdigit() == True):
        x = float(x)
        y = float(y)
    else:
        print("yo")
        hesap(input("ilk sayı"), input("ikinci sayı"), input("hangi işlem?"))()
    
    if (a == "1"):
        print(x + y)
    elif (a == "2"):
        print(x - y)
    elif (a == "3"):
        print(x * y)
    elif (a == "4"):
        print(x/y)
    elif (a == "5"):
        print(x**y)
    elif (a == "6"):
        exit()
    else:
        print("Doğru gir")
    if(input("devamsa y yaz") == "y"):
        hesap(input("ilk sayı"), input("ikinci sayı"), input("hangi işlem?"))
    else:
       exit()

hesap(input("ilk sayı"), input("ikinci sayı"), input("hangi işlem?"))



    

