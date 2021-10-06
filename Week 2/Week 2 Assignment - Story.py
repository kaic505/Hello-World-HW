print ("Welcome to MovieCallOuts!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

actorName1 = raw_input("Enter an actor or actress name: ")
yourName1 = raw_input("What's your name?: ")
adjective1 = raw_input("Enter an adjective: ")
song1 = raw_input("What is your favorite song?: ")
time1 = raw_input("What is your favorite time of the day: ")
character1 = raw_input("Enter your favorite character name: ")
character2 = raw_input("Enter your favorite villain name: ")
pronoun1 = raw_input("Is the villain a she or a he: ")
foodName1 = raw_input("Enter your favorite food: ")
adjective2 = raw_input("Enter one adjective of New York: ")
cost1 = raw_input("Guess how much a opening a Shake Shack cost on Braodway: ")
adjective3 = raw_input("Enter how the ending of any sega makes you feel: ")


story = "Today the headline says, a new born movie star " + yourName1 + \
     " will be starring in a movie with " + actorName1 + ". These two will be in a " \
     + adjective1 + " relationship. The movie is called " + song1 + " in the " + time1 \
     + ", the first one of a comedy trilogy made by Christopher Nolan. " + yourName1 + \
     " will play " + character1 + ", who becomes a villian in this movie." + \
     " And surprisingly, " + character2 + " will make a guest appearance. However, " + \ 
     pronoun1 + " got inspired by " + foodName1 + " and becomes a hero who saves the world(spoiler!). "\
     + "It is certainly a " + cost1 + " budget movie that will leave you feeling "\
     + adjective3 + " throughout the week, pondering over your " +  adjective2 + " life choices. "


print (story)

