import whiskerworld_text
from random import randint, choice
from time import sleep

#Code not implemented yet for riddler game
def play_riddler_game():
    """ Has user answer multiple riddles to earn XP """
    questions = {
        "Q1": "If I have it, I don't share it. If I share it, I don't have it. What is it?",
        "A1": "A secret",
        "Q2": "A cowboy rides into town on Friday, stays for three days and leaves on Friday. How did he do it?",
        "A2": "The horse's name is Friday.",
        "Q3": "Two cowboys live next door to each other and both have a corral for their cows in the back. \
        One day they meet at the back of their homes, standing next to a wall dividing their corrals. \
        The first cowboy gets to thinking and asks his neighbor for a cow so he can double his herd. \
        The other cowboys replies, 'That's fine by me partner, cuz then we'll have the same number of cows.' \
        How many cows does each cowboy own?",
        "A3": "The first cowboy has 1 cow, and the second cowboy has 3 cows.",
        "Q4": "5 cats can catch 5 mice in 5 minutes. How many cats does it take to catch 100 mice in 100 minutes?",
        "A4": "5 cats. The same five could keep catching 5 mice every 5 minutes for 100 minutes.",
        "Q5": "Six men are carrying boxes holding six cats and each cat has 6 kittens. How many legs are there in total?",
        "A5": "1020. There are 6 men with 2 legs each, for a total of 12 legs. There are 36 cats with 4 legs each for a total of 144 legs. \
        There are 216 kittens with 4 legs each for a total of 864 legs. 12 + 144 + 864 = 1020.",
        "Q6": "If you are running in a race and pass the person in second place, what position are you in?",
        "A6": "Second place. If you guessed first place, the person in first place is still there. But I'm sure you're catching up."
    }

def get_user_name():
    """ Asks user name, get's input, and returns it """
    print """
    'Howdy, pawtner!' he says. 'I bet you can't wait to get to WhiskerWorld.
    What's your name?'"""
    user_name = raw_input("""
    >>> """).title()
    return user_name

def display_cat_type(dictionary):
    """ Displays cat type options, gets input for option chosen, and returns it. """
    print """
    'And {}, can you tell me what type of cat you are? Calico, like me,
    or...'""".format(dictionary["name"])
    
    user_cat_type_choice = raw_input("""
    A. Calico
    B. Tuxedo
    C. Orange Tabby
    D. Grey
    E. Black
    F. White
    >>> """).upper()
    return user_cat_type_choice


def display_cat_hat():
    """ Displays cat hat options, gets user's input for option chosen. """
    user_cat_hat_choice = raw_input( """
    'Purr-fect! Now, one final question. Do you want to wear a white hat,
    and live out your hero cat dreams? Or will you be a bad cat bandit and wear
    a black hat?'

    A. White hat
    B. Black hat
    >>> """).upper()
    return user_cat_hat_choice


def display_miss_kitty():
    """ Displays Miss Kitty options, gets user's input for the option chosen. """
    user_miss_kitty_choice = raw_input("""
    'It's just clawful! Can you help meow-t?'
    
    A. Help Miss Kitty by finding the bandits and recovering the milk.
    (Option not yet available) B. Decide to look for other adventures in Whispurr Ridge.
    >>> """).upper()
    
    return user_miss_kitty_choice


def display_sheriff():
    """ Displays sheriff options, gets user's input for the option chosen."""
    user_sheriff_choice = raw_input("""
    'What do you want to do?'
    
    A. Depart to Abermeowthy Ranch with Teddy Fleas.
    B. Stay with Sheriff Pawkitt and question the townscats.
    >>> """).upper()
    
    return user_sheriff_choice

def display_ranch_qs():
    """Displays questions for the Abermeowthy family, gets user's input for the option chosen."""
    user_ranch_q = raw_input("""
    You ask Peter and Dolores:
    
    A. 'How many bandits did you see?'
    B. 'Did you recognize any of the bandits?'
    C. 'Was anyone hurt during the robbery?'
    D. Nothing else. (exit)
    >>> """).upper()
    
    return user_ranch_q

def display_store_qs():
    """Displays questions for Clementine Purryfeather, gets user's input for the option chosen."""
    user_store_q = raw_input("""
    You ask Clementine Purryfeather:
    
    A. 'Have you seen any suspic-hiss types come into your store lately?'
    B. 'Did you sell any goods to newcomers?'
    C. 'Anyone else you think we should talk to?'
    D. Nothing else. (exit)
    >>> """).upper()
    
    return user_store_q


