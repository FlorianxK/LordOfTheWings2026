from collections import deque
from typing import *

def daySixteen():
    with open("Day16/16_1.txt", "r") as file:
        q = list(file.read().strip())

    def count_flips(s):
        d = deque(s)
        flips = 0

        while d:
            reversed = False
            key = d[0]
            tail = deque()

            while d:
                # remove the group key from true left
                while d and (d[-1] if reversed else d[0]) == key:
                    if reversed:
                        d.pop()
                    else:
                        d.popleft()

                # remove non-key elements from the true right
                while d and (d[0] if reversed else d[-1]) != key:
                    if reversed:
                        tail.appendleft(d.popleft())
                    else:
                        tail.appendleft(d.pop())

                # flip the rest
                if d:
                    flips += 1
                    reversed = not reversed

            # all tablets of key have been grouped
            d = tail

        return flips

    return count_flips(q)

def daySixteen2():
    with open("Day16/16_2.txt", "r") as file:
        q = list(file.read().strip())*10

    def count_flips(s):
        d = deque(s)
        flips = 0

        while d:
            reversed = False
            key = d[0]
            tail = deque()

            while d:
                # remove the group key from true left
                while d and (d[-1] if reversed else d[0]) == key:
                    if reversed:
                        d.pop()
                    else:
                        d.popleft()

                # remove non-key elements from the true right
                while d and (d[0] if reversed else d[-1]) != key:
                    if reversed:
                        tail.appendleft(d.popleft())
                    else:
                        tail.appendleft(d.pop())

                # flip the rest
                if d:
                    flips += len(d)
                    reversed = not reversed

            # all tablets of key have been grouped
            d = tail

        return flips

    return count_flips(q)

def daySixteen3():
    with open("Day16/16_3.txt", "r") as file:
        q = list(file.read().strip())*100

    def count_flips(s):
        d = deque(s)
        flips = 0

        while d:
            reversed = False
            key = d[0]
            tail = deque()

            while d:
                # remove the group key from true left
                while d and (d[-1] if reversed else d[0]) == key:
                    if reversed:
                        d.pop()
                    else:
                        d.popleft()

                # remove non-key elements from the true right
                while d and (d[0] if reversed else d[-1]) != key:
                    if reversed:
                        tail.appendleft(d.popleft())
                    else:
                        tail.appendleft(d.pop())

                # flip the rest
                if d:
                    flips += len(d)
                    reversed = not reversed

            # all tablets of key have been grouped
            d = tail

        return flips

    return count_flips(q)

def main():
    print("Hallo")
    print(daySixteen(), "ist die Lösung von Teil 1")
    print(daySixteen2(), "ist die Lösung von Teil 2")
    print(daySixteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()