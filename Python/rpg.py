def first_turn_start(turn):
    global avalon_stack
    avalon_stack = 0
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
    if can_revive:
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
    global max_hp
    global max_mp
    global phys_atk
    global magi_atk
    global avalon_stack
    global hasAvalon
    global invincible
    global test_loop
    global defined_atk
    global defined_magi_atk
    global defined_def
    global defined_magi_def
    global hasExcalibur
    global excalibur_stacks
    invincible = False
    defined_def = phys_def
    defined_def  = defined_def * mult_def
    defined_def = defined_def / phys_def_break
    defined_magi_def = magi_def
    defined_magi_def = defined_magi_def * mult_def
    en_defined_magi_def = en_magi_def
    en_defined_def = en_phys_def
    defined_atk = phys_atk
    defined_magi_atk = magi_atk
    if hasExcalibur:
        defined_atk *= 6
        defined_magi_atk *= 6
    if avalon_stack == 4:
        print("After player searched they found the ultimate defense, Avalon")
        hasAvalon = True
        avalon_stack = 0
    if excalibur_stacks == 4:
        print("There was a lake, and drifting down the lake was the holy blade of destined victory. Excalibur")
        hasExcalibur = True
        excalibur_stacks = 0
    if berserker_defense_Half:
        en_defined_def = en_defined_def/halve_stacks
        en_defined_magi_def = en_defined_magi_def/halve_stacks
    turn = turn + 1
    if burned:
        print("----------------------------------")
        damage = (max_hp/9)
        print("Player took " + str(damage) + "burn damage")
        hp -= damage
    if enemy_mana_drain:
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
    while Recursive_Magic >= 100:
        test_loop += 1
        if max_hp < 1000.0:
            max_hp += 10
            hp += 10
            max_mp += 10
            mp += 10
            phys_atk += 5
            magi_atk += 5
        elif max_hp < 2000.0 and hasExcalibur:
            max_hp += 20
            hp += 20
            max_mp += 20
            mp += 20
            phys_atk += 10
            magi_atk += 10
        Recursive_Magic -= 100
        damage = 0
    test_loop = 0
    if hp > max_hp:
        hp = max_hp
    print("----------------------------------")
    print("player turn: " + str(turn))
    print("HP: " + str(hp) + "/" + str(max_hp))
    print("MP: " + str(mp) + "/" + str(max_mp))
    if avalon_stack > 0:
        print("???: " + str(avalon_stack) + "/4")
    if hasAvalon:
        print("Avalon: Active")
    if excalibur_stacks > 0:
        print("?!?!: " + str(excalibur_stacks) + "/4")
    if hasExcalibur:
        print("Excalibur: Obtained")
    player_choice(turn)
    
