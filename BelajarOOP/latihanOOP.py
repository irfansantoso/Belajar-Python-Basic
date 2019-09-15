class Hero:

    def __init__(self,name,health,attachPower,armor):
        self.name = name
        self.health = health
        self.attachPower = attachPower
        self.armor = armor

    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self)

    def diserang(self, lawan):
        print(self.name + " diserang " + lawan.name)
        print("Serangan diterima = " + str(lawan.attachPower))
        self.health -= lawan.attachPower
        print("darah " + self.name + " tersisa " + str(self.health))

natalia = Hero("natalia",500,50,10)
balmond = Hero("balmond",900,40,30)
minotour = Hero("minotour",1500,20,50)

natalia.serang(balmond)
print("\n")
balmond.serang((natalia))
print("\n")
minotour.serang(balmond)