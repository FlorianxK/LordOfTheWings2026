from collections import defaultdict, deque
from typing import *

def daySix():
    # product -> ingredients
    h = {}
    #read
    with open("Day6/6_1.txt", 'r') as file:
        for line in file:
            product,ingredients = line.strip().split(':')
            h[product] = ingredients.split(',')

    q = deque(["NULL"])
    seen_key = set()
    ingre = set()

    while q:
        curr = q.popleft()
        if curr not in h or curr in seen_key:
            continue
        seen_key.add(curr)

        for i in h[curr]:
            if i != "NULL":
                ingre.add(i)
            q.append(i)

    return len(ingre)

def daySix2():
    # ingredient -> products
    h = defaultdict(list)
    #read
    with open("Day6/6_2.txt", 'r') as file:
        for line in file:
            product,ingredients = line.strip().split(':')
            arr = ingredients.split(',')
            for a in arr:
                h[a].append(product)

    q = deque(["NULL"])
    seen_key = set()
    products = set()

    while q:
        curr = q.popleft()
        if curr not in h or curr in seen_key:
            continue
        seen_key.add(curr)

        for i in h[curr]:
            if i != "NULL":
                products.add(i)
            q.append(i)

    return len(products)

def daySix3():
    # ingredient -> products
    h = defaultdict(list)
    #read
    with open("Day6/6_3.txt", 'r') as file:
        for line in file:
            product,ingredients = line.strip().split(':')
            arr = ingredients.split(',')
            for a in arr:
                h[a].append(product)

    used = defaultdict(set)

    for start in ["NULLv1","NULLv2","NULLv3"]:
        q = deque([start])
        seen_key = set()

        while q:
            curr = q.popleft()
            if curr in seen_key:
                continue
            # no infinite loop
            if curr in h:
                seen_key.add(curr)
            if curr != start:
                used[curr].add(start)
            for i in h[curr]:
                q.append(i)

    res = 0
    for v in used.values():
        if len(v) >= 2:
            res += 1
    return res

def main():
    print("Hallo")
    print(daySix(), "ist die Lösung von Teil 1")
    print(daySix2(), "ist die Lösung von Teil 2")
    print(daySix3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()