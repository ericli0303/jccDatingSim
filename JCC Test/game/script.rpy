# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define g = Character('Gavin', color="#00FF00")
define m = Character('Me')
define bff = Character('Kiomi')

image gavin bigsmile = "gavin_big_smile_1.png"

default totalScore = 0
default name = ""
default isAsian = False
default Chihuahua = False
default outfit = ""

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    "Disclaimer, everything in this dating sim is based on Gavin in real life. Everything he says or does, all of his preferences, all of it is based on Gavin."

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

    m "But first thing’s first, I have to put on my best for him."

    "What would you like to wear for Gavin?"
    menu: 
        # Nothing but a fox tail and fox ears 		+15
        # Nun outfit					            -10
        # Scarf and heavy clothing 			        +7
        # Maid outfit					            +5	

        "Maid outfit":
            $ totalScore += 5
            $ outfit = "maid"

        "Nun outfit":
            $ totalScore -= 10
            $ outfit = "nun"
            m "Something this bold and unique will get his attention for sure."
            m "Although, this might draw some unwanted attention."

        "Scarf and heavy clothing":
            $ totalScore += 7
            $ outfit = "winter"
            m "It’s cold outside, so these will have to do."

        "{b}Nothing{/b} but a fox tail and fox ears":
            $ totalScore += 15
            $ outfit = "fox"
            "You have a sudden craving for wheat…"
            m "hmmm very soft"
            m "He will love this for sure. Though, this might draw some unwanted attention."

        "School uniform":
            $ totalScore += 3
            $ outfit = "school uniform"
            m "Just cause it’s Valentine’s day doesn’t mean I can break the dress code!"

    "{i}I-I seemed to have forgotten my name… {w}that bump to the shelf must have really hurt...{/i}"
    "{i}What’s my name again?{/i}"

    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Shy Guy"
        
    define me = Character("[name]")

    #"{i}{/i}"
    "{i}Right, I'm [me]. Silly me, how could I have forgotten.{/i}"
    m "Alright. I’m off to school. Ittekimasu!"

# End of Bedroom Scene, entering Walking to School Scene
    scene bg_suburban_street # TODO:too small

    "You step out the front door onto your cozy neighborhood street."

    "The weather is beautiful, so you might as well walk to school today. It’s only a 20 minute stroll from here."
 
    "The sun is still low on the horizon, peeking occasionally out from between the houses as you walk down Chihuahua Court. The sidewalks are busy with kids heading to school, and adults rushing to work. "

    "As you are about to turn onto [school] a construction worker halts you."

    "Construction Worker" "Hey kid! You can’t go this way. We’re doing some emergency maintenance for the next few hours."

    "{i}I guess I’ll have to find a way around.{/i}"

    "{i}Let’s see, I could take Shibuya Street, but that’s always so crowded in the morning. {/i}"
    "{i}I could keep going down Chihuahua Court, but it will take me a lot longer to get to school that way. {/i}"
    "{i}On the other hand, Dildo Drive would theoretically get me to school, but I’ve heard that’s not the best part of town...{/i}"


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
