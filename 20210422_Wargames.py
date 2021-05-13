# 5/1/2021 - "2-player" tic-tac-toe for teddie is nearing completion.  Nothing yet added for AI/computer player.

import random
import time
import sys
sys.path.insert(1, './bubs')
import cursor
import colorama
from colorama import Fore, Back, Style, Cursor, win32, init
from colorama.winterm import WinTerm
from msvcrt import getch, kbhit

board = [
    '   ║   ║   ',
    '═══╬═══╬═══',
    '   ║   ║   ',
    '═══╬═══╬═══',
    '   ║   ║   '
]

vertical = '║'
horizontal = '═'
intersection = '╬'

choose_x = "X"
choose_o = "O"

acceptable_entries_list = [13,27,88,79]   # [enter, Esc, "X", "O"]

arrows_codes_list = [72,80,75,77]   # [up, down, left, right]

board_center_x = 30
board_center_y = 7

sections_list = [
    'upper-left',
    'upper-mid',
    'upper-right',
    'mid-left',
    'center',
    'mid-right',
    'lower-left',
    'lower-mid',
    'lower-right',
    'starting'
]

coords_dict = {
    sections_list[0] : Cursor.POS(board_center_x - 4, board_center_y - 2),
    sections_list[1] : Cursor.POS(board_center_x, board_center_y - 2),
    sections_list[2] : Cursor.POS(board_center_x + 4, board_center_y - 2),
    sections_list[3] : Cursor.POS(board_center_x - 4, board_center_y),
    sections_list[4] : Cursor.POS(board_center_x, board_center_y),
    sections_list[5] : Cursor.POS(board_center_x + 4, board_center_y),
    sections_list[6] : Cursor.POS(board_center_x - 4, board_center_y + 2),
    sections_list[7] : Cursor.POS(board_center_x, board_center_y + 2),
    sections_list[8] : Cursor.POS(board_center_x + 4, board_center_y + 2),
    9 : Cursor.POS(board_center_x -30, board_center_y + 6)
}

play_tracking_dict = {
    sections_list[0] : '',
    sections_list[1] : '',
    sections_list[2] : '',
    sections_list[3] : '',
    sections_list[4] : '',
    sections_list[5] : '',
    sections_list[6] : '',
    sections_list[7] : '',
    sections_list[8] : ''
}

color_lib = {
    1 : Fore.RED + Style.BRIGHT,
    2 : Fore.YELLOW + Style.BRIGHT,
    3 : Fore.GREEN + Style.BRIGHT,
    4 : Fore.CYAN + Style.BRIGHT,
    5 : Fore.BLUE + Style.BRIGHT,
    6 : Fore.MAGENTA + Style.BRIGHT,
    7 : Fore.WHITE + Style.BRIGHT
}

def show_board(color : int):
    print(color_lib[color])  
    print(Cursor.POS(board_center_x - 2,board_center_y - 2) + vertical)
    print(Cursor.POS(board_center_x - 2,board_center_y) + vertical)
    print(Cursor.POS(board_center_x - 2,board_center_y + 2) + vertical)
    print(Cursor.POS(board_center_x + 2,board_center_y - 2) + vertical)
    print(Cursor.POS(board_center_x + 2,board_center_y) + vertical)
    print(Cursor.POS(board_center_x + 2,board_center_y + 2) + vertical)
    print(Cursor.POS(board_center_x - 5,board_center_y - 1) + horizontal)
    print(Cursor.POS(board_center_x - 4,board_center_y - 1) + horizontal)
    print(Cursor.POS(board_center_x - 3,board_center_y - 1) + horizontal)
    print(Cursor.POS(board_center_x - 2,board_center_y - 1) + intersection)
    print(Cursor.POS(board_center_x - 1,board_center_y - 1) + horizontal)
    print(Cursor.POS(board_center_x,board_center_y - 1) + horizontal)
    print(Cursor.POS(board_center_x + 1,board_center_y - 1) + horizontal)
    print(Cursor.POS(board_center_x + 2,board_center_y - 1) + intersection)
    print(Cursor.POS(board_center_x + 3,board_center_y - 1) + horizontal)
    print(Cursor.POS(board_center_x + 4,board_center_y - 1) + horizontal)
    print(Cursor.POS(board_center_x + 5,board_center_y - 1) + horizontal)
    print(Cursor.POS(board_center_x - 5,board_center_y + 1) + horizontal)
    print(Cursor.POS(board_center_x - 4,board_center_y + 1) + horizontal)
    print(Cursor.POS(board_center_x - 3,board_center_y + 1) + horizontal)
    print(Cursor.POS(board_center_x - 2,board_center_y + 1) + intersection)
    print(Cursor.POS(board_center_x - 1,board_center_y + 1) + horizontal)
    print(Cursor.POS(board_center_x,board_center_y + 1) + horizontal)
    print(Cursor.POS(board_center_x + 1,board_center_y + 1) + horizontal)
    print(Cursor.POS(board_center_x + 2,board_center_y + 1) + intersection)
    print(Cursor.POS(board_center_x + 3,board_center_y + 1) + horizontal)
    print(Cursor.POS(board_center_x + 4,board_center_y + 1) + horizontal)
    print(Cursor.POS(board_center_x + 5,board_center_y + 1) + horizontal)

