from collections import deque
from typing import *

def dayFive():
    res = 0
    arr = []
    #read
    with open("Day5/5_1.txt", 'r') as file:
        for line in file:
            arr.append(list(line.strip()))
    m,n = len(arr),len(arr[0])

    seen = set()
    around = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
    
    def bfs(i,j):
        q = deque([(i,j)])
        seen.add((i,j))
        count = 1

        while q:
            ci,cj = q.popleft()

            for di,dj in around:
                ni,nj = ci+di,cj+dj

                if 0<=ni<m and 0<=nj<n and arr[ni][nj] != '#':
                    
                    land = 0
                    for neigh_i,neigh_j in around:
                        check_i = ni+neigh_i
                        check_j = nj+neigh_j

                        if 0<=check_i<m and 0<=check_j<n and arr[check_i][check_j] in "1#":
                            land += 1

                    if land >= 5:
                        arr[ni][nj] = '#'
                        seen.add( (ni,nj) )
                        q.append( (ni,nj) )
                        count += 1

        return count
    
    mid_i,mid_j = m//2,n//2
    arr[mid_i][mid_j] = '#'
    res = bfs(mid_i,mid_j)

    return res

def dayFive2():
    # find all water and save in set - go through all water and neigh == # become sand - save sand in set - go through sand like tiles in prev part
    arr = []
    #read
    with open("Day5/5_2.txt", 'r') as file:
        for line in file:
            arr.append(list(line.strip()))
    m,n = len(arr),len(arr[0])

    seen = set()
    around = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
    
    def land(i,j):
        q = deque([(i,j)])
        seen.add((i,j))

        while q:
            ci,cj = q.popleft()

            for di,dj in around:
                ni,nj = ci+di,cj+dj

                if 0<=ni<m and 0<=nj<n and arr[ni][nj] != '#':
                    
                    land = 0
                    for neigh_i,neigh_j in around:
                        check_i = ni+neigh_i
                        check_j = nj+neigh_j

                        if 0<=check_i<m and 0<=check_j<n and arr[check_i][check_j] in "1#":
                            land += 1

                    if land >= 5:
                        arr[ni][nj] = '#'
                        seen.add( (ni,nj) )
                        q.append( (ni,nj) )
    
    mid_i,mid_j = m//2,n//2
    arr[mid_i][mid_j] = '#'
    land(mid_i,mid_j)

    water = set()
    def find_water():
        for i in range(m):
            for j in range(n):
                if arr[i][j] != '#':
                    water.add( (i,j) )
                    arr[i][j] = '.'

    sand_set = set()
    def first_sand():
        for i,j in water:
            for di,dj in around:
                ni,nj = i+di,j+dj
                if 0<=ni<m and 0<=nj<n and arr[ni][nj] == '#':
                    seen.remove( (ni,nj) )
                    arr[ni][nj] = '='
                    sand_set.add( (ni,nj) )
        #edges
        for i in range(m):
            for a,b in [(i,0),(i,n-1)]:
                if arr[a][b] == '#':
                    seen.remove( (a,b) )
                    sand_set.add( (a,b) )
                    arr[a][b] = '='
        for j in range(n):
            for a,b in [(0,j),(m-1,j)]:
                if arr[a][b] == '#':
                    seen.remove( (a,b) )
                    sand_set.add( (a,b) )
                    arr[a][b] = '='

    # look at all sand if ngh is land check his ngh - if more/equal 5 become sand and append to queue
    def fill_sand():
        q = deque(list(sand_set))

        while q:
            ci,cj = q.popleft()

            for di,dj in around:
                ni,nj = ci+di,cj+dj

                if 0<=ni<m and 0<=nj<n and arr[ni][nj] == '#':
                    
                    sand = 0
                    for neigh_i,neigh_j in around:
                        check_i = ni+neigh_i
                        check_j = nj+neigh_j

                        if 0<=check_i<m and 0<=check_j<n and arr[check_i][check_j] == '=':
                            sand += 1

                    if sand >= 5:
                        arr[ni][nj] = '='
                        sand_set.add( (ni,nj) )
                        q.append( (ni,nj) )
    
    find_water()
    first_sand()
    fill_sand()

    return len(sand_set)

def dayFive3():
    return

def main():
    print("Hallo")
    #print(dayFive(), "ist die Lösung von Teil 1")
    print(dayFive2(), "ist die Lösung von Teil 2")
    print(dayFive3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()