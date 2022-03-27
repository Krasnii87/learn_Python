import sys

sys.setrecursionlimit(3000)

def Akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return Akk(m-1, 1)
    return Akk(m-1, Akk(m, n-1))

print(Akk(3, 8))