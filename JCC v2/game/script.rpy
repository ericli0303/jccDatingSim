# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define g = Character('Gavin', color="#00FF00")  # uwu crush
define m = Character('Me', color="#FFFFFF")  # ME the MC
define bff = Character('Lulu')  # the bestie of Me
define kiomi = Character('Kiomi')  # the bitch
define unknown = Character('???')  # used as placeholder for unknown
define teacher = Character('Teacher')
define mbff = Character('Beefu')
define gavinandmbff = Character('[g] and [mbff]')
# Kawazawa

image gavin bigsmile = "gavin big smile 1.png"
image gavin confused = "gavin confused 1.png"
image gavin stern = "gavin stern 1.png"
image gavin shocked = "gavin shock 1.png"
image gavin excited = "gavin excited 1.png"
image gavin surprised = "gavin surprised 1.png"
image gavin thinking = "gavin thinking 1.png"
image gavin villiansmile = "gavin villian smile 1.png"
image gavin villianstare = "gavin villian stare 1.png"
image gavin satisfied = "gavin satisfied 1.png"
image construction = "construction worker.png"  # construction


default totalScore = 0
default inventory = set()
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
    "Disclaimer: everything in this dating sim is based on [g] in real life. Everything he says or does, all of his preferences, all of it is based on [g]."

    scene bg_room_morning_1
    with fade
    play music "audio/morning.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop

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

        "Half Asian":
            $ totalScore += 50

        "Fox Girl":
            $ totalScore += 10

        "Weeb":
            $ totalScore += 5

        "Not Asian":
            $ totalScore += 0

        "Zombie Kawaii Girl":
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

################################################
##          WAKING UP                         ##
################################################
    play sound "<from 2.4 to 4.6>audio/alarm.mp3" volume 0.7
    "\"BEEP BEEP BEEP BEEP...\" your alarm is going off."
    "You get up but --"
    with vpunch
    m "Ouch!"
    "You hit your head on your shelf"
    "{i}What day is it?{/i}"
    with hpunch
    "{i}What?! It’s Valentine’s Day!?!{/i}"
    "Your heart begins to beat wildly-"
    m "Today’s the day I’ve been waiting for. I am going to confess my love to [g]!"
    m "But I’m so nervous… Will he like me back?"
    m "I have to talk to [bff] and come up with a plan!"

    m "But first thing’s first, I have to put on my best for him."

    menu:
        "What would you like to wear for [g]?"
        "Maid outfit":
            $ totalScore += 5
            $ outfit = "maid"
            m "I hope Gavin fantasizes like this... What am I saying, of course he does!"
            m "Though, this might draw some unwanted attention."

        "Nun outfit":
            $ totalScore -= 10
            $ outfit = "nun"
            m "Something this bold and unique will get his attention for sure."
            m "Though, this might draw some unwanted attention."

        "Scarf and heavy clothing":
            $ totalScore += 7
            $ outfit = "winter"
            m "It’s cold outside, so these will have to do."

        "{b}Nothing{/b} but a fox tail and fox ears":
            $ totalScore += 15
            $ outfit = "fox"
            "You have a sudden craving for wheat…"
            m "Hmmm very soft."
            m "He will love this for sure. Though, this might draw some unwanted attention."

        "School uniform":
            $ totalScore += 3
            $ outfit = "school uniform"
            m "Just because it’s Valentine’s day doesn’t mean I can break the dress code!"

    m "Wait... Hmm..."
    "{i}I-I seemed to have forgotten my name… {w}that bump to the shelf must have really hurt...{/i}"
    "{i}What’s my name again?{/i}"

    python:
        name = renpy.input("What's your name?")
        name = name.strip() or "Shy Guy"

    define myName = Character("[myName]")

    # "{i}{/i}"
    "{i}Right, I'm [myName]. Silly me, how could I have forgotten.{/i}"
    m "Alright. I’m off to school. Ittekimasu!"


################################################
##         WALKING TO SCHOOL                  ##
################################################
    scene bg_suburban_street
    with fade

    play music "audio/walkschool.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop

    "You step out the front door onto your cozy neighborhood street."

    "The weather is beautiful, so you might as well walk to school today. It’s only a 20 minute stroll from here."

    "The sun is still low on the horizon, peeking occasionally out from between the houses as you walk down Chihuahua Court. The sidewalks are busy with kids heading to school, and adults rushing to work."

    "As you are about to turn onto Takoyaki Trail a construction worker halts you."

    show construction
    with dissolve

    "Construction Worker" "Hey kid! You can’t go this way. We’re doing some emergency maintenance for the next few hours."

    "{i}I guess I’ll have to find a way around.{/i}"

    hide construction

    "{i}Let’s see, I could take Shibuya Street, but that’s always so crowded in the morning. {/i}"
    "{i}I could keep going down Chihuahua Court, but it will take me a lot longer to get to school that way. {/i}"
    "{i}On the other hand, Dildo Drive would theoretically get me to school, but I’ve heard that’s not the best part of town...{/i}"

    python:
        if "dildo" in inventory:
            inventory.remove("dildo")

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
    scene bg_urban_street with fade
    "{i}Taking Shibuya Street is probably the best option…{/i}"
    "You backtrack a block or so until you are back on Shibuya Street. The street is full of honking cars in a traffic jam caused by something far away. Salarymen pack the sidewalks pushing in all directions, trying to get to their offices."
    "Eventually you push your way through the biggest crowds and find a smaller road to walk on."
    jump street_over

# Chihuahua Court
label chihuahua:
    scene bg_suburban_street_3 with fade
    "Taking Chihuahua Court is probably the best option…"
    "You keep walking, and walking. Chihuahua Court is scenic for sure."
    scene bg toriigate with fade
    # TODO: ADD MUSIC
    "You walk over a wide wooden bridge which passes over a creek. Nearby you spot a torii gate, which marks the entrance to your local shrine. "
    menu:
        "Do you want to stop by for a quick prayer?"

        "Yes":
            $ totalScore += 5
            "You stop in your tracks, then head through the gate into the shrine’s courtyard."
            # TODO: INSERT OFFERING BOX PIC
            "You stop in front of the offering box."
            "Fumbling a bit, you grab a coin out of your pocket and toss it as your offering to the shrine’s kami."
            "You bow, then clap your hands twice, sending a quick prayer to the kami."
            "{i}Please, please let [g] like me back. And please give me the strength to confess to him!{/i}"
            "With that done, you leave the shrine and continue on the scenic route to school."
            "{i}Shit! I’m already late!{/i}"

        "Nah":
            "{i}I want to ask the kami to bless me and give me the courage to confess to [g], but I am already running late.{/i}"
            "You pass the shrine and continue on the scenic route to school."
    "It takes several minutes, but you finally reach a road that will get you back on track."
    "{i} I’ve wasted so much time going this way.{/i}"
    jump street_over

