from hog import *
from dice import make_test_dice


def total(s0, s1):
    print(s0 + s1)
    return echo

def echo(s0, s1):
    print(s0, s1)
    return total

s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)
print(s0, s1)
