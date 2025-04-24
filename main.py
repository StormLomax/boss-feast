# Boss Feast
# Text-Based Adventure Game
# Created by Storm Lomax
# Created on 24/04/2025

inventory = []

# The game intro
def intro():
    while True: 
        print("Welcome to Boss Feast!")
        player = input("What's your name, dungeon crawler? ")
        print("Your name is " + player + ".")
        name = get_valid_input("Is that right? (yes/no): ", ['yes', 'no'])
        if name == 'yes':
            print("Welcome to the dungeon,", player)
            begin()
        if name == 'no':
            break

# Start screen
def begin():
    button = get_valid_input("Type 'start' to begin your adventure: ", ['start'])
    if button == 'start':
        entry()
    else:
        print("Invalid input. Please type 'start'.")
        begin()

# Game intructions
def entry():
    print("You stand in a narrow entryway to the dungeon.")
    print("You have your trusty sword and robust shield, both of which have seen many battles.")
    print("You've fought many bosses, so you're not worried about defeating this dungeon boss - but you really want to see what it tastes like.")
    print("In order to do that, you need to collect a few items from the dungeon before you meet the boss.")
    print("""You will need:
        1) A blue mushroom
        2) Rock salt
        3) Slime gelatin
        4) A cooking pot
        5) Recipe sheet part 1 (ingredients)
        6) Recipe sheet part 2 (instructions)""")
    print("Make your way through the dungeon, collecting all the items, before you reach the boss.")
    start = get_valid_input("Do you accept this quest? (yes/no) ", ['yes', 'no'])
    if start == 'yes':
        entryroom()
    if start == 'no':
        return

# Entry room
def entryroom():
    print("There are two doors leading into the dungeon.")
    door = get_valid_input("Which one do you choose? (left/right) ", ['left', 'right'])
    if door == 'left':
        room1()
    if door == 'right':
        print("You walk through the door to your right.")
        room2() 
  
# Pit room      
def room1():
        print("You stride confidently through the left door, and straight into a pit.")
        print("Unfortunately, dungeons don't come with hazard warning signs (but they probably should).")
        print("The pit is lined with spikes, and you die on impact.")
        print("That was a short-lived adventure.")
        pit = get_valid_input("Do you want to try this room again? (yes/no) ", ['yes', 'no'])
        if pit == 'yes':
            entryroom()
        if pit == 'no':
            return

# Chest monster room   
def room2():
    print("The room is small and cramped, but two large torches hang on the walls, so you can see clearly.")
    print("Against one wall sits a locked chest. There is nothing else of note.")
    chest = get_valid_input("Do you try to lockpick the chest or proceed to the next room? (lockpick/proceed) ", ['lockpick', 'proceed'])
    if chest == 'lockpick':
        print("You attempt to lockpick the chest with absolutely no prior knowledge of lockpicking.")
        print("It turns out not to matter, because as soon as you touch the chest, you realise you've made a mistake.")
        print("The chest opens up into a giant mouth, lined with razor-sharp teeth.")
        print("Before you can even scream, it's swallowed you whole.")
        print("You have a few minutes to contemplate your life choices in the dark of the monster's stomach.")
        print("...")
        print("Times up. Now you're dead.")
        end = get_valid_input("Do you want to try this room again? (yes/no) ", ['yes', 'no'])
        if end == 'yes':
            room2()
        if end == 'no':
            return
    if chest == 'proceed':
        print("You decide to move onto the next room.")
        print("Just as you skirt by the chest, it opens into the mouth of a terrifying monster.")
        print("You scream and bolt for the door, slamming it behind you as the monster wails with disappointment.")
        print("Phew. That was close.")
        room3()
                      
             

