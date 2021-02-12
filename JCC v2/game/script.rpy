# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define g = Character('Gavin', color="#00FF00")  # uwu crush
define m = Character('Me', color="#FFFFFF")  # ME the MC
define bff = Character('Bff')  # the bestie of Me
define kiomi = Character('Kiomi')  # the bitch
define unknown = Character('???') # used as placeholder for unknown
define teacher = Character('Teacher')

image gavin bigsmile = "gavin_big_smile_1.png"
image construction = "construction worker.png" # construction


default totalScore = 0
define inventory = set()
default name = ""
default isAsian = False
default Chihuahua = False
default outfit = ""
default mainDish = ""


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    "Disclaimer: everything in this dating sim is based on Gavin in real life. Everything he says or does, all of his preferences, all of it is based on Gavin."

    scene bg_room_morning_1
    with fade
    play music "audio/soundtrack1.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop

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

    play sound "<from 2.4 to 4.6>audio/alarm.mp3" volume 0.7 
    "\"BEEP BEEP BEEP BEEP...\" your alarm is going off."
    "You get up but --"
    with vpunch
    m "Ouch!"
    "You hit your head on your shelf"
    "{i}What day is it?{/i}"
    with hpunch
    "{i}What?! It’s Valentine’s Day!?!{/i}"
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
    with fade
    "{i}Taking Shibuya Street is probably the best option…{/i}"
    "You backtrack a block or so until you are back on Shibuya Street. The street is full of honking cars in a traffic jam caused by something far away. Salarymen pack the sidewalks pushing in all directions, trying to get to their offices. "
    "Eventually you push your way through the biggest crowds and find a smaller road to walk on."
    jump street_over

# Chihuahua Court
label chihuahua:
    scene bg_suburban_street_3
    with fade
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
    jump street_over

# Dildo Drive
label dildo:
    scene bg_dildoway
    play music "audio/boss music.mp3" volume 0.5
    with fade
    "You head down the road a little longer and turn onto Dildo Drive. "
    "The road is narrow and winding. Buildings here have exposed pipes rusting in the elements. Brick fences are crumbling, and trash piles up in corners. Occasionally you see people loitering on the sidewalks. Some of them stare at you as you walk by. "
    "{i}Ugh, it smells bad here. It’s like the smell of a dog who just got peed on by a human. Gross!{/i}"
    "As you pass by a dark alleyway, you hear a whistle from it’s depths. "
    "A raspy, growling voice" "hey cute girl, come over here."
    "You feel a poke on your lower back"
    "Surprised and scared, you start running down the road. The road slopes downwards pretty intensely here."
    if(not isAsian):
        "{b}thump, thump, thump{/b} go footsteps behind you. Faster, faster!"
        "Because of the steep incline, you lose your balance and fall…"
        with hpunch
        with hpunch
        with hpunch
        play sound "audio/game over.mp3" volume 0.5
        "\"{b}THUD{/b}\""
        "You tumble down the hill, bouncing off of the ground repeatedly as you fall helplessly."
        "Your body comes to a sudden, painful halt, as you hit a light post and your limp body curls around it."
        "{i}Shit, I can’t ask Gavin out like this…{/i} {w} you think as you close your eyes and slowly lose consciousness. "
        "{i}I really got screwed over by them.{/i}"
        return
    else:
        "You hear the voice behind you say \"Shit, forget that brat.\""
        "You keep running and pass by some person making weird moaning sounds by the back alleyway. {b}AIEEEEEE…{/b}"
        "Not bothering to find out who called you a brat, you turn the corner and duck behind one of the nearby trash cans overflowing on the side of the street."
        "\"pant pant\""
        "Breathing heavily, you cautiously peek over the top to see if anyone followed you."
        "The street is empty, but suddenly you look down into the trash can, and it’s just… full of dildos!?"
        "You pull one out for safekeeping (though it looks a bit yellow and crusty)- but also for science (of course)."
        $ inventory.add("dildo")
        "Then you continue down the hilly street to school, turning onto a less trashy road."


