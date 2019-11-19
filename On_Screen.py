import General_Movement
import colorama
import Characters

def print_title():
    print(colorama.Fore.LIGHTCYAN_EX + '''
     ______>>> POLIQUEST <<<_______
     |      The fun has just      |
     |           BEGAN            |
     |____________________________|
    ''')
    print(colorama.Style.RESET_ALL)
    # Usato per resettare ai volori iniziali gli elementi


def battle_menu(level, enemy_list):
    hero_x = Characters.Hero.x
    hero_y = Characters.Hero.y
    possible_choices = []

    print("Possible choices: ")
    if level[hero_x - 1][hero_y].content == "!":
        for enemy in enemy_list:
            if enemy.x == hero_x - 1 and enemy.y == hero_y:
                print(f">>{enemy.name}, up ")
                possible_choices.append(enemy.name)
    if level[hero_x + 1][hero_y].content == "!":
        for enemy in enemy_list:
            if enemy.x == hero_x + 1 and enemy.y == hero_y:
                print(f">>{enemy.name}, down ")
                possible_choices.append(enemy.name)
    if level[hero_x][hero_y + 1].content == "!":
        for enemy in enemy_list:
            if enemy.x == hero_x and enemy.y == hero_y + 1:
                print(f">>{enemy.name}, right ")
                possible_choices.append(enemy.name)
    if level[hero_x][hero_y - 1].content == "!":
        for enemy in enemy_list:
            if enemy.x == hero_x and enemy.y == hero_y - 1:
                print(f">>{enemy.name}, left ")
                possible_choices.append(enemy.name)
    target = input("Target (type return to go back to the previous menu): ")
    if target == possible_choices[:] :
        pass 
    elif target == "return":
        pass # Cosi facendo esco dalla funzione e ritorno al menu
    else:
        print("Invalid input\n")
        battle_menu(level, enemy_list)
# Nel caso in cui l'input non e' un nemico presente



def item_menu():
    pass


def magic_menu():
    pass


def skills_menu():
    pass


def show_menu():
    choice = input('''
    _______________________
    ||Possible actions:  ||
    ||                   ||
    || 1)Move            ||
    || 2)Fight           ||
    || 3)Items           ||
    || 4)Magic           ||
    || 5)Skills          ||
    || 6)Exit            ||
    ||___________________||
    What's your choice HERO? 
    ''')
    return choice
