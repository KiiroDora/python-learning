class Tasit():
    def __init__(self,teker,kapi):
        self.teker = teker
        self.kapi = kapi
def kapiAc():
    print("Kapı Ac")

class Tir(Tasit):
    def __init__(self, teker, kapi, turbo):
        super().__init__(teker, kapi)
        self.turbo = turbo
def dorse():
    print("bırak")

tir = Tir(4,2,1)

print(tir.kapi, tir.teker, tir.turbo)