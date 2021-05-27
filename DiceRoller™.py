
import random
import time
import sys
sys.path.insert(1, './bubs')
import cursor
import colorama
from colorama import Fore, Back, Style, Cursor, win32, init
from colorama.winterm import WinTerm


dice_number = 5

dice_indent = 30 # dice x-indent 25
dice_spacing = 12 # dice separation (x)
y_indent = 8 # dice y-indent 8
x_centering = 31 # for name/roll# 26
y_drop = 7 # for name/roll# 7
centering = 51 # secondary centering for dice player number presentation 

category_list = ['Ones','Twos','Threes','Fours','Fives','Sixes','3-of-a-Kind','4-of-a-Kind','Fullhouse','Small Straight','Large Straight','Yahtzee®','Chance']

category_dict = {
        0 : 'Ones',
        1 : 'Twos',
        2 : 'Threes',
        3 : 'Fours',
        4 : 'Fives',
        5 : 'Sixes',
        6 : '3-of-a-Kind',
        7 : '4-of-a-Kind',
        8 : 'Fullhouse',
        9 : 'Small Straight',
        10 : 'Large Straight',
        11 : 'Yahtzee®',
        12 : 'Chance'
    }

def roll_the_dice(rolls : int, roll_list : list, reroll_list : list) -> list:
    if roll_list == [] and reroll_list == []:
        for i in range (0,dice_number):
            roll_list.append(random.randint(1,6))
        # roll_list = [1,1,1,1,1] # Manual control of starting dice values
    else:
        reroll_num = len(reroll_list)
        for i in range (0,reroll_num):
            j = int(reroll_list[i])
            roll_list[j-1] = random.randint(1,6)
        # roll_list = [2,2,2,2,2] # Manual control of reroll dice values
    # roll_list = [3,3,3,3,3] # Manual control of set dice values
    return roll_list

def count_numbers(roll_list : list) -> list:
    number_count_list = []
    for x in range(1,7):
        value = roll_list.count(x)
        number_count_list.append(value)
    return number_count_list

def numbers_test(roll : list) -> list:
    numbers_test_results = []
    counted = count_numbers(roll)
    for x in range(0,6):
        if counted[x] > 0:
            numbers_test_results.append(1)
        else:
            numbers_test_results.append(0)
    return numbers_test_results

def three_uva_test(roll_list : list) -> bool:
    number_count = count_numbers(roll_list)
    for i in range(0,6):
        if number_count[i] >= 3:
            return 1

def four_uva_test(roll_list : list) -> bool:
    number_count = count_numbers(roll_list)
    for i in range(0,6):
        if number_count[i] >= 4:
            return 1

def fullhouse_test(roll_list : list) -> bool:
    if three_uva_test(roll_list):
        sorted_roll_list = sorted(roll_list)
        the3 = sorted_roll_list[2]
        i = 1
        while i <= 3:
            index = sorted_roll_list.index(the3)
            sorted_roll_list.pop(index)
            i += 1
        if sorted_roll_list[0] == sorted_roll_list[1] and the3 != sorted_roll_list[0]:
            return 1
        else:
            return 0
    else:
        return 0

def sml_str_test(roll_list : list) -> bool:
    if lg_str_test(roll_list):
        return 1
    roll_list = sorted(roll_list)
    if roll_list == [1,2,3,4,6] or roll_list == [1,3,4,5,6]:
        return 1
    for i in range (1,7):
        if roll_list.count(i) > 1:
            roll_list.remove(i)
    if roll_list == [1,2,3,4] or roll_list == [2,3,4,5] or roll_list == [3,4,5,6]:
        return 1
    return 0

def lg_str_test(roll_list : list) -> bool:
    sorted_roll_list = sorted(roll_list)
    if sorted_roll_list == [1,2,3,4,5] or sorted_roll_list == [2,3,4,5,6]:
        return 1
    else:
        return 0

def yahtzee_test(roll_list : list) -> bool:
    number_count = count_numbers(roll_list)
    for i in range(0,6):
        if number_count[i] == 5:
            return 1
    return 0