# Rock salt room
def room3():  
    print("You find yourself in a much bigger room, with a high ceiling and many lit torches lining the walls.")
    print("In the middle of the room sits a wide pool of clear blue water. You get the feeling it's deeper than it looks.")
    print("Sitting to one side is a rock-like creature. Looking at him, you realise he's made of rock salt.")
    print("This would be a good opportunity to get one of your key ingredients.")
    rock = get_valid_input("Do you attack or talk to the creature? (attack/talk)", ['attack', 'talk'])
    if rock == 'attack':
        print("You scream and charge at the creature.")
        print("Completely unprovoked, by the way.")
        print("He was just sitting there.")
        print("You strike a solid blow and split him down the middle.")
        print("Again, completely unprovoked.")
        print("The innocent rock creature dies quickly and, to your dismay, his body turns to dust. Rock salt included.")
        print("Way to go.")
        print("You've failed the quest.")
        end = get_valid_input("Do you want to try this room again? (yes/no)", ['yes', 'no'])
        if end == 'yes':
            room3()
        if end == 'no':
            return
    if rock == 'talk':
        print("You introduce yourself to the rock creature.")
        print("'I'm Dwayne,' he replies miserably.")
        ask = get_valid_input("Do you want to ask what's wrong? (yes/no)", ['yes', 'no'])
        if ask == 'no':
            print("Don't be a dick.")
            print("Try again.")
            ask2 = get_valid_input("Do you want to ask what's wrong? (yes/no)", ['yes', 'no'])
            if ask2 == 'no':
                print("Alright, get outta here.")
                print("Game over.")
                return
            if ask2 == 'yes':
                print("Dwayne tells you he lost his pet rock somewhere in the dungeon.")
                print("You tell him you'll try to find it, and you'll bring it back to him if you do.")
                print("Dwayne only nods sadly.")
                print("It's time to move onto the next room.")
                room4()
        if ask == 'yes':
            print("Dwayne tells you he lost his pet rock somewhere in the dungeon.")
            print("You tell him you'll try to find it, and you'll bring it back to him if you do.")
            print("Dwayne only nods sadly.")
            print("It's time to move onto the next room.")
            room4()

# Slime room          
def room4():
    print("As soon as you enter, you're under attack!")
    print("Something wet and sticky lands on you, and you swipe out with your sword on instinct.")
    print("Your trusty sword slashes through the monster, and it retreats.")
    print("Standing before you is a large blob, bobbing gently up and down.")
    print("You've found a slime!")
    print("It jiggles at you threateningly.")
    slime = get_valid_input("Do you attack or make a break for the next room? (attack/run)", ['attack', 'run'])
    if slime == 'run':
        print("You decide not to fight the slime and try to run around it to the next room.")
        print("The slime is too fast, however, and sends a thick glob across your path.")
        print("You land on your face, sword clattering away.")
        print("The slime grabs your sword, swallowing it into its jiggly body.")
        print("The slime blocks your path, and grabs onto your limbs.")
        print("You try to struggle away but it has you in its sticky grip.")
        print("You die a very unpleasant death.")
        print("You have to wonder why a brave crawler who isn't worried about defeating the boss would try to run from a slime.")
        print("Food for thought.")
        print("Game over.")
        end = get_valid_input("Do you want to try this room again? (yes/no)", ['yes', 'no'])
        if end == 'yes':
            room4()
        if end == 'no':
            return
    if slime == 'attack':
        print("Using your many fighting skills, you expertly swipe across the slime's body, targeting its jiggly organs.")
        print("The slime wobbles and tries to grab your sword, but you spin out of the way with a flourish.")
        print("You're an experienced dungeon crawler who's fought many slimes. This one is no trouble.")
        print("With one final blow, you defeat the slime.")
        print("Like any decent crawler, you ransack the corpse.")
        global inventory
        inventory.append("slime gelatin")
        print("You have collected slime gelatin!")
        print(f"Your inventory now contains: {', '.join(inventory)}")
        print("You proceed to the next room.")
        room5()