# Dildo Drive
label dildo:
    scene bg_dildoway
    play music "audio/boss music.mp3" volume 0.5
    "You head down the road a little longer and turn onto Dildo Drive."
    "The road is narrow and winding. Buildings here have exposed pipes rusting in the elements. Brick fences are crumbling, and trash piles up in corners."
    "Occasionally you see people loitering on the sidewalks. Some of them stare at you as you walk by. "
    "{i}Ugh, it smells bad here. It’s like the smell of a dog who just got peed on by a human. Gross!{/i}"
    "As you pass by a dark alleyway, you hear a whistle from it’s depths."
    "A raspy, growling voice" "Hey cute girl, come over here."
    "You feel a poke on your lower back-"
    "Surprised and scared, you start running down the road. The road slopes downwards pretty intensely here."
    if(not isAsian):
        "{b}thump, thump, thump{/b} go footsteps behind you. Faster, faster!"
        "Because of the steep incline, you lose your balance and fall…"
        with hpunch
        with hpunch
        with hpunch
        "\"{b}THUD{/b}\""
        "You tumble down the hill, bouncing off of the ground repeatedly as you fall helplessly."
        "Your body comes to a sudden, painful halt, as you hit a light post and your limp body curls around it."
        "{i}Shit, I can’t ask [g] out like this…{/i} {w} you think as you close your eyes and slowly lose consciousness. "
        "{i}I really got screwed over by them.{/i}"
        jump dildoending
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
    scene bg_suburban_street_4
    play music "audio/soundtrack1.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop
    "{i}Whew, that was a tiring detour. Only 2 blocks to go!{/i}"
    "Rushing along, you are minding your own business until suddenly..."

    play sound "<from 0 to 1.0>audio/bark.mp3" volume 0.7
    if(Chihuahua):
        show shiba chihuahua at right with easeinright
    else:
        show shiba normal at right with easeinright
    "Dog" "WOOF WOOF BARK BARK."
    $ dog = "chihuahua" if Chihuahua else "shiba"
    "A [dog] bounds up to you and tries to jump in your face."

    $ containsDildo = "dildo" in inventory
    menu:
        "UWAH! What do you do?"
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
                jump peechew
            else:
                jump peeshiba

        "Wield the dildo as a blade" if containsDildo:
            "{i}I can protect myself with my dildo.{i}"
            "The dog yanks the dildo from your hand, leaving you defenseless, and runs away."
            "{i}There goes my science experiment...{/i}"
            $ inventory.remove("dildo")
            jump dog_over


label petshiba:
    show shiba pet with dissolve
    "{i}Awww what a cute doggo!{/i}"
    "You stop to ruffle the smol shib behind the ears as it wags its curly tail. You give the good woofer a nice butt rub and he closes his eyes in shiawasei bliss before you let him go from his lovely massage from a stranger and watch him stroll down the street."
    jump dog_over

label petchew:
    "{i}Well I guess you are into terrifying balls of hate that exude the arrogance of a humans in their small disease ridden bodies.{/i}"
    "Like, I don't know why ANYONE would want to pet this small smelly thing, probably gonna get bitten but go for it."
    "You reach down to pet the dog but it growls at you."
    menu:
        "Do you really wanna pet the dog?"
        "Yes":
            "Wow, not even backing down from the aggressive growl."
            "Well, you’re driven today, so you stick your hand in there against its will and probably the owner's, but whatever."
            "You go for the classic head pat but before you get there its growl grows louder and you sense that every cell is in danger."
            menu:
                "Do you continue?"
                "Yes":
                    "Welp, I guess you’re crazy, but playing this game in the first place definitely says something."
                    "You try to press your hand on its peanut sized head, but as expected when your instinct screams in fright it goes in and attacks your kind being and pierces your skin."
                    "Now you’re bleeding and more late for school, but you gain +3 determination."
                "No":
                    "Well, at least you followed your instincts in the end. You back off and head to school."
        "No":
            "Yeah better off not petting it. You ignore the dog and head off to school."

label kickshiba:
    "{i}Ugh, this dog is about to make me more late!!{/i}"
    "You give the dog a nice kick in the butt with the toe of your shoe."
    "The dog whimpers and gives you a sad face as it hangs its head, tail between its legs."
    jump dog_over

label kickchew:
    "You try to kick the dog, but it growls and quickly bites your leg."
    "Your leg starts to bleed a bit, and now you have to limp the rest of the way."
    jump dog_over

label peeshiba:
    "YEAH ASSERT YOUR DOMINANCE!"
    "Show the dog who’s boss. You let a fluid, continuous stream of pee out."
    "Onlookers stare in half surprise and disgust while mothers shield their children's eyes from your distasteful act."
    "Everyone seems too taken aback from your sudden action in Japan where no one strays from the norm, BUT out of the blue you hear a yell."
    "????" "WTF, WHAT ARE YOU DOING TO TOFU-CHAN!!!!! IS THAT PEE!!!"
    "Oh no, the owner is here! But wait, why does your heart go aflutter at this voice."
    "Why is there bittersweet emotion stirring in your heart? You take a glance in the direction of the voice, then want to hide deep down in a hole and escape this unbelievable reality."
    show gavin surprised at left with easeinleft
    g "Huh… wait… it can’t be… Is that you [myName]-san…?"
    m "Ahh.. G. Ga.. [g] ummm I can explain"
    "{i}Everything is falling apart. Why is he here now? This is the worst.{/i}"
    "{i}It was only a small pee that I have been holding in all day.{/i}"
    "{i}I needed to relieve myself and feel top of my game before confessing but AHHHH now I want to dieeee.{/i}"
    "{i}Wait but go back a second, he said \"Tofu-chan,\" not just dog… This couldn’t possibly be his dog, right?{/i}"
    "You give the dog a second look and try to recall from memory images [g] showed you."
    "He described it as an adorable small dog with a curly tail and pointy ears."
    "It was the same breed everyone in this nation owns… which certainly looks like this small, now wet, guy."
    "{i}Oh it’s over, I can’t, I just can’t explain this. What can I say, maybe it was thirsty?{/i}"
    "{i}Yeah right haha, who would believe that. Maybe it’s a hot, sweaty day today so I didn’t want it to overheat?{/i}"
    m "Ummm.. ye… yeah sorry this dog was overheating an.. And I had to cool it off? You know? I’m so sorry I didn’t know it was your dog."
    show gavin stern with dissolve
    g "I just… I just can’t believe this, who pees on a dog to cool it down. I just don’t know what to do."
    g "Tofu-chan come over here. Oh my, you're all wet we need to give you a nice wash right away."
    "After that… well, you haven’t heard from [g] in a while. Whenever you try to apologize he isn’t having it."
    "You feel terrible but after a few months [g] begins to talk to you. A year later you are friendly again but it’s never the same."
    "He also hasn’t let you within a mile of a dog and looks at you in disgust whenever he sees you near a dog."
    "Bad Ending"
    return


