import math
from typing import *

def dayOne():
    res = 0
    #read
    with open("Day1/1_1.txt", 'r') as file:
        arr = [int(x) for x in file.read().split(',')]

    for v in arr:
        next_square = math.ceil(math.sqrt(v))
        res += next_square**2-v
    
    return res

def dayOne2():
    # before 9 16 25 -> now 8:3x3 12:4x4 16:5x5 20:6x6 24:7x7
    res = 0
    #read
    with open("Day1/1_2.txt", 'r') as file:
        arr = [int(x) for x in file.read().split(',')]

    for v in arr:
        next_val = math.ceil(v/4)+1
        if next_val < 3:
            next_val = 3
        res += 4*next_val-4-v

    return res

def dayOne3():
    res = 0
    #read
    with open("Day1/1_3.txt", 'r') as file:
        arr = [int(x) for x in file.read().split(',')]

    for v in arr:
        next_square = math.ceil(math.sqrt(v+1))
        if next_square < 3:
            next_square = 3
        if next_square%2 == 0:
            next_square += 1
        res += next_square**2-1-v

    return res

def main():
    print("Hallo")
    print(dayOne(), "ist die Lösung von Teil 1")
    print(dayOne2(), "ist die Lösung von Teil 2")
    print(dayOne3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()