def dolores_race():
    # Function that gets user input and compares to NPC output. Whichever gets total to 50 first wins the race.
    print """
    With each section of the race, you will be asked to enter a number from
    1 - 5 to represent your power level for that part of the race. But,
    the race has twists and turns. If you are going too fast, you may tumble
    off the race path. If you go too slow, Dolores may beat you to the finish!
    """
    
    dolores_race_counter = 0
    user_race_counter = 0
    race_counter = 0
    
    while user_race_counter < 50 and dolores_race_counter < 50:
        race_counter += 1
        race_difficulty = randint(1,5)
        
        user_power = raw_input("""
    How much power do you want to use? Enter a number from 1 - 5.
    >>> """)
        user_power = int(user_power)
        while True:
            if 0 < user_power < 6:
                user_progress = user_power * race_difficulty
                if user_progress > 19:
                    print """
        Oh no! You've tumbled off the track.
                    """
                    user_race_counter += (user_progress * 0.25)
                    break
                else:
                    user_race_counter += user_progress
                    break
            else:
                print "Sorry, pawtner, that's not valid choice. Try again."
        
        while True:
            if user_race_counter < 50:
                dolores_power = randint(2,5)
                dolores_progress = dolores_power * race_difficulty
                if dolores_progress > 16: 
                    print """
        Oh no! Dolores has tumbled off the race path.
            """
                    dolores_race_counter += (dolores_progress * 0.25)
                else: 
                    dolores_race_counter += dolores_progress
        
                user_race_percent = int((user_race_counter / 50.0) * 100)
                dolores_race_percent = int((dolores_race_counter / 50.0) * 100)
        
                if user_race_counter == dolores_race_counter:
                    print """
        You and Dolores are tied in the race after {} sections!
        You've finished {}% and Dolores has finished {}% of the race.
            """.format(race_counter, user_race_percent, dolores_race_percent)
                elif user_race_counter > dolores_race_counter:
                    print """
        You're in the lead after {} sections!
        You've finished {}% and Dolores has finished {}% of the race.
            """.format(race_counter, user_race_percent, dolores_race_percent)
                else: 
                    print """
        Dolores is in the lead after {} sections!
        You've finished {}% and Dolores has finished {}% of the race.
            """.format(race_counter, user_race_percent, dolores_race_percent)
                break
            else:
                break
            
    if user_race_counter > dolores_race_counter:
        print """
        Yee-haw! You won the race!
        """
        return True
    elif user_race_counter < dolores_race_counter:
        print """
        Nice try, but unfurtunately, Dolores won the race.
        """
        return False
    else:
        print """
        Boop that snoot! You and Dolores tied.
        """
        return None


