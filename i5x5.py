import random

def normal(ls):
    if ls == [] or ls == [[]]:
        return True
    n = len(ls[0])
    out = True
    for i in ls:
        if len(i) != n:
            out = False
    return out

def trans_mpp2(ls):
    if not(normal(ls)):
        return [[]]
    if ls == [[]] or ls == []:
        return [[]]
    h = len(ls[0])
    w = len(ls)
    out = []
    for i in range(h):
        out.append([])
    print(h,out)
    n = 0
    for i in range(h):
        for j in range(w):
            print(out,i,ls,j,i)
            out[i].insert(0,ls[j][i])
    return out


"""
012
345

30
41
52
"""

def mirror(ls):
    if not(normal(ls)):
        return [[]]
    if ls == [[]] or ls == []:
        return [[]]
    out = []
    for i in ls:
        semiout = []
        for j in i:
            semiout.insert(0,j)
        out.append(semiout)
    return out

"""
123
456

321
654
"""
def symme(self):
    pass

"""
123
456
789

32123
65456
98789
"""

"""
ls = []
for i in range(15):
    ls.append(random.randint(0,1))
print(ls)
n = 0
for i in range(5):
    pass
"""
