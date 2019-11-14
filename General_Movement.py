import Level_Creation
import colorama

def hero_movement(x_hero, y_hero, grid):

    Level_Creation.draw_grid(grid)
    new_x = x_hero
    new_y = y_hero
    up = "UP  "
    down = "DOWN  "
    left = "LEFT  "
    right = "RIGHT  "
    if x_hero + 1 > 9:
        down = "   "
    if x_hero - 1 < 0:
        up = "   "
    if y_hero - 1 > 9:
        left = "   "
    if y_hero + 1 < 0:
        right = "   "
    # Impediscono l'input di una direzione se questa porta fuori dal livello diventa obsoleto se miglioro l'algoritmo
    # per la creazione dei muri e delle vie
    choice = input(f'''
    _____________________________________
    |        |                 |        |
    |        |       {up}      |        |
    |        |                 |        |
    |________|_________________|________|
    |                 |                 |
    |     {left}      |     {right}     |
    |                 |                 |
    |_________________|_________________|
    |        |                 |        |
    |        |     {down}      |        |
    |        |                 |        |
    |________|_________________|________|    
    
    >Where do you wanna go? 
     ''')
# potrei ottimizare ulteriormente il print della cella occupata mediante l'uso di variabili come
# new_x = x_hero + eventuale_incremento e new_y = y_hero + eventuale_incremento

    if choice == "left": # y-1
       new_y -= 1
    if choice == "right":
       new_y += 1
    if choice == "down": # x + 1
        new_x += 1
    if choice == "up":
       new_x -= 1
    if grid[new_x][new_y].content != " ":
        print('''
        ____________________________
        |                          |
        |La cella e' gia occupata  |
        |__________________________|
        ''')
        hero_movement(x_hero, y_hero, grid)
    else:
        grid[x_hero][y_hero].content = " "
        grid[new_x][new_y].content = "@"
        return new_x, new_y
    # aggiorno le coordinate di Hero

def enemy_movement():
    pass