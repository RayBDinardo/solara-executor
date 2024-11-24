import sys

def print_slow(text):
    for letter in text:
        print(letter, end='')
        sys.stdout.flush()
    print()

def start_game():
    print_slow("Welcome to Solara: The Adventure")
    print_slow("You are Solara, a brave adventurer in search of the legendary Amulet of Light.")
    print_slow("Your journey will take you through dark forests, snowy mountains, and mysterious ruins.")
    print_slow("Are you ready to begin your adventure?\n")
    choice = input("Type 'yes' to start or 'no' to exit: ").lower()
    if choice == 'yes':
        forest()
    elif choice == 'no':
        print_slow("Maybe another time. Goodbye!")
        sys.exit()
    else:
        print_slow("Invalid input.")
        start_game()

def forest():
    print_slow("\nYou find yourself at the edge of a dense forest. You can hear sounds of creatures all around.")
    print_slow("There is a path that goes into the forest and another that goes around it.")
    choice = input("What do you want to do? Type 'enter' to go into the forest or 'around' to avoid it: ").lower()
    if choice == 'enter':
        dark_path()
    elif choice == 'around':
        alternative_route()
    else:
        print_slow("Invalid input.")
        forest()

def dark_path():
    print_slow("\nYou decide to take the dark path into the forest.")
    print_slow("The path is narrow and there is barely any light. Suddenly, you hear a growl.")
    print_slow("A wolf appears in your path.")
    choice = input("Do you want to confront it ('confront') or look for an alternative route ('look'): ").lower()
    if choice == 'confront':
        confront_wolf()
    elif choice == 'look':
        look_route()
    else:
        print_slow("Invalid input.")
        dark_path()

def confront_wolf():
    print_slow("\nYou decide to confront the wolf with bravery.")
    print_slow("After a brief fight, you manage to scare it away.")
    print_slow("You continue your path and find an abandoned cabin.")
    choice = input("Do you want to investigate the cabin ('investigate') or keep going ('continue'): ").lower()
    if choice == 'investigate':
        cabin()
    elif choice == 'continue':
        mountain()
    else:
        print_slow("Invalid input.")
        confront_wolf()

def look_route():
    print_slow("\nYou decide to look for an alternative route to avoid the wolf.")
    print_slow("You walk for a while and find a river.")
    choice = input("Do you want to follow the river ('follow') or go back to the path ('back'): ").lower()
    if choice == 'follow':
        river()
    elif choice == 'back':
        dark_path()
    else:
        print_slow("Invalid input.")
        look_route()

def cabin():
    print_slow("\nYou enter the cabin and find an ancient map.")
    print_slow("The map shows the location of the Eldoria Ruins where the Amulet of Light is located.")
    choice = input("Do you want to follow the map to the ruins ('follow') or go back to the forest ('back'): ").lower()
    if choice == 'follow':
        ruins()
    elif choice == 'back':
        confront_wolf()
    else:
        print_slow("Invalid input.")
        cabin()

def mountain():
    print_slow("\nYou decide to continue towards the mountain.")
    print_slow("The ascent is tough and the weather worsens. You reach the summit where you see an ancient door.")
    choice = input("Do you want to open the door ('open') or look for another entrance ('look'): ").lower()
    if choice == 'open':
        mysterious_door()
    elif choice == 'look':
        explore_stones()
    else:
        print_slow("Invalid input.")
        mountain()

def ruins():
    print_slow("\nYou follow the map to the Eldoria Ruins.")
    print_slow("The ruins are guarded by a mystical guardian.")
    choice = input("Do you want to fight the guardian ('fight') or try to negotiate ('negotiate'): ").lower()
    if choice == 'fight':
        fight_guardian()
    elif choice == 'negotiate':
        negotiate_guardian()
    else:
        print_slow("Invalid input.")
        ruins()

def fight_guardian():
    print_slow("\nYou confront the guardian with courage.")
    print_slow("After an intense battle, you manage to defeat it.")
    print_slow("Inside the ruins, you find the Amulet of Light. You have triumphed!")
    good_ending()

def negotiate_guardian():
    print_slow("\nYou try to negotiate with the guardian.")
    print_slow("The guardian allows you to take the amulet in exchange for your promise to protect the land.")
    print_slow("You accept the deal and obtain the Amulet of Light. You have triumphed!")
    good_ending()

def mysterious_door():
    print_slow("\nYou open the door and a blinding light surrounds you.")
    print_slow("You are transported to a secret chamber where you find the Amulet of Light.")
    good_ending()

def explore_stones():
    print_slow("\nYou explore the stones around and discover a hidden passage.")
    print_slow("You follow the passage and find the Amulet of Light.")
    good_ending()

def river():
    print_slow("\nYou follow the river and find an abandoned boat.")
    choice = input("Do you want to use the boat to cross the river ('use') or keep walking ('walk'): ").lower()
    if choice == 'use':
        cross_river()
    elif choice == 'walk':
        keep_river()
    else:
        print_slow("Invalid input.")
        river()

def cross_river():
    print_slow("\nYou use the boat to cross the river.")
    print_slow("On the other side, you find an entrance to a lit cave.")
    choice = input("Do you want to enter the cave ('enter') or go back to the forest ('back'): ").lower()
    if choice == 'enter':
        cave()
    elif choice == 'back':
        look_route()
    else:
        print_slow("Invalid input.")
        cross_river()

def keep_river():
    print_slow("\nYou keep walking along the river and find an abandoned village.")
    print_slow("In the center of the village, there is a statue with a secret compartment.")
    choice = input("Do you want to open the compartment ('open') or ignore the statue ('ignore'): ").lower()
    if choice == 'open':
        statue_amulet()
    elif choice == 'ignore':
        print_slow("You decide to ignore the statue and continue your path, but you do not find the amulet.")
        bad_ending()
    else:
        print_slow("Invalid input.")
        keep_river()

def cave():
    print_slow("\nYou enter the cave and find the Amulet of Light shining brightly.")
    good_ending()

def statue_amulet():
    print_slow("\nYou open the compartment and find the Amulet of Light inside the statue.")
    good_ending()

def confront_wolf():
    print_slow("\nYou decide to confront the wolf with bravery.")
    print_slow("After a brief fight, you manage to scare it away.")
    print_slow("You continue your path and find an abandoned cabin.")
    cabin()

def good_ending():
    print_slow("\nCongratulations! You have successfully completed your adventure and obtained the Amulet of Light.")
    sys.exit()

def bad_ending():
    print_slow("\nYour adventure ends here without obtaining the Amulet of Light.")
    sys.exit()

start_game()
