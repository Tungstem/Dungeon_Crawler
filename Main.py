import Level_Creation_Random
import On_Screen
import General_Movement
import Characters


playing = True
On_Screen.print_title()
level, level_row, level_column = Level_Creation_Random.create_grid()
Level_Creation_Random.initialize_grid(level, level_row, level_column)
enemy_list = Level_Creation_Random.fill_grid(level, level_row, level_column)
# Ritorna la lista dei nemici in modo da poter passare ad altre funzioni le stat dei nemici presenti

while playing:

    # Momentaneamente usato per vedere se funziona la lista enemy
    #for x in enemy_list:
    #    print(x.name)
    #    print(x.x, x.y, x.max_hp, x.max_mp, x.body, x.mind, x.luck)


    Level_Creation_Random.draw_grid(level, level_row, level_column)
    choice = On_Screen.show_menu()
    if choice == "1":
        General_Movement.hero_movement(level, level_row, level_column)
    # I movimenti sono gestiti direttamente nel modulo On Screen
    if choice == "2":
        Level_Creation_Random.draw_grid(level, level_row, level_column)
        On_Screen.battle_menu(level, enemy_list)
    if choice == "3":
        On_Screen.item_menu()
    if choice == "4":
        On_Screen.magic_menu()
    if choice == "5":
        On_Screen.skills_menu()
    if choice == "6":
        playing = False  # In questo modo dico al gioco di fermarsi

    # Cose che mancano:
    # gestione delle entita' player(MC) ed enemy
    # organizzare meglio la creazione della grid di gioco
    # comprendere come usare al meglio pygames
    # i vari menu di gioco
    # un sistema di pathing base per i nemici
    # tutto il sistema di combattimento