label peechew:
    "You let a fluid, continuous stream of pee out. It’s kind of awkward with the cool outfit you put on, but this is really important!"
    "Suddenly a shadow comes up beside you and you look over."
    "WHAT THE F-? Why is [g] here???"
    "Less than 2 seconds later, there is a second stream of pee landing all over the dog in front of you."
    "You and [g] make awkward eye contact."
    jump peechewending

# End of Dog Scene
label dog_over:
    hide shiba
    "As you speed walk the next block, something on the ground suddenly catches your eye."
    "{i}Oh look there’s something shiny and brown on the ground!{/i}"
    menu:
        "Should I pick it up?"

        "Yes":
            "{i}Hmmm I wonder what it is?{/i}"
            "You reach down and attempt to pick up this shiny and brown thing."
            with hpunch
            m "EWWWWWWW!"
            "There is now a big piece of dog poop in your hand and it feels squishy between your fingers."
            python:
                if "poop" in inventory:
                    inventory.remove("poop")
            menu:
                "Should I pocket the poop?"

                "Yes":
                    $ inventory.add("poop")
                    "This might be useful later..."
                    "You pocket the poop and wipe your hand on some nearby grass."
                    m "That should do it."

                "No":
                    "Yuck!"
                    "Dropping the poop like a hot potato, you frantically look around for a tissue to wipe your hands with and accidentally brush your leg."
                    "{i}Ugh, what kind of poopy person doesn’t pick up after their dog?{/i}"
                    "Finally you get the poop off your hand, but you smell a bit funny. Oh well."

        "No":
            "{i}I don’t have time to pick up random things off the ground!! I need to get to school!{/i}"

    "A few paces later, you see another thing on the ground."
    "{i}Oh look there’s another shiny and brown thing on the ground!{/i}"

    python:
        if "money" in inventory:
            inventory.remove("money")

    menu:
        "Should I pick it up?"

        "Yes":
            "You pick it up and find 2000 yen."
            $ inventory.add("money")
            "Wow, look at this free money!! I wonder what I can do with it?"
        "No":
            "I don’t have time to pick up random things off the ground!! I need to get to school!"

    "Finally, you reach the school’s front gates."
    "You have to get to your homeroom, and fast! This would be your third absence this term, and that’s grounds for suspension!"


################################################
##         IN HOMEROOM                        ##
################################################
    # TODO CHANGE TO SCHOOL MUSIC
    scene bg_school_room with fade
    play music "audio/class.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop

    "You arrive in your homeroom, out of breath from running."
    show bff delighted at right with easeinright
    bff "Ohayou [myName]-san! You're late, as usual {i}hehe.{/i}"
    "*She pulls you*"
    show bff smug with dissolve

    menu:
        bff "*whispers* Say, you remember that it's Valentine's day right?"

        "Umm, wait really?":
            bff "Yes, you dummy!"

        "Yeah, I remember.":
            pass

    menu:
        "Sooo... Are you gonna confess to him?"

        "Of course!":

            show bff shocked with dissolve
            bff "Ohh confident, aren't ya? [g]-san is a lucky guy."

        "Confess to who?":
            show bff laugh with dissolve
            bff "Don't be silly, I know you're head over heels for [g]-san"

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

    bff "..."

    show bff shocked with dissolve
    show gavin bigsmile at left with easeinleft
    bff "Look! [g]-san is here!"

    "[g] walks into the classroom. He’s wearing an earthy-toned overcoat over his uniform, and sports a cute maroon scarf."

    show bff smug with dissolve
    bff "He looks so hot today, doesn’t he? Heehee-"
    bff "Quick! Go confess to him dummy! Wait a second… What is happening?"

    hide bff
    # Kiomi ARC
    show nemesis delighted at right with easeinright
    kiomi "[g]-san! Ohayou!"
    kiomi "I made something for you. I hope you like it..."
    "She pulls a box out from behind her back and offers it to [g]-san."

    show gavin surprised with dissolve
    g "... Kiomi-chan... I-I don't know what to say..."

    "{i}That Kiomi-freak! I can’t believe she has the audacity to give chocolates to MY [g]-san! And on Valentine’s Day too!{/i}"
    menu:
        "{i}Should I put an end to this?{/i}"
        "*INTERRUPT*":
            $ totalScore -= 50
            m "HOLD IT RIGHT THERE!"
            "Dashing across the room, you smack the box of chocolates out of her hands. The shiny round chocolates spill out and scatter across the floor."
            show gavin shock with dissolve
            show nemesis angry with dissolve
            kiomi "You... You bitch!"
            show nemesis sad with dissolve
            "*Kiomi starts crying*"
            g "What was that for [myName]-san?"
            # TODO GAVIN CHANGE EXPRESSION
            g "Don't worry Kiomi-san, I'll help you pick these up."
            "[g] and Kiomi drop to the floor and start picking up the chocolates."
            g "See, they’re still fine to eat!"
            "*gulp*"            
            show gavin excited with dissolve
            g "Wow these are delicious! This was super sweet of you, Kiomi-chan!"
            show nemesis smile with dissolve
            kiomi "*sniff* You really mean it?"
            "[g] turns to face you"
            show gavin stern with dissolve
            g "I can't believe you would do something like that, [myName]-san. I thought you were nicer than this."
            "Kiomi lightly grabs [g]'s arm to get his attention"

        "*Just watch*":
            "[g] opens the box"
            show gavin excited with dissolve
            g "Wow! These chocolates look amazing!"
            "*gulp*"
            g "And they taste amazing too! This was super sweet of you, Kiomi-chan!"
            kiomi "Yay! I'm glad you like them!"
            kiomi "..."

    show nemesis smile2 with dissolve
    kiomi "[g]-san..."
    kiomi "I have something I want to tell you-"


    play sound "audio/bell.mp3"
    "*RINNGGGG*"
    show nemesis sad with dissolve
    show gavin shock with dissolve
    "Just before Kiomi is about to finish saying something, the school bell goes off. It is time for your first class."
    g "Ah, it's time for class. See you guys later. Thanks again for the chocolates, Kiomi-chan!"
    "[g] runs off to his first class"
    hide gavin
    show nemesis smug with dissolve
    "Kiomi-san glares at yoo... Then grins."
    kiomi "He's mine, loser."
    show bff angry at left with easeinleft
    bff "Shut up. We all know [g]-san likes [myName]-san, so you're out of luck."
    bff "Tonight when [myName] confesses to him, you’ll see how hopeless your situation is!"
    bff "Come on, [myName]. Let’s go to class."

    scene bg_classroom1 with fade


################################################
##         CLASSES 1                          ##
################################################
    play music "audio/class.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop

    "Your first class of the day is Biology."
    teacher "Hormones are a regulatory substance... ..."
    teacher "... Control metabolism..."
    teacher "... Involved with reproduction..."
    "{i}Huh, what an interesting topic.{/i}"

    "Your next class is Pre-Calculus."
    teacher "Combination is nCr..."
    teacher "... so what is the probability of getting rejected on Valentine's Day? ..."
    teacher "... when [g] folds his pants in thirds ..."
    "{i}Ugh, boring.{/i}"


    "..."

    play sound "audio/bell.mp3"

    "{i}Yes! Class is finally over. It's lunch time! Hmm... I wonder what the cafeteria has today."

