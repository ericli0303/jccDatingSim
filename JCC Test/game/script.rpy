# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define g = Character('Gavin', color="#00FF00")  # uwu crush
define m = Character('Me', color="#FFFFFF")  # ME the MC
define bff = Character('Bff')  # the bestie of Me
define kiomi = Character('Kiomi')  # the bitch

image gavin bigsmile = "gavin_big_smile_1.png"
image construction = "construction worker.png"
image bff smug = "bff_smug.png"
image bff smile = "bff_smile.png"

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
    "Disclaimer: everything in this dating sim is based on Gavin in real life. Everything he says or does, all of his preferences, all of it is based on Gavin."

    scene bg_room_morning_1
    with fade
    play music "audio/soundtrack1.mp3" fadein 1.0 volume 0.3
    queue music "audio/soundtrack2.mp3"  volume 0.3

    menu:
    # Difficulty Level
    # Asian 			    + 10000
    # Half asian 		    + 50
    # Fox girl			    + 10
    # Weeb			        + 5
    # Not asian		        + 0
    # Zombie kawaii girl 	+ 1
    # Deceased		        - 10
        "Choose a difficulty level"
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

    menu:
        # Male 		- 1
        # Female	+ 0
        "Choose Gender"
        "Male":
            $ totalScore -= 1

        "Female":
            $ totalScore

    play sound "<from 1.5 to 2.5>audio/alarm.mp3" volume 0.6  # TODO: BEEP SOUND
    "\"BEEP BEEP BEEP BEEP...\" your alarm is going off."

    "You get up but --"
    with vpunch
    m "Ouch!"
    "You hit your head on your shelf"
    "What day is it?"
    with hpunch
    "What?! It’s Valentine’s Day!?!"
    "Your heart begins to beat wildly"
    m "Today’s the day I’ve been waiting for. I am going to confess my love to Gavin!"
    m "But I’m so nervous… Will he like me back?"
    m "I have to talk to [bff] and come up with a plan!"

    m "But first thing’s first, I have to put on my best for him."

    menu:
        "What would you like to wear for Gavin?"
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

    m "Wait... hmm..."
    "{i}I-I seemed to have forgotten my name… {w}that bump to the shelf must have really hurt...{/i}"
    "{i}What’s my name again?{/i}"

    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Shy Guy"

    define myName = Character("[name]")

    # "{i}{/i}"
    "{i}Right, I'm [myName]. Silly me, how could I have forgotten.{/i}"
    m "Alright. I’m off to school. Ittekimasu!"

# End of Bedroom Scene, entering Walking to School Scene
    scene bg_suburban_street
    with fade

    "You step out the front door onto your cozy neighborhood street."

    "The weather is beautiful, so you might as well walk to school today. It’s only a 20 minute stroll from here."

    "The sun is still low on the horizon, peeking occasionally out from between the houses as you walk down Chihuahua Court. The sidewalks are busy with kids heading to school, and adults rushing to work. "

    "As you are about to turn onto Takoyaki Trail a construction worker halts you."

    show construction at right
    with dissolve

    "Construction Worker" "Hey kid! You can’t go this way. We’re doing some emergency maintenance for the next few hours."

    "{i}I guess I’ll have to find a way around.{/i}"

    hide construction

    "{i}Let’s see, I could take Shibuya Street, but that’s always so crowded in the morning. {/i}"
    "{i}I could keep going down Chihuahua Court, but it will take me a lot longer to get to school that way. {/i}"
    "{i}On the other hand, Dildo Drive would theoretically get me to school, but I’ve heard that’s not the best part of town...{/i}"

    menu:
        "Which street do you take?"

        "Chihuahua Court":
            $ Chihuahua = True
            jump chihuahua

        "Shibuya Street":
            jump shiba

        "Dildo Drive":
            jump dildo

# Shiba Street
label shiba:
    scene bg_urban_street
    "{i}Taking Shibuya Street is probably the best option…{/i}"
    "You backtrack a block or so until you are back on Shibuya Street. The street is full of honking cars in a traffic jam caused by something far away. Salarymen pack the sidewalks pushing in all directions, trying to get to their offices. "
    "Eventually you push your way through the biggest crowds and find a smaller road to walk on."
    jump street_over

# Chihuahua Court
label chihuahua:
    scene bg_suburban_street3
    "Taking Chihuahua Court is probably the best option…"
    "You keep walking, and walking. Chihuahua Court is scenic for sure. You walk over a wide wooden bridge which passes over a creek. Nearby you spot a torii gate, which marks the entrance to your local shrine. "
    menu:
        "Do you want to stop by for a quick prayer?"

        "Yes":
            "You stop in your tracks, then head through the gate into the shrine’s courtyard."
            "You stop in front of the offering box. "
            "Fumbling a bit, you grab a coin out of your pocket and toss it as your offering to the shrine’s kami. "
            "You bow, then clap your hands twice, sending a quick prayer to the kami. "
            "{i}Please, please let Gavin like me back. And please give me the strength to confess to him!{/i}"
            "With that done, you leave the shrine and continue on the scenic route to school. "
            "{i}Shit! I’m already late!{/i}"

        "Nah":
            "{i}I want to ask the kami to bless me and give me the courage to confess to Gavin, but I am already running late.{/i}"
            "You pass the shrine and continue on the scenic route to school."
    "It takes several minutes, but you finally reach a road that will get you back on track. "
    "{i} I’ve wasted so much time going this way.{/i}"