def setup_dice_numbers(delay : float):
    time.sleep(delay)
    indent = int(dice_indent + 2)
    for i in range(0,dice_number):
        x = indent + (dice_spacing * i)
        y = y_indent + 6
        print(Cursor.POS(x,y) + str(i + 1))
        time.sleep(delay)

dice_graphic = ['╔═══╗','║   ║','╚═══╝']

def setup_dice():
    for x in range(0,dice_number):
        print(Cursor.POS((dice_indent + (dice_spacing * x)),(y_indent + 2)) + dice_graphic[0], end='')
        print(Cursor.POS((dice_indent + (dice_spacing * x)),(y_indent + 3)) + dice_graphic[1], end='')
        print(Cursor.POS((dice_indent + (dice_spacing * x)),(y_indent + 4)) + dice_graphic[2], end='')

color_lib = {
    1 : Fore.RED + Style.BRIGHT,
    2 : Fore.YELLOW + Style.BRIGHT,
    3 : Fore.GREEN + Style.BRIGHT,
    4 : Fore.CYAN + Style.BRIGHT,
    5 : Fore.BLUE + Style.BRIGHT,
    6 : Fore.MAGENTA + Style.BRIGHT
}

def rolling_animation(roll : list, reroll_list : list):
    if reroll_list == []:
        roll = []
        rotations = random.randint(15,20)
        for spins in range (0,rotations):
            for rolls in range (0,dice_number):
                roll.append(random.randint(1,6))
            show_roll(roll, 0.0125)
            roll = []
    else:
        temp_roll = roll.copy()
        reroll_count = len(reroll_list)
        rotes = random.randint(15,20)
        for spins in range (0, rotes):
            for i in range (0,reroll_count):
                j = int(reroll_list[i])
                temp_roll[j-1] = random.randint(1,6)
            show_roll(temp_roll, 0.0125)

def show_roll(roll : list, pause : float):
    for x in range(0,dice_number):
        print(color_lib[roll[x]] + Cursor.POS((dice_indent + (dice_spacing * x)),(y_indent + 2)) + dice_graphic[0], end='')
        print(color_lib[roll[x]] + Cursor.POS((dice_indent + (dice_spacing * x)),(y_indent + 3)) + dice_graphic[1], end='')
        print(color_lib[roll[x]] + Cursor.POS((dice_indent + (dice_spacing * x)),(y_indent + 4)) + dice_graphic[2], end='')
        print(color_lib[roll[x]] + Cursor.POS((dice_indent + 2 + (dice_spacing * x)),(y_indent + 3)) + str(roll[x]), end='')
        time.sleep(pause)
    print(Fore.WHITE)


def test_categories(analyze_me : list) -> list:
    categories_summary = []
    numbers_results = numbers_test(analyze_me)
    for num in range(0,6):
        result = numbers_results[num]
        if result == 1:
            categories_summary.append(category_dict[num])
    if three_uva_test(analyze_me):
        categories_summary.append(category_dict[6])
    if four_uva_test(analyze_me):
        categories_summary.append(category_dict[7])
    if fullhouse_test(analyze_me):
        categories_summary.append(category_dict[8])
    if sml_str_test(analyze_me):
        categories_summary.append(category_dict[9])
    if lg_str_test(analyze_me):
        categories_summary.append(category_dict[10])
    if yahtzee_test(analyze_me):
        categories_summary.append(category_dict[11])
    categories_summary.append(category_dict[12])
    return categories_summary

def test_choice(choice : str, roll : list, player, roll_num : int, reroll_list : list) -> str:  
    if choice not in category_list:
        while choice not in category_list:
            print()
            print()
            print('Can you hear the lava bubbling?')
            time.sleep(2)
            winterm.erase_screen(mode=2)
            print()
            present_dice(player, roll, roll_num, reroll_list,False)
            print()
            print()
            print('You maroon.  Try again.  This time, use your brain (if you can find it)')
            choice = input('Use the exact same spelling, capitalization and symbols:  ')
    filtered_response = choice
    return filtered_response

