def first_turn_start(turn):
    print("Player:")
    print("Max_HP: " + str(max_hp))
    print("HP: " + str(hp))
    print("Max_MP: " + str(max_mp))
    print("MP: " + str(mp))
    print("Attack: " + str(phys_atk))
    print("Defense: " + str(phys_def))
    print("Magical Attack: " + str(magi_atk))
    print("Magical Defense: " +  str(magi_def))
    print("----------------------------------")
    print(enemy_name + ":")
    print("Max_HP: " + str(en_max_hp))
    print("HP: " + str(en_hp))
    print("Max_MP: " + str(en_max_mp))
    print("MP: " + str(en_mp))
    print("Attack: " + str(en_phys_atk))
    print("Defense: " + str(en_phys_def))
    print("Magical Attack: " + str(en_magi_atk))
    print("Magical Defense: " +  str(en_magi_def))
    if can_revive == True:
        print("Enemy Revies: " + str(max_en_revives))
    turn_start(turn)

def turn_start(turn):
    global en_defined_def
    global hp
    global en_defined_magi_def
    global mp
    global en_mp
    global halve_stacks
    global Recursive_Magic
    global damage
    en_defined_def = en_phys_def
    for i in range:
        if Recursive_Magic >= 100:
            Recursive_Magic -= 100
               
    if berserker_defense_Half == True:
        en_defined_def = en_defined_def/halve_stacks
        en_defined_magi_def = en_defined_magi_def/halve_stacks
    turn = turn + 1
    if burned == True:
        print("----------------------------------")
        damage = (max_hp/9)
        print("Player took " + str(damage) + "burn damage")
        hp -= damage
    if enemy_mana_drain == True:
        damage = int(round(en_max_mp / 16, 0))
        if damage > en_mp:
            damage = en_mp
        print("Player drained " + str(damage) + " mana from " + str(enemy_name))
        en_mp -= damage
        mp += damage
        if mp > max_mp:
            overflow = mp - max_mp
            Recursive_Magic += overflow
            mp = max_mp
        damage = 0
    print("----------------------------------")
    print("player turn: " + str(turn))
    print("HP: " + str(hp) + "/" + str(max_hp))
    print("MP: " + str(mp) + "/" + str(max_mp))
    player_choice(turn)
    
def en_turn_start(turn):
    global hp
    global defined_def
    global enemy_id
    global defined_magi_def
    global en_burned
    global en_phys_atk
    global en_phys_def
    global en_magi_def
    global en_burned
    global en_hp
    global en_max_hp
    global en_revives
    global en_mp
    global en_max_mp
    defined_def = phys_def
    defined_def  = defined_def * mult_def
    defined_def = defined_def / phys_def_break
    defined_magi_def = magi_def
    defined_magi_def = defined_magi_def * mult_def
    if en_burned == True:
        print("----------------------------------")
        damage = (en_max_hp/16)
        print(enemy_name + " took " + str(damage) + "burn damage")
        en_hp -= damage
    damage = 0
    if enemy_id == 3:
        print("Berserker healed their mana")
        en_mp += en_max_mp/8
    print("----------------------------------")
    print(enemy_name + "'s turn: ")
    print(enemy_name + "'s HP: " + str(en_hp) + "/" + str(en_max_hp))
    print(enemy_name + "'s MP: " + str(en_mp) + "/" + str(en_max_mp))
    if can_revive == True:
        print(enemy_name + "'s Revives: " + str(en_revives) + "/" + str(max_en_revives))
    if enemy_id == 1:
        globin_ai(turn)
    elif enemy_id == 2:
        mage_ai(turn)
    elif enemy_id == 3:
        berserker_AI(turn)
    else:
        globin_ai(turn)
    if hp <= 0:
        print("Player has been defeated the battle and was lost")
        sys.exit("Thanks for playing!")
    turn_start(turn)

