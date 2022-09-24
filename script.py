class Warior(object):
    def __init__(self,name,health,damage):
        self.name   = name
        self.health = health
        self.damage = damage
        print("Warior created succesfully")

    def set_health(self ,health):
        self.health = health 

    def set_damage(self ,damage):
        self.damage = damage

    def attack(self,Warior):
        Warior.health -= self.damage
        print(Warior.name, "has been attaked by", self.name)

    def sayHi(self):
        print("Hey Warior my name is : ",self.name)



class Player(Warior):
    def __init__(self,name,health,damage,speed,defense):
        super().__init__(name,health,damage)
        self.speed   = speed
        self.defense = defense
        print("Player created successfully")

    def sayHi(self):
        print("Hello Player my name is : ",self.name)



# ayoub = Warior("Ayoub", 100 , 20)
# badr  = Warior("Badr" , 100 , 10)



#attack function test
# ayoub.attack(badr)
# print(badr.health)

player1 = Player("Ayoub",100,20,88,72)
player2 = Player("Badr" ,100,10,86,79)


player1.attack(player2)
player2.sayHi()