def calc_score(roll_list : list, category : str) -> int:
    number_count_list = count_numbers(roll_list)
    scoring_lib = {
        category_dict[0] : number_count_list[0] * 1,
        category_dict[1] : number_count_list[1] * 2,
        category_dict[2] : number_count_list[2] * 3,
        category_dict[3] : number_count_list[3] * 4,
        category_dict[4] : number_count_list[4] * 5,
        category_dict[5] : number_count_list[5] * 6,
        category_dict[6] : sum(roll_list),
        category_dict[7] : sum(roll_list),
        category_dict[8] : 25,
        category_dict[9] : 30,
        category_dict[10] : 40,
        category_dict[11] : 50,
        category_dict[12] : sum(roll_list)
    }
    if category not in test_categories(roll_list):
        score = 0
    else:
        score = scoring_lib[category]
    return score

def yahtzee_check(roll : list) -> list:
    print()
    print("Um... are you sure you want to do that?  You have a playable Yahtzee® you know...")
    print()
    double_check = (input("Last chance; are you going to drop your rerolls, instead, like a good Boi, or not?  ")).upper()
    if double_check == "Y" or double_check == "YES":
        reroll_list = []
    else:
        reroll_list = roll
    time.sleep(0.3)
    return reroll_list

def yahtzee_score(player) -> int:
    try:
        yachtz_score = player.get_category_score("Yahtzee®")
        return yachtz_score
    except (KeyError):
        return 1

def present_dice(player, current_roll : list, roll_num : int, reroll_list : list, show_animation : bool):
    roll = current_roll.copy()
    cursor.set_cursor_visible(False)
    if roll_num == 1:
        x_centering = 31
        y_drop = 7
        if show_animation:
            setup_dice_numbers(0.15)
        else:
            setup_dice_numbers(0)
        setup_dice()
        print(color_lib[3] + Style.BRIGHT + Cursor.POS(x_centering,y_drop) + (player.get_name() + ":  Roll #1").center(centering))
    else:
        x_centering = 31
        y_drop = 7
        setup_dice_numbers(0)
        if roll_num == 2:
            print(color_lib[2] + Style.BRIGHT + Cursor.POS(x_centering,y_drop) + (player.get_name() + ":  Roll #2").center(centering))
        else:
            print(color_lib[1] + Style.BRIGHT + Cursor.POS(x_centering,y_drop) + (player.get_name() + ":  Roll #3").center(centering))
    if show_animation:
        rolling_animation(roll, reroll_list)
    if show_animation:
        show_roll(roll, 0.025)
    else:
        show_roll(roll,0)
    if show_animation and yahtzee_score(player) > 0 and yahtzee_test(roll) == 1:
        excited()
        setup_dice_numbers(0)
        show_roll(roll,0)
    player.display_score()
    cursor.set_cursor_visible(True)

def bonus():
    just_got_bonus = [
        'BBBBBBBBBB          OOOOOO       NNNN     NNNNN   UUU       UUUUU      SSSSSSSSSS     !!!!  ',
        '  BBB    BBB      OOO    OOO     NNNNN    NNN     UUU       UUU      SSSSSS     SS    !!!!  ',
        '  BBB     BBB    OOO      OOO    NNNNNN   NNN     UUU       UUU     SSSS              !!!!  ',
        '  BBBBBBBBBB    OOO   OO   OOO   NNN NNN  NNN     UUU       UUU      SSSSSSSS         !!!!  ',
        '  BBB     BBB    OOO      OOO    NNN  NNN NNN     UUU       UUU          SSSSSSS      !!!!  ',
        '  BBB    BBB      OOO    OOO     NNN   NNNNNN      UUUU    UUUU     SS      SSSSS           ',
        ' BBBBBBBBB          OOOOOO     NNNNN    NNNNN        UUUUUUUU UU     SSSSSSSSSSS      !!!!  '
    ]
    time.sleep(0.5)
    winterm.erase_screen(mode=2)
    for cycles in range (1,3):
        for colors in range (1,7):
            print(color_lib[colors])
            x = 25
            y = 10
            print(Cursor.POS(x,y))
            for line in just_got_bonus:
                print(line)
                scroll_speed = random.randint(25,50)
                time.sleep(scroll_speed / 10000000.0)
    print(Fore.WHITE)
    winterm.erase_screen(mode=2)

