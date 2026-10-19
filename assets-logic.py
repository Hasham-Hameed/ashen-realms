name = "Armin"
character_class = "Warrior"
level = 1
health = 100
gold = 50
max_health = 100

damage = int(input("How much damage an enemy deals: "))
def take_damage(health,damage):
    new_health = health - damage
    if new_health < 0:
        new_health = 0
    return new_health

health = take_damage(health,damage)
print(f"Remaining health: {health}")


if health == 0:
    print("Your character is defeated!")
else:
    healing_amount = int(input("How much a potion heals: "))
    def heal(health,healing_amount,max_health):
        updated_health = health + healing_amount
        if updated_health > max_health:
            updated_health = max_health
        return updated_health
    health = heal(health,healing_amount,max_health)
    print(f"Health: {health}")

def show_character(name,character_class,level,health,gold):
    print("===== Character Status =====")
    print(f"Name: {name}")
    print(f"Class: {character_class}")
    print(f"Level: {level}")
    print(f"Health: {health}")
    print(f"Gold: {gold}")
    print(f"Max health: {max_health}")
    print("============================")

show_character(name,character_class,level,health,gold)
