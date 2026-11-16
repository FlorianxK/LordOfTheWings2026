from collections import deque
from typing import *

def daySeven():
    h = {}
    energy = {}
    max_idx = 0
    max_con = 0
    #read
    with open("Day7/7_1.txt", 'r') as file:
        for line in file:
            l,m,r = line.split(", ")
            idx = int(l.split("=")[1])
            temp_energy = int(m.split("=")[1])
            r = r.split("=")[1]
            connect = [int(x) for x in r.split(",")]

            h[idx] = connect
            energy[idx] = temp_energy
            if len(connect) > max_con:
                max_con = len(connect)
                max_idx = idx

    def bfs(start,start_impulse):
        # (id,curr_impulse)
        q = deque([ (start,start_impulse) ])
        while q:
            idx,curr_impulse = q.popleft()
            if curr_impulse < 1:
                continue
            energy[idx] += curr_impulse

            for neigh in h[idx]:
                q.append( (neigh,curr_impulse-1) )

    bfs(max_idx,5)

    return sum(energy.values())


def daySeven2():
    h = {}
    energy = {}
    max_idx = 0
    max_con = 0

    # read
    with open("Day7/7_2.txt", 'r') as file:
        for line in file:
            l, m, r = line.split(", ")

            idx = int(l.split("=")[1])
            temp_energy = int(m.split("=")[1])
            r = r.split("=")[1]
            connect = [int(x) for x in r.split(",")]

            h[idx] = connect
            energy[idx] = temp_energy

            if len(connect) > max_con:
                max_con = len(connect)
                max_idx = idx

    def bfs(start,start_impulse):
        q = {start:1}

        while start_impulse > 0:
            next_q = {}

            for idx,count in q.items():
                energy[idx] += count*start_impulse

                for neigh in h[idx]:
                    next_q[neigh] = next_q.get(neigh,0) + count

            q = next_q
            start_impulse -= 1

    bfs(max_idx, 10)

    return sum(energy.values())

def daySeven3():return
def main():
    print("Hallo")
    print(daySeven(), "ist die Lösung von Teil 1")
    print(daySeven2(), "ist die Lösung von Teil 2")
    #print(daySeven3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()