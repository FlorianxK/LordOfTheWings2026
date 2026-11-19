from typing import *

def dayNine():
    res = 0

    def grow(growth,limit):
        branches = {1:1}
        branch_num = 2
        splits = 0
        total = 1
        seconds = 1

        while total < limit:
            seconds += 1
            new_branches = {}

            for k, val in branches.items():
                if val+1 == growth:
                    # split point
                    splits += 1

                    # same length halves
                    half = (growth-1)//2

                    new_branches[k] = half

                    new_branches[branch_num] = half
                    branch_num += 1

                    new_branches[branch_num] = 1
                    branch_num += 1

                else:
                    new_branches[k] = val+1

            branches = new_branches
            total = sum(branches.values()) + splits

        return seconds

    with open("Day9/9_1.txt", "r") as file:
        for line in file:
            idx,growth,limit = [int(x.split("=")[1]) for x in line.strip().split(", ")]

            res += grow(growth, limit)

    return res

def dayNine2():
    res = 0

    def grow(growth,limit):
        branches = [1]
        leaves = 1
        seconds = 1

        while leaves < limit:
            seconds += 1
            new_branches = []

            for val in branches:
                val += 1

                if val == growth:
                    half = (growth-1)//2

                    new_branches.append(half)
                    new_branches.append(half)

                    new_branches.append(1)

                    leaves += 1
                else:
                    new_branches.append(val)

            branches = new_branches

        return seconds

    with open("Day9/9_2.txt", "r") as file:
        for line in file:
            idx,growth,limit = [int(x.split("=")[1]) for x in line.strip().split(", ")]

            res += grow(growth,limit)

    return res

def dayNine3():
    return

def main():
    print("Hallo")
    print(dayNine(), "ist die Lösung von Teil 1")
    print(dayNine2(), "ist die Lösung von Teil 2")
    #print(dayNine3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()