################################################
##        LUNCH                               ##
################################################
    scene bg cafeteria with fade
    play music "audio/lunch.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop

    "Your stomach grumbles as you head to the cafeteria."
    unknown "[myName]-san!!! Over here!"
    "You hear a voice calling you. That's [mbff]-san, [g]'s best friend."
    "{i}It’s not like I’m jealous of him or anything… Baka.{/i}"
    "[mbff] is sitting at a table with [g] and [bff]. He motions for you to take a seat with them."
    "{i}I’ll go sit down with them after I grab some food.{/i}"

    menu:

        "Speaking of which, what should I eat today?"

        "Tempura Udon":
            $ mainDish = "Tempura Udon"
            "{i}They have tempura udon today! So delicious!{/i}"
            "{i}Plus, I know [g]-san likes this stuff. Maybe he’ll share with me, heehee.{/i}"

        "Dino nuggies":
            $ mainDish = "Dino nuggies"
            "{i}I know it’s childrens’ food, but dino nuggies are so good!{/i}"
            "{i}Should I really be stooping to a child’s level on Valentine’s Day?{/i}"
            "{i}What if [g]-san judges me?{/i}"
            "{i}Oh, screw it. I can’t help myself.{/i}"

        "Bowl of soy sauce":
            $ mainDish = "Bowl of soy sauce"
            "{i}I read in a beauty magazine that soy sauce helps clear your complexion!{/i}"
            "{i}Of course I am going to eat this for lunch. I want to look beautiful for [g]!{/i}"

        "Microwaved salad":
            $ mainDish = "Microwaved salad"
            "{i}I’m so stressed by all this Valentine’s Day drama. I just need to eat my No. 1 comfort food.{/i}"
            "{i}A salad made of romaine lettuce and red onions, topped with ranch dressing and microwaved for 2 minutes! Mmm, so good.{/i}"
            "{i}It’s not a traditional option, but [g]-san will understand. He’s open-minded like that.{/i}"

    menu:

        "{i}But this alone won't be enough for me. What side dish should I get?{/i}"

        "Natto":
            "{i}Some people think this is gross, but I love it!{/i}"

        "Miso soup":
            "{i}A classic, Japanese side dish like this will complement my [mainDish] perfectly. {/i}"

        "Lays Potato Chips®":
            "{i}I learned about these the other day at American Culture Club.{/i}"
            "{i}They’re salty, fatty, and delicious!{/i}"
            "{i}But not very healthy… Whatever!{/i}"

        "3 shots of vodka":
            "{i}Heheh, I snuck a flask to school. Hopefully nobody notices that it’s not water!{/i}"
            "{i}I need this liquid courage to ask [g] out today!{/i}"

    "{i}I hope [g] appreciates my good taste in food!{/i}"

    "Food in hand, you head to the table and take a seat next to Lulu-san."
    show bff delighted at left with easeinleft
    bff "Hey slowpoke! Come on, let’s eat!"
    show gavin bigsmile at right with easeinright
    g "Hi [myName]-san. What did you get to eat?"

    g "..."

    if mainDish == "Tempura Udon":
        show gavin excited with dissolve
        g "Tempura Udon! I love that stuff!"

        menu:
            g "Can I take a sip? Pleeease?"

            "{b}Sure!{/b}":
                $ totalScore += 15
                "[g] reaches across the table and takes hold of your bowl of udon."
                "He takes a generous sip of the steaming, decadent broth."
                "{i}His lips are touching my bowl so gently.{/i}"
                "{i}If I drink from there, does it count as a kiss?{/i}"
                "He puts your udon back down in front of you. Is that a small blush you see on his face?"
                g "Thank’s [myName]-chan, that was delicious."

            "{b}No way!{/b}":
                show gavin thinking with dissolve
                g "Oh, okay then."
                "[g] looks longingly towards the soup station."
                g "Maybe I should get my own bowl of udon..."

    elif mainDish == "Dino nuggies":
        show gavin confused with dissolve
        g "Dino nuggies?! What are you, a child?"
        "..."

        menu:
            g "I'm kidding, please share one with me! I love dino nuggies!"

            "{b}Here you go{/b}":
                $ totalScore += 12
                show gavin excited with dissolve
                "You give [g] a few of your dino nuggies."
                "He eats them with a big smile on his face. (like a kid)"
                "You look at the way he eats and start smiling. He looks like an innocent child that’s trying dino nuggies for the first time. He looks so cute when he’s eating dino nuggies."
                g "Thanks [myName]-san! It’s been a while since I ate dino nuggies! They are delicious like always. Let me treat you dino nuggies for lunch tomorrow, and we'll eat them together!"

            "{b}No! I want my precious dino nuggies.":
                show gavin stern with dissolve
                g "Fine. I guess everyone loves dino nuggies."
                "[g] pouts slightly and stands up"
                g "I’ll buy my own dino nuggies then."

    else:
        show gavin thinking with dissolve
        g "Oh- That’s... an interesting choice for sure."
        g "... Just a bit unconventional, that’s all."
        "[g] looks a little bit uncomfortable."

        menu:
            g "Wait. Are you actually going to eat that?"

            "{b}Yeah":
                show gavin stern with dissolve
                g "Umm, gross..."
                "{i}He thinks my choice in food is gross! Ahhh! This is so embarrassing-{/i}"

            "{b}Actually, no. This is just a joke.":
                show gavin bigsmile with dissolve
                $ totalScore += 20
                g "Hahaha good one [myName]-san."
                g "But since you actually paid for that, don’t you need some actual food to eat?"
                g "Here, take some of my food instead."
                "He grabs a long, uncut maki roll from his plate, holding it towards you."
                g "Here, take a bite of this."
                hide gavin
                hide bff
                show maki at top with dissolve
                "You lean across the table and take it into your mouth. It’s seaweed wrapping feels smooth against your tongue."
                "It goes deeper and deeper, until it's pressed up against the back of your throat."
                "*Chomp*"
                "You bite down and the roll’s flavors burst into your mouth."
                "{i}Sooo delicious!{/i}"
                hide maki
                show gavin bigsmile at right with easeinright
                g "Looks like you liked it. Here, have the rest of my roll."
                "{i}It’s kind of exciting getting fed by [g]-san like this.{/i}"
                "{i}I hope we can do this more often.{/i}"

    "You feel [bff] poke you in the leg, trying to get your attention."
    "She leans over to whisper in your ear."
    show bff smile2 at left with dissolve
    bff "[myName]-san, I think this is it. I think I’m going to give [mbff]-san chocolates now."
    bff "Wish me luck..."
    show bff sad with dissolve
    bff "I hope I don’t mess it up like what I usually d..."
    hide gavin
    show bff angry with dissolve
    bff "Ahem. Hey! [mbff]-san pay attention, I have something for you!"
    show male bff concerned at right with easeinright
    "{i}She takes out a heart-shaped box from her bag and put it on the table.{/i}"
    show male bff surprised with dissolve
    mbff "Oh?!"
    mbff "Oh wow, I didn’t know you’d actually go all the way to make me this-"
    show bff annoyed with dissolve
    bff "Don't get the wrong idea... I just ended up making too many of them!"
    m "{i}Oh no... She’s doing it again...{/i}"
    show male bff concerned with dissolve
    mbff "Oh… Yes, right, of course."
    "[mbff] leaves a heavy sigh."
    mbff "..."
    mbff "You know, I have been wanting to tell you this, but you don’t have to be so defensive in front of me."
    show bff angry with dissolve
    bff "What do you mean?! I’m not-"
    mbff "But-"
    show male bff hold glasses
    mbff "I’m glad that you are giving it to me though, whatever reason it might be."
    "[bff] blushes a little."
    show bff annoyed
    bff "Um... well I told you I-I just made too many of them..."
    mbff "Yeah?"
    "He chuckles a little."
    show male bff neutral
    mbff "Well, you know, sometimes I also like that part about yo-"

    play sound "audio/bell.mp3"
    "*RINNGGGG*"

    g "Ah, it looks like lunch period is just about over."
    g "See you all at club after classes!"
    mbff "Yeah, see y’all later."
    hide male bff
    "As [mbff] turns around and leaves, you see him looking down at the box of chocolates from [bff]."
    "He smiles gently."
    "You look over to [bff], and she keep mumbling to herself."
    show bff shocked
    bff "Oh god, I can't believe I did that again, whyyyyy am I such a baka, why do I act like this!"
    show bff sad
    bff "Oh no... why am I like this @#@#$@##%%$"
    m "..."
    hide bff
    "{i}She was too drowned by her own thoughts, I doubt she heard what he was trying to say...{/i}"
    "{i}Anyways, it’s up to them to figure it out! And it’s time to go to class again.{/i}"
    "{i}Hopefully it’ll be more interesting than the classes this morning...{/i}"

    "Right as you are about to leave the cafeteria, you remember about the Valentine’s Day pop-up shop that supposedly sells chocolates."
    "You walk by the shop to assess your options."
    "{i}Dang, these are expensive!{/i}"
    "{i}But they sell dark chocolates with raspberry filling! Those are [g]-san’s favorites!{/i}"

    python:
        if "chocolates" in inventory:
            inventory.remove("chocolates")
            inventory.add("money")

    menu:

        "Should I get something for Gavin?"

        "Nevermind, I don't have enough money" if "money" not in inventory:
            "{i}This really sucks! If only I had miraculously found some money on the street earlier today.{/i}"
            "{i}Oh well… I’ll do my best to confess to him without chocolates.{/i}"

        "Not buying" if "money" in inventory:
            "{i}Oh well… It's not worth the price. I’ll have to do my best to confess to him without the chocolates.{/i}"

        "Buying" if "money" in inventory:
            "{i}Good thing I found some cash on the street earlier today, otherwise I wouldn’t be able to afford these.{/i}"
            "{i}Now I can do a real Valentine’s Day confession! Chocolates and all!{/i}"
            $ inventory.remove("money")
            $ inventory.add("chocolates")

