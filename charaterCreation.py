
def charaterCreation():
    import  os , time , Varbailes
    Varbailes.name = input("What is you name going to be? : ")
    Varbailes.race = input("""What charter type would you like to be
    
1. Orc: Orcs specialize in melee combat they have high Strength and high Dexterity, but are low health    
2. Elf: Elves specialize in magic. They are low in health and low in Strength and high in intelligence and Dexterity    
3. Human: Humans are midrange in all categories but looks    
4. Dwarf: Dwarfs are short but mighty they use melee combat they have mid damage and are high and health, and Strength    
5. Minotaur: Minotaurs are a half human and half horse made from the gods    
6. Fiends: Fiends are a devil like creature     
7. Tabaxi: Tabaxi are a humanoid like creature with felione like features
    
What would you like to be? :""").strip().title()

    time.sleep(2)
    os.system("clear")

    Varbailes.classes = input("""What class do you want to be each class has its own special ability?!! :

1. Knight : They are high in health and high in Strength
2. Assassin : They are fast as well intellgene 
3. Wizard : They are wise and intellgent
4. Theif : They are fast as well at good at speaking
5. Brawler : They are high in health as well as Strength
6. Archer : They're high in speed and Dexterity
    
What class do you chose ? : """).strip().title()

    time.sleep(2)
    os.system("clear")


    Varbailes.classWepons = {
        "Knight": ["Sword", "Mace", "Greatsword"],
        "Assassin": ["Twin Daggers", "Bow", "Short Sword"],
        "Wizard": ["Staff", "Wand", "Orb"],
        "Thief": ["Dagger", "Short Bow", "Throwing Knives"],
        "Brawler": ["Gauntlets", "Twin Handaxes", "Club"],
        "Archer": ["Bow", "Crossbow", "Throwing Daggers"]
    }
        
    if Varbailes.classes not in Varbailes.classWepons:
        print("Invalid class! Defaulting to Knight.")
        Varbailes.classes = "Knight"

    weapons_list = Varbailes.classWepons[Varbailes.classes]
    print(" ")
    print("Available weapons: " + ", ".join(weapons_list))
    print(" ")
    Varbailes.mainWepons= input("Choose your weapon from the list above: ").title()


    time.sleep(2)
    os.system("clear")

    Varbailes.background = input("""What do you want your background to be?!! 
1. Iseaki
2. Farmhand
3. Gamabler
4. Scholar
5. Warrior
6. Alchemist 
    
What background do you chose ? :""").strip().title()
    print(" ")
   


    ##Races 
    
    if Varbailes.race == "Orc":
        Varbailes.Strength += 3
        Varbailes.Dexterity += 1
        Varbailes.Charisma -= 2
        Varbailes.Constitution += 2
        Varbailes.raceAbility = "Rage"

    elif Varbailes.race == "Elf":
        Varbailes.Wisdom += 2
        Varbailes.Intelligence += 2
        Varbailes.Charisma += 2
        Varbailes.Strength -= 2
        Varbailes.Constitution -= 2
        Varbailes.raceAbility = "Overcharged" 
    

    elif Varbailes.race == "Human":
        Varbailes.Strength += 1
        Varbailes.Dexterity += 1
        Varbailes.Constitution += 1
        Varbailes.Wisdom += 1
        Varbailes.Intelligence += 1
        Varbailes.Charisma -= 1
        Varbailes.raceAbility = "Undying Will"  

    elif Varbailes.racee == "Dwarf":
        Varbailes.Strength += 2
        Varbailes.Dexterity += 3
        Varbailes.Constitution += 1
        Varbailes.Charisma -= 2
        Varbailes.raceAbility = "Persice Strike"
    
    elif Varbailes.race == "Minotaur":
        Varbailes.Strength += 2
        Varbailes.Dexterity += 3
        Varbailes.Constitution += 2
        Varbailes.raceAbility = "Toughen skin"

    elif Varbailes.race == "Fiend":
        Varbailes.Intelligence += 2
        Varbailes.Wisdom += 2
        Varbailes.Charisma += 3
        Varbailes.raceAbility = "Undying Will"
    
    elif Varbailes.race == "Tabaxi":
        Varbailes.Dexterity += 3
        Varbailes.Charisma += 2
        Varbailes.raceAbility = "Godspeed"

    
    ##Wepaons
    
    if Varbailes.classes == "Knight":
        Varbailes.Constitution += 1
        Varbailes.Strength += 1
        Varbailes.abilty1 = "Sword Slash"

        if Varbailes.mainWepons in ["Mace","GreatSword","Sword"]:
            Varbailes.Strength += 1
            Varbailes.Constitution += 1

    
    elif Varbailes.classes == "Assassin":
        Varbailes.Dexterity += 1
        Varbailes.Intelligence += 1
        Varbailes.abitly1 = "Stealth Cloak"
        
        if Varbailes.mainWepons in ["Twin Daggers","Bow", "Short Sword"]:
            Varbailes.Dexterity += 1
            Varbailes.Intelligence += 1

    
    elif Varbailes.classes == "Wizard":
        Varbailes.Intelligence += 1
        Varbailes.Wisdom += 1
        Varbailes.abilty1 = "Fireball"

        if Varbailes.mainWepons in ["Staff","Orb","Wand"]:
            Varbailes.Wisdom += 1
            Varbailes.Intelligence += 1
    
    elif Varbailes.classes == "Theif":
        Varbailes.Dexterity += 1
        Varbailes.Charisma += 1
        Varbailes.abilty1 = "Kine eye"

        if Varbailes.mainWepons in  ["Dagger", "Short Bow", "Throwing Knives"]:
            Varbailes.Wisdom += 1
            Varbailes.Intelligence += 1
    
    elif Varbailes.classes == "Brawler":
        Varbailes.Constitution += 1
        Varbailes.Strength += 1
        Varbailes.abilty1 = "Rush"
        
        if Varbailes.mainWepons in ["Ganluents","Twin handaxes","Club"]:
            Varbailes.Constitution += 1
            Varbailes.Strength += 1
    
    elif Varbailes.classes == "Archer":
        Varbailes.Dexterity += 2

        if Varbailes.mainWepons in ["Bow","CrossBow","Throwing Daggers"]:
            Varbailes.Dexterity += 2

    if Varbailes.background == "Farmhand":
        Varbailes.Strength += 1
    
    elif Varbailes.background == "Iseaki":
        Varbailes.Strength += 1
        Varbailes.expMuiplier = 2
    
    elif Varbailes.background == "Gamabler":
        Varbailes.Intelligence -= 2
        Varbailes.Wisdom -= 1
        Varbailes.critChance1 = 1.5 

    elif Varbailes.background == "Scholar":
        Varbailes.Intelligence += 2
        Varbailes.Wisdom += 1
    
    elif Varbailes.background == "Warrior":
        Varbailes.Strength += 2
        Varbailes.Constitution += 1

    elif Varbailes.background == "alchemist":
        Varbailes.Wisdom += 2
        Varbailes.Intelligence += 1

    Varbailes.ConstitutionB = Varbailes.Constitution * 10
    Varbailes.health_total = Varbailes.Health + Varbailes.ConstitutionB

    time.sleep(2)
    os.system("clear")
    print(Varbailes.name,"the almighty")
    print("Race:", Varbailes.race)
    print("Class:", Varbailes.classes)
    print("Background:", Varbailes.background)
    print("Race Ability:", Varbailes.raceAbility)
    print("Class Ability:", Varbailes.abilty1)
    print("Abilty 1:",Varbailes.abilty2)
    print("Abilty 2",Varbailes.abilty3)
    print("\nStats")
    print("Strength:", Varbailes.Strength)
    print("Dexterity:", Varbailes.Dexterity)
    print("Wisdom:", Varbailes.Wisdom)
    print("Intelligence:", Varbailes.Intelligence)
    print("Charisma:", Varbailes.Charisma)
    print("Constitution", Varbailes.Constitution)
    print("Health:", Varbailes.health_total)
    print("\nWeapon :", Varbailes.mainWepons)
    next=input("Begin ...")
    
         