def cat_fight(dictionary):
    # Function that gets user input, compares to NPC output. Whichever is first to decrease health to 0 first, loses the game.
    
    print """
    With each round of the fight, you'll be asked to enter a letter to represent
    the area of Hisstor's body you want to claw. Hisstor will be defending against
    your attacks, so choose well! Then, Hisstor will attack you, and you'll need
    to choose an area to defend. The first to have health reach 0 is a goner, and
    loses the cat fight! 
    """
    # Start health for each player at 100 and round of fight at 0
    hisstor_health = 100
    user_health = 100
    fight_round = 0
    
    # Loop until one player's health hits 0
    while user_health > 0 and hisstor_health > 0:
        fight_round += 1
        attack_defense_area = {"A":20, "B": 10, "C": 15, "D": 10, "E": 10, "F": 5}
        print whiskerworld_text.round_header.format(fight_round)
        
        # Get user attack area
        while True:
            user_attack_area = raw_input("""
        What area do you want to attack?
        A. Head
        B. Back
        C. Belly
        D. Front legs
        E. Back legs
        F. Tail
        >>> """).upper()
            if user_attack_area not in "ABCDEF":
                print "Sorry, pawtner, that's not a valid choice!"
            else:
                break
        
        # Get random area that Hisstor defends
        hisstor_defense_area = choice(attack_defense_area.keys())

        # Compare user attack area to Hisstor defense area, and deduct points as required
        if user_attack_area == hisstor_defense_area:
            print """
            Oh, scratch! Hisstor defended against your attack.
            """
        else:
            print """
            A purrfect scratch! Your attack hits Hisstor!
            """
            # Hisstor health decreases by number value corresponding to key
            hisstor_health -= attack_defense_area[user_attack_area]
        
        # Get random area that Hisstor attacks
        hisstor_attack_area = choice(attack_defense_area.keys())

        # Get user defense area
        while True:
            user_defense_area = raw_input("""
        What area do you want to defend?
        A. Head
        B. Back
        C. Belly
        D. Front legs
        E. Back legs
        F. Tail
        >>> """).upper()
            if user_defense_area not in "ABCDEF":
                print "Sorry, pawtner, that's not a valid choice!"
            else:
                break
        
        # Compare user defense area to Hisstor attack area, and deduct points as required
        if hisstor_attack_area == user_defense_area:
            print """
            Your feline instincts worked! You defend against Hisstor's attack. 
            """
        else:
            print """
            Oh, scratch! Hisstor's attack hurts you. 
            """
            # User health decreases by number value corresponding to key
            user_health -= attack_defense_area[hisstor_attack_area]
        
        # Compare user health to Hisstor health, and let them know if they are winning/losing fight
        if user_health == hisstor_health:
            print """
            You and Hisstor are tied after {} rounds!
            """.format(fight_round)
        elif user_health > hisstor_health:
            print """
            You're winning the fight after {} rounds!
            """.format(fight_round)
        else: 
            print """
            Hisstor is winning the fight after {} rounds!
            """.format(fight_round)

    if user_health > hisstor_health:
        print whiskerworld_text.fight_win.format(dictionary["name"])
        return True
    elif user_health < hisstor_health:
        print whiskerworld_text.fight_lose.format(dictionary["name"])
        return False
    else:
        print whiskerworld_text.fight_tie
        return None

def get_dice_points(user_round_rolls):
    user_round_total = 0
    dice_count = {"one count": 0, "two count": 0, "three count": 0, "four count": 0, "five count": 0, "six count": 0}
            
    for key in user_round_rolls:
        if user_round_rolls[key] == 1:
            dice_count["one count"] += 1
        elif user_round_rolls[key] == 2: 
            dice_count["two count"] += 1
        elif user_round_rolls[key] == 3:
            dice_count["three count"] += 1
        elif user_round_rolls[key] == 4:
            dice_count["four count"] += 1
        elif user_round_rolls[key] == 5:
            dice_count["five count"] += 1
        elif user_round_rolls[key] == 6:
            dice_count["six count"] += 1

    for key in dice_count:
        if key == "one count":
            user_round_total += (dice_count["one count"] * 100)
        elif key == "five count":
            if dice_count["five count"] == 3:
                user_round_total += 300
            elif dice_count["five count"] == 4:
                user_round_total += 350
            elif dice_count["five count"] == 5:
                user_round_total += 400
            elif dice_count["five count"] == 6:
                user_round_total += 600
            else:
                user_round_total += (dice_count["five count"] * 50)
        else:
            if 3 <= dice_count[key] <= 5:
                user_round_total += 300
            elif dice_count[key] == 6:
                user_round_total += 600
    return user_round_total

def parse_string_of_dice(user_dice_string):
    dice_list = []
                
    temp_dice_list = user_dice_string.split(',')
    
    for die in temp_dice_list:
        die = int(die)
        dice_list.append(die)
    
    return dice_list


