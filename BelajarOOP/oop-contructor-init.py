class Hero:
    def __init__(self,z):
        print("Haiiii",z)

hero1 = Hero("cewek")

print("\n")
print(10*"#")
print("\n")

class Heroo:
    def __init__(self,x,y,z):
        self.name = x
        self.hp = y
        self.armor = z

hero2 = Heroo("natali",100,50)
hero3 = Heroo("minotaur",1000,300)

print(hero2.__dict__)
print(hero2.armor)

print(hero3.__dict__)
print(hero3.armor)