import random 

#Definicion de personajes
class Character:
    def __init__(self, hp, attack, defend):
        self.hp = hp
        self.attack = attack
        self.defend = defend
    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defend
        if damage < 0:
            damage = 0
        enemy.hp -= damage
        return damage
    def defend_enemy(self, enemy):
        damage = enemy.attack - self.defend
        if damage < 0:
            damage = 0
        self.hp -= damage
        return damage

class Archer(Character):
    def __init__(self, hp, attack, defend, name):
        super().__init__(hp, attack, defend)
        self.name = name
        self.type = "Archer"
class Warrior(Character):
    def __init__(self, hp, attack, defend, name):
        super().__init__(hp, attack, defend)
        self.name = name
        self.type = "Warrior"
class Mage(Character):
    def __init__(self, hp, attack, defend, name):
        super().__init__(hp, attack, defend)
        self.name = name
        self.type = "Mage"
#Funcion
def invalid_date():
    print("----------ERROR----------")
    print("You is enter invalid date")
    print("-------------------------------------------")
#Funcion para validar el personaje
def validate_character(character):
    if choose_main != "Warrior" or choose_main != "warrior":
        if(choose_main != "Archer" or choose_main != "archer") and choose_main != "Mage":
            invalid_date()
            choose_main = input("Choose your character from the 3 characters: \nWarrior, Archer or Mage \n")
            validate_character(choose_main)
    else:
        print("You is choose a character")

#Creacion de personajes   
mage = Mage(100, 20, 5, "Mage")
warrior = Warrior(120, 25, 10, "Warrior")
archer = Archer(80, 15, 3, "Archer")
characters = [mage, warrior, archer]

#Inicio del juego:
#1. Elegir personaje
print("Welcome to the game!")
choose_main = input("Choose your character from the 3 characters: \nWarrior, Archer or Mage \n")
validate_character(choose_main)
rund = True

while rund:
    if choose_main == "Warrior" or choose_main == "warrior":
        main_character = warrior
    elif choose_main == "Archer" or choose_main == "archer":
        main_character = archer
    elif choose_main == "Mage" or choose_main == "mage":
        main_character = mage

    #Vida del Enemigo ramdon
    random_enemy = random.choice(characters)

    #Aparece el enemigo y hay una condicion para iniciar el juego
    print("-------------------------------------------")
    print("OH NO!! One enemy ramdon is challenge.")
    start = input(f"This enemy is a {random_enemy.name} , are you prepare? \n (Choose any number for continue except 1) \n")
    if start == "1":
        print("You are scaped")
        break
    else:
        turn = True
        while turn:
            #Eleccion random de la maquina
            enemy_choose = random.choice(["Attack", "Defend"])

            #Combate del Usuario
            print("-------------------------------------------")
            move = int(input("Choose your next move: \n(1: Attack, 2:Defend, 3:Run) \n"))

            #Por si alguien decide no seguir la instruccion
            while move < 0 or move > 3:
                invalid_date()
                move = int(input("Choose your next move: \n(1: Attack, 2:Defend, 3:Run) \n"))

            if move == 1 and enemy_choose == "Attack":
                #Si tanto enemigo como jugador atacan el mismo turno
                damage_enemy = main_character.attack_enemy(random_enemy)
                damage_main = random_enemy.attack_enemy(main_character)
                print("-------------------------------------------")
                print(f"{random_enemy.name} is attack you with {damage_main} Damage")
                print(f"You have {main_character.hp} HP now")
                print(f"Your are does {damage_enemy} Damage")
                print(f"The enemy has {random_enemy.hp} HP")
            elif move == 1 and enemy_choose == "Defend":
                #Si el jugador ataca y el enemigo defiende
                damage_enemy = main_character.attack_enemy(random_enemy)
                print("-------------------------------------------")
                print(f"{random_enemy.name} is defend you with {damage_enemy} Damage")
                print(f"You have {main_character.hp} HP now")
                print(f"Your are does {damage_enemy} Damage")
                print(f"The enemy has {random_enemy.hp} HP")
            elif move == 2 and enemy_choose == "Attack":
                #Si el jugador defiende y el enemigo ataca
                damage_main = random_enemy.attack_enemy(main_character)
                print("-------------------------------------------")
                print(f"You are defend whit {main_character.defend} point of defend")
                print(f"{random_enemy.name} is attack you with {damage_main} Damage")
                print(f"You have {main_character.hp} HP now")
            elif move == 2 and enemy_choose == "Defend":
                #Si tanto el jugador como el enemigo defienden
                print("-------------------------------------------")
                print(f"{random_enemy.name} is Defend")
                print("You are defend too")
                print("This turn not damage")
            elif move == 3:
                #Si el jugador decide correr
                print("You are scaped")
                rund = False
                break

            #Victorio o derrota
            if main_character.hp <= 0:
                print("-------------------------------------------")
                print("You are lose")
                turn = False
            elif random_enemy.hp <= 0:
                print("-------------------------------------------")
                print("You are win")
                turn = False
    
    #Elige otro enemigo
    print("-------------------------------------------")
    next_enemy = input("You want a next enemy?: (1:Yes, Any:No)")
    if next_enemy == "1":
        rund = True
    else:
        rund = False