def play_dice_game():
    """User plays rounds of dice against Lion Leo. First to 2000 points wins"""
    print """
    You and Lion Leo each have 6 dice. In each round, you will roll all 6 dice, 
    and hope to get 1's (worth 100 points), 5's (worth 50 points), or three of a 
    kind (worth 300 points). You can reroll 3 times with any dice that you would 
    like to get a better result. If you choose not to reroll, or you've used all 
    3 of your rerolls, you keep the final round score and add it to your total. 
    Then Lion Leo does the same, and the round ends. The first player to 2000
    points wins.
    """
    
    raw_input("""
            Press ENTER to start next round. 
            """)
    
    
    # Start dice round 0, and add one each loop. Start players points at 0.
    dice_round = 0
    user_total_points = 0
    leo_total_points = 0
    
    # Loop until one player's point reaches 2000
    while user_total_points < 2000 and leo_total_points < 2000:
        dice_round += 1
        reroll_count = 0
        print whiskerworld_text.round_header.format(dice_round)
        
        user_round_rolls = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        
        # Get user's 6 random dice rolls and add to dictionary
        for key in user_round_rolls:
            # Assign a random number from 1-6 to each die
            user_round_rolls[key] = randint(1,6)
        
        while reroll_count < 4:
            # Show user output, and ask if they want to keep the dice, or reroll any of them
            print """
            You've rolled:
            Die 1: {}
            Die 2: {}
            Die 3: {}
            Die 4: {}
            Die 5: {}
            Die 6: {}""".format(user_round_rolls[1], user_round_rolls[2], user_round_rolls[3], user_round_rolls[4], user_round_rolls[5], user_round_rolls[6]) 
            
            # Call the dice point total function
            user_round_total = get_dice_points(user_round_rolls)
            
            if reroll_count < 3:
                current_round = "current"
            else:
                current_round = "final"

            print """
            Your {} round total is: {}""".format(current_round, user_round_total)
            
            if reroll_count < 3:
                user_reroll_choice = raw_input("""
            Would you like to reroll any of the dice? (Y)es or (N)o.
            >>> """).upper()
            
                if user_reroll_choice == "Y":
                    reroll_count += 1
                    user_dice_string = raw_input("""
            Which dice would you like to reroll? List all here, separated by a comma.
            >>> """)
                    
                    # Slice user string into list of ints and return to dice_list
                    dice_list = parse_string_of_dice(user_dice_string)
                    
                    # Reset the dice in dice_list to value 0
                    for die in dice_list:
                        if die in user_round_rolls.keys():
                            user_round_rolls[die] = 0
                    
                    # Reroll for the dice with value 0
                    for key in user_round_rolls:
                        if user_round_rolls[key] == 0:
                            user_round_rolls[key] = randint(1,6)

                elif user_reroll_choice == "N":
                    break
                else: 
                    print """
            Sorry, pawtner, that's not valid choice. Try again.
                """
            
            else:
                break

        #Update user total points after their part in the round has ended
        user_total_points += user_round_total
        
        # If user hasn't hit 2000 points in the previous section, move on to Lion Leo's round
        # Randomly assign Leo points in a range for the round and add to his total points
        if user_total_points < 2000:
            leo_round_total = choice(range(300, 551, 50))
            leo_total_points += leo_round_total
        
            print """
            Lion Leo rolls..."""
            sleep(0.5)
            print """
            ... """
            sleep(0.5)
            print """
            ... """
            sleep(0.5)
            print """
            Lion Leo scores a round total of {}. 
            """.format(leo_round_total)
        
            print """
            Point totals after {} rounds:
            - Your total points: {}
            - Lion Leo's total points: {}
            """.format(dice_round, user_total_points, leo_total_points)
        
            raw_input("""
            Press ENTER to start next round. 
            """)
        else:
            print """
            Your total points: {}
            """.format(user_total_points)
        
    if user_total_points > leo_total_points:
        return True
    elif user_total_points < leo_total_points:
        return False
    else:
        return None


def get_western_name(dictionary):
    """If user wins game, give them a nickname. Would like to make this dictionary that uses the first
    letter of the users name to find the matching western name. For now, it is based on points. """
    if dictionary["experience"] >= 80:
        return "Calamity"
    else:
        return "Cactus"



###########################################################################################

