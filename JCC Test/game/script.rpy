# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define g = Character('Gavin', color="#00FF00")
define m = Character('Me')

image gavin bigsmile = "gavin_big_smile_1.png"

default totalScore = 0
default name = ""
default isAsian = False
default bff = "Mikasa"
default Chihuahua = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_room_morning_1

    "Choose a difficulty level"
    
    menu:

    # Difficulty Level
    # Asian 			    + 10000  
    # Half asian 		    + 50
    # Fox girl			    + 10
    # Weeb			        + 5
    # Not asian		        + 0
    # Zombie kawaii girl 	+ 1
    # Deceased		        - 10
        
        "Asian": 
            $ totalScore += 10000
            $ isAsian = True

        "Half asian":
            $ totalScore += 50

        "Fox girl":
            $ totalScore += 10

        "Weeb":
            $ totalScore += 5

        "Not asian":
            $ totalScore += 0

        "Zombie kawaii girl":
            $ totalScore += 1

        "Deceased":
            $ totalScore -= 10


    "Choose Gender"

    menu:
        # Male 		- 1
        # Female	+ 0

        "Male":
            $ totalScore -= 1
        
        "Female":
            $ totalScore 

    "\"BEEP BEEP BEEP BEEP...\" your alarm is going off." # TODO: BEEP SOUND
    "You get up but --"
    m "Ouch!"
    "You hit your head on your shelf"
    "What day is it?"
    "What?! It’s Valentine’s Day!?!" 
    "Your heart begins to beat wildly"
    m "Today’s the day I’ve been waiting for. I am going to confess my love to Gavin!"
    m "But I’m so nervous… Will he like me back?"
    m "I have to talk to [bff] and come up with a plan!"


    menu: 
        # Nothing but a fox tail and fox ears 		+15
        # Nun outfit					            -10
        # Scarf and heavy clothing 			        +7
        # Maid outfit					            +5	

        "Maid outfit":
            $ totalScore += 5

        "Nun outfit":
            $ totalScore -= 10

        "Scarf and heavy clothing":
            $ totalScore += 7

        "Nothing but a fox tail and fox ears":
            $ totalScore += 15

    "Time to go to school!"

    scene bg_suburban_street # TODO:too small

    "You see many paths down the road. Which street do you take?"

    menu:

        "Chihuahua Court":
            $ Chihuahua = True

        "Shibuya Street":
            "hi" # TODO: add

        "Husky Hill":
            "hi" # TODO: add

        "Dildo Dive":
            "hi" # TODO: add

    "Awww! It's a cute dog! What are you going to do with it?" # TODO: INSERT A RANDOM DOG PIC

    menu:

        "Pet Dog": 
            if Chihuahua:
                $ totalScore -= 5
            else:
                $ totalScore += 10

        "Kick Dog":
            if Chihuahua:
                $ totalScore += 10
            else:
                $ totalScore -= 5

        "Pee on Dog":
            if Chihuahua or isAsian:
                # TODO: SOMETHING SHOULD HAPPEN
                pass
            else:
                # First bad ending
                "Turns out the dog was Gavin's dog. He gets upset and pees on you. Bad Ending."

    show gavin bigsmile

    if (totalScore >= 1000):

        g "I love you"

        "Gavin grabs you by the hair and kisses you. Happy Ending."

    else:

        g "I'm not interested"
        
        "Gavin grabs you by the hair and throws you out of his room. Bad Ending"

    # This ends the game.

    return
