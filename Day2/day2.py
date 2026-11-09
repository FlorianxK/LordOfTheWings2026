from collections import defaultdict, deque
from typing import *

def dayTwo():
    res = []
    #read
    with open("Day2/2_1.txt", 'r') as file:
        for line in file:
            arr = line.split()
            h = defaultdict(int)
            for a in arr:
                l = a[0]
                m = a[1]
                r = a[2]
                # h[number] = counted_smaller
                if m == '>':
                    h[r] += 1
                    if l not in h:
                        h[l] = 0
                else:
                    h[l] += 1
                    if r not in h:
                        h[r] = 0

            # add together and append
            temp = [0]*len(h)
            for k,v in h.items():
                temp[v] = k
            res.append(int(''.join(temp)))

    return sum(res)

def dayTwo2():
    res = []
    #read
    with open("Day2/2_2.txt", 'r') as file:
        for line in file:
            arr = line.split()
            h = defaultdict(int)
            compared = defaultdict(int)
            for a in arr:
                l = a[0]
                m = a[1]
                r = a[2]
                # h[number] = counted_smaller
                if m == '>':
                    h[r] += 1
                    if l not in h:
                        h[l] = 0
                else:
                    h[l] += 1
                    if r not in h:
                        h[r] = 0
                compared[l] += 1
                compared[r] += 1

            # add missing compare
            min_val = min(compared.values())
            pair = []
            for k,v in compared.items():
                if v == min_val:
                    pair.append(k)
            l,r = pair[0],pair[1]
            if h[l] < h[r]:
                h[r] += 1
            else:
                h[l] += 1

            # add together and append
            temp = [0]*len(h)
            for k,v in h.items():
                temp[v] = k
            
            res.append(int(''.join(temp)))

    return sum(res)

def dayTwo3():
    res = []
    #read
    with open("Day2/2_3.txt", 'r') as file:
        for line in file:
            arr = line.split()
            h = defaultdict(list)
            for a in arr:
                l = int(a[0])
                m = a[1]
                r = int(a[2])
                # h[parent] = children
                if m == '>':
                    h[l].append(r)
                else:
                    h[r].append(l)

            all_nodes = set()
            children = set()
            # find root and amount of nodes
            for k,v in h.items():
                all_nodes.add(k)
                for node in v:
                    children.add(node)
                    if node not in all_nodes:
                        all_nodes.add(node)

            root = (all_nodes-children).pop()

            # bfs from root and if length of path equals length of all_nodes result is found
            # (curr_node,path)
            q = deque([ (root,"") ])
            temp = []
            while q:
                curr,path = q.popleft()
                path += str(curr)

                if not h[curr]:
                    temp.append(path)
                    continue

                for child in h[curr]:
                    q.append( (child,path) )

            for t in temp:
                if len(t) == len(all_nodes):
                    res.append(int(t))
                    break

    return sum(res)

def main():
    print("Hallo")
    print(dayTwo(), "ist die Lösung von Teil 1")
    print(dayTwo2(), "ist die Lösung von Teil 2")
    print(dayTwo3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()