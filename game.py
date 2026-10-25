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

    def attack_enemy(self, enemy):
        if enemy.health == 0:
            print("The enemy has already been defeated!")
        else:
            enemy.health = enemy.health - self.attack
            if enemy.health < 0:
                enemy.health = 0
            print(f"Enemy's remaining health: {enemy.health}")
            return enemy.health

class Enemy:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
    
    def take_damage(self,damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name}'s remaining health: {self.health}")

    def attack_character(self,character):
        if character.health == 0:
            print("The character has already been defeated!")
        else:
            character.health -= self.attack
            if character.health < 0:
                character.health = 0
            print(f"{character.name}'s remaining health: {character.health}")

armin = Character("Armin", "Warrior", 1, 10, 100, 10, 50)
enemy = Enemy("Goblin", 30)

enemy.attack_character(armin)
enemy.attack_character(armin)