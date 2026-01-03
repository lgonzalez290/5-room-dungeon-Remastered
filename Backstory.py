import Varbailes, os , time
def backStory():
    time.sleep(1)
    os.system("clear")
    print("""Ashkara was shaped by ancient continental shifts and wars long forgotten. 
Magic fractured the land into distinct regions, each claimed by a race that adapted to survive there. 
Borders were not drawn by fairness, but by power, fear, and loss.
Magic flows through all races, but how it is used—and who controls it—defines history. """)
    
    if Varbailes.race == "Orc":
        print("You have been born brutania a land full of proud orc warriors. They thrive on battle and seek nothing but pridful combact. ")
        print("You have been born into the home of timjohn and his wife barabrica.")
        print("You wake up in on your stone and you smell dinner cooking.")
        if Varbailes.game_start == True: 
            print("")

    elif Varbailes.race == "Fiend":
        print("You have been casted aside")
        print("We look the same but they didnt acept our differences")
        print("They didnt acpect out horns and tail they called us abnormal")
        print("They called us demons they perfomred a ritual and banished us to hell")
        print("Each and everyone of us they searched the lands to make sure")
        print("They banished us to hell but we lived and survied")
    
    elif Varbailes.race == "Human":
        print("""Innovators and conquerors. Humans built machines, firearms, and clockwork automatons (the first Robots). 
Fearing what they could not control, they hunted the Fiends, branding them heretics and monsters. 
Human cities sprawl across the plains, connected by roads, gambling halls, and horse routes.""")
    
    elif Varbailes.race == "Dwarf":
        print("""Unchanged and unbroken. Dwarves live as they always have: in colossal underground cities carved over millennia. 
Mining towns dot the surface above deep vaults of stone, gold, and ancient weapons. 
Their history remains untouched by the Ice Cream Cut.""")
    
    elif Varbailes.race == "Tabaxi":
        print("""Once numerous, now nearly myth. 
Elves are bound to ley lines and ancient living trees. 
Each elf born weakens the forest, so births are rare. 
They are masters of magic, but secrecy keeps them alive.""")
    
    elif Varbailes.race == "Mintor":
        print("""Born with an undying bloodlust. 
Mintor culture channels this curse into ritual combat and war‑chants. 
Without battle, they go mad.""")

    if Varbailes.background == "Gamabler" and Varbailes.backstoryTrue == True:
        Varbailes.start1 = print("As a child my house burned down. ...")
        Varbailes.enter1 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start2 = print("My entire family died ...")
        Varbailes.enter2 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start3 = print("Somone passsing by sees me on the street. My house burning in front of me. He walks up to me and asks ...")
        Varbailes.enter3 = input("Press enter to contuine ... ")
        time.sleep(2)
        os.system("clear")
        Varbailes.start4 = print("He says flip the coin it was a 50 50 chance he said he would save me if it landed on tails he would help me")
        Varbailes.enter4 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start5 = print("The coin flipped i waited in antpaction the coin land on the ground it landed on its side he said ""your one luck kid"" ")
        Varbailes.start6 = print("Then he gave me some money to help me back on my feet and ever since then i have been seraching for that man.")

    elif Varbailes.backgroundStory == "alchemist":
        Varbailes.start1 = print("As a child my household was never a normal one ...")
        Varbailes.enter1 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start2 = print("My parent being rennowed senctist they went mad over their research...")
        Varbailes.enter2 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start3 = print("After a failed experiment i playing outside with my friends my house exploxed ...")
        Varbailes.enter3 = input("Press enter to contuine ... ")
        time.sleep(2)
        os.system("clear")
        Varbailes.start4 = print("Even though my parents were world renowed scientist they always taught me to get everything myself. THey lefted me nothing")
        Varbailes.enter4 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start5 = print("I wandered the land teaching people my skills in alchemcy for money to get by.")
        Varbailes.start6 = print("Now i wander the eaarth serching the world for the best alchemist")


    elif Varbailes.backgroundStory == "Warrior":
        Varbailes.start1 = print("As a child my family was never thier  ...")
        Varbailes.enter1 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start2 = print("I never took that as a bad things i grew from it i became stronger...")
        Varbailes.enter2 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start3 = print("I lived my life valuing strength over anything else ...")
        Varbailes.enter3 = input("Press enter to contuine ... ")
        time.sleep(2)
        os.system("clear")
        Varbailes.start4 = print("The only way to get true strength is through hard work and prsvence")
        Varbailes.enter4 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start5 = print("My purpose is to defeat those who have wrong me i will show them that strength trumps all")
    
    elif Varbailes.backgroundStory == "Scholar":
        Varbailes.start1 = print("As a child my household was poor...")
        Varbailes.enter1 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start2 = print("We struggled even buying food my parents weren't given much but they fought for my edcation...")
        Varbailes.enter2 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start3 = print("They wanted a goodlife for me and I wont waste how much they have given to me ...")
        Varbailes.enter3 = input("Press enter to contuine ... ")
        time.sleep(2)
        os.system("clear")
        Varbailes.start4 = print("I will get the best edcation and make them proud. I will show and prove that no matter where you come from you can make somthing out of it")
        Varbailes.enter4 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")

    elif Varbailes.backgroundStory == "Isekai":
        Varbailes.start1 = print("I died...")
        Varbailes.enter1 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start2 = print("I didn't want to live anymore i had given up thought there was nothing left for me...")
        Varbailes.enter2 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start3 = print("When i died I woke up infront of god he gave me to options he said renincarte in a new world or die right here and never be rembered for anything...")
        Varbailes.enter3 = input("Press enter to contuine ... ")
        time.sleep(2)
        os.system("clear")
        Varbailes.start4 = print("I will make something of this new life even if i am not the hero i will make somthing of this life and become happy.")
        Varbailes.enter4 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")


    elif Varbailes.backgroundStory == "Farmhand":
        Varbailes.start1 = print("As a child my household was poor...")
        Varbailes.enter1 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start2 = print("We struggled even buying food my parents weren't given much but they fought for my edcation...")
        Varbailes.enter2 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")
        Varbailes.start3 = print("They wanted a goodlife for me and I wont waste how much they have given to me ...")
        Varbailes.enter3 = input("Press enter to contuine ... ")
        time.sleep(2)
        os.system("clear")
        Varbailes.start4 = print("I will get the best edcation and make them proud. I will show and prove that no matter where you come from you can make somthing out of it")
        Varbailes.enter4 = input("Press enter to contuine ...")
        time.sleep(2)
        os.system("clear")             
        