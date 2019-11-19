import Level_Creation_Random
import Characters

def hero_movement(grid, row_range, column_range):

    Level_Creation_Random.draw_grid(grid, row_range, column_range)
    new_x = Characters.Hero.x
    new_y = Characters.Hero.y
    up = "UP  "
    down = "DOWN  "
    left = "LEFT  "
    right = "RIGHT  "

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
    elif choice == "right":
       new_y += 1
    elif choice == "down": # x + 1
        new_x += 1
    elif choice == "up":
       new_x -= 1
    else:
        print('''Invalid move
        
        ''')
        hero_movement(grid, row_range, column_range)

    if grid[new_x][new_y].content != " ":
        print('''
        ____________________________
        |                          |
        |La cella e' gia occupata  |
        |__________________________|
        ''')
        hero_movement(grid, row_range, column_range)
    else: # E' riferito all'if direttamente sopra
        grid[Characters.Hero.x][Characters.Hero.y].content = " "
        grid[new_x][new_y].content = "@"
        Characters.Hero.x, Characters.Hero.y = new_x, new_y
    # aggiorno le coordinate di Hero

def enemy_movement():
    pass