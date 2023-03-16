class Asker():
    #tüm classlar için ortak
    def __init__(self, isim, guc): #örnek oluşturulurken yapılan işlemler buraya
        self.kabiliyetleri = [] #Asker.kabiliyetleri işe yaramaz
        self.isim = isim
        self.guc = guc

ahmet = Asker("Ahmet", 324)
mehmet = Asker("Mehmet", 23)

ahmet.kabiliyetleri += ["123"]
mehmet.kabiliyetleri += ["sdasdas"]

print(ahmet.kabiliyetleri)
print(mehmet.isim)
print(ahmet.isim)
