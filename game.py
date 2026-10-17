name = "Armin"
character_class = "Warrior"
level = 1
health = 100
attack = 10
gold = 50

print("==== RPG Character ====")
print(f"Name: {name}")
print(f"Class: {character_class}")
print(f"Level: {level}")
print(f"Health: {health}")
print(f"Attack power: {attack}")
print(f"Gold: {gold}")

damage = int(input("How much damage got from enemy: "))
remaining_health = health - damage
if remaining_health < 0:
    remaining_health = 0

print("==== Battle Results ====")
print(f"Character's name: {name}")
print(f"Damage received: {damage}")
print(f"Remaining health: {remaining_health}")