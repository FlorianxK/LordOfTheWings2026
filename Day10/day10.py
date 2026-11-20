from typing import *

def dayNine():
    arr = []
    ghosts = []
    with open("Day10/10_1.txt", "r") as file:
        for i,line in enumerate(file):
            line = line.strip()
            for j in range(len(line)):
                if line[j] in "^<>v":
                    if line[j] == "^":
                        ghosts.append( [(i,j),0] )
                    elif line[j] == ">":
                        ghosts.append( [(i,j),1] )
                    elif line[j] == "v":
                        ghosts.append( [(i,j),2] )
                    elif line[j] == "<":
                        ghosts.append( [(i,j),3] )
                    line = list(line)
                    line[j] = '.'
                    
            arr.append(line)

    dirs = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}
    def move_ghosts(ghosts):
        colls = 0
        is_on_space = DefaultDict(list)
        for (i,j),dir in ghosts:
            di,dj = dirs[dir]
            ni,nj = i+di,j+dj
            # wall
            if arr[ni][nj] == '#':
                new_dir = (dir+1)%4
                is_on_space[(i,j)].append(new_dir)
                colls += 1
            # free
            elif arr[ni][nj] == '.':
                is_on_space[(ni,nj)].append(dir)

        new_ghosts = []
        # ghost collisions
        for k,v in is_on_space.items():
            if len(v) == 1:
                new_ghosts.append( [k,v[0]] )
            else:
                colls += len(v)
                for ghost_dir in v:
                    ghost_dir = (ghost_dir+2)%4
                    new_ghosts.append( [k,ghost_dir] )
        
        return colls,new_ghosts

    # 0N:(-1,0), 1E:(0,1), 2S:(1,0), 3W:(0,-1) -> n%4
    # is_on_space hashmap (i,j) after all moved check if one space has double change
    res = 0
    rounds = 10
    for round in range(1,rounds+1):
        colls,ghosts = move_ghosts(ghosts)
        #print(f"Round: {round}, collisions: {colls}")
        res += colls
    
    return res

def dayNine2():
    arr = []
    ghosts = []
    collisions = 10000
    with open("Day10/10_2.txt", "r") as file:
        for i,line in enumerate(file):
            line = line.strip()
            for j in range(len(line)):
                if line[j] in "^<>v":
                    if line[j] == "^":
                        ghosts.append( [(i,j),0,collisions] )
                    elif line[j] == ">":
                        ghosts.append( [(i,j),1,collisions] )
                    elif line[j] == "v":
                        ghosts.append( [(i,j),2,collisions] )
                    elif line[j] == "<":
                        ghosts.append( [(i,j),3,collisions] )
                    line = list(line)
                    line[j] = '.'
                    
            arr.append(line)

    dirs = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}
    def move_ghosts(ghosts):
        is_on_space = DefaultDict(list)
        for (i,j),dir,colls in ghosts:
            di,dj = dirs[dir]
            ni,nj = i+di,j+dj
            # wall
            if arr[ni][nj] == '#':
                new_dir = (dir+1)%4
                if colls-1 > 0:
                    is_on_space[(i,j)].append([new_dir,colls-1])
            # free
            elif arr[ni][nj] == '.':
                is_on_space[(ni,nj)].append([dir,colls])

        new_ghosts = []
        # ghost collisions
        for k,v in is_on_space.items():
            # v = [ [a,b],[c,d]... ]
            if len(v) == 1:
                new_ghosts.append( [k,v[0][0],v[0][1]] )
            else:
                for ghost_dir,curr_colls in v:
                    ghost_dir = (ghost_dir+2)%4
                    if curr_colls-1 > 0:
                        new_ghosts.append( [k,ghost_dir,curr_colls-1] )
        
        return new_ghosts

    # 0N:(-1,0), 1E:(0,1), 2S:(1,0), 3W:(0,-1) -> n%4
    # is_on_space hashmap (i,j) after all moved check if one space has double change
    rounds = 1
    while True:
        ghosts = move_ghosts(ghosts)
        if len(ghosts) == 0:
            break
        else:
            rounds += 1

    return rounds

def dayNine3():return

def main():
    print("Hallo")
    print(dayNine(), "ist die Lösung von Teil 1")
    print(dayNine2(), "ist die Lösung von Teil 2")
    #print(dayNine3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()