################################################
##         ClASSES 2                          ##
################################################
    scene bg_school_room with fade
    play music "audio/class.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop

    "You head to English class."
    " “... Peter piper picked ...” "
    m "... Peter pip-er pecked a pick … Whoops!"
    "{i}My tongue got super twisted!{/i}"

    "The last class of the day is World History! Almost done!"
    teacher "... it was the bloodiest war in the history of mankind..."
    teacher "...and that’s why [g]'s favorite food is sush..."

    "{i}I’m falling asleep...{/i}"

    teacher "Now class, I’m pleased to announce that we have a pop quiz today!"

    "{i}Oh no! I was half-asleep! What’s this quiz about?{/i}"

    teacher "[myName]-san, it’s your turn first. Please answer these questions and then you are free to leave."

    "{i}Oh no, I’m doomed.{/i}"

    teacher "Question one: what is [g]-san’s GPA?"

    "{i}Wait… What the hell is this question?{/i}"

    "You look around but everyone is looking at you awaiting an answer."

    "{i}Is no one questioning why we’re asking questions about [g]? Ugh whatever...{/i}"

    menu:
        "{i}What should I answer?{/i}"
        "3.7":
            teacher "The answer is 3.9."

            "{i}Shit! I totally knew that!{/i}"

            "[g] looks at you disappointedly."

            $ totalScore -= 5

        "3.9":
            teacher "Correct, the answer was 3.9."

            "{i}Yes! I’m as smart as him! Haha!{/i}"

            "[g] nods approvingly."

            $ totalScore += 5

        "4.0":
            teacher "The answer is 3.9."

            "{i}What is this guy talking about? [g]-san is way too smart to only have a 3.9!{/i}"

            "[g] looks at you disappointedly."

            $ totalScore -= 3

    teacher "Question 2. What was [g]-san wearing this morning?"

    "{i}Again? Why are they asking me about [g]-san? This will be too easy.{/i}"

    menu:
        "{i}What should I answer?{/i}"

        "A red overcoat":
            teacher "Incorrect, the answer is a maroon scarf."

            "{i}Shit! I literally sniffed his coat this morning. How could I forget that it wasn’t red!?{/i}"

            "[g] shakes his head."

            $ totalScore -= 5

        "A Red Sox cap":
            teacher "Incorrect, the answer is a maroon scarf."

            "{i}Damn it! He’s an esports fan, not a baseball fan!{/i}"

            "[g] shakes his head."

            $ totalScore -= 5

        "A maroon scarf":
            "Correct, [g] sure likes his scarfs."

            "{i}That was so obvious.{/i}"

            "[g] smiles at you."

            $ totalScore += 5

    teacher "Question 3. How does [g]-san fold his pants?"

    "{i}Shoot, I think I remember something about this in my pre-calculus class…{/i}"

    menu:
        "{i}What should I answer?{/i}"

        "In half":
            teacher "Incorrect, the answer is in thirds."

            "{i}Who the hell folds their pants in thirds?{/i}"

            "[g] facepalms."

            $ totalScore -= 5

        "In thirds":
            teacher "Correct, [g] is the only one weird enough that does this."

            "{i}Whew, that was a lucky guess{/i}"

            "[g] bites his lips."

            $ totalScore += 5

        "In fourths":
            teacher "Incorrect, the answer is in thirds."

            "{i}Who the hell folds their pants in thirds?{/i}"

            "[g] facepalms."

            $ totalScore -= 5

    "{i}That was a weird quiz. I wonder what that was all about...{/i}"

