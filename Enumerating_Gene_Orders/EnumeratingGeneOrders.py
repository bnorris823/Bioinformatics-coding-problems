from itertools import permutations

def get_permutations(n):

    numbers = list(range(1,1+n))
    perm = list(permutations(numbers))
    print(len(perm))

    for p in perm:
        p = str(p)
        p = p.replace(",", "")
        p = p[1:len(p) - 1]
        print(p)



get_permutations(7)


