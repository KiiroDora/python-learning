rehber = { "karakter1" : {"ev":555555555, "iş": 333333333}, 
            "karakter2" : {"ev":32312323, "iş":324324324}}

isimler = rehber.keys()

aranan = input("dare")
if aranan in isimler:
    flag = True
else:
    flag = False
arananb = input("docchi")
if flag:
    print(rehber.get(aranan, "kişi bulunamadı desu").get(arananb, "tel bulunamadı desu"))
else:
    print("no")