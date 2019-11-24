import General_Movement
import colorama
import Characters
import Battle

def print_title():
    print(colorama.Fore.LIGHTCYAN_EX + '''
     ______>>> POLIQUEST <<<_______
     |      The fun has just      |
     |           BEGAN            |
     |____________________________|
    ''')
    print(colorama.Style.RESET_ALL)
    # Usato per resettare ai volori iniziali gli elementi


def target_menu(level, enemy_list):
    hero_x = Characters.Hero.x
    hero_y = Characters.Hero.y
    possible_choices = []
    # E' possibile ottimizzare facendo scorrere solo un volta la lista e includendo tutti gli if accorpati per ogni direzione
    print("Possible choices: ")
    for enemy in enemy_list:
        if (level[hero_x - 1][hero_y].content == "!" or "%") and enemy.x == hero_x - 1 and enemy.y == hero_y:
            print(f">>{enemy.name}, up ")
            possible_choices.append("up")
        elif (level[hero_x + 1][hero_y].content == "!" or "%") and enemy.x == hero_x + 1 and enemy.y == hero_y:
            print(f">>{enemy.name}, down")
            possible_choices.append("down")
        elif (level[hero_x][hero_y + 1].content == "!" or "%") and enemy.x == hero_x and enemy.y == hero_y + 1 :
            print(f">>{enemy.name}, right ")
            possible_choices.append("right")
        elif (level[hero_x][hero_y - 1].content == "!" or "%") and enemy.x == hero_x and enemy.y == hero_y - 1:
            print(f">>{enemy.name}, left ")
            possible_choices.append("left")

    target = input('Target (type his position or "return" to go back to the previous menu): ')
    # if target == possible_choices[:] : # Confronta con le opzioni disponibili e mi dice se l'input e' valido
    # Il controllo nella lista era al quanto ridondante
    # Sulla base di target passo alla funzione batle_menu la lista nemici e il nemico scelto
    if target == "up":
        for enemy in enemy_list: # up
            if enemy.x == hero_x - 1 and enemy.y == hero_y:
                battle_menu(level, enemy_list, enemy)
    elif target == "down":
        for enemy in enemy_list:  # down
            if enemy.x == hero_x + 1 and enemy.y == hero_y:
                battle_menu(level, enemy_list, enemy)
    elif target == "right":
        for enemy in enemy_list:  # right
            if enemy.x == hero_x  and enemy.y == hero_y + 1:
                battle_menu(level, enemy_list, enemy)
    elif target == "left":
        for enemy in enemy_list:  # right
            if enemy.x == hero_x and enemy.y == hero_y - 1:
                battle_menu(level, enemy_list, enemy)
    elif target == "return":
        pass # Cosi facendo esco dalla funzione e ritorno al menu
    else:
        print("Invalid input\n")
        target_menu(level, enemy_list)
# Nel caso in cui l'input non e' un nemico presente


def battle_menu(level, enemy_list, enemy):
    battle = True
    turn = 1
    effective_turn = 0
    while battle :
        if enemy.hp <= 0:
            print("!!! CONGRATULATIONS !!!\n")
            for to_delete in enemy_list:
                if to_delete.x == enemy.x:
                    if to_delete.y == enemy.y:
                        enemy_list.remove(enemy)
                        level[enemy.x][enemy.y].content = " "
            return
        if Characters.Hero.hp == 0:
            print("Such a shame, you LOST!!!")
            break
        show_hp(enemy)
        print(f"Turn:{turn}")
        choice = input('''
           _______________________
           ||Possible actions:  ||
           ||                   ||
           || 1)Attack          ||
           || 2)Magic           ||
           || 3)Skills          ||
           || 4)Items           ||
           || 5)Run             ||            
           ||___________________||
           What's your choice HERO? 
           ''')
        for x in range(2):
            if choice == "1": # Negli effective_turn pari agisce hero,
                hit, actor = Battle.Hit_calculation_Enemy(enemy, effective_turn)
                if hit :
                    damage, crit, actor = Battle.Damage_Calculation_Enemy(enemy, effective_turn)
                    enemy.hp -= damage
                    if crit == 1:
                        print(f"Awesome strike {actor} critted for {damage}\n ")
                    else:
                        print(f"Great strike {actor} dealt {damage}\n ")
                else:
                    print(f"{actor} you missed the target\n")
            effective_turn += 1
        turn += 1

def show_hp(enemy):
    hp_value_enemy = int(enemy.hp/10)
    hp_value_hero = int(Characters.Hero.hp/10)
    enemy_hp = ""
    hero_hp = ""
    for n in range(hp_value_enemy):
        enemy_hp += "O"
    for n in range(10 - hp_value_enemy):
        enemy_hp += "X"
    for n in range(hp_value_hero):
        hero_hp += "O"
    for n in range(10 - hp_value_hero):
        hero_hp += "X"
    print(f'''
    {enemy.name}: [{enemy_hp}] {enemy.hp}/{enemy.max_hp}

    {Characters.Hero.name}: [{hero_hp}] {Characters.Hero.hp}/{Characters.Hero.max_hp}
    ''')

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
