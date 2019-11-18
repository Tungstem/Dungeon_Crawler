import random


class Cell:
    def __init__(self, x, y, content):
        self.x = x
        self.y = y
        self.content = content  # Serve in futuro per indicare cosa contiene la cella
        # 0 = wall
        # 1 = road
        # 2 = enemy
        # 3 = MC


def create_grid():
    grid = [[0 for x in range(10)] for y in range(10)]
    return grid


def initialize_grid(grid):
    for x in range(10):
        for y in range(10):
            grid[x][y] = Cell(x, y, random.randint(0, 1))


def draw_grid(grid):
    for row in range(10):
        for column in range(10):
            if (column == 10):
                if grid[row][column].content == 0:
                    print(" # |")
                elif grid[row][column].content == 2:
                    print(" ! |")
                elif grid[row][column].content == 3:
                    print(" @ |")
                else:
                    print("   |")
            if grid[row][column].content == 0:
                print("| # |", end="")
            elif grid[row][column].content == 2:
                print("| ! |", end="")
            elif grid[row][column].content == 3:
                print("| @ |", end="")
            else:
                print("|   |", end="")
        print("")


def fill_grid(current_grid):
    free_cells = []
    for row in range(10):
        for column in range(10):
            if current_grid[row][column].content == 1:
                free_cells.append([row, column])
    limit = len(free_cells)
    num_enemies = random.randint(1, limit)
    for iteration in range(num_enemies): #genera un numero casuale di nemici
        chosen = random.choice(free_cells) #sceglie a random tra le posizioni libere
        free_cells.remove(chosen) #in questo modo non puo' uscire la stessa cella due volte
        row, column = chosen
        current_grid[row][column].content = 2 #modifico il contenuto della cella scelta
    chosen = random.choice(free_cells) #tra le restanti ne cerco un adove posizionare MC
    row, column = chosen
    current_grid[row][column].content = 3
    return row, column #restituisco a main le coordinate di MC in modo da potermi muovere