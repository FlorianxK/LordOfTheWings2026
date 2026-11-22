from collections import deque
from typing import *

def dayTwelve():
    arr = []
    # read
    with open("Day12/12_1.txt", "r") as file:
        for line in file:
            arr.append(list(line.strip()))
    
    seen = set()
    m,n = len(arr),len(arr[0])

    def bfs(i,j):
        q = deque([(i,j)])
        seen.add( (i,j) )
        min_i,max_i = i,i
        min_j,max_j = j,j
        while q:
            ci,cj = q.popleft()
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj = ci+di,cj+dj
                if 0<=ni<m and 0<=nj<n and arr[ni][nj] == '#' and (ni,nj) not in seen:
                    seen.add( (ni,nj) )
                    q.append( (ni,nj) )
                    min_i = min(min_i,ni)
                    max_i = max(max_i,ni)
                    min_j = min(min_j,nj)
                    max_j = max(max_j,nj)
        
        return min( max_i-min_i+1, max_j-min_j+1 )

    res = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '#' and (i,j) not in seen:
                res += bfs(i,j)
    return res

def dayTwelve2():
    arr = []
    # read
    with open("Day12/12_2.txt", "r") as file:
        for line in file:
            arr.append(list(line.strip()))
    
    seen = set()
    m,n = len(arr),len(arr[0])

    def bfs(i,j):
        q = deque([(i,j)])
        seen.add( (i,j) )
        shape = [(i,j)]
        while q:
            ci,cj = q.popleft()
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj = ci+di,cj+dj
                if 0<=ni<m and 0<=nj<n and arr[ni][nj] == '#' and (ni,nj) not in seen:
                    seen.add( (ni,nj) )
                    q.append( (ni,nj) )
                    shape.append( (ni,nj) )
        return shape

    def get_length(shape):
        graph = DefaultDict(list)
        for i,j in shape:
            graph[i].append(j)

        # memo
        match = {}
        def dfs(i,visited):
            for c in graph[i]:
                if c in visited:
                    continue

                visited.add(c)

                if c not in match or dfs(match[c],visited):
                    match[c] = i
                    return True

            return False

        matching = 0
        for i in graph.keys():
            if dfs(i,set()):
                matching += 1

        return matching

    res = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '#' and (i,j) not in seen:
                shape = bfs(i,j)
                res += get_length(shape)
    return res

def dayTwelve3():return

def main():
    print("Hallo")
    print(dayTwelve(), "ist die Lösung von Teil 1")
    print(dayTwelve2(), "ist die Lösung von Teil 2")
    #print(dayTwelve3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()