def player_choice(turn):
    global damage
    global en_hp
    global enemy_name
    global hp
    global defined_def
    global mp
    global always_status
    global en_phys_atk
    global en_phys_def
    global en_magi_def
    global en_burned
    global en_hp
    global en_max_hp
    global en_revives
    defined_def = phys_def
    defined_def  = defined_def * mult_def
    defined_def = defined_def / phys_def_break
    defined_magi_def = magi_def
    defined_magi_def = defined_magi_def * mult_def
    damage = 0
    print("Choices: ")
    print("1.Fight: ")
    print("2.Magic: ")
    print("3.Guard: ")
    print("4.Stats: ")
    choice = int(input("Choice your decision: "))
    if choice == 1:
        rng = random.randrange(80,100)/100
        damage = (rng * phys_atk) - en_defined_def
        if damage < 0:
            damage = 0
        print(enemy_name + " took " + str(damage) + " damage!")
    elif choice == 2:
        magic_menu(turn)
    elif choice == 3:
        defined_def = defined_def * 2
    elif choice == 1987:
        print("You used DevTool, and drained all MP")
        mp = 0
    elif choice == 1048596:
        print("You used DevTool, drained your life force")
        hp = 0
    elif choice == 310:
        print("You used DevTool Barghest, You can never resist status effects :)")
        always_status = True
    elif choice == 284:
        print("You used DevTool, You just kick started your doom :)")
        en_revives = 4
        en_hp = 0
        hp = 2000
    elif choice == 4:
        stats(turn)
    else:
        print("Choice a valid input")  
        player_choice(turn)
    en_hp = en_hp - damage
    if en_hp <= 0 and en_revives >= 1:
        enemy_revives(turn)
    elif en_hp <= 0:
        print("Player has finished the battle and won") 
        sys.exit("Thanks for playing!")
    en_turn_start(turn)

def magic_menu(turn):
    global mult_def
    global en_hp
    global damage
    global mp
    global hp
    global status_chance
    global en_burned
    global enemy_mana_drain
    global en_phys_atk
    global en_phys_def
    global en_magi_def
    global en_burned
    global en_hp
    global en_max_hp
    global en_revives
    damage = 0
    print("Magic:")
    print("----------------------------------")
    print("1.Fire 2MP")
    print("2.Holy Bless 4MP")
    print("3.Heal 6MP")
    print("4.Self Sacrifice 10HP")
    print("5.Mana Drain 8MP")
    print("N.Back")
    choice = input("Choice your decision: ").lower()
    if choice == "1":
        if mp >= 2:
            print("Player uses Fire")
            magic_power = 15
            rng = random.randrange(80,100)/100
            damage = ((rng * magi_atk) + magic_power) - en_defined_magi_def
            if damage < 0:
                damage = 0
            print(enemy_name + " took " + str(damage) + " damage!")
            status_chance = random.randrange(1,11)
            if status_chance == 1:
                print("Player was burned")
                en_burned = True
            mp -= 2
        else:
            print("Out of MP!")
            return player_choice(turn)
    elif choice == "2":
        if mp >= 4:
            print("Player used Holy Bless!")
            print("Their defense was multiplied")
            mult_def += 1.5
            mp -= 4
        else:
            print("Out of MP!")
            return player_choice(turn)
    elif choice == "3":
        if mp >= 6:
            print("Player used Heal!")
            damage = max_hp/5
            print("Player has healed" + str(damage) + "Damage")
            hp += damage
            mp -= 6
        else:
            print("Out of MP!")
            return player_choice(turn)
    elif choice == "4":
        if hp >= 10:
            print("Player used Self Sacrifice!")
            print("Player swapped 10 HP for 10 MP")
            hp -= 10
            mp += 10
        else:
            print("Out of MP!")
            return player_choice(turn)
    elif choice == "5":
        if mp >= 8:
            print("Player used Mana Drain!")
            print("Player inflicted " + str(enemy_name) + " with a mana drain spell")
            enemy_mana_drain = True
            mp -= 8
        else:
            print("Out of MP!")
            return player_choice(turn)
    elif choice == "n":
        return player_choice(turn)
    else:
        print("Invalid choice")
        return player_choice(turn)
    en_hp -= damage
    if en_hp <= 0 and en_revives >= 1:
        enemy_revives(turn)
    elif en_hp <= 0:
        print("Player has finished the battle and won") 
        sys.exit("Thanks for playing!")
    en_turn_start(turn)


def globin_ai(turn):
    global hp
    print("The " + enemy_name + " swung their club at player")
    rng = random.randrange(80,100)/100
    damage = (rng * en_phys_atk) - defined_def
    if damage < 0:
        damage = 0
    print("Player took " + str(damage) + " damage!")
    hp = hp - damage

