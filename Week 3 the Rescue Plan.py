
import random # random numbers (https://docs.python.org/3.3/library/random.html)
import sys # system stuff for exiting (https://docs.python.org/3/library/sys.html)

player = { 
    "name": "p1", 
    "items" : ["gun"],
    "rescued": ["Erin"],
    "score": 0,
    "location" : "start"
}

Chapters = {
    "Chapter1" : "firstencounter",
    "Chapter2" : "turningPoint",
    "Chapter3" : "finalShot"
}

def printGraphic(name):
    if (name == "time"):
        print (' ------     -------     -------    ------- ')
        print ('       |   |       |   |       |  |       |')
        print ('       |   |       |   |       |  |       |')
        print (' ------    |       |           |  |       |')
        print ('|          |       |           |  |       |')
        print ('|          |       |           |  |       |')
        print (' ------     -------            |   ------- ')

    if (name == "Masked Joker"):
        print ('      _____      ')
        print ('     /     \     ')
        print ('    / /\ /\ \    ')
        print ('   /  o   o  \   ')
        print ('   \  (_V_)  /   ')
        print ('    \  \_/  /    ')
        print ('     \_____/     ')
        print ('   Masked Joker  ')

    if (name == "Notebook"):
        print ('     _____________  ')
        print ('    ( |           | ')
        print ('    ( |           | ')
        print ('    ( |           | ')
        print ('    ( |          O| ')
        print ('    ( |           | ')
        print ('    ( |           | ')
        print ('    (_|___________| ')
        print ('       Notebook     ')
    
    if (name == "Photo"):
        print ('  ____________  ')
        print (' |   __       | ')
        print (' |  /  \      | ')
        print (' |  \  /      | ')
        print (' |   ||  O W  | ')
        print (' |  /||\/|\V  | ')
        print (' |   /\  /\   | ')
        print ('  ------------  ')
        print ('     Photo      ')

    if (name == "Key"):
        print ('      .````.     ')
        print ('     : [][] :    ')
        print ('     `.    .`    ')
        print ('       :  :      ')
        print ('       :  `>     ')
        print ('       :  |      ')
        print ('       :   >     ')
        print ('       :   >     ')
        print ('       :  ]      ')
        print ('        \/       ')
        print ('       Key       ')

    if (name == "Open"):
        print ('  ___________ ___________  ')
        print (' | 09/14/2069| 4 a year  | ')
        print (' |  I am an  |in exchange| ')
        print (' |  AI too.  |of gaining | ')
        print (' |           | my own    | ')
        print (' |  I will   | mind.     | ')
        print (' |  passout  |           | ')
        print (' |___________|___________| ')
        print ('    Open Notebook          ')
        
    if (name == "PhotoZoom"):
        print ('  wwww ')
        print ('  (  ) ')
        print ('   ||  ')
        print ('  \||/ ')
        print ('   \/  ')
    
    if (name == "Room"):
        print ('                      _______         ')
        print ('     _________       /___$__/|   www  ')
        print ('    /____$___/|  ___|______|/|   \ /  ')
        print ('   |=========|| /____$___/||/|   / \  ')
        print ('   |=========|||=========|||/|  / $ \ ')
        print ('   |_________|/|_________|/|/   \___/ ')
        
    if (name == "Dan"):
        print ('    /`````\    ')
        print ('   `|`>`<`|`   ')
        print ('     \_o_/     ')
        print ('     /   \     ')
        print ('  \\|     |//  ')
        print ('    |     |    ')
        print ('     |`|`|     ')
        print ('     |`|`|     ')
        print ('      O O      ')

    if (name == "Dan2"):
        print ('    /`````\    ')
        print ('   `|`^`^`|`   ')
        print ('     \_v_/     ')
        print ('     /   \     ')
        print ('  \\|     |//  ')
        print ('    |     |    ')
        print ('     |`|`|     ')
        print ('     |`|`|     ')
        print ('      O O      ')
    
    if (name == "Money"):
        print ('      www    ')
        print ('      \ /    ')
        print ('      / \    ')
        print ('     /   \   ')
        print ('    /  $  \  ')
        print ('    \_____/  ')
       