def en_turn_start(turn):
    global hp
    global defined_def
    global defined_magi_def
    global enemy_id
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
    global max_en_revives
    global invincible
    global prehp
    global avalon_mult
    if hp > max_hp:
        hp = max_hp
    if hasAvalon:
        defined_def = defined_def * avalon_mult
        defined_magi_def = defined_magi_def * avalon_mult
    if en_burned:
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
    if can_revive:
        print(enemy_name + "'s Revives: " + str(en_revives) + "/" + str(max_en_revives))
    prehp = hp
    if enemy_id == 1:
        globin_ai(turn)
    elif enemy_id == 2:
        mage_ai(turn)
    elif enemy_id == 3:
        berserker_AI(turn)
    elif enemy_id == 4:
        golem_ai(turn)
    else:
        globin_ai(turn)
    if hp <= 0:
        if invincible:
            hp = prehp
        else:
            print("Player has been defeated the battle and was lost")
            sys.exit("Thanks for playing!")
    elif invincible:
        hp = prehp
    if invincible:
        print("Player is invincible and didn't take any damage!")
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
    global choice
    global mult_def
    global can_revive
    global avalon_stack
    global enemy_id
    global invincible
    global Recursive_Magic
    global hasAvalon
    global halfhp
    choice = 0
    damage = 0
    halfhp = max_hp / 2
    print("Choices: ")
    print("1.Fight: ")
    print("2.Magic: ")
    print("3.Guard: ")
    print("4.Stats: ")
    try:
        choice = int(input("Choice your decision: "))
    except:
        choice = 0
    if choice == 1:
        rng = random.randrange(80,100)/100
        if not hasExcalibur:
            damage = (rng * defined_atk) - en_defined_def
        else:
            damage = (rng * defined_atk) + (defined_magi_atk * 1.16) - en_defined_def
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
        mult_def = 22.5
        en_revives = 3
        can_revive = True
        en_hp = 0
        hp = 2000
    elif choice == 4:
        stats(turn)
    elif choice == 353:
        print("You used DevTool, You gained avalon stack)")
        avalon_stack += 1
    elif choice == 85181312419:
        print("You used DevTool, Heracles Ichor has been awakened")
        en_revives = 1
        en_hp = 0
        hasAvalon = True
        mult_def = 16
        Recursive_Magic = 9000
        invincible = True
        can_revive = True
    elif choice == 411314:
        en_revives = 3
        can_revive = True
        en_hp = 0 
        invincible = True
    elif choice == 851212:
        en_revives = 1
        can_revive = True
        en_hp = 0 
        invincible = True
        Recursive_Magic = 9000
        hasAvalon = True
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
    global invincible
    damage = 0
    print("Magic:")
    print("----------------------------------")
    print("1.Fire 2MP")
    print("2.Holy Bless 4MP")
    print("3.Heal 6MP")
    print("4.Self Sacrifice 10HP")
    print("5.Mana Drain 8MP")
    print("6.Invincible All MP")
    print("N.Back")
    choice = input("Choice your decision: ").lower()
    print("----------------------------------")
    if choice == "1":
        if mp >= 2:
            print("Player uses Fire")
            magic_power = 15
            if hasExcalibur:
                magic_power *= 4
            rng = random.randrange(80,100)/100
            damage = ((rng * defined_magi_atk) + magic_power) - en_defined_magi_def
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
            if hasExcalibur:
                mult_def += 1.5
            mp -= 4
        else:
            print("Out of MP!")
            return player_choice(turn)
    elif choice == "3":
        if mp >= 6:
            print("Player used Heal!")
            damage = (max_hp/5)*(magi_atk*.10)
            print("Player has healed" + str(damage) + "Damage")
            hp += damage
            mp -= 6
            damage = 0
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
    elif choice == "6":
        if mp >= 1:
            print("Player used Invincible!")
            print("Player used their mana to cover their body in invincible mana")
            invincible = True
            mp = 0
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
    global defined_def
    global defined_magi_def
    global en_phys_atk
    global charge_up
    global avalon_stack
    global excalibur_stacks
    global avalon_mult
    global en_mp
    global damage
    if can_revive and en_revives == 0:
        if not charge_up:
            rng = random.randrange(1,5)
        elif charge_up:
            print("1st Demonic Magick: inner caves of space-time")
            avalon_mult -= 0.5
            print(avalon_mult)
            magic_power = 30
            rng = random.randrange(80,100)/100
            damage = ((rng * (en_phys_atk + en_magi_atk))*magic_power) - (en_defined_def / 16)
            en_mp -= 20
        if en_mp < 1:
            en_hp = 0
        if rng == 1:
            print("The " + enemy_name + " swung their greatsword")
            rng = random.randrange(80,100)/100
            damage = (rng * en_phys_atk) - defined_def
        if rng == 2:
            print("The " + enemy_name + " rapidly slashed you with their greatsword")
            for i in range(10):
                rng = random.randrange(80,100)/100
                damage = ((rng * en_phys_atk))/6
                if damage < 0:
                    damage = 0
                print("Player took " + str(damage) + " damage!")
                hp -= damage
            damage = 0
        if rng == 3:
            print("The " + enemy_name + " laid down")
            en_hp *= 1.20
            if en_hp > en_max_hp:
                en_hp = en_max_hp
            if not hasAvalon:
                print("You wandered around to find a way to escape")
                avalon_stack += 1
            elif hasAvalon and not hasExcalibur:
                print("You wandered around to find a way to escape")
                excalibur_stacks += 1
            else:
                print("The golem stared at you")
        if rng == 4:
            print("1st Demonic Magick")
            charge_up = True
    elif can_revive:
        rng = random.randrange(1,4)
        if rng == 1:
            print("The " + enemy_name + " swung their club at player")
            rng = random.randrange(80,100)/100
            damage = (rng * en_phys_atk) - defined_def
        if rng == 2:
            print("The " + enemy_name + " used a rapid barrage")
            for i in range(9):
                rng = random.randrange(80,100)/100
                damage = ((rng * en_phys_atk) - defined_def)/6
                if damage < 0:
                    damage = 0
                print("Player took " + str(damage) + " damage!")
        if rng == 3:
            print("The " + enemy_name + " swung their club at player weakly")
            rng = random.randrange(80,100)/100
            damage = ((rng * en_phys_atk) - defined_def)/6
            print("Allowing them to save their power increasing it by 5%")
            en_phys_atk *= 1.05
    else:
        print("The " + enemy_name + " swung their club at player")
        rng = random.randrange(80,100)/100
        damage = (rng * en_phys_atk) - defined_def
    if damage < 0:
        damage = 0
    if en_phys_atk > 700:
        en_phys_atk = 700
        print("The " + enemy_name + "'s attack can no longer grow")
    print("Player took " + str(damage) + " damage!")
    hp = hp - damage

