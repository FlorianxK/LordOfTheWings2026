from collections import deque
from typing import *

def dayFourteen():
    arr = []
    # read
    with open("Day14/14_1.txt", "r") as file:
        for line in file:
            arr.append(list(line.strip()))

    seen = set()
    seen_groups = set()
    seen_pairs = set()
    m,n = len(arr),len(arr[0])

    def bfs(i,j):
        group = arr[i][j]
        outer = 0
        seen_groups.add(group)
        seen.add( (i,j) )
        q = deque([(i,j)])
        while q:
            ci,cj = q.popleft()
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj = ci+di,cj+dj
                if 0<=ni<m and 0<=nj<n:

                    if arr[ni][nj] == group:

                        if (ni,nj) in seen:
                            continue
                        seen.add( (ni,nj) )
                        q.append( (ni,nj) )
                    else:
                        # different group
                        if ((ci,cj),(ni,nj)) not in seen_pairs:
                            outer += 1
                            seen_pairs.add( ((ci,cj),(ni,nj)) )
                            seen_pairs.add( ((ni,nj),(ci,cj)) )
                else:
                    outer += 1
        print(group,outer)
        return outer

    res = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] not in seen_groups:
                res += bfs(i,j)
    return res

def dayFourteen2():return
def dayFourteen3():return

def main():
    print("Hallo")
    print(dayFourteen(), "ist die Lösung von Teil 1")
    #print(dayFourteen2(), "ist die Lösung von Teil 2")
    #print(dayFourteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()