import random

key_character = ["Saber", "Archer", "Berserk"]

enemy_move = ["Attack", "Defend"]

characters = {
    "Saber" : (125, 40, 25),
    "Archer" : (75, 60, 10),
    "Berserk" : (110, 50, 20),
}

choose_main = input("Choose your character from the 3 characters: \nSaber, Archer or Berserk \n")
rund = True

while rund:
    #Vida del Aventurero elegido
    main_character = characters.get(choose_main)
    list(main_character)
    hp_main = main_character[0]

    #Vida del Enemigo ramdon
    random_enemy = random.choice(key_character)
    enemy = characters.get(random_enemy)
    list(enemy)
    hp_enemy = enemy[0]

    #Aparece el enemigo y hay una condicion para iniciar el juego
    print("-------------------------------------------")
    print("OH NO!! One enemy ramdon is challenge.")
    start = input("This enemy is a " + random_enemy + ", are you prepare? \n (Choose any number for continue except 1) \n")
    
    if start == "1":
        print("You are scaped")
        break
    else:
        turn = True
        while turn:
            #Eleccion random de la maquina
            enemy_choose = random.choice(enemy_move)

            #Combate del Usuario
            print("-------------------------------------------")
            move = int(input("Choose your next move: \n(1: Attack, 2:Defend, 3:Run) \n"))

            #Por si alguien decide no seguir la instruccion
            while move < 0 or move > 3:
                print("----------ERROR----------")
                print("You is enter invalid date")
                print("-------------------------------------------")
                move = int(input("Choose your next move: \n(1: Attack, 2:Defend, 3:Run) \n"))

            if move == 1 and enemy_choose == "Attack":
                #Si tanto enemigo como jugador atacan el mismo turno
                hp_enemy = hp_enemy - main_character[1]
                hp_main = hp_main - enemy[1]
                print("-------------------------------------------")
                print(random_enemy, " is attack you with ", enemy[1]," Damage")
                print("You have ", hp_main, " HP now")
                print("Your are does ", main_character[1]," Damage")
                print("The enemy has ", hp_enemy, " HP")
            elif move == 1 and enemy_choose == "Defend":
                #Si enemigo defiende y jugador ataca
                hp_enemy = hp_enemy - (main_character[1] - enemy[2])
                print("-------------------------------------------")
                print(random_enemy, " is defended whit ", enemy[2], " point of defend")
                print("Your are does attack ", main_character[1] - enemy[2] ," Damage")
                print("The enemy has ", hp_enemy, " HP")
            elif move == 2 and enemy_choose == "Attack":
                #Si jugador defiende y enemigo ataca
                hp_main = hp_main - (enemy[1] - main_character[2])
                print("-------------------------------------------")
                print("You are does defend whit ", main_character[2] ," point of defend")
                print(random_enemy, " is attack you with ", enemy[1] - main_character[2]," Damage")
                print("You have ", hp_main, " HP now")
            elif move == 2 and enemy_choose == "Defend":
                print("-------------------------------------------")
                print(random_enemy," is does Defend")
                print("You are does defend too")
                print("This turn not damage")
            elif move == 3:
                break
            
            #Victorio o derrota
            if hp_enemy <= 0:
                print("-------------------------------------------")
                print("You are win")
                turn = False
            elif hp_main <= 0:
                print("-------------------------------------------")
                print("You are loss")
                turn = False
            else:
                turn = True
    #Elige a otro enemigo random o se termina el juego
    print("-------------------------------------------")
    next_enemy = input("You want a next enemy?: (1:Yes, Any:No)")
    if next_enemy == "1":
        round = True
    else:
        round = False
    




    
       
    


    
    

