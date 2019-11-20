import Characters
import random


def Hit_calculation_Enemy(enemy): # Ritorna True se lo colpisce
    evade_chance = enemy.body + enemy.luck
    evade_chance = int(evade_chance/2)
    if enemy.luck > 50:
        evade_chance +=1
    bonus = int(Characters.Hero.luck/2)
    hit_chance = random.randint(bonus, bonus + Characters.Hero.body)
    if hit_chance >= evade_chance:
        return True
    else:
        return False

def Damage_Calculation_Enemy(enemy):
    print("Colpito")
    pass