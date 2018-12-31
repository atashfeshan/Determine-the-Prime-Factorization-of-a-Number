def prim(x: int) -> iter:
    b = [True for _ in range(2, x+1)]
    for i in range(2, x+1):
        if b[i-2] == 0:
            continue
        for j in range(i*2, x+1, i):
            b[j-2] = False
    for i in range(2, len(b)+2):
        if b[i-2] == 1:
            yield i


def to_prim(x: int) -> dict:
    numbers = dict()
    prim_number = list(prim(x))
    for ii in prim_number:
        while x%ii == 0:
           x = x//ii
           if ii not in numbers:
               numbers[ii] = 1
           else:
               numbers[ii] += 1

    return numbers


if __name__ == '__main__':
    n = 97
    print(to_prim(n))
