import random

class Dusman():
    def __init__(self):
        self.sagmi = True
        self.saglik = random.randint(30,70)
        self.kalkan = random.randint(0,10)
        self.guc = random.randint(20,50)
    def vur(self,player): 
        damage = self.guc - player.kalkan
        player.saglik -= damage

class Player():
    def __init__(self):
        self.sagmi = True
        self.saglık = 500
        self.kalkan = 20
        self.guc = 55

dusmanlar = list()

def vur(self, dusman):
    damage = self.guc - dusman.kalkan
    dusman.saglik -= damage
    if dusman.saglik <= 0:
        dusman.sagmi = False
        dusmanlar.remove(dusman)

    

    for i in range(10):
        dusmanlar.append(Dusman())
        print(dusmanlar)

    player = Player()

    while True:
        print("TAŞÇI -->>> Saglik: {} ---- Guc: {} ---- Kalkan: {}".format(player.saglık, player.guc, player.kalkan))
        if player.sagmi == False:
            print("lol ezk")
            quit()
        if not dusmanlar:
            print("ok")
        for i in dusmanlar:
            print("{}. Dusman -->>> Saglik: {} ---- Guc: {} ---- Kalkan: {}".format(i, i.saglik, i.guc, i.kalkan))
            break