def excited():
    celebrate = [
    'YYYYY   YYYYY     AAA       HHHH   HHHH   TTTTTTTTTTT    ZZZZZZZZZZZZZ    EEEEEEEEEE     EEEEEEEEEE ',
    '  YYY   YYY     AAA AAA      HHH   HHH   TT  TTTTT  TT   ZZZ     ZZZZ    EEEEEE    EE   EEEEEE    EE',
    '   YYY YYY     AAA   AAA     HHH   HHH   T    TTT    T   Z      ZZZZ     EEE            EEE         ',
    '    YYYYY      AAAAAAAAA     HHHHHHHHH        TTT              ZZZZ       EEEEEEEEE      EEEEEEEEE  ',
    '     YYY       AAA   AAA     HHH   HHH        TTT            ZZZZ    Z   EEE            EEE         ',
    '     YYY       AAA   AAA     HHH   HHH        TTT          ZZZZ    ZZZ   EEEEE     EE   EEEEE     EE',
    '    YYYYY     AAAA   AAAA   HHHH   HHHH       TTT        ZZZZZZZZZZZZZ    EEEEEEEEEE     EEEEEEEEEE '
    ]
    time.sleep(0.5)
    winterm.erase_screen(mode=2)
    for cycles in range (1,6):
        for colors in range (1,7):
            print(color_lib[colors])
            x = 25
            y = 10
            print(Cursor.POS(x,y))
            for line in celebrate:
                print(line)
                scroll_speed = random.randint(25,50)
                time.sleep(scroll_speed / 10000000.0)
    print(Fore.WHITE)
    winterm.erase_screen(mode=2)

def reroll_check(roll : list, reroll : list) -> bool:
    list_length = len(reroll)
    ok_nums = ['1','2','3','4','5']
    check_2 = []
    for i in range(0,list_length):
        if reroll[i] in ok_nums:
            if check_2.count(reroll[i]) > 0:
                return 0
            else:
                check_2.append(reroll[i])

        else:
            return 0
    return 1

def reroll_func(roll : list):
    print()
    print()
    print("Which dice would you like rerolled?  Type only dice numbers (1 - 5). No letters nor symbols nor punctuation or spaces, or you're screwed.")
    reroll_list = list(input("For example, type '135' to reroll dice numbers 1, 3 and 5 (Leave blank if none).  Press Enter when satisfied:  "))
    reroll_length = len(reroll_list)
    while reroll_check(roll, reroll_list) == 0 or reroll_length > dice_number:
        print()
        print()
        print("What's wrong with you1?  This is very simple and very straightforward.  There are 5 dice.  They were presented above.")
        print("All you have to do, is type in the numbers corresponding to the dice you'd like to re-roll.")
        reroll_list = list(input("Which dice would you like to reroll?  Type only numbers; no letters, no symbols, no punctuation, no friggin' spaces; just NUMBERS:  "))
        reroll_length = len(reroll_list)
    return reroll_list

def extra_yahtzee_score_func(player, roll : list):
    if yahtzee_test(roll) and yahtzee_score(player) == 50:
        return 1
    else:
        return 0

