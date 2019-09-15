class Hero:
    def __init__(self,name,health,armor):
        #private
        self.__name = name
        self.__health = health
        self.__armor = armor

    @property
    def info(self):
        return "hero ini bernama = ", self.__name

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self,input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("delete armor")
        self.__armor = None

mino = Hero("minotaur",1000,300)
print(mino.info)
print(mino.armor)
mino.armor = 50
print(mino.armor)
print(mino.__dict__)
del mino.armor
print(mino.__dict__)
print(mino.armor)
