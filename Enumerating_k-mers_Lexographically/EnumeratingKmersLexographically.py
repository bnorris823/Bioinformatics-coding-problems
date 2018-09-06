from itertools import product

def get_permutations(DNA, n):

    letters = DNA.replace(" ", "")
    perm = list(product(letters, repeat=n))
    for p in perm:
        p = str(p)
        bad_chars = "()', "
        for char in bad_chars:
            p = p.replace(char, "")
        print(p)




get_permutations("A B C D E F G H", 3)