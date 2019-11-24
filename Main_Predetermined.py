import Level_Creation_Predetermined
import On_Screen
import General_Movement
import Characters
import random

on_level = True
playing = True
On_Screen.print_title()
current_level = 1
while playing:
    level, level_row, level_column = Level_Creation_Predetermined.level_selector(current_level)
    Level_Creation_Predetermined.converter(level, level_row, level_column)
    enemy_list = Level_Creation_Predetermined.fill_stat(level, level_row, level_column)
    # Ritorna la lista dei nemici in modo da poter passare ad altre funzioni le stat dei nemici presenti
    while on_level and Characters.Hero.hp >0 : # On-level serve per cambiare il livello
        print(f"Level: {current_level}")
        Level_Creation_Predetermined.draw_grid(level, level_row, level_column)
        choice = On_Screen.show_menu()
        if choice == "1":
            General_Movement.hero_movement(level, level_row, level_column)
        # I movimenti sono gestiti direttamente nel modulo On Screen
        if choice == "2":
            Level_Creation_Predetermined.draw_grid(level, level_row, level_column)
            On_Screen.target_menu(level, enemy_list)
        if choice == "3":
            On_Screen.item_menu()
        if choice == "4":
            On_Screen.magic_menu()
        if choice == "5":
            On_Screen.skills_menu()
        if choice == "6":
            playing = False  # In questo modo dico al gioco di fermarsi
            break
        # TO DO LIST:
        # comprendere come usare pygames
        # i vari menu di gioco
        # un sistema di pathing base per i nemici
        # migliorare gli algoritmi per il calcolo del danno
        # aggiungere la condizione per il passaggio di livello ossia raggiungere le scale
