import General_Movement
import colorama

def print_title():
    print(colorama.Fore.LIGHTCYAN_EX + '''
     ______>>> POLIQUEST <<<_______
     |      The fun has just      |
     |           BEGAN            |
     |____________________________|
    ''')
    print(colorama.Style.RESET_ALL)
    # Usato per resettare ai volori iniziali gli elementi


def battle_menu():
    pass


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
