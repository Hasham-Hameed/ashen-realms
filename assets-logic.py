# health = 100
# max_health = 100
# damage = int(input("How much damage an enemy deals: "))
# health = health - damage
# if health < 0:
#     health = 0

# if health == 0:
#     print("Your character is defeated...")

# else:
#     healing = int(input("How a much health points does the healing costs: "))
#     new_health = health + healing
#     if new_health > max_health:
#         new_health = max_health
#     print(f"The health of the character is {new_health}")

'''def take_damage(health,damage):
    new_health = health - damage
    if new_health < 0:
        new_health = 0
    return new_health

result = take_damage(100,30)
print(f"Remaining health: {result}")

def heal(health,healing_amount,max_health):
    updated_health = health + healing_amount
    if updated_health > max_health:
        updated_health = max_health
    return updated_health
result = heal(60,25,100)
print(f"Health: {result}")'''

def show_character(name,character_class,level,health,gold):
    print("===== Character Status =====")
    print(f"Name: {name}")
    print(f"Class: {character_class}")
    print(f"Level: {level}")
    print(f"Health: {health}")
    print(f"Gold: {gold}")
    print("============================")

result = show_character("Armin","Warrior",2,85,75)
print(result)