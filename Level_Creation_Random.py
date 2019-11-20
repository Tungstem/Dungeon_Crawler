import random
import colorama
import Characters


class Cell:
    def __init__(self, x, y, content):
        self.x = x
        self.y = y
        self.content = content  # Serve in futuro per indicare cosa contiene la cella
        # "#" = wall
        # " " = road
        # "!" = enemy
        # "@" = MC


def create_grid():
    row_range = random.randint(5, 10)
    column_range = random.randint(row_range, 25)  # in questo modo e' sempre un rettangolo
    grid = [[0 for x in range(column_range)] for y in range(row_range)]
    # For x in range (y_range) crea le colonne e for y ... crea le righe
    return grid, row_range, column_range


def initialize_grid(grid, row_range, column_range):
    rappresentation = [" ", "#"]
    for x in range(row_range):
        for y in range(column_range):
            grid[x][y] = Cell(x, y, random.choice(rappresentation))
    for x in range(row_range):
        for y in range(column_range):
            if x == row_range -1:
                grid[x][y].content = "#"
            if y == column_range -1:
                grid[x][y].content = "#"
            if x == 0:
                grid[x][y].content = "#"
            if y == 0:
                grid[x][y].content = "#"


def draw_grid(grid, row_range, column_range):
    for row in range(row_range):
        for column in range(column_range):
            if (column == column_range - 1):
                print(colorama.Fore.WHITE + f" {grid[row][column].content} |")
            else:
                if grid[row][column].content == "!":
                    print(colorama.Fore.RED + f"| {grid[row][column].content} |", end="")
                elif grid[row][column].content == "%":
                    print(colorama.Fore.MAGENTA + f"| {grid[row][column].content} |", end="")
                elif grid[row][column].content == "@":
                    print(colorama.Fore.YELLOW + f"| {grid[row][column].content} |", end="")
                else:
                    print(colorama.Fore.WHITE + f"| {grid[row][column].content} |", end="")
        # print("")
    # print(colorama.Style.RESET_ALL + "") # in questo modo resetto il colore del resto delle scritte
    print(colorama.Fore.CYAN)


def fill_grid(current_grid, row_range, column_range):
    free_cells = []
    enemy_list = []
    enemy_names = ["Bat", "SkellyBoy", "Spider", "SpookyGhost", "Mummy", "Slime", "PolipoPoli"]
    for row in range(row_range):
        for column in range(column_range):
            if current_grid[row][column].content == " ":
                free_cells.append([row, column])
    limit = len(free_cells)
    num_enemies = random.randint(1, limit)
    for iteration in range(num_enemies):  # genera un numero casuale di nemici
        chosen = random.choice(free_cells)  # sceglie a random tra le posizioni libere
        free_cells.remove(chosen)  # in questo modo non puo' uscire la stessa cella due volte
        row, column = chosen
        current_grid[row][column].content = "!"  # modifico il contenuto della cella scelta
        enemy = Characters.Enemy(row, column, random.choice(enemy_names), 0, 0, 0, 0, 0, 0, 0)
        if enemy.name == "PolipoPoli":
            enemy_names.remove("PolipoPoli")  # Essendo un nemico unice se spawna non ne puo' creare un altro
            current_grid[row][column].content = "%"
        enemy.max_hp, enemy.max_mp, enemy.body, enemy.mind, enemy.luck = Characters.initialize_enemy(enemy.name)
        enemy.hp, enemy.mp = enemy.max_hp, enemy.max_mp
        enemy_list.append(enemy)  # Aggiungo il mio nemico all'interno della lista
    chosen = random.choice(free_cells)  # tra le restanti ne cerco un adove posizionare MC
    row, column = chosen
    Characters.Hero.x, Characters.Hero.y = row, column
    current_grid[row][column].content = "@"
    # Inizializzo hero momenaneamente per verificare che tutto funzioni
    Characters.Hero.name = "H_Jack"
    Characters.Hero.max_hp = 100
    Characters.Hero.hp = 100
    Characters.Hero.max_mp = 100
    Characters.Hero.mp = 100
    Characters.Hero.body = 100
    Characters.Hero.mind = 100
    Characters.Hero.luck = 100
    # Ricordati di rimuoverlo
    return enemy_list  # restituisco a main le coordinate di MC in modo da potermi muovere