################################################
##        AMERICAN CULTURE CLUB               ##
################################################
    scene bg_classroom1 with fade
    play music "audio/soundtrack2.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop

    "{i}Phew, classes are over now, and American Culture Club starts in 5 minutes.{w} [g]-san should be there, so that’s when I’ll confess to him. {/i}"

    "You arrive at Eru Hall, room 408, where American Culture Club is being held."
    "[bff] and [mbff] are chatting in one corner. You see [bff] laugh and playfully push [mbff] away from her."
    "{i}Looks like they’re getting along quite well.{/i}"
    "{i}Guess that box of chocolates really sends a message across.{/i}"
    "At the front of the classroom, [g]-san and the eboard are leading a discussion about America’s Super Bowl sports event."

    show gavin thinking at left with easeinleft
    g "... Running an advertisement at the Super Bowl can cost thousands of dollars per second! No wonder Americans can only afford McDonalds..."
    g "... And the Americans throw parties to watch the advertisements. Isn’t that insane? Why do they like watching advertisements so much?…"
    "The discussion is fun and heated."
    "{i}Americans have such an interesting culture. Ahh, someday I want to visit there.{/i}"

    show bff smile at right with easeinright
    hide gavin with dissolve
    "At the end of the discussion, [bff]-san comes over and pokes you to get your attention."
    "*poke poke*"
    bff "Hey [myName]-san. [mbff] and I are going to karaoke after this. It'll be too awkward if it's just the two of us though, so you’re coming too!"
    "..."
    bff "Sooo…"
    bff "This is your last chance to make a move on [g]-san."

    menu:
        bff "Are you going to invite him or not?"

        "Yes":
            bff "YES FINALLY. I mean-"
            bff "It’s no big deal! Just go invite him, dummy!"

            hide bff with dissolve
            "You finally build up the courage to ask [g] out to karaoke. If you don’t act now, you'll miss your chance to grow closer!"

            show gavin bigsmile with dissolve
            m "[g]-san, are you free after school today?"

            g "Yeah, I’m free. What’s the matter?"

            m "Ano… actually me, [bff] and [mbff] are going to karaoke. I was wondering if you would want to join us?"

            show gavin excited with dissolve
            g "Karaoke? Ooh, that sounds fun! Sure, I’ll join."

            m " I will send you the address! See you there!"

            jump karaoke

        "No":
            jump karaokenotinvite

# didn't invite ending
label karaokenotinvite:
    show bff shocked with dissolve
    bff "Really?!"
    bff "After all this, you couldn't bring yourself to even ask him to come with us?"
    show bff sad with dissolve
    bff "I tried my hardest to motivate you today..."
    bff "Oh well..."
    show bff annoyed with dissolve
    bff "Fine! But I don’t want a third wheel tonight."
    bff "I’m going to karaoke alone with [mbff]-san."
    bff "Him… and me…"
    bff "Alone…"
    show bff shocked with dissolve
    bff "...a Valentine's date!"
    show bff smug with dissolve
    bff "I’m gonna go now."
    bff "Ahem. [mbff]-kun!!! Get over here! Let’s get going!"
    show male bff surprised at right with easeinleft
    mbff "!!!!"
    hide male bff with dissolve
    hide bff with dissolve
    "{i}I'm kind of jealous of them.{/i}"
    "{i}I wish I had the courage to ask out [g]-san...{/i}"
    "{i}I should at least ask him to walk home with me.{/i}"
    "{i}After all, we’re going the same direction.{/i}"
    "{i}It’s my last chance…{/i}"
    "{i}I can’t screw this up.{/i}"
    show gavin satisfied at left with easeinleft
    "..."
    g "You wanna walk home together? Sure!"
    g "We can walk together to Chihuahua Court, but then I have to go my separate way."
    "{i}Alright! This is better than nothing.{/i}"
    jump walk

################################################
##         KARAOKE                            ##
################################################

label karaoke:

    scene bg_kareoke with fade
    play music "<from 21>audio/karaoke.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop

    show gavin excited at right with easeinright

    menu:
        g "What song should we sing, [myName]-chan? You pick!"

        "Grand Blue":
            $ totalScore += 15
            g "YOOO THAT’S A STRAIGHT BANGER!!! ATSUKUNARE MY FRIENNNNDSS!"

            play music "<from 21>audio/grandblue.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop
            "*Play Grand Blue*"

            "{i}I’m... I’m so nervous.. I hope [g] won’t judge me for my voice.. It’s my first time singing and I feel so nervous >.<{/i}"
            "{i}Especially… In front of someone I like.{/i}"
            "You try to calm yourself down…"
            "Just as you sing the first two words of the song, [g] moves beside you and joins you singing."
            "You feel your heart rate increase, and your cheeks heat up."
            "{i}Oh no.. he's right beside me.. W-we are so close,, I think my face is going to overheat from being so embarrassed.{/i}"
            "{i}He’s different when he sings. His voice is in the mid-range, soft and nasally.{/i}"
            "{i}He’s so perfect and…{/i}"
            "{i}I think... I-I am falling deeper i-in love.{/i}"
            "As you are lost in thought, he turns to you and gives you a bright smile."

            g "Hey, what are you doing [myName]-chan? Let's sing together!"

            "Doki doki, you felt your heart skipping a beat.."
            "{i}Did [g] just ask t-to sing together?! Is... Is this a duet?!{/i}"
            "[g] nudges you and you started singing with him… Drifting away in a world with only you two."
            "You have no idea how much time has passed since you started singing with [g]."
            "You feel less embarrassed and nervous when you sing with [g]."
            "You only know that both of you had a lot of fun, and you wish that time would stop..."

            g "Wow [myName].. your taste in music is incredible. Some of the songs were similar to mine. I had a fun time singing with you."
            g "We should go to concerts and karaoke together more often."

            m "Ehhh? Eto.. O-Okay! I’m done with my song!"

        "Snow Halation":
            $ totalScore += 10
            g "YOOO [mbff] the classsssic! Dude, you should sing this!"

            play music "<from 64>audio/snow.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop
            "*Play Snow Halation*"

            show male bff hold glasses at left with easeinleft
            "{i}Oh shit I forgot [mbff]-san was really into love live. Now he is singing it.{/i}"
            "{i}At least [g] didn’t judge me for this choice, but we didn’t get to sing together :({/i}"
            "You try to follow the lyrics, but you forgot how embarrassing this song gets."
            "{i}But hot damn, [mbff] is belting it! The man isn't holding back at all.{/i}"
            "You wonder what [bff] thinks about this."
            hide male
            show bff annoyed at left with easeinleft
            "You take a glance over, and her eyes are throwing daggers at you. She is jealous that you are singing alongside [mbff]"
            "{i}UGH how could a simple song choice turn out so subpar.{/i}"
            "Well, you get some songs in and overall you are glad you came."
            "Although, after setting the mood, idol music continued for a while, and you never got the chance to sing with [g]."

        "All Star":
            $ totalScore -= 5
            g "ALL STAR!"
            g "I didn't expect that choice from you. Normally, that's a late game song to end the night, but if you want, let's go."

            play music "<from 36>audio/allstar.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop
            "*Play All Star*"

            show male bff excited at right with easeinright
            gavinandmbff "SOOOOOOOOOOOMMMM..."

            "{i}Huh, wait what are they doing, why are they yellin...{/i}"

            gavinandmbff "MMMMMMMMMMEBOOODY ONCE TOLD ME THE WORLD WAS GONNA ROLL ME, I AIN’T THE SHARPEST TOOL IN THE SHED"

            "{i}Wow it seems [g] and [mbff] go back with this song. They are completely lost and now just singing together.{/i}"
            "You and [bff] lightly sing in the background, but [g] and [mbff] are having too much fun and are too loud to hear your voices."
            "The night continues with a lot of group songs and energetic music and you enjoy it, but you wish you could have sung together with [g]."

        "Dick in a box":
            g "Huh, what’s this song? Haha, it sounds highly inappropriate, but it says it's a Christmas song."
            g "You wanted to sing it, right [myName]-chan, so shikataganai ne."

            play music "<from 17>audio/dick.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop
            "*Play Dick in a Box*"

            g "Alright, starting off kinda slow here, but I like these jazzy vibes."
            g "You know it’s Christmas, hmmm hm"

            "{i}Whhhat is this song, I thought the funny pick might get a good joke, but they actually are singing it.{/i}"
            "{i}Well… guess there's no choice now, we are committing{/i}"

            gavinandmbff "IT'S MY DICK IN BOX!!!!"

            "Well your friendship has taken a step… in some direction."
            "You now bond with [g] on a new level but it's different. He now looks at you the same way as [mbff]."

            jump dickboxending


