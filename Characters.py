class Enemy:
    def __init__(self, x, y, name, hp, mp, body, mind):
        self.x = x
        self.y = y
        self.name = name  # Il nome della creatura
        self.hp = hp  # Il numero di hit points
        self.mp = mp  # In futuro se aggiungo dei nemici caster
        self.body = body  # Un mix tra STR e DEX piu' avanti probabilmente le separero'
        self.mind = mind  # Un mix tra INT e WIS come sopra

class Hero:
    def __init__(self, x, y, name, hp, mp, body, mind):
        self.x = x
        self.y = y
        self.name = name  # Il nome della creatura
        self.hp = hp  # Il numero di hit points
        self.mp = mp  # In futuro se aggiungo dei nemici caster
        self.body = body  # Un mix tra STR e DEX piu' avanti probabilmente le separero'
        self.mind = mind  # Un mix tra INT e WIS come sopra