#Set up
def introduction():
    print ("Welcome to 2070! Tell us your name")
    player["name"] = raw_input("Enter your name here:")
    #Chapter 0
    print ("Welcome to 2070 " + player["name"] + "!")
    print ("You are now in a mixed wolrd of Money Heist and Joker, only 50 years after.")
    print ("The decision you make in this world will determine if a little boy lives or not.")
    print ("There is no right or wrong endings.")
    print ("Are you ready to take on the job?")

    pcmd = raw_input("please choose yes or no: ")

    #the player chooses yes or no
    if (pcmd == "yes"):
        print ("Let us begin...")
        print ("You open your eyes, and see yourself holding a gun in your hand.")
        print ("However, it felt a bit too light, so you know there's no bullet in it anymore.")
        print ("Because of that, you panicked a bit.")
        raw_input("press enter: ")
        firstEncounter()
    else:
        print ("Oops...come back when you're ready for the future!")
        pcmd == raw_input("press enter: ")
        introduction()

def firstEncounter():
    printGraphic("Masked Joker")
    print ("You then look up and find a masked person standing in front of you.")
    raw_input("press enter: ")
    printGraphic("Dan")
    print ("He has captured a young boy named Dan, and is pointing his gun to him right now.")
    raw_input("press enter: ")

    print ("'I suggest you be smarter and put down your gun' the masked person says.")
    print ("You soon realize that you three are the only standing people in the room, and all the noises coming from the outside aren't helping.")
    printGraphic("Room")
    print ("You take a quick scan of the room, and see gold, cash, and jewlary laying around. You begin to piece together everything...you're in a bank!")
    raw_input("press enter: ") 

    print ("'Who are you?' you say.")
    print ("'I'm Joker from 2070. And I'll save you some time by telling you I'm an AI robot. You wouldn't stand a chance beating me.' he laughed.")
    raw_input("press enter: ")

    print ("You cool down and have two options on your mind: [A. Find clues first, B. Fight him]")
    pcmd = raw_input("You choose an option:")

    #option 1:find clues first
    if (pcmd == "B"):
        print ("You got shot by Joker because there's no bullet in your gun ...")
        looseGame()
    #option 2:fight
    elif (pcmd == "A"):
        printGraphic("Notebook")
        printGraphic("Photo")
        printGraphic("Key")
        print ("You see a notebook, a photo, and a key on the floor, but you only have time to check out one of them.")
        print ("You point your 'gun' at Joker, and choose to pick up: [notebook, photo, key]")

    pcmd = raw_input(":")

    #option A: notebook
    if (pcmd == "notebook"):
        printGraphic("Open")
        player["items"].append("notebook")
        print ("You discovered a shocking truth in the notebook. You, just like Joker, are also a robot with conciousness.")
        turningPoint()

    #optionB: photo
    elif (pcmd == "photo"):
        printGraphic("PhotoZoom")
        player["items"].append("photo")
        print ("You saw an AI robot happy with a human boy in the photo. They are holding hands, and the boy is holding a flower too beautiful to be true.")
        turningPoint()

    #optionC: key
    elif (pcmd == "key"):
        printGraphic("Key")
        player["items"].append("key")
        print ("You hold up the key, and find 'Dan, since 2060' ingraved on it")
        print ("You realized that Joker has been taking care of Dan since he was 5. But something happened...")
        turningPoint()

