class Heroo:
    #class variable
    jumlah = 0
    def __init__(self,x,y,z):
        self.name = x
        self.hp = y
        self.armor = z
        Heroo.jumlah += 1

    #void function atau method tanpa return
    def panggil(self):
        print("hai, namaku adalah", self.name)

    #method dengan argumen, tanpa return
    def tambahDarah(self,up):
        self.hp += up

    #methode dengan return
    def getHealth(self):
        return self.up


hero2 = Heroo("natali",100,50)
hero3 = Heroo("minotaur",1000,300)

hero2.panggil()
hero2.panggil()
print(hero2),1000,100
