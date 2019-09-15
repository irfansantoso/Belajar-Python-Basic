class Heroo:
    #class variable
    jumlah = 0
    def __init__(self,x,y,z):
        self.name = x
        self.hp = y
        self.armor = z
        Heroo.jumlah += 1
        print("membuat heroo dengan nama", x)

hero2 = Heroo("natali",100,50)
hero3 = Heroo("minotaur",1000,300)

print(Heroo.jumlah)