################################################
##         HEADING HOME/PRE-ENDING            ##
################################################

    play music "audio/walkhome.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop
    scene bg_kareoke with fade

    "You hear a knock at the door to your karaoke room."

    unknown "Excuse me, but your time is up! Please wrap up and head to the front desk, thank you very much."

    "{i}Dang, has it already been two hours?{/i}"

    "You and Gavin have been singing your hearts out for hours."
    "In the corner of the room, [bff] is passed out on [mbff]’s lap."

    show male bff hold glasses at right with easeinright
    mbff "Wake up, sleepyhead. We’re getting kicked out."

    show bff sleepy at left with easeinleft
    bff "Hnnng sooo sleepyyy..."
    bff "*AAAAAIIIIIIEEEE*"

    show bff angry with dissolve
    bff "Why didn’t you wake me up, stupid! I was on your lap! That’s so embarrassing!!!"
    bff "That was-"
    bff "Kind of…"
    bff "Nice."
    show bff delighted with dissolve
    bff "Hrmph."

    "{i}Why does flirting come so easy to Lulu? It’s not fair.{/i}"

    show gavin bigsmile with dissolve
    g "Get up, you lovebirds. It’s time to head home."
    "[bff], getting up from her position on [mbff]'s lap, sidles up to you and whispers into your ear."

    show bff laugh with dissolve
    bff "You didn’t get up to anything funny with Gavin-chan while I was asleep, did you? Heehee-"

    show bff normal with dissolve

    menu:
        bff "So, are you going to ask him to walk home with you?"

        "Yes":
            hide bff
            hide male bff
            show gavin bigsmile at right with easeinleft
            "{i}This is it. I’m going to confess to him while we walk together.{/i}"
            "{i}It’s my final chance...{/i}"
            "{i}I can’t screw this up.{/i}"

            g "..."
            show gavin excited with dissolve
            g "You want to walk home together? Sure!"
            g "We can walk together to Chihuahua Court, but then we have to go our separate ways."

            "{i}Alright! I can do this!{/i}"

            jump walk

        "No":
            "{i}If I walk him home, I’ll have to confess to him...{/i}"
            "{i}But I just can’t gather enough courage to confess!{/i}"
            "{i}He’s so dreamy, but that will make it hurt more if he rejects me.{/i}"
            "{i}I can’t do it!{/i}"

            bff "Alright, suit yourself."
            "She gives you a disapproving look, but takes your arm and starts dragging you out."

            "{i}I think we’re better off if he never finds out how I feel...{/i}"
            "{i}Even if he smells really good.{/i}"

            jump chickened_ending


################################################
##         ENDINGS                  ##
################################################

label walk:
    scene bg_possible_farewell with fade
    show gavin satisfied with easeinright
    "You and Gavin decide to walk back home together, when you realize your pockets feel awfully heavy..."
    if not inventory:
        "hm... there's nothing in my pockets... I must be going crazy..."
    else:
        "Hmmm... I should give Gavin a gift!"
        menu:
            "What should I give him?"

            "Chocolates" if "chocolates" in inventory:
                "You pull out the box of chocolates that you bought earlier."
                show gavin excited with dissolve
                g "What's this? Are these… Valentine’s Day chocolates?"
                "Gavin opens the box."
                show gavin thinking with dissolve
                g "*Sniff, sniff*"
                show gavin excited with dissolve
                g "These are raspberry chocolates! How did you know to get these? Raspberry flavor is my favorite!"
                g "*Chomp*"
                g "Wow, they're so delicious!"
                g "In fact, they’re better than the ones that Kiomi-chan gave me earlier today."
                m "..."
                show gavin bigsmile with dissolve
                g "Oh, don’t worry about her. She told me how she felt earlier today, but I don’t feel the same way."
                g "Not that I think you’d be worried about her..."
                show gavin thinking with dissolve
                "He seems to be deep in thought for a moment."
                g "Anyways, this was really nice of you, [myName]-chan."
                show gavin bigsmile with dissolve
                g "Thank you."

                $ totalScore += 40

            "Money" if "money" in inventory:
                "You pull out the wad of money that you found earlier in the day."
                show gavin excited with dissolve
                g "A gift? For me?"
                g "Thanks [myName]-san!"
                show gavin confused with dissolve
                g "I’m not sure why you’re giving me this though. Do I owe you something?"
                "..."
                g "Oh, it’s really just a heartfelt gift? That’s nice, I guess."
                show gavin satisfied with dissolve
                g "Well, anyways…"
                $ totalScore += 10

            "Poop" if "poop" in inventory:
                "You pull out the mushy poop from your pocket."
                show gavin excited with dissolve
                g "A gift? For me?"
                g "Wait a second…"
                show gavin shocked with dissolve
                g "Why are you carrying poop? That’s what that smell was? That’s really gross, [myName]-chan."
                "Gavin gives you a disgusted and disgruntled look."
                show gavin stern with dissolve
                g "Thanks, I guess… But honestly, no thanks."
                "Gavin gestures for you to drop it on the curb."
                g "Please don’t do that again…"
                $ totalScore -= 5

            "Dildo" if "dildo" in inventory:
                "You pull the floppy yellow dildo out from your pack. It’s still crusty."
                show gavin confused with dissolve
                g "OHHH, [myName]-chan. What the hell is that?"
                "..."
                g "That’s… a gift? For me?"
                g "Umm, that’s really disgusting. Why would you give that to me?"
                "..."
                g "I guess I’ll take it… For science reasons…"
                g "But just so you know, that was totally uncalled for. You probably shouldn’t give gifts like that."
                $ totalScore += 5

        jump calculateending