label street_over:
    play music "audio/soundtrack1.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop
    "{i}Whew, that was a tiring detour. Only 2 blocks to go!{/i}"
    "Rushing along, you are minding your own business until suddenly..."
    
    play sound "<from 0 to 1.0>audio/bark.mp3" volume 0.7
    show chihuahua at right with fade
    "Dog" "WOOF WOOF BARK BARK."
    "A dog bounds up to you and tries to jump in your face."

    "UWAH! What do you do?"
    menu:

        "Pet Dog":
            if Chihuahua:
                $ totalScore -= 2
                jump petchew
            else:
                $ totalScore += 5
                jump petshiba

        "Kick Dog":
            if Chihuahua:
                $ totalScore += 5
                jump kickchew
            else:
                $ totalScore -= 3
                jump kickshiba

        "Pee on Dog":
            if Chihuahua or isAsian:
                # TODO: SOMETHING SHOULD HAPPEN
                pass
            else:
                jump peeshiba
                
        "Wield the dildo as a blade" if inventory.contains("dildo"):
            "hi" #TODO

label petshiba:
    "{i}Awww what a cute doggo!{/i}"
    "You stop to ruffle the smol shib behind the ears as it wags its curly tail. You give the good woofer a nice butt rub and he closes his eyes in shiawasei bliss before you let him go from his lovely massage from a stranger and watch him stroll down the street."
    jump dog_over

label petchew:
    "{i}Well I guess you are into terrifying balls of hate that exude the arrogance of a humans in their small disease ridden bodies.{/i}"
    "Like idk why ANYONE would want to pet this small smelly thing, probably gonna get bitten but go for it."
    "You reach down to pet the dog but it growls at you."
    menu:
        "Do you really wanna pet the dog?"
        "Yes":
            "Wow not even backing down from the aggressive growl."
            "Well you’re driven today so you stick your hand in there against its will and probably the owners but whatever."
            "You go for the classic head pat but before you get there its growl grows louder and you sense every cell is in danger."
            menu:
                "Do you continue?"
                "Yes":
                    "Welp, I guess you’re crazy but playing this game in the first place definitely says something."
                    "You try to press your hand on its peanut sized head but as expected when your instinct screams in fright it goes in and attacks your kind being and pierces your skin."
                    "Now you’re bleeding and more late for school, but you gain +3 determination."
                "No":
                    "Well, at least you followed your instincts in the end, you back off and head to school." 
        "No":
            "Yeah better off not petting it. You ignore the dog and head off to school."

label kickshiba:
    "{i}Ugh, this dog is about to make me more late!!{/i}"
    "You give the dog a nice kick in the butt with the toe of your shoe."
    "The dog whimpers and gives you a sad face as it hangs its head and tail between its legs."
    jump dog_over

label kickchew:
    "You try to kick the dog, but it growls and quickly bites your leg."
    "Your leg starts to bleed a bit and now you have to limp the rest of the way."
    jump dog_over

peeshiba
    "YEAH ASSERT YOUR DOMINANCE!"
    "Show the dog who’s boss. You let a fluid, continuous stream of pee out."
    "Onlookers stare in half surprise and disgust while mothers shield their children's eyes from your distasteful act."
    "Everyone seems too taken aback from your sudden action in Japan where no one strays from the norm, BUT out of the blue you hear a yell."
    "????" "WTF, WHAT ARE YOU DOING TO TOFU-CHAN!!!!! IS THAT PEE!!!"
    "Oh no, the owner is here but wait, why does your heart go aflutter at this tone."
    "Why is there a bittersweet emotion stirring in your heart. You take a glace in the direction of the voice but want to hide deep down in a hole and escape this unbelievable reality."
    g "Huh… wait… it can’t be… is that you [myName]-san…?"
    m "Ahh.. G. Ga.. Gavin ummm I can explain"
    "{i}Everything is falling apart. Why is he here now. Ah this is the worst.{/i}"
    "{i}It was only a small pee that I have been holding in all day.{/i}"
    "{i}I needed to relieve myself and feel top of my game before confessing but AHHHH now I want to dieeee.{/i}"
    "{i}Wait but go back a second, he said \"Tofu-chan\" not just dog… This couldn’t possibly be his dog, right?{/i}"



