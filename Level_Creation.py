import random
import colorama

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
    grid = [[0 for x in range(10)] for y in range(10)]
    return grid


def initialize_grid(grid):
    rappresentation = [" ", "#"]
    for x in range(10):
        for y in range(10):
            grid[x][y] = Cell(x, y, random.choice(rappresentation))


def draw_grid(grid):
    for row in range(10):
        for column in range(10):
            if (column == 10):
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
        print("")
    #print(colorama.Style.RESET_ALL + "") # in questo mod resetto il colore del resto delle scritte
    print(colorama.Fore.CYAN)
def fill_grid(current_grid):
    free_cells = []
    for row in range(10):
        for column in range(10):
            if current_grid[row][column].content == " ":
                free_cells.append([row, column])
    limit = len(free_cells)
    num_enemies = random.randint(1, limit)
    for iteration in range(num_enemies): # genera un numero casuale di nemici
        chosen = random.choice(free_cells) # sceglie a random tra le posizioni libere
        free_cells.remove(chosen) # in questo modo non puo' uscire la stessa cella due volte
        row, column = chosen
        current_grid[row][column].content = "!" # modifico il contenuto della cella scelta
    chosen = random.choice(free_cells) # tra le restanti ne cerco un adove posizionare MC
    row, column = chosen
    current_grid[row][column].content = "@"
    return row, column # restituisco a main le coordinate di MC in modo da potermi muovere