def turningPoint():
    print ("With the clue you discovered, you begin to formulate your next move.")
    print ("And you decided to talk to Joker first.")
    raw_input("press enter: ")
    if ("notebook" in player["items"]):
        print ("options: [A: Reveal your true identity to Joker to get him on your side, B: Talk senses to him by citing famous quotes, C: Fight him believing you can now]")
    elif ("photo" in player["items"]):
        print ("options: [A: Reveal your true identity to Joker to get him on your side, D: Empathize with his past, E: Offer him laods of money]")
    elif ("key" in player["items"]):
        print ("Your plan is to: [A: Reveal your true identity to Joker to get him on your side, D: Empathize with his past, E: Offer him laods of money")

    pcmd = raw_input(":")
    if (pcmd == "A"):
        player["score"] += 50
        print ("'Hey, I may not know thr reason you're doing this, especially why you're holding this human boy hostage, but I am your pal, I'm also an AI robot. Talk to me, Let's sort things out together.' you say.")
        raw_input("press enter:")
        print ("'Good, you are the same team, so you'll know why I am doing this. Dan and I used to be so close, but it didn't change the fact we are in totally different places' said the Joker.")
        pcmd = raw_input("Choose your next move: [A. Threaten to open the door for police locked outside cause it's taking too long B. You are intuiged by him response, dig deepper into the story C. Say you'll help him escape if he doesn't hurt the boy.] Which one?")
        
        if (pcmd == "A"):
           print ("Joker gets mad and defeats you.")
           looseGame()

        elif (pcmd == "B"):
            print ("'What happned?' you say.")
            print ("'10 years ago, when he was so little, we used to be so close. I'd make him ice-cream, I'd grow him pretty flowers, and I'd build him robot toys' Joker laughed. 'Sarcastic right?'")
            raw_input("press enter: ")
            print ("'But as the world changes and as he grows up, the more devided the world is. Robots are no longer considered family because of our counciousness, and Dan only hangs with his human friends due to this shift. I don't fit in anymore and I'm not normal.' Joker continues.")
            raw_input("press enter: ")
            print ("His words make you think of your past experiences, you decided to share it.") 
            print ("'I was just like you. I was in a human family for over 20 years and I also find it hard to face our differences. But what you are saying is the world's problem, not this young boy's. He is not to blame for the division and internal struggle.' you say. ")
            print ("'Then...what should I do?' Joker says.")
            pcmd = raw_input("you see a chance here, so you decided to [A. Arrest Joker while he was distracted with your words B. Keep talking. Which option?: ]")
            if (pcmd == "A"):
               print ("You catch him and the police breaks in on time.")
               okGame()
            elif (pcmd == "B"):
               print ("You and Joker have a long talk. Finally the police break in and capture him")
               winGame()
        elif (pcmd == "C"):
            print ("'I know it's hard, but Dan isn't the problem. Think of all the memories you've been through. Please at least let him go. If you do that, I promise you, I'll never turn you in. Take everything you want from here, lash out your anger but not on Dan.'")
            print ("Joker takes everything in the room but leaves Dan.")
            okGame()
        
                
    elif (pcmd == "B"):
        print ("Joker looses patience and attacks you.")
        looseGame()
    elif (pcmd == "C"):
        player["score"] += 30
        print ("You turn out to be just as strong as Joker, just without a gun.")
        print ("So you lower you body, and attack him unexpectedly from the side, eventually saving Dan.")
        winGame()

    elif (pcmd == "D"):
        player["score"] += 50
        print ("From the clues you got. You imagine Joker has a difficult past that makes him want to turn on all humans, even to the extreme of catching the young boy he was once so close with.")
        pcmd = raw_input("What do you think Joker wants, attention, the money, or neither?: ")

        if (pcmd == "attention"):
            print ("'Hey. Listen to me. You don't have to harm the young boy. The whole country and humans are paying attention to you, and litsening to what you have to say.'you say.")
            print ("'Why are you saying this?' Joker reponds.")
            raw_input("press enter: ")
            print ("'I'm saying this because whatever you say right now matters. You don't have to harm the boy to make your point. You just have to communicate with the people outside.  Me, as a robot myself, have the same thought. I am woke and am not so satisfied with the system.'")
            print ("'Will you turn me in if I let go of my hostage?' Joker remains skeptical.")
            print ("'No.' you say.")
            print ("Joker lets go of Dan.")
            raw_input("press enter: ")
            pcmd = raw_input("What is your next move, A. Keep your promise and let Joker go. B. Turn on him and catch him while Dan is safe:")
            
            if (pcmd == "A"):
                okGame()
            elif (pcmd == "B"):
                winGame()
        elif (pcmd == "money"):
            print ("'I do love money and I'm going to take Dan away with me for what's worth.' Joker laughs.")
            looseGame()

        elif (pcmd == "neither"):
            Gameover()
    
    elif (pcmd == "E"):
        print ("'I'll give you 1000 grands. Man, I'll even persuade the government to give you more if you let go of Dan!' you say.")
        raw_input("press enter: ")
        print ("'Why would I want the money when I'm already in a bank I'm taking full control of' Joker laughed. 'Not to mention I don't even care about it. Caio" + player["name"] + "!'")
        looseGame()
            

def looseGame():
    print ("The boy and the money are both lost. Joker ran away. Try again next time:) " + player["name"] )

def okGame():
    player["score"] += 150
    printGraphic("Dan1")
    player["rescued"].append("Dan")
    print ("Wow...that was tough right? " + player["name"] + " Congratulation on saving Dan.")
    raw_input("press enter:")
    print ( "Your score is: " + str(player["score"]) )

def winGame():
    player["score"] += 100
    printGraphic("Dan1")
    printGraphic("Money")
    player["rescued"].append("Dan")
    player["items"].append("money")
    print ("Dan is safe and nothing got rubbed. You guess this is the best outcome, but the same time, it's hard for you to tell if this is what real justice is. To be continued...")
    raw_input("press enter:")
    print ( "Your score is: " + str(player["score"]) )

def Gameover():
    player["score"] += 200
    print (player["name"] + " You are right! He might seems to care about the money and the attention. But what he really wants, is to make connection with both robots and humans. You win:)")
    raw_input("press enter:")
    print ( "Your score is: " + str(player["score"]) )

def main():
    printGraphic("time")
    introduction()

main()

