from collections import deque
from typing import *

def dayThree():
    res = []
    #read
    with open("Day3/3_1.txt", 'r') as file:
        for line in file:
            arr = line[4:].split()
            expo = len(arr[0])-1
            temp = 0
            for l,r in zip(arr[0],arr[1]):
                l = int(l)
                r = int(r)
                temp += r*(l**expo)
                expo -= 1
            res.append(temp)

    return sum(res)

def dayThree2():
    res = []
    #read
    with open("Day3/3_2.txt", 'r') as file:
        for line in file:
            arr = line[4:].split()

            # find shorter and appendleft until same length
            l = deque(arr[0])
            r = deque(arr[1])
            if len(l) < len(r):
                loop = l.copy()
                i = len(loop)-1
                while len(l) < len(r):
                    l.appendleft(loop[i])
                    i = (i-1)%len(loop)
            elif len(l) > len(r):
                l = list(l)[len(l)-len(r):]

            expo = len(l)-1
            temp = 0
            for a,b in zip(l,r):
                a = int(a)
                b = int(b)
                temp += b*(a**expo)
                expo -= 1
            res.append(temp)

    return sum(res)

def dayThree3():
    res = []

    with open("Day3/3_3.txt", 'r') as file:
        for line in file:
            if not line.strip():
                continue

            arr = line[5:].split()

            l = deque(arr[0])
            r = deque(arr[1])

            if len(l) < len(r):
                loop = l.copy()
                i = len(loop)-1

                while len(l) < len(r):
                    l.appendleft(loop[i])
                    i = (i-1) % len(loop)

            elif len(l) > len(r):
                l = list(l)[len(l)-len(r):]

            expo = len(l)-1
            temp = 0
            for a,b in zip(l,r):
                a = int(a)
                b = int(b)
                temp += b*(a**expo)
                expo -= 1

            score = temp

            weights = [ int(l[i])**(len(l)-1-i) for i in range(len(l)) ]

            reachable = [set() for _ in range(len(l)+1)]
            reachable[len(l)].add(0)

            for i in range(len(l)-1,-1,-1):
                for digit in range(10):
                    for rest in reachable[i+1]:
                        reachable[i].add(digit*weights[i]+rest)

            build = []
            remaining = score

            for i in range(len(l)):
                for digit in range(10):
                    rest = remaining-digit*weights[i]

                    if rest in reachable[i+1]:
                        build.append(str(digit))
                        remaining = rest
                        break

            if int(''.join(r)) == int(''.join(build)):
                res.append(score)

    return sum(res)

def main():
    print("Hallo")
    print(dayThree(), "ist die Lösung von Teil 1")
    print(dayThree2(), "ist die Lösung von Teil 2")
    print(dayThree3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()