def show_board2(color : int):
    print(color_lib[color])  
    for y in range(0,len(board)):
        print(Cursor.POS(board_center_x - 5,board_center_y - 2 + y) + board[y])
    print()

def show_board3():
    board_color = random.randint(1,6)
    X_color = random.randint(1,6)
    O_color = random.randint(1,6)
    while X_color == board_color:
        X_color = random.randint(1,6)
    while O_color == board_color or O_color == X_color:
        O_color = random.randint(1,6)
    winterm.erase_screen(mode=2)
    show_board2(board_color)
    for mark in range(0,len(play_tracking_dict)):
        if play_tracking_dict[sections_list[mark]] == choose_x:
            print(color_lib[X_color] + coords_dict[sections_list[mark]] + choose_x)
        elif play_tracking_dict[sections_list[mark]] == choose_o:
            print(color_lib[O_color] + coords_dict[sections_list[mark]] + choose_o)

def intro():
    cursor.set_cursor_visible(False)
    time.sleep(0.25)
    for board_cycle in range(1,5):
        temp_board = random.randint(1,6)
        show_board2(temp_board)
        temp_xo = choose_x
        intro_play_tracking = sections_list.copy()
        intro_play_tracking.pop(9)
        for xo_cycle in range(1,10):
            temp_color = random.randint(1,6)
            temp_color_board = random.randint(1,6)
            temp_pos = random.randint(0,len(intro_play_tracking)-1)
            xo_loc = coords_dict[intro_play_tracking[temp_pos]]
            show_board(temp_color_board)
            print(color_lib[temp_color] + xo_loc + temp_xo)
            intro_play_tracking.pop(temp_pos)
            if temp_xo == choose_x:
                temp_xo = choose_o
            else:
                temp_xo = choose_x
            time.sleep(0.075)       
    cursor.set_cursor_visible(True)

def start_cursor():
    print(Cursor.POS(board_center_x - 8,board_center_y - 4), end = "")

def place_cursor(location : int):
    print(coords_dict[sections_list[location]], end = "")

def check_for_win(mark : str) -> bool:
    verdict = False
    if mark == play_tracking_dict[sections_list[0]] and play_tracking_dict[sections_list[0]] == play_tracking_dict[sections_list[1]] and play_tracking_dict[sections_list[0]] == play_tracking_dict[sections_list[2]]:
        verdict = True
    elif mark == play_tracking_dict[sections_list[3]] and play_tracking_dict[sections_list[3]] == play_tracking_dict[sections_list[4]] and play_tracking_dict[sections_list[3]] == play_tracking_dict[sections_list[5]]:
        verdict = True
    elif mark == play_tracking_dict[sections_list[6]] and play_tracking_dict[sections_list[6]] == play_tracking_dict[sections_list[7]] and play_tracking_dict[sections_list[6]] == play_tracking_dict[sections_list[8]]:
        verdict = True
    elif mark == play_tracking_dict[sections_list[0]] and play_tracking_dict[sections_list[0]] == play_tracking_dict[sections_list[3]] and play_tracking_dict[sections_list[0]] == play_tracking_dict[sections_list[6]]:
        verdict = True
    elif mark == play_tracking_dict[sections_list[1]] and play_tracking_dict[sections_list[1]] == play_tracking_dict[sections_list[4]] and play_tracking_dict[sections_list[1]] == play_tracking_dict[sections_list[7]]:
        verdict = True
    elif mark == play_tracking_dict[sections_list[2]] and play_tracking_dict[sections_list[2]] == play_tracking_dict[sections_list[5]] and play_tracking_dict[sections_list[2]] == play_tracking_dict[sections_list[8]]:
        verdict = True
    elif mark == play_tracking_dict[sections_list[0]] and play_tracking_dict[sections_list[0]] == play_tracking_dict[sections_list[4]] and play_tracking_dict[sections_list[0]] == play_tracking_dict[sections_list[8]]:
        verdict = True
    elif mark == play_tracking_dict[sections_list[2]] and play_tracking_dict[sections_list[2]] == play_tracking_dict[sections_list[4]] and play_tracking_dict[sections_list[2]] == play_tracking_dict[sections_list[6]]:
        verdict = True
    return verdict