# Recipe part 1 room       
def room5():
    print("You enter a small library, full to the brim with books.")
    print("It smells of paper and dust, and in the middle sits a lone dungeon crawler.")
    print("'You don't happen to have seen a recipe card in here?' you ask.")
    print("'A recipe card for what?' they reply without looking up from their book.")
    print("'For the dungeon boss,' you reply.")
    print("No one says anything for a long time.")
    print("'You want to cook that thing?' the crawler asks, which is a fair question.")
    print("'Yes,', you reply. 'Have you seen the recipe card?")
    print("'I think I saw half of one. I'll give it to you in return for something.'")
    print("Oh great. It's one of those quests.")
    print("'If you can bring me a book on dungeon romance, I'll find the recipe card for you.'")
    print("Again, there's a long silence.")
    answer = get_valid_input("What do you say? (yes/no)", ['yes', 'no'])
    if answer == 'no':
        print("'No, weirdo,' you say.")
        print("'Oho! Judgement coming from the monster eater,' the crawler snaps back.")
        print("They have a point.")
        print("'Find the recipe card yourself,' the crawler grumbles, turning back to their book.")
        print("You decide to do so.")
        print("It's only when you've spent three days searching that you realise you might have made a mistake.")
        print("Maybe less judgement next time, hmm?")
        end = get_valid_input("Do you want to try this room again? (yes/no)", ['yes', 'no'])
        if end == 'yes':
            room5()
        if end == 'no':
            return
    if answer == 'yes':
        print("'Okay, you have a deal,' you say.")
        print("'Excellent!' the crawler replies. 'There should be one in the next room.' They wave at one of two doors.")
        print("'The next room?' you say. 'Why can't you go and get it then?'")
        print("'Oh, I'm cursed.' The crawler shrugs. 'Anyone who reads in this room is.'")
        print("'Sorry, what?'")
        print("'Yeah, as soon as you read in here, you can never leave. I think I've been here for like, seven years. But who knows.'")
        print("Wtf")
        print("You decide not to think about how close to came to being cursed, and quickly cross over to the next room.")
        room6()

# Romance book room - puzzle/trap room      
def room6():
    print("This is clearly a trap room.")
    print("The floor is made of large tiles split into three paths: left, right, and middle.")
    print("Holes line the walls and experience tells you either arrows or fire will shoot out if you take the wrong path.")
    print("On the opposite wall sits a degraded plaque with a riddle.")
    print("""It says:
          At forks in the rod, I might be your plight,
          I’m not quite right, though I’m always in sight.
          I’m what remains when all else is gone,
          A single direction, yet never head-on.""")
    path = get_valid_input("What path do you choose? (left/right/middle)", ['left', 'right', 'middle'])
    if path == 'middle':
        print("You choose the middle path.")
        riddle()
    if path == 'right':
        print("You choose the right path.")
        riddle()
    if path == 'left':
        print("You choose the left path.")
        print("You make it safely across the room and to the other side.")
        print("Awaiting you is a chest.")
        print("You eagerly open it to find several gold coins and a book with a half-naked minotaur on the cover.")
        global inventory
        inventory.append("gold coins")
        inventory.append("romance book")
        print("You have collected gold coins!")
        print("You have collected a romance book!")
        print(f"Your inventory now contains: {', '.join(inventory)}")
        proceed = get_valid_input("Are you ready to return to the library? (yes/no)", ['yes', 'no',])
        if proceed == 'no':
            print("There is nothing more to do in this room")
            print("You head back to the library.")
            room5again()
        if proceed == 'yes':
            print("You head back to the library.")
            room5again()      
        
# Picking the wrong path in room6
def riddle():
        print("As soon as you step on the tile, you hear a click in the walls.")
        print("Poison arrows fly from the holes, turning you into a pincushion.")
        print("It's quickly followed by flames shooting out and engulfing you.")
        print("Whoever made this room really left nothing up to chance.")
        print("You're dead before you hit the floor.")
        end = get_valid_input("Do you want to try this room again? (yes/no)", ['yes', 'no'])
        if end == 'yes':
            room6()
        if end == 'no':
            return   

# Room5 - returning the romance book
def room5again():
    print("The crawler's eyes light up when you show them the book.")
    print("'Yes, that's perfect!' they say.")
    print("'A deal's a deal,' you reply, handing the book over.")
    print("'Sure, yeah, whatever.' The crawler pulls out a piece of paper from between two books and gives it to you.")
    print("'This isn't going to curse me, is it?' you ask, eyeing it warily.")
    print("'Nah, as long as you read it outside of the library, you'll be fine.' The crawler sounds pretty confident.")
    print("You decide to take it.")
    global inventory
    if "romance book" in inventory:
        inventory.remove("romance book")
    inventory.append("recipe card part 1")
    print("You have given away romance book.")
    print("You have collected recipe card part 1!")
    print(f"Your inventory now contains: {', '.join(inventory)}")
    print("With your new items secured, you take the other available door in the library and move deeper into the dungeon.")
    cont = get_valid_input("Do you wish to continue? (yes/no)", ['yes', 'no'])
    if cont == 'no':
        quit = get_valid_input("Are you sure you want to quit the game? (yes/no)", ['yes', 'no'])
        if quit == 'yes':
            return
        if quit == 'no':
            print("You proceed to the next room.")
            room7()
    if cont == 'yes':
        print("You proceed to the next room.")
        room7()
        
