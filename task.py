class Player:
    def _init_(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has died.")
        else:
            print(f"{self.name} has {self.health} health left.")

    def pick_up_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item}.")

    def show_inventory(self):
        print("Inventory: ", self.inventory)


def introduction():
    print("Welcome to the Adventure Game!")
    name = input("Enter your character's name: ")
    player = Player(name)
    print(f"Welcome, {player.name}!")
    return player


def first_decision(player):
    print("You find yourself at a crossroad.")
    print("1. Go left")
    print("2. Go right")
    choice = input("What do you want to do? (1/2): ")

    if choice == "1":
        left_path(player)
    elif choice == "2":
        right_path(player)
    else:
        print("Invalid choice. Try again.")
        first_decision(player)


def left_path(player):
    print("You encounter a wild beast!")
    print("1. Fight the beast")
    print("2. Run away")
    choice = input("What do you want to do? (1/2): ")

    if choice == "1":
        print("You fight bravely but take damage.")
        player.take_damage(20)
        if player.health > 0:
            print("You defeated the beast and find a treasure.")
            player.pick_up_item("Treasure")
        else:
            print("Game Over")
    elif choice == "2":
        print("You run away safely.")
        first_decision(player)
    else:
        print("Invalid choice. Try again.")
        left_path(player)


def right_path(player):
    print("You find a puzzle blocking your way.")
    answer = input("Solve this puzzle: What is 2 + 2? ")

    if answer == "4":
        print("Correct! You move forward and find a healing potion.")
        player.pick_up_item("Healing Potion")
    else:
        print("Wrong answer. Try again.")
        right_path(player)


def quest(player):
    print("You have a quest to find the magical amulet.")
    print("1. Search the forest")
    print("2. Search the cave")
    choice = input("What do you want to do? (1/2): ")

    if choice == "1":
        search_forest(player)
    elif choice == "2":
        search_cave(player)
    else:
        print("Invalid choice. Try again.")
        quest(player)


def search_forest(player):
    print("You search the forest and find a group of bandits.")
    print("1. Fight the bandits")
    print("2. Sneak past them")
    choice = input("What do you want to do? (1/2): ")

    if choice == "1":
        print("You fight bravely but take damage.")
        player.take_damage(30)
        if player.health > 0:
            print("You defeated the bandits and find the magical amulet.")
            player.pick_up_item("Magical Amulet")
        else:
            print("Game Over")
    elif choice == "2":
        print("You sneak past the bandits and find the magical amulet.")
        player.pick_up_item("Magical Amulet")
    else:
        print("Invalid choice. Try again.")
        search_forest(player)


def search_cave(player):
    print("You search the cave and find a sleeping dragon.")
    print("1. Steal the treasure")
    print("2. Leave the cave")
    choice = input("What do you want to do? (1/2): ")

    if choice == "1":
        print("You steal the treasure but wake the dragon.")
        player.take_damage(50)
        if player.health > 0:
            print("You escape with the treasure.")
            player.pick_up_item("Dragon Treasure")
        else:
            print("Game Over")
    elif choice == "2":
        print("You leave the cave safely.")
        quest(player)
    else:
        print("Invalid choice. Try again.")
        search_cave(player)


def main():
    player = introduction()
    first_decision(player)
    quest(player)
    print("Thank you for playing!")


if _name_ == "_main_":
    main()