def take_your_turn(player_list : list, rounds : int):
    player_list_length = int(len(player_list))
    for turn in range(0,player_list_length):
        winterm.erase_screen(mode=2)
        player = player_list[turn]
        reroll_list = []
        print("Looks like it's " + str(player.get_name()) + "'s turn:  ")
        first_roll = roll_the_dice(dice_number, [], [])
        roll_num = 1
        present_dice(player, first_roll, roll_num, reroll_list, True)
        reroll_list = reroll_func(first_roll)
        roll = first_roll.copy()
        if reroll_list != []:
            if yahtzee_test(roll) == 1:
                if yahtzee_score(player) == 1:
                    reroll_list = yahtzee_check(reroll_list)  
                else:
                    if player.get_category_score('Yahtzee®') != 0:
                        reroll_list = yahtzee_check(reroll_list)
            if reroll_list != []:
                winterm.erase_screen(mode=2)
                second_roll = roll_the_dice(dice_number, first_roll, reroll_list)
                roll_num = 2
                present_dice(player, second_roll, roll_num, reroll_list, True)
                reroll_list = reroll_func(second_roll)
                roll = second_roll.copy()
                if reroll_list != []:
                    if yahtzee_test(roll) == 1:
                        if yahtzee_score(player) > 0:
                            reroll_list = yahtzee_check(reroll_list)
                        else:
                            if player.get_category_score('Yahtzee®') != 0:
                                reroll_list = yahtzee_check(reroll_list)
                    if reroll_list != []:
                        if roll_num == 2:
                            winterm.erase_screen(mode=2)
                            third_roll = roll_the_dice(dice_number, second_roll, reroll_list)
                            roll_num = 3
                            present_dice(player, third_roll, roll_num, reroll_list, True)
                            roll = third_roll.copy()
        print()
        print()
        print("Which category do you choose?")
        print("Must be typed EXACTLY as presented here")
        print()
        choose_category = input("If you don't choose one from the above, Ima douse you in lava like a Wandering Trader and watch you melt before my eyes:  ")
        confirmed_choice = test_choice(choose_category, roll, player, roll_num, reroll_list)
        secondary_confirmed_choice = player.check_category(confirmed_choice, roll, roll_num, reroll_list)
        if yahtzee_test(roll) == 1 and secondary_confirmed_choice != "Yahtzee®" and "Yahtzee®" not in player.score_sheet:
            print()
            change = input("Wow!  I cannot believe you're choosing to not score a yahtzee.  You sure?  ").upper()
            if change != "YES" and change != "Y":
                print()
                choose_yahtzee = input("I'll take your cryptic response as a 'No'.  A wise choice, indeed.  So are we choosing Yahtzee® then?  ").upper()
                if choose_yahtzee == "YES" or choose_yahtzee == "Y":
                    secondary_confirmed_choice = category_dict[11]
                else:
                    time.sleep(0.5)
                    print()
                    print("I just give up on you...")
                    time.sleep(1)
        extra_yahtzee_confirmation = extra_yahtzee_score_func(player,roll)
        if extra_yahtzee_confirmation:
            player.set_extra_yahtzee_counter()
            extra_yahtzee_score_display = extra_yahtzee_points
        else:
            extra_yahtzee_score_display = 0
        score = calc_score(roll, secondary_confirmed_choice)
        print()
        print()
        player.set_score(roll,secondary_confirmed_choice)
        if player.upper_total() >= 63:
            if player.have_bonus == False:
                cursor.set_cursor_visible(False)
                bonus()
                cursor.set_cursor_visible(True)
                print()
                print()
            player.set_bonus()        
        if extra_yahtzee_score_display == 100:
            print(str(secondary_confirmed_choice) + ':  ' + str(player.score_sheet[secondary_confirmed_choice]) + ' + ' + str(extra_yahtzee_score_display))
        else:
            print(str(secondary_confirmed_choice) + ':  ' + str(player.score_sheet[secondary_confirmed_choice]))
        missed_yahtzee = yahtzee_score(player)
        if missed_yahtzee != 1:
            if (yahtzee_test(roll) == 1) and (player.get_category_score("Yahtzee®") == 0):
                time.sleep(2)
                print()
                print("Hahahahahahaha!!!  You just missed out on a Yahtzee®.  I bet you feel really dumb right now.  HA-HA!!")
                time.sleep(3)
        time.sleep(2)

def show_final_scores(player_list : list):
    for summary in player_list:
        winterm.erase_screen(mode=2)
        player = player_list[summary]
        print(str(player.get_name()) + "'s Summary:  ")
        print()
        print()
        player.display_score()
        print()
        pause = input("Press Enter to continue:  ")