def mage_ai(turn):
    global status_chance
    global hp
    global burned
    global defined_def
    global defined_magi_def
    #The next code will try to make a decision for the attack
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
        if always_status:
            status_chance = 1
        else:
            status_chance = random.randrange(1,17)
    if damage < 0:
        damage = 0
    print("Player took " + str(damage) + " damage!")
    if status_chance == 1 and used_magick:
        print("Player was burned")
        burned = True
    hp = hp - damage

def berserker_AI(turn):
    global hp
    global damage
    global status_chance
    global berserker_defense_Half
    global halve_stacks
    global avalon_stack
    global hasAvalon
    global Avalon_pity
    global Avalon_wait
    global en_phys_atk
    global mp 
    global excalibur_stacks
    global hasExcalibur
    global defined_def
    global max_hp
    global halfhp
    global prehp
    Avalon_pity = 0
    Avalon_wait = False
    excalibur_pity = 0
    excalibur_wait = False
    if en_revives == 0:
        rng = random.randrange(1,9)
        if rng == 8:
            en_phys_atk += 50
            print("Heracles Ichor used their Valor A+ skil")
        rng = random.randrange(1,6)
        if excalibur_pity == 3:
            rng = 5
        if rng == 1:
            print("Heracles Ichor used it's Noble Phantasm 'Breakage Giganomachia, Slaying the Hundred Gods'.")
            for i in range(10):
                rng = random.randrange(80,100)/100
                damage = ((rng * en_phys_atk))/6
                if damage < 0:
                    damage = 0
                print("Player took " + str(damage) + " damage!")
                hp -= damage
            status_chance = random.randrange(1,4)
            if status_chance == 1:
                if not berserker_defense_Half:
                    print("berserker's posistion has been weakened")
                    berserker_defense_Half = True
                    halve_stacks = 2
                else:
                    print("berserker's posistion has been further weakened")
                    halve_stacks += 1
            if hp < 0 and prehp > halfhp:
                hp = 1
            damage = 0
        if rng == 2:
            print("Heracles Ichor used their Glorious Greatsword")
            rng = random.randrange(80,100)/100
            damage = ((rng * en_phys_atk) - defined_def) * 4
            if damage < 0:
                damage = 0
            print("Player took " + str(damage) + " damage!") 
            en_phys_atk *= 1.20
            print("Heracles ichor's power has increased by 20%")
        if rng == 3:
            print("Heracles Ichor used Cold-Hearted Unyeilding Bow")
            rng = random.randrange(80,100)/100
            damage = ((rng * en_phys_atk) - defined_def)*8
            if damage < 0:
                damage = 0
            print("Player took " + str(damage) + " damage!")
            print("Player's mp decreased by 20%")
            mp *= 0.20
        if rng == 4:
            print("Heracles Ichor used Battleaxe of Destruction")
            rng = random.randrange(80,100)/100
            damage = ((rng * en_phys_atk))
            if damage > 799 and prehp > halfhp:
                damage = 799
            if damage < 0:
                damage = 0
            print("Player took " + str(damage) + " damage!")
            damage += 200
            print("Player took 200 instant damage")
        if rng == 5:
            if not hasExcalibur:
                print("Heracles Ichor's madness enchancement paralyzed him")
                excalibur_stacks += 1
                hp += (max_hp/30)
                Avalon_wait = True
            else:
                print("Heracles Ichor was paralyzd by his extreme madness")
    elif en_revives == 1:
        rng = random.randrange(1,5)
        if Avalon_pity == 4:
            rng = 4
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
                if not berserker_defense_Half:
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
        if rng == 4:
            if not hasAvalon:
                print("Berserker stoood still")
                avalon_stack += 1
                hp += (max_hp/15)
                Avalon_wait = True
            else:
                print("Berserker looks angry")
    elif en_revives == 2:
        rng = random.randrange(1,4)
        if Avalon_pity == 4:
            rng = 4
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
                if not berserker_defense_Half:
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
    elif en_revives <= 9 and en_revives >2:
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
                if not berserker_defense_Half:
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
                if not berserker_defense_Half:
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
    if Avalon_wait:
        Avalon_pity = 0
    else:
        if not hasAvalon:
            Avalon_pity += 1
    if can_revive and en_revives == 0:
        if excalibur_wait:
            excalibur_pity = 0
        else:
            if not hasExcalibur:
                excalibur_pity += 1
    hp = hp - damage