def add_gap(length : str):
    print(Cursor.POS((board_center_x - 30),(board_center_y + 5)))
    print()
    print()
    print()
    if length == "long":
        print()
        print()
        print()
        print()
        print()

def confirm_input() -> int:
    done = False
    while not done:
        if kbhit():
            key = ord(getch())
            if key == 0 or key == 224:  # 0 for VS code, 224 for DOS window
                key = ord(getch())
                if key in arrows_codes_list:
                    done = True
                else:
                    show_board3()
                    add_gap("long")
                    print("Nice try.  You don't seem to understand how to play tic-tac-toe.")
                    print("How about you stop messing with me and just do it right next time.  For now, you have been black-listed.....")
                    time.sleep(50000)  # This is rude!
                    exit()
            elif key in acceptable_entries_list:
                if key == 27:
                    exit()
                elif key == 13:
                    show_board3()
                    add_gap("long")
                    print(coords_dict[9] + color_lib[3] + 'No, don' + "'" + 't press "enter".  It' + "'" + 's not necessary.')
                    time.sleep(0.1)
                    start_cursor()
                else:
                    done = True
            else:
                show_board3()
                add_gap("short")
                print(coords_dict[9] +"Try again....                            ")
                time.sleep(0.1)
                start_cursor()
    return key

def show_mark(mark : int, square : str, turn : int) -> bool:
    if square in play_tracking_dict:
        if play_tracking_dict[square] == choose_o or play_tracking_dict[square] == choose_x:
            show_board3()
            add_gap("short")
            print('Um.... No, we do not tolerate that sort of behavior here.  Try again')
            verdict = False
        else:
            verdict = True
    else:
        show_board3()
        add_gap("short")
        print("How about let's not place marks outside the playing field.")
        verdict = False
    return verdict

def mark_it_X_dude(mark : str, square : str, turn : int):
    if mark == 88:
        if turn % 2 == 1:
            print(coords_dict[square] + choose_x)
            play_tracking_dict[square] = choose_x
        else:
            show_board3()
            add_gap("short")
            text_color = random.randint(1,6)
            frickin_color = random.randint(1,6)
            while text_color == frickin_color:
                frickin_color = random.randint(1,6)
            print(color_lib[text_color])
            print("Win if you can, Lose if you must, but ALWAYS cheat:  ")
            print('Sigh....  I think you meant to place an "O" right there, in the ' + square + ', so I went ahead and took care of that.')
            print("If I am wrong, too bad, because you're a " + color_lib[frickin_color] + "frickin'" + color_lib[text_color] + " cheater!")
            print(coords_dict[square] + choose_o)
            play_tracking_dict[square] = choose_o
    if mark == 79:
        if turn % 2 == 0:
            print(coords_dict[square] + choose_o)
            play_tracking_dict[square] = choose_o           
        else:
            show_board3()
            add_gap("short")
            text_color = random.randint(1,6)
            frickin_color = random.randint(1,6)
            while text_color == frickin_color:
                frickin_color = random.randint(1,6)
            print(color_lib[text_color])
            print("Win if you can, Lose if you must, but ALWAYS cheat:  ")
            print('Sigh....  I think you meant to place an "X" right there, in the ' + square + ', so I went ahead and took care of that.')
            print("If I am wrong, too bad, because you're a " + color_lib[frickin_color] + "frickin'" + color_lib[text_color] + " cheater!")
            print(coords_dict[square] + choose_x)
            play_tracking_dict[square] = choose_x

