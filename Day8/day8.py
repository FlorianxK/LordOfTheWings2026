from typing import *

def dayEight():
    arr = []
    #read
    with open("Day8/8_1.txt", 'r') as file:
        for line in file:
            line = line.strip()
            nums = []
            for c in line:
                if c.isnumeric():
                    nums.append(int(c))
                else:
                    nums.append(0)
            arr.append(nums)

    def shadow(ci,cj):
        # down right = ci+1,cj+1
        total = 0
        curr_h = 0
        while 0<=ci<m and 0<=cj<n and arr[ci][cj] != 0:
            if arr[ci][cj] > curr_h:
                total += 1
                curr_h = arr[ci][cj]

            curr_h -= 1
            ci += 1
            cj += 1
        
        return total

    m,n = len(arr),len(arr[0])
    res = 0

    j = 0
    for i in range(m//2,-1,-1):
        res += shadow(i,j)
        j += 1

    start = j+1
    goal = n-start+1
    for j in range(start,goal+1,2):
        res += shadow(0,j)
    
    return res

def dayEight2():
    arr = []
    #read
    with open("Day8/8_2.txt", 'r') as file:
        for line in file:
            line = line.strip()
            nums = []
            for c in line:
                if c.isnumeric():
                    nums.append(int(c))
                else:
                    nums.append(0)
            arr.append(nums)

    m, n = len(arr), len(arr[0])

    def shadow(ci,cj,di,dj):
        total = 0
        curr_h = 0
        while 0<=ci<m and 0<=cj<n and arr[ci][cj] != 0:
            if arr[ci][cj] > curr_h:
                total += 1
                curr_h = arr[ci][cj]

            curr_h -= 1
            ci += di
            cj += dj
        
        return total
    # ↘1,1 = (m//2,0) to (0,leftJ) -> (0,leftJ+2) to (0,rightJ)
    # ↙1,-1 = (m//2,n-1) to (0,rightJ) -> (0,rightJ-2) to (0,leftJ)
    # ←0,-2 = special just to left
    # ↖-1,-1 = (m//2,n-1) to (m-1,rightJ) -> (m-1,rightJ-2) to (m-1,leftJ)
    # ↗-1,1 = (m//2,0) to (m-1,leftJ) -> (m-1,leftJ+2) to (m-1,rightJ)
    # →0,2 = special just to right

    # start_j = -1 == (m//2,n-1)
    # start_j = 1 == (m//2,0)
    # start_i = -1 == m-1 rightJ and leftJ swap -> if j=-1 its rightJ first
    # start_i = 1 == 0 and if j=1 leftJ first
    dirs = [(1,1),(1,-1),(0,-2),(-1,-1),(-1,1),(0,2)]
    res = 0
    for di,dj in dirs:
        for i in range(m):
            for j in range(n):

                if arr[i][j] == 0:
                    continue

                pi = i-di
                pj = j-dj

                if (0<=pi<m and 0<=pj<n and arr[pi][pj] != 0):
                    continue

                res += shadow(i,j,di,dj)

    return res

def dayEight3():return

def main():
    print("Hallo")
    print(dayEight(), "ist die Lösung von Teil 1")
    print(dayEight2(), "ist die Lösung von Teil 2")
    #print(dayEight3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()