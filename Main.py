import Level_Creation
import On_Screen
import General_Movement


playing=True
On_Screen.print_title()
level = Level_Creation.create_grid()
Level_Creation.initialize_grid(level)
x, y = Level_Creation.fill_grid(level)
while playing == True:
    Level_Creation.draw_grid(level)
    choice = On_Screen.show_menu()
    if choice == "1":
        x, y = General_Movement.hero_movement(x, y, level) #I movimenti sono gestiti direttamente nel modulo on screen
    if choice == "2":
        On_Screen.item_menu()
    if choice == "3":
        On_Screen.magic_menu()
    if choice == "4":
        On_Screen.skills_menu()
    if choice == "5":
        playing = False  #In questo modo dico al gioco di fermarsi


#Cose che mancano:
# gestione delle entita' player(MC) ed enemy
# organizzare meglio la creazione della grid di gioco
# comprendere come usare al meglio pygames
# i vari menu di gioco
# un sistema di pathing base per i nemici
# tutto il sistema di combattimento