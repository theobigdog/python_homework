#   Use recursion to calculate factorial for a number
#   Use recursion to calculate a fibonacci number

import time
import colorama
from colorama import Fore, Back, Style, Cursor, win32, init
from colorama.winterm import WinTerm

choices = ["factorial","Fibonacci"]

factorial_list = []

Fibonacci_list = ['0','1']

def which_type() -> str:
    calc_type = None
    while calc_type not in choices:
        print()
        print("So here are your rather limited choices.  I know.  Deal with it.")
        calc_type = input('Would you prefer to calculate a factorial, or a Fibonacci value?  ')
        if calc_type not in choices:
            print()
            calc_type = input("Let's try that again.  \"factorial\" or \"Fibonacci?\"?  (extra credit if you spell it correctly!)  ")
    return calc_type
  
def check_counter(counter : int):
    if counter == 5:
        print()
        print()
        print("I'm seriously getting pissed here.")
        time.sleep(1.5)
    if counter > 5:
        print()
        print()
        print("Peace out.")
        time.sleep(1)
        print()
        print()
        exit()

def input_value(calc_type : str) -> int:
    print()
    if calc_type == "factorial": 
        value = input("Alrighty then.  What positive integer would you like to evaluate (less than 30, please)?  ")
    else:
        value = input("Alrighty then.  Which term are you looking for (less than 30, please)?  ")
    happy = False
    counter = 0
    while not happy:
        try:
            value = int(value)
            if value < 1:
                counter += 1
                check_counter(counter)
                print()
                value = input("Sigh....   No, no negatives and no zeroes.  It doesn't work like that.  Try again:  ")
            elif value > 30:
                counter += 1
                check_counter(counter)
                print()
                value = input("Too big (bet you've never heard that before), it'll mess up your screen, trust me.   Try again please, something less than 30:  ")
            else:
                happy = True
        except(ValueError):
            try:
                value = float(value)
                counter += 1
                check_counter(counter)
                print()
                value = input("I don't think you know what an integer is, do you?  Well you know what?  Your FACE is an integer!  Try again:  ")
            except(ValueError):
                counter += 1
                check_counter(counter)
                print()
                print("You are really starting to chaffe my hide.  Please, for the love of God, give me a usable integer!  No letters, no decimals, no frickin' negatives.")
                value = input("Shall we try again?  What positive integer would you like to evaluate?  P-O-S-I-T-I-V-E I-N-T-E-G-E-R!  ")
    return value

def calc_fact(value : int , counter : int) -> int:
    if counter > 1:
        counter -= 1
        factorial_list.append(str(value) + " * ")
        value = value * calc_fact(value - 1,counter)
    else:
        factorial_list.append(str(1))
    return value

def factorial(value : int , display : bool):
    counter = value
    result = calc_fact(value,counter)
    if display == True:
        print()
        print(str(value) + "!  = ", end='')
        for term in factorial_list:
            print(term, end='')
            time.sleep(0.1)
        time.sleep(0.5)
    print()
    print()
    print("And the final result:")
    print()
    print(result)

def calc_fib(value : int , counter : int , hold_value : int): # -> int:
    if counter < hold_value - 2:
        counter += 1
        value = int(Fibonacci_list[counter - 2]) + int(Fibonacci_list[counter - 1])
        Fibonacci_list.append(str(value))
        value = calc_fib(value, counter, hold_value)
    else:
        Fibonacci_list.append(str(value + int(Fibonacci_list[counter - 1])))

def Fibonacci(value : int , display : bool):
    counter = 1
    hold_value = value
    calc_fib(value,counter,hold_value)
    if display == True:
        fib_len = len(Fibonacci_list)
        print()
        for fib in range(0,fib_len - 1):
            print(str(Fibonacci_list[fib]) + ', ', end='')
            time.sleep(0.125)
        print(Fibonacci_list[fib_len - 1])
    print()
    print()
    print("And the final result:")
    time.sleep(0.3)
    print()
    print(Fibonacci_list[hold_value - 1])


init() # this makes sure the graphics work correctly in DOS windows
winterm = WinTerm()  # enables the next line
winterm.erase_screen(mode=2) # this clears the screen

print()
print()
print('Ok, so I hear you want something?  Recursion-related, yes?')
calc_type = which_type()
value = input_value(calc_type)
if value == 30:
    print()
    print()
    print("I said less than....  Nevermind, forget it, we'll do 30.")
    time.sleep(1)
print()
print()
if calc_type == "factorial":
    show_process = input("Would you prefer a display of the calculation processes?  ").upper()
else:
    show_process = input("Would you like to see the whole series?  ").upper()
if show_process != "Y" and show_process != "YES":
    time.sleep(2)
    print()
    print("Seriously, why did you even bother looking at this if you don't want to see how it's done?  There's something wrong with you.")
    time.sleep(3)
    # print().upper()
    # time.sleep(2.5)
if show_process == "Y" or show_process == "YES":
    display = True
else:
    display = False
if calc_type == choices[0]:
    factorial(value, display)
else:
    Fibonacci(value,display)
time.sleep(0.5)
print()
print()
print("Thank you, and have a lovely day.")
print()
print()





