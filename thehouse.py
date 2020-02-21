#####################################
#            THE HOUSE              #
# written and coded by Liam Iverson #
#####################################
import os
clear = lambda: os.system("cls")


#character related stats
playerName = ''
food = 0
water = 0
wood = 0
scrapMetal = 0
spareParts = 0
ammo = 0
flamerFuel = 0
fuel = 0


#NPC
npcs = []

#Locations
world = ["SaltedEarth","Yard"]




gameOn = False
def startGame():
    global food,water,wood,scrapMetal,spareParts,ammo,flamerFuel,fuel,gameOn
    print("#########################################\n")
    print("##############THE.HOUSE##################\n")
    print("#########################################\n")
    playerName = input("Please Enter your name: ")
    clear()
    print("##################################################################################\n")
    print("#            You remember the days before the great fall, hardly.                #\n")
    print("#            The sky was still blue and warmth still reached the                 #\n")
    print("#            surface. Bringing life where now only a radioactive                 #\n")
    print("#            desert lay. The Salted Earth as called by the tribals,              #\n")
    print("#            haunted by the horrifying creatures we left behind. That            #\n")
    print("#            had caused all this. Nuclear hellfire had not rained down for       #\n")
    print("#            without a reason. No. A great purging, of something that had        #\n")
    print("#            found itself here. Crawled its way out of Antarctica after a        #\n")
    print("#            million years of rest. The people it touched became 'it', they      #\n")
    print("#            might have resembled themselves but they were nothing but an        #\n")
    print("#            extension. A horrible amalgametion of all its genetic material      #\n")
    print("#            once its shell human exterior was revealed. By the time our         #\n")
    print("#            planets surface was scorched no one in the White House or           #\n")
    print("#            Kremlin new who was human or it. Some legends say the missiles      #\n")
    print("#            were fired once the president saw most of his chief of staff        #\n")
    print("#            turn. It didn't matter now. All that did was you survived,          #\n")
    print("#            forced to wonder this blighted land.                                #\n")
    print("##################################################################################")
    input("")
    food = 3
    water = 2
    wood = 0
    scrapMetal = 0
    spareParts = 0
    ammo = 0
    flamerFuel = 0
    fuel = 0

    gameOn = True
    gameLoop()



def gameLoop():
    global gameOn

    while (gameOn):
        drawEnviroment(world[0])
        input()



def drawEnviroment(location):
    clear()
    if(location == "SaltedEarth"):
        print("#################################################################")
        print("#                                                               #")
        print("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
        print("#       ~                                   /\                  #")
        print("#     ~  ~                                 /  \                 #")
        print("#                                          |  |                 #")
        print("#                                                               #")
        print("#                            .                                  #")
        print("#                                                               #")
        print("#                                                               #")
        print("#                                                               #")
        print("#        *              *              *                        #")
        print("#################################################################")




startGame()