def golem_ai(turn):
    global status_chance
    global hp
    global burned
    global defined_def
    global defined_magi_def
    global en_mp
    global en_hp
    global damage
    global en_magi_atk
    global en_phys_atk
    global avalon_stack
    global excalibur_stacks
    global charge_up
    global self_turn
    global slow_start
    global extra_math
    global phys_def_break
    global avalon_mult
    if self_turn < 3:
        slow_start = True
        extra_math = 1 / 3
    if can_revive and en_revives == 0:
        if not charge_up:
            rng = random.randrange(1,5)
        elif charge_up:
            print("3rd Demonic Magick: True full potential of a Golem")
            avalon_mult -= 0.5
            print(avalon_mult)
            magic_power = 180
            rng = random.randrange(80,100)/100
            damage = ((rng * en_magi_atk)*magic_power) - (defined_magi_def / 16)
            en_mp -= 20
        if en_mp < 1:
            en_hp = 0
        if rng == 1:
            print("The golem swung their arm")
            rng = random.randrange(80,100)/100
            damage = (rng * en_phys_atk) - defined_def
        if rng == 2:
            if en_mp >= 20:
                print("The golem used a mouth beam")
                magic_power = 30
                rng = random.randrange(80,100)/100
                damage = ((rng * en_magi_atk)+magic_power) - defined_magi_def
                en_mp -= 20
        if rng == 3:
            print("The golem recharged")
            en_mp += 20
            if not hasAvalon:
                print("You wandered around to find a way to escape")
                avalon_stack += 1
            elif hasAvalon and not hasExcalibur:
                print("You wandered around to find a way to escape")
                excalibur_stacks += 1
            else:
                print("The golem stared at you")
        if rng == 4:
            print("3rd Demonic Magick")
            charge_up = True
    elif can_revive:
        rng = random.randrange(1,4)
        if en_mp < 1:
            en_hp = 0
        if rng == 1:
            print("The golem swung their arm")
            rng = random.randrange(80,100)/100
            damage = (rng * en_phys_atk) - defined_def
        if rng == 2:
            if en_mp >= 20:
                print("The golem used a mouth beam")
                magic_power = 30
                rng = random.randrange(80,100)/100
                damage = ((rng * en_magi_atk)+magic_power)- defined_magi_def
                en_phys_atk *= 1.20
                en_magi_atk *= 1.20
                en_mp -= 20
        if rng == 3:
            print("The golem recharged")
            en_mp += 20
            if not hasAvalon:
                print("You wandered around to find a way to escape")
                avalon_stack += 1
            elif hasAvalon and not hasExcalibur:
                print("You wandered around to find a way to escape")
                excalibur_stacks += 1
            else:
                print("The golem stared at you")
    else:
        rng = random.randrange(1,3)
        if en_mp < 1:
            en_hp = 0
        if rng == 1:
            print("The golem swung their arm")
            rng = random.randrange(80,100)/100
            damage = (rng * en_phys_atk) - defined_def
        if rng == 2:
            if en_mp >= 20:
                print("The golem used a mouth beam")
                magic_power = 30
                rng = random.randrange(80,100)/100
                damage = ((rng * en_magi_atk)+magic_power)- defined_magi_def
                en_mp -= 20
    if slow_start:
        damage *= extra_math
    if damage < 0:
        damage = 0
    print(damage)
    print("Player took " + str(damage) + " damage!")
    self_turn += 1
    hp = hp - damage
    extra_math = 0

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
    global enemy_name
    global start_pity
    global en_mp
    global en_magi_atk
    global en_max_mp
    global self_turn
    global hasAvalon
    global invincible
    global revive_cure
    start_pity = False
    print(enemy_name + " has revived")
    en_revives -= 1
    if revive_cure:
        en_burned = False
        berserker_defense_Half = False
        halve_stacks = 1
        enemy_mana_drain = False
    if enemy_id == 3:
        if en_revives == 10:
            print("Player: He revived?!")
            en_max_hp = 2050.0
            en_phys_atk = 90
            en_phys_def = 45
            en_magi_def = 55
        if en_revives == 9:
            print("Player: Are you kidding me...")
            en_max_hp = 2300.0
            en_phys_atk = 130
            en_phys_def = 70
            en_magi_def = 80
        if en_revives == 8:
            print("Player: Okay this is getting tedious!")
            en_max_hp = 2450.0
            en_phys_atk = 190
            en_phys_def = 100
            en_magi_def = 130
        if en_revives == 7:
            en_max_hp = 2500.0
            en_phys_atk = 230
            en_phys_def = 140
            en_magi_def = 190
        if en_revives <= 6 and en_revives >2:
            en_max_hp += 300.0
            en_phys_atk += 60
            en_phys_def += 30
            en_magi_def += 20
        if en_revives == 2:
            print("[He found his true weapon, Marmyadose]")
            en_max_hp = 3700.0
            en_phys_atk = 360
            en_phys_def = 280
            en_magi_def = 230
            start_pity = True
        if en_revives == 1:
            print("[His full aura weakened your defenses]")
            en_max_hp = 4000.0
            en_phys_atk = 440
            en_phys_def = 380
            en_magi_def = 320
            phys_def_break += 0.25
        if en_revives == 0:
            print("[The grand of the berserker class has awaken, Heracles Ichor]")
            en_max_hp = 40000.0
            en_phys_atk = 500
            en_phys_def = 4000
            en_magi_def = 380
            phys_def_break += 0.75
            en_max_mp = 16000
            en_mp = en_max_mp
            enemy_name = "Heracles Ichor"
    elif enemy_id == 4:
        if en_revives > 0:
            self_turn = 0
            enemy_name = "Abyssal Golem"
            en_max_hp = 1000.0
            en_max_mp = 1000
            en_phys_atk = 250
            en_phys_def = 300
            en_magi_atk = 225
            en_magi_def = 300
        if en_revives == 0:
            enemy_name = "Demon King General 3rd Seat: Golem"
            en_max_hp = 4500.0
            en_max_mp = 40000
            en_phys_atk = 2000
            en_phys_def = 750
            en_magi_atk = 450
            en_magi_def = 450
    elif enemy_id == 1:
        if en_revives > 0:
            self_turn = 0
            enemy_name = "Elite Goblin"
            en_max_hp = 550.0
            en_max_mp = 550
            en_phys_atk = 100
            en_phys_def = 50
            en_magi_atk = 0
            en_magi_def = 25
        elif en_revives == 0:
            enemy_name = "Demon King General 1st Seat: Goblin"
            en_max_hp = 5500.0
            en_max_mp = 50000
            en_phys_atk = 4000
            en_phys_def = 500
            en_magi_atk = 1000
            en_magi_def = 225
            print("The world realized the power inbalance and reflexively saved you")
            hasAvalon = True
            invincible = True
    en_hp = en_max_hp
    en_mp = en_max_mp

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
    print("Defined Attack: " + str(defined_atk))
    print("Defined Defense: " + str(defined_def))
    print("Magical Defined Attack: " + str(defined_magi_atk))
    print("Magical Defined Defense: " + str(defined_magi_def))
    print("Multiply Defense by: " + str(mult_def))
    print("Physical Defense Break: " + str(phys_def_break))
    print("Recursive Magic: " + str(Recursive_Magic))
    player_choice(turn)

