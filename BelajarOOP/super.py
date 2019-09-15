class monster:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("monster {} darahnya {}".format(self.name, self.health))

class monsterDarat(monster):
    def __init__(self,name):
        #monster.__init__(self,name,100)
        super().__init__(name,100)
        super().showInfo()

class monsterAir(monster):
    def __init__(self,name):
        #monster.__init__(self,name,150)
        super().__init__(name,150)
        super().showInfo()

lizard = monsterDarat("Lizard")
shark = monsterAir("shark")

