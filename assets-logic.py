health = 100
max_health = 100
damage = int(input("How much damage an enemy deals: "))
health = health - damage
if health < 0:
    health = 0

if health == 0:
    print("Your character is defeated...")

else:
    healing = int(input("How a much health points does the healing costs: "))
    new_health = health + healing
    if new_health > max_health:
        new_health = max_health
    print(f"The health of the character is {new_health}")