# Dildo Drive
label dildo:
    scene bg_dildoway
    "You head down the road a little longer and turn onto Dildo Drive. "
    "The road is narrow and winding. Buildings here have exposed pipes rusting in the elements. Brick fences are crumbling, and trash piles up in corners. Occasionally you see people loitering on the sidewalks. Some of them stare at you as you walk by. "
    "{i}Ugh, it smells bad here. It’s like the smell of a dog who just got peed on by a human. Gross!{/i}"
    "As you pass by a dark alleyway, you hear a whistle from it’s depths. "
    "A raspy, growling voice" "hey cute girl, come over here."
    "You feel a poke on your lower back"
    "Surprised and scared, you start running down the road. The road slopes downwards pretty intensely here."
    if(isAsian):
        "{b}thump, thump, thump{/b} go footsteps behind you. Faster, faster!"
        "Because of the steep incline, you lose your balance and fall…"
        with hpunch
        with hpunch
        with hpunch
        "{b}THUD{/b}"
        "You tumble down the hill, bouncing off of the ground repeatedly as you fall helplessly."
        "Your body comes to a sudden, painful halt, as you hit a light post and your limp body curls around it."
        "{i}Shit, I can’t ask Gavin out like this…{/i} {w} you think as you close your eyes and slowly lose consciousness. "
        "{i}I really got screwed over by them.{/i}"
        return
    else:
        "hi"  # TODO

label street_over:
    "hi"  # TODO: Add this

    # TODO: INSERT A RANDOM DOG PIC
    show chihuahua at right
    play sound "bark.mp3"
    "Awww! It's a cute dog! What are you going to do with it?"
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

    scene bg_school_room with fade

    "You arrive in your homeroom, out of breath from running."

    # show bff delighted with easeinright

    bff "Ohayou [myName]-san! You're late, as usual {i}hehe.{/i}"

    with fade

    "*She pulls you*"

    menu:

        # show bff smug with dissolve
        bff "*whispers* Say, you remember that it's Valentine's day right?"

        "Of course!":

            # show bff shocked with dissolve
            bff "Ohh confident, aren't ya? Gavin-san is a lucky guy."

        "Confess to who?":
            # show bff laugh with dissolve
            bff "Don't be silly, I know you're head over heels for Gavin-san"

    menu:

        # show bff smile with dissolve
        bff "So, are you going to give him chocolates?"

        "No, I can't...":

            # show bff annoyed with dissolve
            bff "Do it, you dummy! How else will he know that you have feelings for him?"

        "Shit, I forgot!":

            # show bff annoyed with dissolve
            bff "You dummy! How could you forget about something this important?"

    # show bff smile with dissolve
    bff "I hear the cafeteria is running a Valentine's Day special. You can buy chocolates there if you have enough money!"

    "..."

    # show bff shocked with dissolve
    "Look! Gavin-san is here! Wait... What is happening?"

    # hide bff
    # Kiomi ARC
    kiomi "Gavin-san! Ohayou!"
    kiomi "I made something for you. I hope you like it..."
    "She pulls a box out from behind her back and offers it to Gavin-san."

    g "... Kiomi-chan... I-I don't know what to say..."

    menu:

        "*INTERRUPT*":
            m "HOLD IT RIGHT THERE!"
            "Dashing across the room, you smack the box of chocolates out of her hands. The shiny round chocolates spill out and scatter across the floor."
            kiomi "You... You bitch!"
            "*Kiomi starts crying*"
            g "What was that for [myName]-san?"
            g "Don't worry Kiomi-san, I'll help you pick these up."
            "Gavin and Kiomi drop to the floor and start picking up the chocolates."
            g "See, they’re still fine to eat!"
            "*gulp*"
            g "Wow these are delicious! This was super sweet of you, Kiomi-chan!"
            kiomi "*sniff* You really mean it?"
            "Gavin turns to face you"
            g "I can't believe you would do something like that, [myName]-san. I thought you were nicer than this."
            "Kiomi lightly grabs Gavin's arm to get his attention"

        "*Just watch*":
            "Gavin opens the box"
            g "Wow! These chocolates look amazing!"
            "*gulp*"
            g "And they taste amazing too! This was super sweet of you, Kiomi-chan!"
            kiomi "Yay! I'm glad you like them!"
            kiomi "..."

    kiomi "Gavin-san..."
    "I have something I want to tell you-"

    "*RINNGGGG*"
    "Just before Kiomi is about to finish saying something, the school bell goes off. It is time for your first class."
    g "Ah, it's time for class. See you guys later. Thanks again for the chocolates Kiomi-chan!"
    "Gavin runs off to his first class"
    "Kiomi-san glares at yoo... Then grins."
    kiomi "He's mine, loser."
    bff "Shut up. We all know Gavin-san likes [myName]-san, so you're out of luck."
    bff "Tonight when [myName] confesses to him, you’ll see how hopeless your situation is!"
    bff "Come on, [myName]. Let’s go to class."

    show gavin bigsmile

    if (totalScore}=1000):

        g "I love you"

        "Gavin grabs you by the hair and kisses you. Happy Ending."

    else:

        g "I'm not interested"

        "Gavin grabs you by the hair and throws you out of his room. Bad Ending"

    # This ends the game.

    return