label calculateending:
    show gavin satisfied with dissolve
    if totalScore >= 100:
        jump veryniceending
    elif totalScore >= 20:
        jump niceending
    else:
        jump verybadending


label dickboxending:
    show gavin villiansmile with dissolve
    "You have become one of [g]'s bros, and a romantic relationship is no longer possible. You can’t exactly feel happy about the outcome, but you did sing Dick in a Box alongside [g]. At least you are still close friends…"
    "Dick in a Box Ending"
    return


label dildoending:
    scene bg_youdied with fade
    stop music
    play sound "audio/game over.mp3" volume 0.5
    "While you were unconscious, no one passed by the sketchy Dildo Drive you decided to take. As you hopelessly waited for help, you die due to blood loss."
    return

label peechewending:
    "Weird Ending"
    return

label chickened_ending:
    scene bg chicken with fade
    play sound "<from 0.5 to 2.5>audio/chicken.mp3" volume 0.5
    "How could you do this? Our protagonist. The main character of the story. Chickened out. We believed in you. Pitiful."
    "Chicken Ending"
    return

label niceending:
    play music "audio/niceending.mp3" fadein 1.0 fadeout 1.3 volume 0.3 loop
    scene bg nightstreet with fade
    "You and Gavin decide to walk back home together. You fidget with your hair wondering when you should confess to Gavin."
    "You take deep breaths, trying to calm down, as you feel that your heart is going to explode."
    "You keep on wondering how you should confess to Gavin-san, not realizing that you have already arrived at the intersection where you and Gavin are going to head in different directions."
    "You stop and turn to face Gavin."
    m "Ga-Gacchan I-I have something to tell you."
    "You look away, trying to hide your blush."
    show gavin confused
    g "What is it [myName]-chan?"
    m "I-I don’t know when-when this started. B- But whenever I see you my heart goes doki doki b-because... I like you. I-I know this wasn’t what you e-expected but, I just want to say… I love you!"
    "You turn away from Gavin, waiting for his response."
    show gavin surprised with dissolve
    "Gavin doesn’t speak for a while."
    show gavin stern with dissolve
    g "Eto... I'm very happy that you like me, and it’s okay, you don’t have to worry."
    g "Love always comes unexpected. Um... but I have always thought of you as my best friend, wait, actually best friend like siblings."
    g "And I am very glad that you like me, but I’m sorry."
    g "Right now I think we are so close to each other, that I don’t want to make things awkward later."
    g "But I think we should remain like best friends."
    g "Maybe someday my feelings will change, if you still have feelings for me at that time. So don’t be sad."
    "GAME OVER - You got friendzoned"

    return

label veryniceending:
    play music "audio/niceending.mp3" fadein 1.0 fadeout 1.3 volume 0.3 loop
    scene bg nightstreet with fade
    "You are walking home with Gavin after school. You try to act normal, hiding your blush. You feel like your heart is going to explode, and all you hear is your heart going doki doki."
    "Suddenly, you are filled with resolve. {i}You can do it!{/i}"
    "You turn to face Gavin."
    show gavin stern with dissolve
    m "Ga- Gacchan. I- I"
    "Just as you are about to tell Gavin your true feelings, a motorcycle rushes by too close for comfort. Surprised, you lose your balance."
    "*Crash*"
    "You fall onto your back. Wait, but something cushioned your head from hitting the solid pavement."
    scene otome with fade
    "When you open your eyes, you see that Gavin fell right above you. His hand is placed in between your head and the sidewalk. He must have jumped down to protect you."
    "His face is very close to yours. It’s like time has stopped. Gavin pulls you up, his face flushed."

    g "Are you ok? So-Sorry, I hope you don’t get mad. By the way, what did you want to say earlier?"
    m "Ga-Gacchan, I- I like you. I- I have had feelings for you for a long time. I- I know this is sudden so you don’t have to answer me right now."
    g "[myName] chan, a-actually I- I was so scared just now when you fell. I-I was afraid that you got hurt, b-because I like you too!"
    m "Ehhhh?! R-Really Gacchan?"
    "You feel your face heating up with… Joy? Embarrassment? You haven’t quite felt like this before."
    "Gavin suddenly props up his arm next to you, locking you in a kabedon."
    g "Y-Yeah. I’ve  liked you since the day we met. I- I want to protect you. I don’t want you to think of me as a best friend. I-I want to be your boyfriend. P-please go out with me!"
    "Your eyes meet his in a tender gaze. He leans forward, bringing his lips closer, and closer..."
    "You meet him in the middle. Your lips intertwine with his in a brief, but sweet kiss."
    scene bg beach
    "After that day, you and Gavin have been walk to and from school everyday holding hands."
    "Gavin often shows his love to you in front of your classmates, making you blush, and both of you hang out almost every day after school to go on dates."
    "Your friends describe you guys as a \“sweet couple.\" Your friends envy that you have such a sweet boyfriend who is always by your side, protecting you at all costs. "
    "Best Ending"
    return


label verybadending:
    play music "audio/badending.mp3" fadein 1.0 fadeout 1.0 volume 0.3 loop
    scene bg rain
    "You and Gavin start to walk back home. You decided that this is a good time to confess to [g]."

    m "Gachan, I have something to tell you."

    show gavin confused with dissolve
    g "What’s the matter? [myName]-chan"

    m "Actually, I-I started having feelings for you. I know that this is s-so sudden, but I just want to say that I like you."

    "You look at the ground as you feel your face heat up."
    "Gavin stares at you, with a awkward smile."

    show gavin bigsmile with dissolve
    g "Errrrm, [myName]-chan, was this a prank that someone put you up to? They dared you to say this, right?"

    "You shake your head."

    m "I... I really mean it. I mean it from the bottom of my heart! I- I know this is very sudden but, but I hope that you un-understand my feelings, I-I really really meant it."

    "Gavin’s face turns incredulous for a moment, only being able to be described as *NANI?!?*"
    show gavin villianstare with dissolve
    g "[myName]-chan. Thank you for telling me your feelings towards me."
    g "I’m sorry."
    g "I don’t think we are suitable for each other. You view things... differently than I do."
    g "You have been good to me most of the time. I’m sorry, I don’t think I can be your boyfriend... and-"

    "You try to get a glimpse of Gavin’s expression as he turns to walk away."

    show gavin stern with dissolve
    g "More importantly, I like someone else…"

    hide gavin
    "You try to hold back your tears as you look up at the sky, noticing that it’s starting to rain."
    "You feel water droplets on your face, but you can’t quite tell if it’s tears or the rain."
    "Very Bad Ending"
    return


# TODO if have time
# chicken pic and sound for chicken out ending
