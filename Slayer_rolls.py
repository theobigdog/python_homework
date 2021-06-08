
import random

def get_coin_toss():
    roll = random.randint(1,2)
    if roll == 1:
        result = "Heads"
    else:
        result = "Tails"
    return result

def multi_roll(low_range : int, high_range : int) -> int:
    low = low_range
    high = high_range
    roll = random.randint(low,high)
    return roll
