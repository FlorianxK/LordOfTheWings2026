from collections import deque
from typing import *

def dayEleven():
    # read
    with open("Day11/11_1.txt", "r") as file:
        portals,p2 = file.read().split("\n\n")
        portals = int(portals.split(": ")[1])
        p2 = p2.split("\n")
        connects = []
        for p in p2:
            temp = set(int(x) for x in p.split())
            connects.append(temp)

    def bfs(h,start):
        q = deque([start])
        seen = set()
        seen.add(start)
        dist = 1
        teleports = 0
        while True:

            next_q = deque([])
            while q:
                curr = q.popleft()
                for ngh in h[curr]:
                    if ngh not in seen:
                        seen.add(ngh)
                        next_q.append(ngh)
                        teleports += dist
            if next_q:
                q = next_q
                dist += 1
            else:
                break  
        
        return teleports
    
    h = DefaultDict(list)
    for i in range(2,portals+1):
        h[i-1].append(i)
        h[i].append(i-1)
    h[1].append(portals)
    h[portals].append(1)

    f_strain = 0
    for i in range(1,portals+1):
        f_strain += bfs(h,i)

    for u,v in connects:
        h[u].append(v)
        h[v].append(u)

    s_strain = 0
    for i in range(1,portals+1):
        s_strain += bfs(h,i)

    return f_strain-s_strain

def dayEleven2():
    # read
    with open("Day11/11_2.txt", "r") as file:
        portals,p2 = file.read().split("\n\n")
        portals = int(portals.split(": ")[1])
        p2 = p2.split("\n")
        connects = []
        for p in p2:
            temp = set(int(x) for x in p.split())
            connects.append(temp)

    def bfs(h,start):
        q = deque([start])
        seen = set()
        seen.add(start)
        dist = 1
        teleports = 0
        while True:

            next_q = deque([])
            while q:
                curr = q.popleft()
                for ngh in h[curr]:
                    if ngh not in seen:
                        seen.add(ngh)
                        next_q.append(ngh)
                        teleports += dist
            if next_q:
                q = next_q
                dist += 1
            else:
                break  
        
        return teleports
    
    h = DefaultDict(list)
    for i in range(1,portals+1):
        # left -3 -2 -1
        for j in range(-3,0):
            val = i+j
            if val <= 0:
                val = (val-1)%(portals+1)
            h[i].append(val)

        # right 1 2 3
        for j in range(1,4):
            val = i+j
            if val > portals:
                val = val%portals                
            h[i].append(val)

    f_strain = 0
    for i in range(1,portals+1):
        f_strain += bfs(h,i)

    for u,v in connects:
        h[u].append(v)
        h[v].append(u)

    max_res = 0
    # find optimal placement for 1 extra connection
    portal_set = set([i for i in range(1,portals+1)])
    for i in range(1,portals+1):

        rest = (portal_set-set(h[i]))
        rest.remove(i)

        for r in rest:
            h[i].append(r)
            h[r].append(i)
        
            s_strain = 0
            for j in range(1,portals+1):
                s_strain += bfs(h,j)

            max_res = max(max_res, f_strain-s_strain)

            h[i].remove(r)
            h[r].remove(i)

    return max_res

def dayEleven3():return

def main():
    print("Hallo")
    print(dayEleven(), "ist die Lösung von Teil 1")
    print(dayEleven2(), "ist die Lösung von Teil 2")
    #print(dayEleven3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()