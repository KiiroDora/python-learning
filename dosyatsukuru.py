dosya = open("deneme.txt", "r+")

yazi = "\nkimochi warui"
dosya.write(yazi)
okunan = dosya.readlines()
print(okunan)

dosya.close()

"""
r okuma

w yazma (dosya varsa overwrite)
a yazma (ekleme)
x yazma (dosya varsa hata)

r+ okuma yazma (dosya var olması lazım)
w+ okuma yazma (varsa overwrite)
a+ okuma yazma (ekleme)
x+ okuma yazma (dosya varsa hata)

"""