# The memory room - rock pet
def room7():
    print("This looks like a... weirdly normal room.")
    print("It's large, with a pool of water in the middle.")
    print("Actually, it looks exactly like that room you saw the rock creature in.")
    print("Didn't you already come here?")
    print("To the side sits a rock creature.")
    print("You feel a sense of deja vu but... your memory becomes foggy.")
    memory = get_valid_input("Do you attack or talk to the rock creature? (attack/talk)", ['attack', 'talk'])
    if memory == 'attack':
        print("You draw your sword and make to attack the rock creature.")
        print("Wait, no.")
        memorymonster()
    if memory == 'talk':
        print("You introduce yourself to the rock creature.")
        print("'I'm Dwayne,' he replies miserably.")
        ask = get_valid_input("Do you want to ask what's wrong? (yes/no)", ['yes', 'no'])
        if ask == 'no':
            print("You ignore the rock creature and try to leave the room.")
            print("Your legs stop.")
            print("You can't leave.")
            memorymonster()
        if ask == 'yes':
            print("Dwayne tells you he lost his pet rock somewhere in the dungeon.")
            print("You tell him you'll try to find it, and you'll bring it back to him if you do.")
            print("Dwayne only nods sadly.")
            print("Before you can leave the room, something hisses angrily.")
            print("The room shimmers like a mirage before dissolving right in front of you.")
            print("Instead of the room with the water pool, it's a dark, gloomy cavern.")
            print("A creature screeches from above you before landing with a thump on the ground.")
            print("The illusion is shattered and the memory monster is dead.")
            print("On the far side of the cavern, you hear a rustle in the dark.")
            rustle = get_valid_input("Do you investigate? (yes/no)", ['yes', 'no'])
            if rustle == 'no':
                print("You cross the room, ignoring the rustle, and try to open the door.")
                print("It's locked.")
                petrock()
            if rustle == 'yes':
                petrock()
                
# When the player gets the memories wrong in room7
def memorymonster():
    print("This is wrong.")
    print("This isn't how it went.")
    print("Something hisses and cackles in your ear, distinctly pleased.")
    print("You've changed the memory.")
    print("You've failed the task.")
    print("Dazed, you can only stand there as your mind fights with itself.")
    print("The creature in the shadows slithers closer.")
    print("Caught in your memories, you don't even fight back as it swallows you whole.")
    end = get_valid_input("Do you want to try this room again? (yes/no)", ['yes', 'no'])
    if end == 'yes':
        room7()
    if end == 'no':
        return 
                    
# Investigating the pet rock noise
def petrock():
    print("You cautiously investigate the noise.")
    print("To your surprise, a small rock wearing a dog colalr totters out of the shadows.")
    print("Unless there are other pet rocks around here, this must be Dwayne's.")
    print("You gently pick up the pet rock.")
    global inventory
    inventory.append("pet rock")
    print("You have a pet rock!")
    print(f"Your inventory now contains: {', '.join(inventory)}")
    dwayne = get_valid_input("Are you ready to return to Dwayne? (yes/no)", ['yes', 'no'])
    if dwayne == 'no':
        print("There is nothing else to do in this room.")
        print("You head back to Dwayne's room.")
        dwaynereturn()
    if dwayne == 'yes':
        print("You head back to Dwayne's room.")
        dwaynereturn()

def dwaynereturn():
    print("Dwayne is overjoyed when he sees his pet rock.")
    print("The pet rock is also, somehow, very excited.")
    global inventory
    if "pet rock" in inventory:
        inventory.remove("pet rock")
    print("You have given away the pet rock.")
    print(f"Your inventory now contains: {', '.join(inventory)}")
    print("'You have my eternal gratitude for rescuing Pebble.' Dwayne says.")
    print("He roots around in his inventory for a while before pulling out a large cooking pot and a small silver key.")
    print("'You can have these,' he says. 'The key will lead to the kitchens, where I used to work. Don't tell anyone I stole a pot.")
    print("You pocket the items.")
    inventory.append("rock salt")
    inventory.append("silver key")
    print("You have collected rock salt!")
    print("You have collected a silver key!")
    print(f"Your inventory now contains: {', '.join(inventory)}")
    print("With your new items, you head back to the room with the dead memory monster.")
    cont = get_valid_input("Do you want to continue? (yes/no)", ['yes', 'no'])
    if cont == 'no':
        exit = get_valid_input("Are you sure you want to quit the game?")
        if exit == 'yes':
            return
        if exit == 'no':
            print("You continue on.")
            betweenroom()  
    if cont == 'yes':
        print("You continue on.") 
        betweenroom() 