def mage_ai(turn):
    global status_chance
    global hp
    global burned
    #The next cpde will try to make a decision for the attack
    used_magick = False
    rng = random.randrange(1,3)
    if rng == 1:
        print("The mage swung their wand")
        rng = random.randrange(80,100)/100
        damage = (rng * en_phys_atk) - defined_def
    if rng == 2:
        used_magick = True
        print("The mage sent out a fireball")
        magic_power = 15
        rng = random.randrange(80,100)/100
        damage = ((rng * en_magi_atk)+magic_power)- defined_magi_def
        if always_status == True:
            status_chance = 1
        else:
            status_chance = random.randrange(1,17)
    if damage < 0:
        damage = 0
    print("Player took " + str(damage) + " damage!")
    if status_chance == 1 and used_magick == True:
        print("Player was burned")
        burned = True
    hp = hp - damage

def berserker_AI(turn):
    global hp
    global damage
    global status_chance
    global berserker_defense_Half
    global halve_stacks
    if en_revives == 3:
        rng = random.randrange(1,4)
        if rng == 1:
            print("Bersker used it's Noble Phantasm 'Nine lives'.")
            for i in range(9):
                rng = random.randrange(80,100)/100
                damage = ((rng * en_phys_atk) - defined_def)/2
                if damage < 0:
                    damage = 0
                print("Player took " + str(damage) + " damage!")
                hp -= damage
            status_chance = random.randrange(1,4)
            if status_chance == 1:
                if not berserker_defense_Half == True:
                    print("berserker's posistion has been weakened")
                    berserker_defense_Half = True
                    halve_stacks = 2
                else:
                    print("berserker's posistion has been further weakened")
                    halve_stacks += 1
            damage = 0
        if rng == 2:
            print("Berserker threw a boulder at you")
            rng = random.randrange(80,100)/100
            damage = ((rng * en_phys_atk) - defined_def) * 4
            if damage < 0:
                damage = 0
            print("Player took " + str(damage) + " damage!")
        if rng == 3:
            print("Berserker stomped and summoned an earthquake")
            rng = random.randrange(80,100)/100
            damage = ((rng * en_phys_atk) - defined_def)*6
            if damage < 0:
                damage = 0
            print("Player took " + str(damage) + " damage!")
    elif en_revives <= 10 and en_revives >3:
        rng = random.randrange(1,4)
        if rng == 1:
            print("Bersker used it's Noble Phantasm 'Nine lives'.")
            for i in range(9):
                rng = random.randrange(80,100)/100
                damage = ((rng * en_phys_atk) - defined_def)/4
                if damage < 0:
                    damage = 0
                print("Player took " + str(damage) + " damage!")
                hp -= damage
            status_chance = random.randrange(1,4)
            if status_chance == 1:
                if not berserker_defense_Half == True:
                    print("berserker's posistion has been weakened")
                    berserker_defense_Half = True
                    halve_stacks = 2
                else:
                    print("berserker's posistion has been further weakened")
                    halve_stacks += 1
            damage = 0
        if rng == 2:
            print("Berserker threw a boulder at you")
            rng = random.randrange(80,100)/100
            damage = (rng * en_phys_atk) - defined_def
            if damage < 0:
                damage = 0
            print("Player took " + str(damage) + " damage!")
        if rng == 3:
            print("Berserker stomped and summoned an earthquake")
            rng = random.randrange(80,100)/100
            damage = ((rng * en_phys_atk) - defined_def)*2
            if damage < 0:
                damage = 0
            print("Player took " + str(damage) + " damage!")
    else:
        rng = random.randrange(1,3)
        if rng == 1:
            print("Bersker used it's Noble Phantasm 'Nine lives'.")
            for i in range(9):
                rng = random.randrange(80,100)/100
                damage = ((rng * en_phys_atk) - defined_def)/4
                if damage < 0:
                    damage = 0
                print("Player took " + str(damage) + " damage!")
                hp -= damage
            status_chance = random.randrange(1,4)
            if status_chance == 1:
                if not berserker_defense_Half == True:
                    print("berserker's posistion has been weakened")
                    berserker_defense_Half = True
                    halve_stacks = 2
                else:
                    print("berserker's posistion has been further weakened")
                    halve_stacks += 1
            damage = 0
        if rng == 2:
            print("Berserker threw a boulder at you")
            rng = random.randrange(80,100)/100
            damage = (rng * en_phys_atk) - defined_def
            if damage < 0:
                damage = 0
            print("Player took " + str(damage) + " damage!")
    hp = hp - damage