def winner(player : str):
    x_winner = [
        'XXXXXX    XXXXXX     WWWWW   W   WWWWW   IIIIIIIIIIII   NNN      NNNN     SSSSSSSSSS    !!!!',
        '  XXX      XXX        WWW    W    WWW       IIPPII      NNNNN    NNN     SSSS      SS   !!!!',
        '   XXX    XXX         WWW   WWW   WWW        IEEI       NNNNNN   NNN    SSSS            !!!!',
        '      XXXX             WW   WWW   WW         INNI       NNN NNN  NNN     SSSSSSSSSSS    !!!!',
        '   XXX    XXX           WW  WWW  WW          IIII       NNN  NNN NNN             SSSS   !!!!',
        '  XXX      XXX           WWWW WWWW          IISSII      NNN   NNNNNN    SS      SSSS        ',
        'XXXXXX    XXXXXX          WW   WW        IIIIIIIIIIII  NNNN     NNNN     SSSSSSSSSS     !!!!'
    ]

    o_winner = [
        '    OOOOOOOO          WWWWW   W   WWWWW   IIIIIIIIIIII   NNN      NNNN     SSSSSSSSSS    !!!!',
        '  OOOO    OOOO         WWW    W    WWW       IIPPII      NNNNN    NNN     SSSS      SS   !!!!',
        ' OOO        OOO        WWW   WWW   WWW        IEEI       NNNNNN   NNN    SSSS            !!!!',
        'OOO    OO    OOO        WW   WWW   WW         INNI       NNN NNN  NNN     SSSSSSSSSSS    !!!!',
        ' OOO        OOO          WW  WWW  WW          IIII       NNN  NNN NNN             SSSS   !!!!',
        '  OOOO    OOOO            WWWW WWWW          IISSII      NNN   NNNNNN    SS      SSSS        ',
        '    OOOOOOOO               WW   WW        IIIIIIIIIIII  NNNN     NNNN     SSSSSSSSSS     !!!!'
    ]

    if player == choose_x:
        winner = x_winner
    else:
        winner = o_winner
    cursor.set_cursor_visible(False)
    time.sleep(0.5)
    winterm.erase_screen(mode=2)
    for cycles in range (1,4):
        for colors in range (1,7):
            print(color_lib[colors])
            x = 25
            y = 10
            print(Cursor.POS(x,y))
            for line in winner:
                print(line)
                scroll_speed = random.randint(25,50)
                time.sleep(scroll_speed / 10000000.0)
    cursor.set_cursor_visible(True)
    print(color_lib[7])
    winterm.erase_screen(mode=2)



