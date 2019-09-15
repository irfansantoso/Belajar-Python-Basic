class Hero:
    def __init__(self,name,health,attachPower,armor):
        #private
        self.__name = name
        self.__health = health
        self.__attachPower = attachPower
        self.__armor = armor

    #cara untuk mendapatkan variable private, dengan trik membuat methode baru seperti dibawah ini getInfoHero
    #getter
    def getInfoHero(self):
        print(self.__name)
        print(self.__health)
        print(self.__attachPower)
        print(self.__armor)

    #setter
    def levelUp(self):
        self.__health += 100
        self.__attachPower += 50
        self.__armor += 10

natalia = Hero("natalia",500,50,10)

print(natalia.getInfoHero())
natalia.levelUp()
print(natalia.getInfoHero())