label dog_over:

    scene bg_school_room with fade

    "You arrive in your homeroom, out of breath from running."

    show bff delighted with easeinright
    with fade

    bff "Ohayou [myName]-san! You're late, as usual {i}hehe.{/i}"


    "*She pulls you*"
    show bff smug with dissolve
    
    menu: 
        bff "*whispers* Say, you remember that it's Valentine's day right?"

        "Of course!":

            show bff shocked with dissolve
            bff "Ohh confident, aren't ya? Gavin-san is a lucky guy."

        "Confess to who?":
            show bff laugh with dissolve
            bff "Don't be silly, I know you're head over heels for Gavin-san"


    show bff smile with dissolve
    menu:
        bff "So, are you going to give him chocolates?"

        "No, I can't...":

            show bff annoyed with dissolve
            bff "Do it, you dummy! How else will he know that you have feelings for him?"

        "Shit, I forgot!":

            show bff annoyed with dissolve
            bff "You dummy! How could you forget about something this important?"

    show bff smile with dissolve
    bff "I hear the cafeteria is running a Valentine's Day special. You can buy chocolates there if you have enough money!"

    "..."

    show bff shocked with dissolve
    "Look! Gavin-san is here! Wait... What is happening?"

    
    
    hide bff
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

    scene bg_classroom1

    "Your first class of the day is Biology."
    teacher "Hormones are a regulatory substance... ..."
    teacher "... Control metabolism..."
    teacher "... Involved with reproduction..."
    "{i}Huh, what an interesting topic.{/i}"

    "Your next class is Pre-Calculus."
    teacher "Combination is nCr..."
    teacher "... so what is the probability of getting rejected on Valentine's Day? ..."
    teacher "... calculate the factorial..."
    "{i}Ugh, boring.{/i}"

    "..."

    play sound "audio/bell.mp3"

    "{i}Yes! Class is finally over. It's lunch time! Hmm... I wonder what the cafeteria has today."

    # TODO: INSERT CAFETERIA IMAGE

    "Your stomach grumbles as you head to the cafeteria.Your stomach grumbles as you head to the cafeteria."
    unknown "[myName]-san!!! Over here!"
    "You hear a voice beckon you. That's Gaybff-san, Gavin's annoying best friend."
    "{i}It’s not like I’m jealous of him or anything… Baka.{/i}"
    "Gaybff is sitting at a table with Gavin and BFF. He motions for you to take a seat with them."
    "{i}I’ll go sit down with them after I grab some food.{/i}"
    
    menu:

        "Speaking of which, what should I eat today?"

        "Tempura Udon":
            $ mainDish = "Tempura Udon"
            "{i}They have tempura udon today! So delicious!{/i}"
            "{i}Plus, I know Gavin-san likes this stuff. Maybe he’ll share with me, heehee.{/i}"

        "Dino nuggies":
            $ mainDish = "Dino nuggies"
            "{i}I know it’s childrens’ food, but dino nuggies are so good!{/i}"
            "{i}Should I really be stooping to a child’s level on Valentine’s Day?{/i}"
            "{i}What if Gavin-san judges me?{/i}"
            "{i}Oh, screw it. I can’t help myself.{/i}"

        "Bowl of soy sauce":
            $ mainDish = "Bowl of soy sauce"
            "{i}I read in a beauty magazine that soy sauce helps clear your complexion!{/i}"
            "{i}Of course I am going to eat this for lunch. I want to look beautiful for Gavin!{/i}"
            
        "Microwaved salad":
            $ mainDish = "Microwaved salad"
            "{i}I’m so stressed by all this Valentine’s Day drama. I just need to eat my No. 1 comfort food.{/i}"
            "{i}A salad made of romaine lettuce and red onions, topped with ranch dressing and microwaved for 2 minutes! Mmm so good.{/i}"
            "{i}It’s not a traditional option, but Gavin-san will understand. He’s open-minded like that.{/i}"

    menu:

        "{i}But this alone won't be enough for me. What side dish should I get?{/i}"

        "Natto":
            "{i}Some people think this is gross, but I love it!{/i}"

        "Miso soup":
            "{i}A classic, Japanese side dish like this will complement my [main dish] perfectly. {/i}"

        "Lays Potato Chips®":
            "{i}I learned about these the other day at American Culture Club.{/i}"
            "{i}They’re salty, fatty, and delicious!{/i}"
            "{i}But not very healthy… Whatever!{/i}"


        "3 shots of vodka":
            "{i}Heheh, I snuck a flask to school. Hopefully nobody notices that it’s not water!{/i}"
            "{i}I need this liquid courage to ask Gavin out today!{/i}"
    
    "{i}I hope Gavin appreciates my good taste in food!{/i}"

    "Food in hand, you head to the table and take a seat next to BFF-san."
    bff "Hey slowpoke! Come on, let’s eat!"
    g "Hi [myName]-san. What did you get to eat?"
    
    "..."

    if mainDish == "Tempura Udon":
        g "Tempura Udon! I love that stuff!"

        menu:
            g "Can I take a sip? Pleeease?"
            
            "{b}Sure!{/b}":
                "Gavin reaches across the table and takes hold of your bowl of udon."
                "He takes a generous sip of the steaming, decadent broth."
                "{i}His lips are touching my bowl so gently.{/i}"
                "{i}If I drink from there, does it count as a kiss?{/i}"
                "He puts your udon back down in front of you. Is that a small blush you see on his face?"
                g "Thank’s [myName]-chan, that was delicious."

            "{b}No way!{/b}":
                g "Oh, okay then."
                "Gavin looks longingly towards the soup station."
                g "Maybe I should get my own bowl of udon..."

    elif mainDish == "Dino nuggies":
        g "Dino nuggies?! What are you, a child?"
        "..."

        menu:
            g "I'm kidding, please share one with me! I love dino nuggies!"

            "{b}Here you go{/b}":
                "You gave Gavin a few of your Dino nuggies."
                "He ate it with a big smile on his face. (like a kid)"
                "You look at the way he eats and start smiling. He looks like an innocent child that’s trying dino nuggets for the first time. He looks so cute when he’s eating dino nuggets."
                g "Thank’s [myName]-san! It’s been a while since I ate dino nuggies! They are delicious like always. Let me treat you dino nuggies for lunch tomorrow and we will eat it together!"

            "{b}No! I want my precious Dino nuggies.":
                g "Fine. I guess Dino nuggies are being loved by everyone."
                "Gavin pouts slightly and wanted to stand up"
                g "I’ll buy my own Dino nuggies then"

    else:
        g "Oh- That’s... an interesting choice for sure."
        g "... Just a bit unconventional, that’s all."
        "Gavin looks a little bit uncomfortable."
        
        menu:
            g "Wait. Are you actually going to eat that?"
        
            "{b}Yeah.":
                g "Umm, gross..."
                "{i}He thinks my choice in food is gross! Ahhh! This is so embarrassing-{/i}"
            
            "{b}Actually, no. This is just a joke.":
                g "Hahaha good one MC-san."
                g "But since you actually paid for that, don’t you need some actual food to eat?"
                g "Here, take some of my food instead."
                "He grabs a long, uncut maki roll from his plate, holding it towards you."
                g "Here, take a bite of this."
                hide gavin
                "You lean across the table and take it into your mouth. It’s seaweed wrapping feels smooth against your tongue."
                "It goes deeper and deeper, until it is pressed up against the back of your throat."
                "*Chomp*"
                "You bite down and the roll’s flavors burst into your mouth."
                "{i}Sooo delicious!{/i}"
                g "Looks like you liked it. Here, have the rest of my roll."
                "{i}It’s kind of exciting getting fed by Gavin-san like this.{/i}"
                "{i}I hope we can do this more often.{/i}"
                

    "You feel BFF poke you in the leg, trying to get your attention."
    show bff smile at left
    "She leans over to whisper in your ear."
    bff "[myName]-san, I think this is it. I think I’m going to give Gaybff-san chocolates now."
    show bff smile2 with dissolve
    bff "Wish me luck..."
    "Oh and pay attention. You might learn something from me. Heehee…"
    hide bff
    show bff normal
    bff "Ahem. Hey! Gaybff-san pay attention, I have something for you!"


    show gavin bigsmile

    if (totalScore == 1000):

        g "I love you"

        "Gavin grabs you by the hair and kisses you. Happy Ending."

    else:

        g "I'm not interested"

        "Gavin grabs you by the hair and throws you out of his room. Bad Ending"

    # This ends the game.

    return
