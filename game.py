
# ==========================================
# CHARACTER CLASS
# ==========================================

class Character:

    # __init__ runs automatically whenever we create a Character object.
    # It receives the character's starting information.
    def __init__(self, name, character_class, level, health, max_health, attack, gold):

        # Store the received values inside this particular object.
        # self refers to the object being created.
        self.name = name
        self.character_class = character_class
        self.level = level
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.gold = gold

    # Display the character's current information.
    def show_status(self):
        print(f"Name: {self.name}")
        print(f"Character class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")

    # Reduce the character's health when they receive damage.
    def take_damage(self, damage):

        # Subtract the received damage from current health.
        self.health = self.health - damage

        # Health should never go below zero.
        if self.health < 0:
            self.health = 0

        # If health reaches zero, the character is defeated.
        if self.health == 0:
            print(f"{self.name} has been defeated!")
        else:
            # Otherwise, display the remaining health.
            print(f"Remaining health: {self.health}")

    # Restore some health to the character.
    def heal(self, healing_amount):

        # A defeated character cannot recover health.
        if self.health == 0:
            print("A defeated character cannot heal!")

        else:
            # Add the healing amount to current health.
            self.health = healing_amount + self.health

            # Health cannot exceed the character's maximum health.
            if self.health > self.max_health:
                self.health = self.max_health

            # Display the updated health.
            print(f"Updated health: {self.health}")

    # Character attacks an Enemy object.
    def attack_enemy(self, enemy):

        # A defeated character cannot attack.
        if self.health == 0:
            print(f"{self.name} has been defeated and cannot attack!")

        # Don't attack an enemy that is already defeated.
        elif enemy.health == 0:
            print("The enemy has already been defeated!")

        else:
            # Subtract the character's attack power from enemy health.
            # enemy refers to the Enemy object passed into this method.
            enemy.health = enemy.health - self.attack

            # Prevent enemy health from becoming negative.
            if enemy.health < 0:
                enemy.health = 0

            # Check whether the enemy has been defeated.
            if enemy.health == 0:
                print(f"{enemy.name} has been defeated!")
            else:
                # Display the enemy's remaining health.
                print(f"Enemy's remaining health: {enemy.health}")

            # Return the enemy's updated health.
            return enemy.health


# ==========================================
# ENEMY CLASS
# ==========================================

class Enemy:

    # Initialize an enemy whenever we create an Enemy object.
    def __init__(self, name, health, attack):

        # Store the enemy's information in its object.
        self.name = name
        self.health = health
        self.attack = attack

    # Reduce the enemy's health when it receives damage.
    def take_damage(self, damage):

        # An already defeated enemy cannot receive more damage.
        if self.health == 0:
            print(f"{self.name} has already been defeated!")

        else:
            # Subtract damage from the enemy's current health.
            self.health = self.health - damage

            # Prevent health from becoming negative.
            if self.health < 0:
                self.health = 0

            # Check whether the enemy has been defeated.
            if self.health == 0:
                print(f"{self.name} has been defeated!")
            else:
                # Display the enemy's remaining health.
                print(f"{self.name}'s remaining health: {self.health}")

    # Enemy attacks a Character object.
    def attack_character(self, character):

        # Don't attack a character that is already defeated.
        if character.health == 0:
            print(f"{character.name} has already been defeated!")

        else:
            # Subtract the enemy's attack power from character health.
            # character refers to the Character object passed into this method.
            character.health -= self.attack

            # Prevent character health from becoming negative.
            if character.health < 0:
                character.health = 0

            # Check whether the character has been defeated.
            if character.health == 0:
                print(f"{character.name} has been defeated!")
            else:
                # Display the character's remaining health.
                print(f"{character.name}'s remaining health: {character.health}")


# ==========================================
# TESTING OUR RPG SYSTEM
# ==========================================

# TEST 1: Armin survives the enemy's attack.

# Create a Character object named Armin.
armin = Character("Armin", "Warrior", 1, 100, 100, 10, 50)

# Create an Enemy object named Goblin.
goblin = Enemy("Goblin", 30, 5)

# Goblin attacks Armin.
# Goblin's attack power is 5, so Armin's health becomes 95.
goblin.attack_character(armin)


# TEST 2: Armin gets defeated.

# Create a new Armin object with only 5 health.
armin = Character("Armin", "Warrior", 1, 5, 100, 10, 50)

# Goblin attacks Armin again.
# Goblin deals 5 damage, reducing Armin's health to zero.
goblin.attack_character(armin)
