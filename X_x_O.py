import itertools
import random
def show(tab,num,ing):
    tab[num-1]=ing
    tele= [tab[i:i+3]for i in range(0,7,3)]
    for i in tele:
        print(i)
    print()
def iter(box):
    box.sort()
    iter1 = list(itertools.combinations(box,3))
    org = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in iter1:
        if list(i) in org:
            return 1
def main():
    
    tab = ["•","•","•","•","•","•","•","•","•"]
    x = []
    o = []
    source = [1,2,3,4,5,6,7,8,9]
    for _ in range(2):
        rand = random.choice(source)
        x.append(rand)
        source.remove(rand)
        show(tab,rand,"X")
        rand = random.choice(source)
        o.append(rand)
        source.remove(rand)
        show(tab,rand,"0")
    rand = random.choice(source)
    x.append(rand)
    source.remove(rand)
    show(tab,rand,"X")
    if iter(x) ==1:
        return "X won"
    rand = random.choice(source)
    o.append(rand)
    source.remove(rand)
    show(tab,rand,"0")
    if iter(o) == 1:
        return "0 won"
    rand = random.choice(source)
    x.append(rand)
    source.remove(rand)
    show(tab,rand,"X")
    if iter(x) == 1:
        return "X won"
    rand = random.choice(source)
    o.append(rand)
    source.remove(rand)
    show(tab,rand,"0")
    if iter(o) == 1:
        return "0 won"
    rand = random.choice(source)
    x.append(rand)
    source.remove(rand)
    show(tab,rand,"X")
    if iter(x) == 1:
        return "X won"
    else:
        return "Match Draw"
print(main())
