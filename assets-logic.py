health = 100
max_health = 100
if health == max_health:
    print("Your health is already full!")
else:
    health_points = int(input("How many health points does the potion restores: "))
    current_health = health + health_points
    if current_health > max_health:
        current_health = max_health
    print(f"The health before potion is {health} and after is {current_health}")