def play_whiskerworld():
    """ Main code to run the game. Calls on functions above and text from external file. """
    #Set up dictionary to store all user info and choices
    character_info = {
        "experience": 5
        }

    # PART 1: Start with intro dialogue and gather info about the player
    print whiskerworld_text.intro_text

    #Gather player name, store in dictionary, and reward experience
    character_info["name"] = get_user_name()
    character_info["experience"] += 5

    #Gather player cat type, store in dictionary, and reward experience
    while True:
        user_cat_type = display_cat_type(character_info)
        if user_cat_type == "A":
            character_info["cat type"] = "calico"
            character_info["experience"] += 5
            break
        elif user_cat_type == "B":
            character_info["cat type"] = "tuxedo"
            character_info["experience"] += 5
            break
        elif user_cat_type == "C":
            character_info["cat type"] = "orange tabby"
            character_info["experience"] += 5
            break
        elif user_cat_type == "D":
            character_info["cat type"] = "gray"
            character_info["experience"] += 5
            break
        elif user_cat_type == "E":
            character_info["cat type"] = "black"
            character_info["experience"] += 5
            break
        elif user_cat_type == "F":
            character_info["cat type"] = "white"
            character_info["experience"] += 5
            break
        else:
            print "Sorry, pawtner, that's not valid choice. Try again."

    #Gather player hat type, store in dictionary, and reward experience
    while True:
        user_cat_hat = display_cat_hat()
        if user_cat_hat == "A":
            character_info["cat hat"] = "white"
            character_info["experience"] += 5
            break
        elif user_cat_hat == "B":
            character_info["cat hat"] = "black"
            character_info["experience"] += 5
            break
        else:
            print "Sorry, pawtner, that's not valid choice. Try again."

    print whiskerworld_text.outro_text
    raw_input("""
    Press ENTER to continue
    >>> """)


    # PART 2: Get user decision to help Miss Kitty, store in dictionary, reward experience
    print whiskerworld_text.intro_miss_kitty.format(character_info["name"])
    while True:
        user_miss_kitty = display_miss_kitty()
        if user_miss_kitty == "A":
            character_info["Help Miss Kitty"] = True
            character_info["experience"] += 5
            break
        elif user_miss_kitty == "B":
            character_info["Help Miss Kitty"] = False
            character_info["experience"] += 5
            break
        else:
            print "Sorry, pawtner, that's not valid choice. Try again."


    # PART 3: Get user decision to stay with Sheriff or go with Teddy, store in dictionary, reward experience (follows PART 2)
    if "Help Miss Kitty" in character_info.keys():
        if character_info["Help Miss Kitty"] == True:
            print whiskerworld_text.intro_sheriff.format(character_info["name"], character_info["cat type"], character_info["name"], character_info["name"])
            while True:
                user_sheriff = display_sheriff()
                if user_sheriff == "A":
                    character_info["Go with Teddy"] = True
                    character_info["experience"] += 5
                    break
                elif user_sheriff == "B":
                    character_info["Go with Teddy"] = False
                    character_info["experience"] += 5
                    break
            else:
                print "Sorry, pawtner, that's not valid choice. Try again."


    # PART 4: Get user outcome of dice game, store in dictionary, reward experience (follows PART 2)
    if "Help Miss Kitty" in character_info.keys():
        if character_info["Help Miss Kitty"] == False:
            print "You don't help Miss Kitty, and play a dice game with Lion Leo instead. This section hasn't been written yet!"


    # PART 5: Get user input for questions, user outcome of race with Dolores, store in dict, reward with XP (follows PART 3)    
    if "Go with Teddy" in character_info.keys():
        if character_info["Go with Teddy"] == True:
            # If you go with Teddy, meet the Abermeowthy family, ask them questions, race against Dolores
            print whiskerworld_text.intro_teddy.format(character_info["name"])
            raw_input("""
    Press ENTER to continue
    >>> """)
            print whiskerworld_text.intro_ranch.format(character_info["name"])
        
            # Loop allows user to ask 3 different questions. They can ask 1 or all three. Must choose D to quit and move to next phase.
            character_info["Abermeowthy Qs"] = []
            while True:
                user_ranch_qs = display_ranch_qs()
                if user_ranch_qs == "A":
                    print """
            Peter answers 'There were three... Pawsibly four? It all happened very quickly.
                    """
                    character_info["Abermeowthy Qs"].append("A")
                    character_info["experience"] += 5
                elif user_ranch_qs == "B":
                    print """
            'One looked furmiliar,' said Delores. 'I think it was that bandit Hisstor
            Eskitten! He had a scar across one eye.'
                    """
                    character_info["Abermeowthy Qs"].append("B")
                    character_info["experience"] += 5
                elif user_ranch_qs == "C":
                    print """
            'Delores was fine,' Peter says. 'But one of the bandits was quick on the
            claw! She got me pretty good.'
                    """
                    character_info["Abermeowthy Qs"].append("C")
                    character_info["experience"] += 5
                elif user_ranch_qs == "D":
                    break
                else:
                    print "Sorry, pawtner, that's not valid choice. Try again."
        
            # Dolores challenges user to a race, outcome doesn't change the story, add to dictionary, reward with XP
            print whiskerworld_text.dolores_race_intro.format(character_info["name"])
            character_info["Dolores Race"] = dolores_race()
            if character_info["Dolores Race"] == True:
                character_info["experience"] += 20
            elif character_info["Dolores Race"] == False:
                character_info["experience"] += 5
            else: 
                character_info["experience"] += 10
        
            print whiskerworld_text.outro_ranch.format(character_info["name"])
            raw_input("""
    Press ENTER to continue
    >>> """)

    # PART 6: Get user outcome questioning Purryfeather, Lion Leo, store in dictionary, reward experience (follows PART 3)           
        else:
            print whiskerworld_text.intro_purryfeather.format(character_info["name"], character_info["name"])
            
            # Loop allows user to ask 3 different questions. They can ask 1 or all three. Must choose D to quit and move to next phase.
            character_info["Purryfeather Qs"] = []
            while True:
                user_store_qs = display_store_qs()
                if user_store_qs == "A":
                    print """
            Clementine answers 'Well, I do remember one cat that stood out. Definitely
            never saw her before. She was a pure white cat with an orange and black swirl
            that wrapped around her body like a snake!'
                    """
                    character_info["Purryfeather Qs"].append("A")
                    character_info["experience"] += 5
                elif user_store_qs == "B":
                    print """
            'Yes, there was one orange tabby kitten that came in and bought THREE catnip
            mice. Three! I don't know how he had the money for it. He was purring to 
            himself when he left. Something about hiss... hisstor...' she says.  
                    """
                    character_info["Purryfeather Qs"].append("B")
                    character_info["experience"] += 5
                elif user_store_qs == "C":
                    print """
            'You might want to stop in the saloon and talk to Lion Leo. He's back to
            gambling again and I'm afraid he's had more than one run in with cats from
            the wrong side of the scratching post.' says Clementine.
                    """
                    character_info["Purryfeather Qs"].append("C")
                    character_info["experience"] += 5
                elif user_store_qs == "D":
                    break
                else:
                    print "Sorry, pawtner, that's not valid choice. Try again."
            
            # Lion Leo challenges user to a dice game, outcome doesn't change story, store in dictionary
            print whiskerworld_text.outro_purryfeather
            character_info["Lion Leo Dice Game"] = play_dice_game()
            
            # Outcome of dice game earns XP
            if character_info["Lion Leo Dice Game"] == True:
                character_info["experience"] += 20
                print whiskerworld_text.sheriff_leo_win.format(character_info["name"], character_info["cat type"])
                print whiskerworld_text.sheriff_leo_outro.format(character_info["name"])
            elif character_info["Lion Leo Dice Game"] == False:
                character_info["experience"] += 5
                print whiskerworld_text.sheriff_leo_lose.format(character_info["name"])
                print whiskerworld_text.sheriff_leo_outro.format(character_info["name"])
            
            raw_input("""
    Press ENTER to continue
    >>> """)
    

    # PART 7: Get user outcome from fight with the bandits, store in dictionary, reward experience (follows PARTS 5 or 6)
    if "Dolores Race" in character_info.keys() or "Purryfeather Qs" in character_info.keys():
        print whiskerworld_text.intro_purebred_pass.format(character_info["name"])
        raw_input("""
    Press ENTER to continue
    >>> """)
        print whiskerworld_text.fight_intro
        raw_input("""    
    Press ENTER to continue
    >>> """)
        character_info["Hisstor Fight"] = cat_fight(character_info)
    # PART 8: Reward user for Hisstor Fight, store in dictionary, end of game
    if "Hisstor Fight" in character_info.keys():
        if character_info["Hisstor Fight"] == True:
            character_info["experience"] += 30
            user_western_name = get_western_name(character_info)
            print whiskerworld_text.fight_win_tie_outro.format(character_info["name"], character_info["name"], user_western_name, character_info["name"])
        elif character_info["Hisstor Fight"] == False:
            character_info["experience"] += 10
            print whiskerworld_text.fight_lose_outro.format(character_info["name"], character_info["name"])
        else:
            character_info["experience"] += 20
            user_western_name = get_western_name(character_info)
            print whiskerworld_text.fight_win_tie_outro.format(user_western_name, character_info["name"])
    raw_input("""    
    Press ENTER to continue
    >>> """)
    print whiskerworld_text.final_screen
    

###########################################################################################

play_whiskerworld()
