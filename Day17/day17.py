from collections import deque
from typing import *

def daySeventeen():
    arr = []
    with open("Day17/17_1.txt", "r") as file:
        for line in file:
            arr.append(list(line.strip()))

    m,n = len(arr),len(arr[0])
    start = (0,0)
    end = (m-1,n-1)

    res = 0
    q = deque([(start,0)])
    seen = set()
    seen.add(start)
    while q:
        (ci,cj),steps = q.popleft()
        if (ci,cj) == end:
            res = steps
            break
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni,nj = ci+di,cj+dj
            if 0<=ni<m and 0<=nj<n and arr[ni][nj] == '#' and (ni,nj) not in seen:
                seen.add( (ni,nj) )
                q.append( ((ni,nj),steps+1) )
    
    return res

def daySeventeen2():
    with open("Day17/17_2.txt", "r") as file:
        arr = [line.strip() for line in file]

    m,n = len(arr),len(arr[0])

    # each edge keeps the # square on its right
    edges = set()

    for i in range(m):
        for j in range(n):
            if arr[i][j] != '#':
                continue

            # top edge: west -> east
            if i == 0 or arr[i-1][j] == '.':
                edges.add( ((i,j),(i,j+1)) )

            # right edge: north -> south
            if j == n-1 or arr[i][j+1] == '.':
                edges.add( ((i,j+1),(i+1,j+1)) )

            # bottom edge: east -> west
            if i == m-1 or arr[i+1][j] == '.':
                edges.add( ((i+1,j+1),(i+1,j)) )

            # left edge: south -> north
            if j == 0 or arr[i][j-1] == '.':
                edges.add( ((i+1,j),(i,j)) )

    start = ( (0,0),(0,1) )
    current = start

    visited = set()
    result = 0

    while current not in visited:
        visited.add(current)
        result += 1

        a,b = current

        di = b[0]-a[0]
        dj = b[1]-a[1]

        # right -> straight -> left -> reverse
        options = [(dj,-di),(di,dj),(-dj,di),(-di,-dj)]

        for ndi,ndj in options:
            nxt = ( b,(b[0]+ndi,b[1]+ndj) )

            if nxt in edges:
                current = nxt
                break

    return result

def daySeventeen3():
    with open("Day17/17_3.txt", "r") as file:
        arr = [line.strip() for line in file]

    m,n = len(arr),len(arr[0])

    # each edge keeps the # square on its right
    edges = set()

    for i in range(m):
        for j in range(n):
            if arr[i][j] != '#':
                continue

            # top edge: west -> east
            if i == 0 or arr[i-1][j] == '.':
                edges.add( ((i,j),(i,j+1)) )

            # right edge: north -> south
            if j == n-1 or arr[i][j+1] == '.':
                edges.add( ((i,j+1),(i+1,j+1)) )

            # bottom edge: east -> west
            if i == m-1 or arr[i+1][j] == '.':
                edges.add( ((i+1,j+1),(i+1,j)) )

            # left edge: south -> north
            if j == 0 or arr[i][j-1] == '.':
                edges.add( ((i+1,j),(i,j)) )

    start = ( (0,0),(0,1) )
    current = start

    visited = set()
    result = 0

    while current not in visited:
        
        visited.add(current)
        result += 1

        a,b = current

        di = b[0]-a[0]
        dj = b[1]-a[1]

        if current[1] == (m,n):
            one_way = result

        # right -> straight -> left -> reverse
        options = [(dj,-di),(di,dj),(-dj,di),(-di,-dj)]

        for ndi,ndj in options:
            nxt = ( b,(b[0]+ndi,b[1]+ndj) )

            if nxt in edges:
                current = nxt
                break

    return min(one_way,result-one_way)

def main():
    print("Hallo")
    print(daySeventeen(), "ist die Lösung von Teil 1")
    print(daySeventeen2(), "ist die Lösung von Teil 2")
    print(daySeventeen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()