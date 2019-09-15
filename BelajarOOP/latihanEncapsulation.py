class Hero:
    def __init__(self,name,health,attPower,armor,experience,level):
        self.name = name
        self.health = health
        self.attPower = attPower
        self.armor = armor
        self.experience = experience
        self.level = level

    @property
    def experiencex(self):
        return self.experience

    @experiencex.setter
    def experiencex(self,input):
        self.experience = input

    def serang(self):
        print(self.name + " Menyerang")

vans = Hero("vans",500,50,10,10,1)
sant = Hero("sant",400,40,10,10,1)

vans.experience += 10
print(vans.experiencex)
vans.serang()