def start_game(player_list : list):
    for rounds in range(0,13):
        take_your_turn(player_list, rounds)
    show_final_scores(player_list)
    player_length = len(player_list)
    if player_length > 1:
        winterm.erase_screen(mode=2)
        player_score_dict = {}
        print()
        for i in range(0,player_length):
            player = player_list[i]
            player_score_dict[player] = player.get_total()
            print(player.get_name() + ":  " + str(player_score_dict[player]))
            print()
        temp = input("Press Enter to continue")
        winterm.erase_screen(mode=2)
        print("And the winner is:  ")
        time.sleep(0.75)
        print()
        print("Drum Roll!")
        time.sleep(1)
        name = "NOT Bubba!!! NEVERRRRRRR!!!!!!"
        cursor.set_cursor_visible(False)
        for cycle in range(1,20):
            for color in range(1,6):
                print(color_lib[color] + Cursor.POS(40,20) + str(name))
                time.sleep(0.075)
        cursor.set_cursor_visible(True)
        

low_category_score = [
        "You really botched that one now, didn'tcha...",
        "That is pathetic.",
        "Is that the best you can do?",
        "Don't think I've ever seen this low a score for this category...",
        "This makes me think you don't understand how to play this game...",
        "That really sucked the high-tit...",        
        ]

low_overall_score = [
        "How is a score this low even possible?", #insults for below 180
        "This ain't golf ya know.....",
        "The object of the game was to get a high score.  Dumbass.",
        "Well that whole game was just one giant bevulf...",
        "Ok, be honest; were you even trying?",
        "You should consider playing a different game..."
        ]

single_player_insults = [
        "You have no friends.",
        "One?  Really?  What a loser!",
        "Maybe next time, get your imaginary friend to join you...",
        "Who plays DiceRoller™ solo?!"
        ]

name_insults = [
        "Really?  Wow, school must have sucked for you...  ",
        "What kind of stupid name is that?  ",
        "You should consider a name change...  ",
        "I'm sorry; what?  That name is so stupid I can't believe my ears...  ",
        "No, comeon; that name is too stupid.  What is it for real?  ",
        "Boring.  Such a boring name...  ",
        "I'm so sorry... did your parents hate you or something?  "
        ]

cool_names = ["Ted", "Theodore", "T-Bone", "T-Bear", "Teddy", "Teddie", "Robert", "Brandon", "Teddy-B"]

extra_yahtzee_points = 100

