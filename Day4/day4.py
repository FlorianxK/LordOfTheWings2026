from collections import defaultdict
from heapq import heappop, heappush
from typing import *

def dayFour():
    res = 0
    h = defaultdict(int)
    #read
    with open("Day4/4_1.txt", 'r') as file:
        for line in file:
            parts = line.split()
            for p in parts:
                l,r = p.split('=')
                if l == "id":
                    id = int(r)
                elif l == "time":
                    time = int(r)
            h[id] += time
    
    times = []
    for v in h.values():
        times.append(v)
    times.sort()
    
    for i,times in enumerate(times,1):
        res += i*times
    
    return res

def dayFour2():
    res = 0
    # (parts,time)
    h = defaultdict(list)
    #read
    with open("Day4/4_2.txt", 'r') as file:
        for line in file:
            parts = line.split()
            for p in parts:
                l,r = p.split('=')
                if l == "id":
                    id = int(r)
                elif l == "time":
                    time = int(r)
            if not h[id]:
                h[id] = [1,time]
            else:
                h[id][0] += 1
                h[id][1] += time

    times = []
    for v in h.values():
        times.append(tuple(v))
    times.sort( key=lambda x:(-x[0],x[1]) )
    
    for i,times in enumerate(times,1):
        res += i*times[1]
    
    return res

def dayFour3():
    # first sort first for quest, second for part
    res = 0
    # (quest,part,id,time)
    arr = []
    #read
    with open("Day4/4_3.txt", 'r') as file:
        for line in file:
            parts = line.split()
            for p in parts:
                l,r = p.split('=')
                if l == "id":
                    id = int(r)
                elif l == "quest":
                    quest = int(r)
                elif l == "part":
                    part = int(r)
                elif l == "time":
                    time = int(r)
            
            arr.append( (quest,part,id,time) )

        arr.sort(key=lambda x: (x[0],x[1]) )

        points = defaultdict(int)
        win = {1:50,2:100,3:150}
        curr_quest = arr[0][0]
        curr_part = arr[0][1]

        id_times = defaultdict(int)
        heap_part = []

        def give_points():
            prize = win[curr_part]
            prev_time = None
            last_prize = 0

            while heap_part:
                curr_time, curr_id = heappop(heap_part)

                if prev_time == curr_time:
                    points[curr_id] += max(0,last_prize)
                else:
                    last_prize = prize
                    points[curr_id] += max(0,prize)

                prev_time = curr_time
                prize -= 1
        
        for quest,part,id,time in arr:

            # quest is done
            if quest != curr_quest:
                give_points()
                curr_quest = quest
                curr_part = part
                for k in id_times.keys():
                    id_times[k] = 0


            if curr_part == part:
                heappush(heap_part, (time+id_times[id],id) )
                id_times[id] += time
            else: # part is done
                give_points()
                # work with first element of new part
                curr_part = part
                heappush(heap_part, (time+id_times[id],id) )
                id_times[id] += time

        give_points()

    points_arr = []
    for v in points.values():
        points_arr.append(v)
    points_arr.sort(reverse=True)
    res = 0

    prev_time = None
    last_place = 0
    for place,time in enumerate(points_arr,1):
        if time == prev_time:
            res += last_place*time
        else:
            res += place*time
            last_place = place
        prev_time = time
    
    return res

def main():
    print("Hallo")
    print(dayFour(), "ist die Lösung von Teil 1")
    print(dayFour2(), "ist die Lösung von Teil 2")
    print(dayFour3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()