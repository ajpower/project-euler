#!/usr/bin/env python3
"""Project Euler, Problem 8

Iterates throught the 1000-digit number, calculating the product of N digit
sequences as it goes and storing the result. The result from the previous N
digit product can be used to calculate the current N digit product more
efficiently. If a zero digit is discovered, the iteration skips ahead to the
subsequent digit and resumes its calcuations.
"""
N = 13
NUMBER_BLOCK = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
""".replace('\n', '')


def largest_product(n):
    """Return the largest product of n consecutive digits in NUMBER_BLOCK.
    """
    current_max = 0
    last_product = 0
    i = 0
    while i < len(NUMBER_BLOCK) - (n-1):
        if last_product == 0:
            last_product = 1
            for j in range(i, i+n):
                last_product *= int(NUMBER_BLOCK[j])
            i += 1

        elif NUMBER_BLOCK[i+n-1] == 0:
            last_product = 0
            i += n

        else:
            last_product = last_product * int(NUMBER_BLOCK[i+n-1]) // int(NUMBER_BLOCK[i-1])
            i += 1

        if last_product > current_max:
            current_max = last_product

    return current_max

def main():
    """Print the largest product of N consecutive digits in NUMBER_BLOCK. 
    """
    print(largest_product(N))


if __name__ == "__main__":
    main()
