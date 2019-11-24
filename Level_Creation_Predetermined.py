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


class Level:
    def __init__(self, name, grid):
        self.name = name
        self.grid = grid


def level_selector(level_index):
    current_level = open(f"Level_{level_index}.txt", "r")
    maps = [Level("", []) for i in range(3)]  # Una lista inizializzata con degli oggetti level, il range deve essere
    # specificato sopra e corrisponde al nummero di diverse var nel file
    for i in range(3):  # Come sopra
        name = current_level.read(6)
        out = current_level.read(4)  # In questo modo dopo non devo tenere conto di newline
        coordinate = out.split(",")
        # Impara a usare map()
        grid = [[int(current_level.read(2)) for column in range(int(coordinate[1]))] for row in
                range(int(coordinate[0]))]
        # Il cast mi permette di prelevare i valori con il newline e considerare solo il  numero
        maps[i].name = name
        maps[i].grid = grid
    obj = random.choice(maps)
    row_limit, column_limit = int(coordinate[0]), int(coordinate[1])
    current_level.close()
    return obj.grid, row_limit, column_limit
# Prova a modificare la lettura in modo rendere piu' agevole la scrittura


def converter(level, row_limit, column_limit):
    for row in range(row_limit):
        for column in range(column_limit):
            if level[row][column] == 1:
                content = "#"
            elif level[row][column] == 2:
                content = "!"
            elif level[row][column] == 3:
                content = "@"
                Characters.Hero.x, Characters.Hero.y = row, column # Da a Hero le sue coordinate
            elif level[row][column] == 4:
                content = "£"
            else:
                content = " "
            level[row][column] = Cell(row, column, content)
    return level

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
                elif grid[row][column].content == "£":
                    print(colorama.Fore.LIGHTYELLOW_EX + f"| {grid[row][column].content} |", end="")
                elif grid[row][column].content == "@":
                    print(colorama.Fore.YELLOW + f"| {grid[row][column].content} |", end="")
                else:
                    print(colorama.Fore.WHITE + f"| {grid[row][column].content} |", end="")
        # print("")
    # print(colorama.Style.RESET_ALL + "") # in questo modo resetto il colore del resto delle scritte
    print(colorama.Fore.CYAN)


def fill_stat(current_grid, row_range, column_range):
    enemy_list = []
    enemy_names = ["Bat", "SkellyBoy", "Spider", "SpookyGhost", "Mummy", "Slime", "PolipoPoli"]
    # Soluzione momentanea, in futuro intendo inserirli da file i mostri e le loro stat
    for row in range(row_range):
        for column in range(column_range):
            if current_grid[row][column].content == "!":
                enemy = Characters.Enemy(row, column, random.choice(enemy_names), 0, 0, 0, 0, 0, 0, 0)
                if enemy.name == "PolipoPoli":
                    enemy_names.remove("PolipoPoli")  # Un nemico potrebbe trasformarsi in Polipoli
                    current_grid[row][column].content = "%"
                enemy.max_hp, enemy.max_mp, enemy.body, enemy.mind, enemy.luck = Characters.initialize_enemy(enemy.name)
                enemy.hp, enemy.mp = enemy.max_hp, enemy.max_mp
                enemy_list.append(enemy)
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
