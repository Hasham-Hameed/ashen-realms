class Character:
    def __init__(self,name,character_class,level,health,max_health,attack,gold):
        self.name = name
        self.character_class = character_class
        self.level = level
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.gold = gold

    def show_status(self):
        print(f"Name: {self.name}")
        print(f"Character class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")

    def take_damage(self,damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
        if self.health == 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"Remaining health: {self.health}")

    def heal(self,healing_amount):
        if self.health == 0:
            print("A defeated character cannot heal!")
        else:
            self.health = healing_amount + self.health
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"Updated health: {self.health}")
armin = Character("Armin","Warrior",1,100,100,10,50)
armin.take_damage(100)
armin.heal(50)
armin.show_status()