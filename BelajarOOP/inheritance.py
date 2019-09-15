class monster:
    def __init__(self,name,health):
        self.name = name
        self.health = health

class monsterDarat(monster):
    pass

class monsterAir(monster):
    pass

monsterKadal = monsterDarat("lizard",1000)
monsterIkan = monsterAir("shark",20000)
print(monsterKadal.name)
print(monsterIkan.name)