import sys
sys.setrecursionlimit(50000)
global max_en_revives
global test_loop
global excalibur_stacks
global hasExcalibur
global defined_atk
global defined_magi_atk
global halfhp
global charge_up
global slow_start
global extra_math
global self_turn
global avalon_mult
global revive_cure
revive_cure = False
avalon_mult = 6
self_turn = 0
extra_math = 0
slow_start = False
charge_up = False
hasExcalibur = False
excalibur_stacks = 0
test_loop = 0
max_en_revives = 0
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
hasAvalon = False
invincible = False
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
defined_atk = phys_atk + .0
defined_magi_atk = magi_atk + .0
mult_def = 1
halfhp = max_hp / 2
import random
rng = 1
rng = random.randrange(1,5) #picks an enemy for you to fight randomly
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
    max_en_revives = 11
    en_revives = max_en_revives
    enemy_name = "Berserker"
    en_max_hp = 2000.0
    en_hp = en_max_hp
    en_max_mp = 3000
    en_mp = en_max_mp
    en_phys_atk = 70
    en_phys_def = 20
    en_magi_atk = 0
    en_magi_def = 20
    can_revive = True
    revive_cure = True
    en_defined_def = en_phys_def
    en_defined_magi_def = en_magi_def
if rng == 4:
    enemy_name = "Golem"
    en_max_hp = 450.0
    en_hp = en_max_hp
    en_max_mp = 500
    en_mp = en_max_mp
    en_phys_atk = 50
    en_phys_def = 40
    en_magi_atk = 35
    en_magi_def = 15
first_turn_start(turn)
#test1