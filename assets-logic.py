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
        print(f"Remaining health: {self.health}")

    def heal(self,healing_amount):
        self.health = healing_amount + self.health
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"Updated health: {self.health}")
armin = Character("Armin","Warrior",1,100,100,10,50)
armin.take_damage(30)
armin.heal(20)
armin.show_status()



# damage = int(input("How much damage an enemy deals: "))
# def take_damage(health,damage):
#     new_health = health - damage
#     if new_health < 0:
#         new_health = 0
#     return new_health

# health = take_damage(health,damage)
# print(f"Remaining health: {health}")


# if health == 0:
#     print("Your character is defeated!")
# else:
#     healing_amount = int(input("How much a potion heals: "))
#     def heal(health,healing_amount,max_health):
#         updated_health = health + healing_amount
#         if updated_health > max_health:
#             updated_health = max_health
#         return updated_health
#     health = heal(health,healing_amount,max_health)
#     print(f"Health: {health}")

# def show_character(name,character_class,level,health,gold):
#     print("===== Character Status =====")
#     print(f"Name: {name}")
#     print(f"Class: {character_class}")
#     print(f"Level: {level}")
#     print(f"Health: {health}")
#     print(f"Gold: {gold}")
#     print(f"Max health: {max_health}")
#     print("============================")

# show_character(name,character_class,level,health,gold)
