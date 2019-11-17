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


def draw_grid(grid, row_range, column_range):
    for row in range(row_range):
        for column in range(column_range):
            if (column == column_range - 1):
                if grid[row][column].content == "!":
                    print(colorama.Fore.RED + f" {grid[row][column].content} |")
                elif grid[row][column].content == "@":
                    print(colorama.Fore.YELLOW + f" {grid[row][column].content} |")
                else:
                    print(colorama.Fore.WHITE + f" {grid[row][column].content} |")
            else:
                if grid[row][column].content == "!":
                    print(colorama.Fore.RED + f"| {grid[row][column].content} |", end="")
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
    enemy_names = ["Bat", "SkellyBoy", "Spider", "SpookyGhost", "Mummy"]
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
        enemy = Characters.Enemy(row, column, random.choice(enemy_names), 10, 0, 5, 3)
        # Il metodo di assegnazione e' provvisorio
        enemy_list.append(enemy) # Aggiungo il mio nemico all'interno della lista
    chosen = random.choice(free_cells)  # tra le restanti ne cerco un adove posizionare MC
    row, column = chosen
    Characters.Hero.x, Characters.Hero.y = row, column
    current_grid[row][column].content = "@"
    return enemy_list  # restituisco a main le coordinate di MC in modo da potermi muovere
