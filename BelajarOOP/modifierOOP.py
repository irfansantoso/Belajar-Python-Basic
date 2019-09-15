class Hero:
    def __init__(self,name,health,attachPower,armor):
        #public
        self.name = name
        self.health = health
        self.attachPower = attachPower
        self.armor = armor

        #protected
        self._tinggi = 15

        #private
        self.__exp = 10

    #cara untuk mendapatkan variable private, dengan trik membuat methode baru seperti dibawah ini getExp
    def getExp(self):
        print(self.__exp)



natalia = Hero("natalia",500,50,10)

print(natalia.name)
print(natalia._tinggi)
print(natalia.getExp())