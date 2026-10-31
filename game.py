class Character:
    def __init__(self,name,character_class,level,health,max_health,attack,gold):
        self.name = name
        self.character_class = character_class
        self.level = level
        self._health = health
        self.max_health = max_health
        self.attack = attack
        self.gold = gold
    @property
    def health(self):
        return self._health

    def show_status(self):
        print(f"Name: {self.name}")
        print(f"Character class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")

    def take_damage(self,damage):
        self._health -= damage
        if self._health < 0:
            self._health = 0
        if self._health == 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"Remaining health: {self._health}")

    def heal(self,healing_amount):
        if self._health == 0:
            print("A defeated character cannot heal!")
        else:
            self._health = healing_amount + self._health
            if self._health > self.max_health:
                self._health = self.max_health
            print(f"Updated health: {self._health}")

    def attack_enemy(self, enemy):
        if self.health == 0:
            print(f"{self.name} has been defeated and cannot attack!")
        elif enemy.health == 0:
            print("The enemy has already been defeated!")
        else:
            enemy.health = enemy.health - self.attack
            if enemy.health < 0:
                enemy.health = 0
            if enemy.health == 0:
                print(f"{enemy.name} has been defeated!")
            else:
                print(f"Enemy's remaining health: {enemy.health}")
            return enemy.health

class Enemy:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
    
    def take_damage(self,damage):
        if self.health == 0:
            print(f"{self.name} has already been defeated!")
        else:
            self.health = self.health - damage
            if self.health < 0:
                self.health = 0
            if self.health == 0:
                print(f"{self.name} has been defeated!")
            else:
                print(f"{self.name}'s remaining health: {self.health}")

    def attack_character(self,character):
        if character.health == 0:
            print(f"{character.name} has already been defeated!")
        else:
            character.health -= self.attack
            if character.health < 0:
                character.health = 0
            if character.health == 0:
                print(f"{character.name} has been defeated!")
            else:
                print(f"{character.name}'s remaining health: {character.health}")

armin = Character("Armin", "Warrior", 1, 100, 100, 10, 50)

armin.health = 500
print(armin.health)