from heapq import heappop, heappush
from typing import *

def dayEighteen():
    heights = []
    with open("Day18/18_1.txt", "r") as file:
        for line in file:
            l,r = line.split()
            x = int(l.split("=")[1])
            y = int(r.split("=")[1])
            heights.append( (x,y) )

    arr = []
    prev_x = 0
    for x,y in heights:
        arr.extend( [0]*( max(0,x-prev_x-1) ) )
        arr.append(y)
        prev_x = x

    l,r = 0,0
    n = len(arr)
    res = 0
    # heap
    next_height = []
    while r < n:
        if l == r:
            r += 1

        if arr[l] > arr[r]:
            if arr[r] > 0:
                heappush( next_height,(-arr[r],r) )
            r += 1

        elif arr[l] <= arr[r]:
            h = []
            l_height = arr[l]
            while l < r:
                l += 1
                if l != r:
                    res += l_height-arr[l]

    if len(next_height) > 0:
        while l < n-1:
            right_val,right_index = heappop(next_height)
            right_val *= -1

            l_height = arr[l]
            while l < right_index:
                l += 1
                if l != right_index:
                    res += right_val-arr[l]

    return res+sum(arr)

def dayEighteen2():
    heights = []
    with open("Day18/18_2.txt", "r") as file:
        for line in file:
            l,m,r = line.split()
            x = int(l.split("=")[1])
            y = int(m.split("=")[1])
            width = int(r.split("=")[1])
            heights.append( (x,y,width) )

    arr = []
    prev_x = 0
    prev_width = 0
    for x,y,width in heights:
        arr.extend( [0]*( max(0,x-prev_x-prev_width) ) )
        arr.extend([y]*width)
        prev_x = x
        prev_width = width
    
    l,r = 0,0
    n = len(arr)
    res = 0
    # heap
    next_height = []
    while r < n:
        if l == r:
            r += 1

        if arr[l] > arr[r]:
            if arr[r] > 0:
                heappush( next_height,(-arr[r],r) )
            r += 1

        elif arr[l] <= arr[r]:
            h = []
            l_height = arr[l]
            while l < r:
                l += 1
                if l != r:
                    res += l_height-arr[l]

    if len(next_height) > 0:
        while l < n-1:
            right_val,right_index = heappop(next_height)
            right_val *= -1

            l_height = arr[l]
            while l < right_index:
                l += 1
                if l != right_index:
                    res += right_val-arr[l]

    return res+sum(arr)

def dayEighteen3():return

def main():
    print("Hallo")
    print(dayEighteen(), "ist die Lösung von Teil 1")
    print(dayEighteen2(), "ist die Lösung von Teil 2")
    #print(dayEighteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()