class scoresheet:

    # Designed to store scores for the DiceRoller™ player

    def __init__ (self, name):
        self.name = name
        self.score_sheet = {}
        self.yachtz_counter = 0
        self.have_bonus = False

    def get_name(self) -> str:
        return self.name
    
    def set_score(self, roll_list : list, choice : str) -> dict:
        category_score = calc_score(roll_list, choice)
        self.score_sheet[choice] = category_score
    
    def set_extra_yahtzee_counter(self):
        self.yachtz_counter += 1
    
    def check_categories(self, cateegory):
        verdict = False
        try:
            if self.score_sheet[cateegory] > -1:
                verdict = True
            return (verdict)
        except (KeyError):
            return verdict
    
    def upper_total(self):
        upper_tot = 0
        for cat in range(0,6):
            checking_category = category_dict[cat]
            check = self.check_categories(checking_category)
            if check:
                cat_score = self.score_sheet[category_dict[cat]]
                upper_tot += cat_score
        # upper_tot = 63 # for testing bonus
        return upper_tot

    def set_bonus(self):
        self.have_bonus = True

    def get_total(self) -> int:
        numbers_total = 0
        lower_total = 0
        for i in range(0,6):
            category = category_dict[i]
            numbers_total += self.score_sheet[category]
        if numbers_total >= 63:
            bonus = 35
        else:
            bonus = 0
        for i in range(6,13):
            category = category_dict[i]
            lower_total += self.score_sheet[category]
        extra_yahtzee_score = extra_yahtzee_points * self.yachtz_counter
        total = int(numbers_total + bonus + lower_total + extra_yahtzee_score)
        return total
    
    def display_score(self):
        numbers_total = 0
        for i in range(0,6):
            category = category_dict[i]
            if category in self.score_sheet:
                numbers_total += self.score_sheet[category]
                print("│" + str(category) + ":  " + str(self.score_sheet[category]))
            else:
                print("│" + str(category) + ":  ")
        if numbers_total >= 63:
            bonus = 35
        else:
            bonus = 0
        print(color_lib[6] + "┌─────────────────────────┐")
        print('│ "Numbers" Total:  ' + str(numbers_total))
        print("│ Category Bonus(≥63):  " + str(bonus))
        print('│ "Upper" Total:  ' + str(numbers_total + bonus))
        print("└─────────────────────────┘" + Fore.WHITE)
        lower_total = 0
        for i in range(6,13):
            category = category_dict[i]
            if category in self.score_sheet:
                print("│" + str(category) + ":  " + str(self.score_sheet[category]))
                lower_total += self.score_sheet[category]
            else:
                print("│" + str(category) + ":  ")
        extra_yahtzee_score = extra_yahtzee_points * self.yachtz_counter
        print(color_lib[3] + "╔═════════════════════════╗")
        print('║ "Upper" Total:  ' + str(numbers_total + bonus))
        print('║ "Lower" Total:  ' + str(lower_total))
        print('║ Extra Yahtzee® Pts:  ' + str(extra_yahtzee_score))
        print('║ Grand Total:  ' + str(numbers_total + bonus + lower_total + extra_yahtzee_score))
        print("╚═════════════════════════╝" + Fore.WHITE)
    
    def check_category(self, category : str, testing_roll : list, roll_num : int, reroll_list : list) -> str:
        for i in range(0,13):
            if category in self.score_sheet:
                while category in self.score_sheet:
                    print()
                    category = input("That category has already been used.  Try again, " + self.get_name() + ":  ")
                    category = test_choice(category, testing_roll, self, roll_num, reroll_list)
        return category

    def get_category_score(self, category : str) -> int:
        category_score = self.score_sheet[category]
        return category_score

def get_player_total(attempt : int) -> int:
    try:
        if attempt == 1:
            player_total = int(input("How many y'all playin'?  "))
            if player_total < 1:
                print()
                print("Don't waste my time.")
                print()
                exit()               
        else:
            print()
            print("That's just too damn many people; trust me, it's not worth it.")
            print("Again, how many y'all playin'?  I won't ask again:  ")
            time.sleep(1)
            print()
            player_total = int(input("Again, how many y'all playin'?  Try not to drool on yourself when you answer....  "))
    except (ValueError):
        player_total = 'reaquire'
        while player_total == 'reaquire':
            print()
            print("Not starting things out on the right foot, now are we.")
            try:
                print()
                player_total = int(input("Let's try this again:  How many players y'all have on this fine day?  "))
            except (ValueError):
                player_total = 'reaquire'
    return player_total

                                                                                 # Processing begins right here:

init() # this makes sure the graphics work correctly in DOS windows
winterm = WinTerm()  # enables the next line
winterm.erase_screen(mode=2) # this clears the screen, but doesn't actually "erase" anything

print()
print()
player_dict = {}
player_total = get_player_total(1)
if player_total == 1:
    print()
    single_length = len(single_player_insults)
    single_insult = single_player_insults[random.randint(0,single_length-1)]
    print(single_insult)
    time.sleep(1.75)
if player_total > 5:
    player_total = get_player_total(2)
    if player_total > 5:
        print()
        print("Ok.  I warned you.  Tell your families you'll see them at the end of the year....")
        time.sleep(1.5)
for i in range (0,player_total):
    print()
    player_dict[i] = scoresheet(input("Alrighty then.  Player " + str(i + 1) + ", what's your name?  "))
    if player_dict[i].get_name() not in cool_names:
        insult_list_length = len(name_insults)
        insult = name_insults[random.randint(0,insult_list_length-1)]
        print()
        print(insult)
        time.sleep(1.75)
        print()
        print("Ok...  " + str(player_dict[i].get_name()) + "...." )
        time.sleep(1.75)

start_game(player_dict)
exit()