# Unlocking the memory room to the kitchens
def betweenroom():
    print("You make it back to the memory monster room, and it's still safely dead.")
    print("You use the silver key to unlock the door on the other side.")
    room8()

# The kitchens - blue mushroom   
def room8():
    print("You find yourself in a large kitchen, full of rock creatures in chef hats.")
    print("'BEHIND YOU,' one screams before torpedoing past, nearly knocking you off your feet.")
    print("'Who are you? What do you want? Do you have any kitchen experience?' another one says, grabbing you by the shoulders.")
    print("Before you can answer, something round and blue catches your eye.")
    print("On the counter sits a basket overflowing with blue mushrooms.")
    mushrooms = get_valid_input("Do you steal the mushrooms or try to make a deal? (steal/deal)", ['steal', 'deal'])
    if mushrooms == 'steal':
        cooked()
    if mushrooms == 'deal':
        print("You decide to try and strike a deal.")
        print("'If you give me those mushrooms, I'll share the meal I make with it later,' you say.")
        print("The chef quirks a rocky brow.")
        print("'What meal are you making exactly?' he asks.")
        lie = get_valid_input("Do you tell the truth or lie? (truth/lie)", ['truth', 'lie'])
        if lie == 'lie':
            print("You decide the truth doesn't sound appealing to anyone except you.")
            print("You tell him you're going to cook a mushroom stew.")
            print("The chef looks unimpressed.")
            print("'Sounds boring,' he says. 'No thanks.'")
            mushrooms = get_valid_input("Do you steal the mushrooms or tell him the truth? (steal/truth)", ['steal', 'truth'])
            if mushrooms == 'steal':
                cooked()
            if mushrooms == 'truth':
                print("You decide you might as well tell him the truth.")
                print("'I'm going to cook the dungeon boss,' you say.")
                print("The chef looks amused.")
                print("'Now that does sound interesting,' he says. 'Alright, count me in. Take the mushrooms and bring me back what you make with it.")
                print("Happily, you stuff a bunch of mushrooms in your pockets.")
                inventory.append("blue mushrooms")
                print("You have collected blue mushrooms!")
                print(f"Your inventory now contains: {', '.join(inventory)}")
                print("You're ready to move to the next room.")
                cont = get_valid_input("Are you ready to continue? (yes/no)", ['yes', 'no'])
                if cont == 'no':
                    exit = get_valid_input("Are you sure you want to quit the game?")
                    if exit == 'yes':
                        return
                    if exit == 'no':
                        print("You continue on.")
                        room9()  
                if cont == 'yes':
                    print("You continue on.") 
                    room9()
                    
# The shrine room - recipe card 2
def room9():
    print("This room is currently under construction")
    return
                
                
            
        
def cooked():
    print("You snatch the basket of mushrooms and try to make a break for it.")
    print("In a room full of rock monsters, you obviously don't get very far.")
    print("'Thief!' someone yells.")
    print("Oh shit, that's you they're talking about.")
    print("You heroically leap over a rock monster who lunged at you")
    print("And then you land on a stray banana peel and hit the deck.")
    print("One of the chefs picks you up by the scruff of your collar.")
    print("'Thieves get cooked' he says with a wicked grin.")
    print("'But I'm not tasty!' you protest.")
    print("'I'll eat anything once,' he simply replies with a shrug.")
    print("For what it's worth, you end up not being very tasty at all, so you were right.")
    print("You're still dead though.")
    end = get_valid_input("Do you want to try this room again? (yes/no)", ['yes', 'no'])
    if end == 'yes':
        room8()
    if end == 'no':
        return 
       
        
# Lets players play again from the beginning   
def play_game():
    while True:
        intro()
        again = get_valid_input("\nWould you like to play again? (yes/no): ", ['yes', 'no'])
        if again != 'yes':
            break  

#  Lets players enter a choice again if they enter a spelling mistake, etc.
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid choice. Please choose from {', '.join(valid_options)}.")    

# Start the game
play_game()