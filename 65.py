class character:
    name = None
    health = 100
    mp = 100

    def __init__(self, name):
        self.name = name
    
    def print(self):
        print(f"{self.name} HP: {self.health} MP: {self.mp} Nickname: {self.nickname}! Lives: {self.lives}")

    def setSats(self, health, mp):
        self.health = health
        self.mp = mp

class player(character):
    nickname = None
    lives = 3

    def __init__(self, nickname):
        self.name = "Player"
        self.nickname = nickname

    def isAlive(self):
        if self.lives > 0:
            print(f"{self.nickname} lives on!")
            return True
        else:
            print(f"{self.nickname} has expired.")
            return False

ian = player("Ian the mighty")
ian.print()
print(ian.isAlive())

class enemy(character):
    type = None
    strength = None

    def __init__(self, name, type, strength):
        self.name = name
        self.type = type
        self.strength = strength
    
    def print(self):
        print(f"{self.name} HP: {self.health} MP: {self.mp} Type: {self.type} Strength: {self.strength}")

class orc(enemy):
    speed = None

    def __init__(self, speed):
        self.name = 'Orc'
        self.type = 'Orc'
        self.strength = 200
        self.speed = speed
    
    def print(self):
        print(f"{self.name} HP: {self.health} MP: {self.mp} Type: {self.type} Strength: {self.strength}")  

sharron = orc(250)  
gary = orc(205)

sharron.print()
gary.print()

class vampire(enemy):
    day = True

    def __init__(self, day):
        self.name = "Vampire"
        self.type = "Vampire"
        self.strength = 150
        self.day = day

    def print(self):
        print(f"{self.name} HP: {self.health} MP: {self.mp} Type: {self.type} Day: {self.day}")  

eric = vampire(False)
eric.print()