def move_cursor(d_erection : str, start_pt : str) -> str:
    if start_pt == sections_list[9]:
        if d_erection == arrows_codes_list[0]:
            place_cursor(8)
            location = sections_list[8]
        elif d_erection == arrows_codes_list[1]:
            place_cursor(0)
            location = sections_list[0]
        elif d_erection == arrows_codes_list[2]:
            place_cursor(2)
            location = sections_list[2]
        elif d_erection == arrows_codes_list[3]:
            place_cursor(0)
            location = sections_list[0]
    elif start_pt == sections_list[0]:
        if d_erection == arrows_codes_list[0]:
            place_cursor(6)
            location = sections_list[6]
        elif d_erection == arrows_codes_list[1]:
            place_cursor(3)
            location = sections_list[3]
        elif d_erection == arrows_codes_list[2]:
            place_cursor(2)
            location = sections_list[2]
        elif d_erection == arrows_codes_list[3]:
            place_cursor(1)
            location = sections_list[1]
    elif start_pt == sections_list[1]:
        if d_erection == arrows_codes_list[0]:
            place_cursor(7)
            location = sections_list[7]
        elif d_erection == arrows_codes_list[1]:
            place_cursor(4)
            location = sections_list[4]
        elif d_erection == arrows_codes_list[2]:
            place_cursor(0)
            location = sections_list[0]
        elif d_erection == arrows_codes_list[3]:
            place_cursor(2)
            location = sections_list[2]
    elif start_pt == sections_list[2]:
        if d_erection == arrows_codes_list[0]:
            place_cursor(8)
            location = sections_list[8]
        elif d_erection == arrows_codes_list[1]:
            place_cursor(5)
            location = sections_list[5]
        elif d_erection == arrows_codes_list[2]:
            place_cursor(1)
            location = sections_list[1]
        elif d_erection == arrows_codes_list[3]:
            place_cursor(0)
            location = sections_list[0]
    elif start_pt == sections_list[3]:
        if d_erection == arrows_codes_list[0]:
            place_cursor(0)
            location = sections_list[0]
        elif d_erection == arrows_codes_list[1]:
            place_cursor(6)
            location = sections_list[6]
        elif d_erection == arrows_codes_list[2]:
            place_cursor(5)
            location = sections_list[5]
        elif d_erection == arrows_codes_list[3]:
            place_cursor(4)
            location = sections_list[4]
    elif start_pt == sections_list[4]:
        if d_erection == arrows_codes_list[0]:
            place_cursor(1)
            location = sections_list[1]
        elif d_erection == arrows_codes_list[1]:
            place_cursor(7)
            location = sections_list[7]
        elif d_erection == arrows_codes_list[2]:
            place_cursor(3)
            location = sections_list[3]
        elif d_erection == arrows_codes_list[3]:
            place_cursor(5)
            location = sections_list[5]
    elif start_pt == sections_list[5]:
        if d_erection == arrows_codes_list[0]:
            place_cursor(2)
            location = sections_list[2]
        elif d_erection == arrows_codes_list[1]:
            place_cursor(8)
            location = sections_list[8]
        elif d_erection == arrows_codes_list[2]:
            place_cursor(4)
            location = sections_list[4]
        elif d_erection == arrows_codes_list[3]:
            place_cursor(3)
            location = sections_list[3]
    elif start_pt == sections_list[6]:
        if d_erection == arrows_codes_list[0]:
            place_cursor(3)
            location = sections_list[3]
        elif d_erection == arrows_codes_list[1]:
            place_cursor(0)
            location = sections_list[0]
        elif d_erection == arrows_codes_list[2]:
            place_cursor(8)
            location = sections_list[8]
        elif d_erection == arrows_codes_list[3]:
            place_cursor(7)
            location = sections_list[7]
    elif start_pt == sections_list[7]:
        if d_erection == arrows_codes_list[0]:
            place_cursor(4)
            location = sections_list[4]
        elif d_erection == arrows_codes_list[1]:
            place_cursor(1)
            location = sections_list[1]
        elif d_erection == arrows_codes_list[2]:
            place_cursor(6)
            location = sections_list[6]
        elif d_erection == arrows_codes_list[3]:
            place_cursor(8)
            location = sections_list[8]
    elif start_pt == sections_list[8]:
        if d_erection == arrows_codes_list[0]:
            place_cursor(5)
            location = sections_list[5]
        elif d_erection == arrows_codes_list[1]:
            place_cursor(2)
            location = sections_list[2]
        elif d_erection == arrows_codes_list[2]:
            place_cursor(7)
            location = sections_list[7]
        elif d_erection == arrows_codes_list[3]:
            place_cursor(6)
            location = sections_list[6]
    return location

def game_play():
    turn = 1
    show_board2(7)
    location = sections_list[9]
    while turn < 10 and check_for_win(choose_x) == False and check_for_win(choose_o) == False:  # set turns to 10 when ready to play
        good = False
        get_input = confirm_input()
        board_color = random.randint(1,6)
        show_board(board_color)
        if get_input in arrows_codes_list:
            location = move_cursor(get_input, location)
        else:
            good = show_mark(get_input, location, turn)
        if good:
            show_board3()
            mark_it_X_dude(get_input, location, turn)
            turn += 1
    if check_for_win(choose_x) == True:
        winner(choose_x)
        show_board3()
    elif check_for_win(choose_o) == True:
        winner(choose_o)
        show_board3()
    else:
        show_board3()
        add_gap("short")
        print("You tied.  What losers.")        


init() # this makes sure the graphics work correctly in DOS windows
winterm = WinTerm()  # enables the next line
winterm.erase_screen(mode=2) # this clears the screen, but doesn't actually "erase" anything


intro()
add_gap("short")
print()
print()
print("Welcome to Teddie's Tic-Tac-Toe, a game for all to enjoy")
print("All are quite welcome here.")
print("Let the game commence!")
time.sleep(2)
game_play()
add_gap("short")
replay = input('Would you like to play again?  ').upper()
if replay == "YES" or replay == "Y":
    while replay == "YES" or replay == "Y":
        play_tracking_dict = {
        sections_list[0] : '',
        sections_list[1] : '',
        sections_list[2] : '',
        sections_list[3] : '',
        sections_list[4] : '',
        sections_list[5] : '',
        sections_list[6] : '',
        sections_list[7] : '',
        sections_list[8] : ''
        }

        game_play()
        replay = input("Again?  ").upper()
add_gap("short")

exit()

