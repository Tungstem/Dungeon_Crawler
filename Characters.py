class Enemy:
    def __init__(self, x, y, name, max_hp, hp, max_mp, mp, body, mind, luck):
        self.x = x
        self.y = y
        self.name = name  # Il nome della creatura
        self.max_hp = max_hp  # Massimo numero di hit points
        self.hp = hp  # Il numero di hit points attuale
        self.max_mp = max_mp  # Massimo numero di magic points
        self.mp = mp  # In futuro se aggiungo dei nemici caster
        self.body = body  # Un mix tra STR e DEX piu' avanti probabilmente le separero'
        self.mind = mind  # Un mix tra INT e WIS come sopra
        self.luck = luck  # Influenza la probabilita' dei colpi critici e di schivare


def initialize_enemy(name):
    if name == "Bat":
        return 12, 0, 6, 3, 2
    elif name == "SkellyBoy":
        return 25, 0, 15, 2, 6
    elif name == "Spider":
        return 15, 0, 13, 6, 5
    elif name == "SpookyGhost":
        return 15, 0, 1, 19, 23
    elif name == "Mummy":
        return 25, 0, 15, 14, 10
    elif name == "Slime":
        return 9, 0, 30, 20, 3
    elif name == "PolipoPoli":
        return 100, 100, 50, 50, 99
    else:
        return 0,0,0,0,0

class Hero:
    def __init__(self, x, y, name, max_hp, hp, max_mp, mp, body, mind, luck):
        self.x = x
        self.y = y
        self.name = name  # Il nome della creatura
        self.max_hp = max_hp  # Massimo numero di hit points
        self.hp = hp  # Il numero di hit points attuale
        self.max_mp = max_mp  # Massimo numero di magic points
        self.mp = mp  # In futuro se aggiungo dei nemici caster
        self.body = body  # Un mix tra STR e DEX piu' avanti probabilmente le separero'
        self.mind = mind  # Un mix tra INT e WIS come sopra
        self.luck = luck