# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character('Gavin', color="#00FF00")
define m = Character('Me')


# The game starts here.

label start:

    $ totalScore = 0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene morning

    "Choose a difficulty level"
    
    menu:
    # Difficulty Level
    # Asian 			+ 10000  ⇒ 
    # Half asian 		+ 50
    # Fox girl			+ 10
    # Weeb			+ 5
    # Not asian		+ 0
    # Zombie kawaii girl 	+ 1
    # Deceased		- 10
        
        "Asian": 
            $ totalScore += 10000

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


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show gavin happy

    if (totalScore >= 10000):

        g "I love you"

        "Gavin grabs you by the hair and kisses you. Happy Ending."

    else:

        g "I'm not interested"
        
        "Gavin grabs you by the hair and throws you out of his room. Bad Ending"

    
    # These display lines of dialogue.

    # g "You've created a new Ren'Py game."

    # g "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
