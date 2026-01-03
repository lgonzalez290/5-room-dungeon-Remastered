import Backstory
import Varbailes
import chararterSheet

def startG ():
    if Varbailes.game_start == True and Varbailes.race == "Human":
        print("You wake up in you bed in a villege in the Open plains")
        print("Objective: Find tasks")
        
        while Varbailes.playingShome:
            print("You can move around using inputs like (r)ight , (l)eft and (f)oward")
            Varbailes.actionh1 == input("Where would you like to move L/R/F")
            if Varbailes.action1.upper == "L":
                print("You walk over to a desk thier is a note on the top")
                print("Aquired note")
                print("Objective complted")
                print("Task:Go to the gamabling den")

    if Varbailes.game_start == True and Varbailes.race == "Orc":
        print("You wake up on a stone and you smell meat simmering and you see the the sun peaking over the mounatins.")
        
        while Varbailes.playingShome:
            print("You can move around using inputs like (r)ight , (l)eft and (f)oward")
            Varbailes.actionh1 == input("Where would you like to move L/R/F")
            if Varbailes.action1.upper == "":
                print("")