def enemy_revives(turn):
    global en_phys_atk
    global en_phys_def
    global en_magi_def
    global en_burned
    global en_hp
    global en_max_hp
    global en_revives
    global berserker_defense_Half
    global halve_stacks
    global enemy_mana_drain
    global phys_def_break
    print(enemy_name + " has revived")
    en_revives -= 1
    en_burned = False
    berserker_defense_Half = False
    halve_stacks = 1
    enemy_mana_drain = False
    if enemy_id == 3:
        if en_revives == 11:
            en_max_hp = 2050.0
            en_phys_atk = 90
            en_phys_def = 65
            en_magi_def = 75
        if en_revives == 10:
            en_max_hp = 2300.0
            en_phys_atk = 130
            en_phys_def = 90
            en_magi_def = 100
        if en_revives == 9:
            en_max_hp = 2450.0
            en_phys_atk = 190
            en_phys_def = 120
            en_magi_def = 150
        if en_revives == 8:
            en_max_hp = 2500.0
            en_phys_atk = 230
            en_phys_def = 160
            en_magi_def = 210
        if en_revives <= 7 and en_revives >3:
            en_max_hp += 300.0
            en_phys_atk += 60
            en_phys_def += 50
            en_magi_def += 40
        if en_revives == 3:
            print("He found his true weapon, Marmyadose")
            en_max_hp = 3700.0
            en_phys_atk = 360
            en_phys_def = 300
            en_magi_def = 250
        if en_revives == 2:
            print("His full aura weakened your defenses")
            en_max_hp = 4000.0
            en_phys_atk = 440
            en_phys_def = 400
            en_magi_def = 340
            phys_def_break += 0.5
    en_hp = en_max_hp

def stats(turn):
    global max_hp
    global hp
    global max_mp
    global mp
    global phys_atk
    global phys_def
    global magi_atk
    global magi_def
    global defined_def
    global defined_magi_def
    global mult_def
    global phys_def_break
    global Recursive_Magic
    print("Max_HP: " + str(max_hp))
    print("HP: " + str(hp))
    print("Max_MP: " + str(max_mp))
    print("MP: " + str(mp))
    print("Attack: " + str(phys_atk))
    print("Defense: " + str(phys_def))
    print("Magical Attack: " + str(magi_atk))
    print("Magical Defense: " +  str(magi_def))
    print("Defined Defense: " + str(defined_def))
    print("Magical Defined Defense: " + str(defined_magi_def))
    print("Multiply Defense by: " + str(mult_def))
    print("Physical Defense Break: " + str(phys_def_break))
    print("Recursive Magic: " + str(Recursive_Magic))
    player_choice(turn)

import sys
Recursive_Magic = 0
phys_def_break = 1
halve_stacks = 1
en_burned = False
en_revives = 0
enemy_mana_drain = False
berserker_defense_Half = False
always_status = False
status_chance = 0
burned = False
turn = 0
max_hp = 120.0
hp = max_hp
max_mp = 20
mp = max_mp
phys_atk = 30
phys_def = 15
magi_atk = 30
magi_def = 15
defined_def = phys_def + .0
defined_magi_def = magi_def + .0
mult_def = 1
import random
rng = 1
rng = random.randrange(1,4) #picks an enemy for you to fight randomly
enemy_id = rng
can_revive = False
if rng == 1:
    enemy_name = "Goblin"
    en_max_hp = 110.0
    en_hp = en_max_hp
    en_max_mp = 0
    en_mp = en_max_mp
    en_phys_atk = 25
    en_phys_def = 10
    en_magi_atk = 0
    en_magi_def = 5
if rng == 2:
    enemy_name = "Mage"
    en_max_hp = 70.0
    en_hp = en_max_hp
    en_max_mp = 40
    en_mp = en_max_mp
    en_phys_atk = 5
    en_phys_def = 5
    en_magi_atk = 30
    en_magi_def = 30
if rng == 3:
    max_en_revives = 12
    en_revives = max_en_revives
    enemy_name = "Berserker"
    en_max_hp = 2000.0
    en_hp = en_max_hp
    en_max_mp = 3000
    en_mp = en_max_mp
    en_phys_atk = 70
    en_phys_def = 40
    en_magi_atk = 0
    en_magi_def = 40
    can_revive = True
en_defined_def = en_phys_def
en_defined_magi_def = en_magi_def
first_turn_start(turn)
#test