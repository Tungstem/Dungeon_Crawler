import Characters
import random


# entrambe le funzioni sono nei riguardi del danno fisico ricodati di aggiungere le altre
def Hit_calculation_Enemy(enemy, turn):  # Ritorna True se lo colpisce
    if turn % 2 == 0:
        defender = enemy
        attacker = Characters.Hero
        actor = Characters.Hero.name
    else:
        defender = Characters.Hero
        attacker = enemy
        actor = enemy.name
    evade_chance = defender.body + defender.luck
    evade_chance = int(evade_chance / 2)
    if defender.luck > 50:
        evade_chance += 1
    bonus = int(attacker.luck / 2)
    hit_chance = random.randint(bonus, bonus + attacker.body)
    if hit_chance >= evade_chance:
        return True, actor
    else:
        return False, actor


def Damage_Calculation_Enemy(enemy, turn):
    if turn % 2 == 0:
        defender = enemy
        attacker = Characters.Hero
        actor = Characters.Hero.name
    else:
        defender = Characters.Hero
        attacker = enemy
        actor = enemy.name
    possibilities = []
    for x in range(attacker.luck):
        possibilities.append(1)
    for x in range(100 - attacker.luck):
        possibilities.append(0)
    # Piu' sei fortunato e piu' possibilita hai di crittare
    crit = random.choice(possibilities)
    if attacker.body > defender.body:
        damage = attacker.body - defender.body * 2 * int(crit)
    else:
        damage = 0
    return damage, crit, actor
