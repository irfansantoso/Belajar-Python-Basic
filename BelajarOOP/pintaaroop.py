class Hero: # template / class / cetakannya
    pass

hero1 = Hero() # object / instance
hero2 = Hero()

hero1.nama = "natali"
hero1.hp = 100

hero2.nama = "minotaur"
hero2.hp = 1000

print(hero1.__dict__)
print(hero2.hp)