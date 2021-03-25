from functools import reduce

def square(x):
    return x^2

def add(x,y):
    return x + y

def is_even(n):
    return n % 2 == 0

if __name__ == "__main__":

    # map
    l1 = list(map(square,range(10)))

    l2 = list(map(lambda x: 0-1,range(10)))
    print(l1)
    print(l2)

    # reduce
    r1 = reduce(add, range(10))
    print(r1)

    # filter
    l3 = list(filter(is_even, range(10)))
    print(l3)

    # sort
    # ref: https://www.liaoxuefeng.com/wiki/1016959663602400/1017408670135712
    print(sorted([1,4,2,-1]))
    print(sorted([1,4,2,-1],key=abs))
