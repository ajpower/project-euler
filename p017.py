#!/usr/bin/env python3
"""Project Euler, Problem 17

Brute force solution. The function 'int2word' defined below converts integers
to their corresponding word.
"""
MAX_NUM = 1000


DIGIT_TO_WORD = { 1 : "one",
                  2 : "two",
                  3 : "three",
                  4 : "four",
                  5 : "five",
                  6 : "six",
                  7 : "seven",
                  8 : "eight",
                  9 : "nine" }

TEENS_TO_WORD = { 10 : "ten",
                  11 : "eleven",
                  12 : "twelve",
                  13 : "thirteen",
                  14 : "fourteen",
                  15 : "fifteen",
                  16 : "sixteen",
                  17 : "seventeen",
                  18 : "eighteen",
                  19 : "nineteen" }

TENS_TO_WORD = { 20 : "twenty",
                 30 : "thirty",
                 40 : "forty",
                 50 : "fifty",
                 60 : "sixty",
                 70 : "seventy",
                 80 : "eighty",
                 90 : "ninety" }

MAGNITUDE = { 3  : "thousand",
              6  : "million",
              9  : "billion",
              12 : "trillion",
              15 : "quadrillion",
              18 : "quintillion",
              21 : "sextillion",
              24 : "septillion",
              27 : "octillion",
              30 : "nonillion",
              33 : "decillion" }


def tens2word(num):
    """Return positive integer 'num' as a word, provided it is less than one
    hundred.
    """
    if num < 10:
        return DIGIT_TO_WORD[num]
    elif num < 20:
        return TEENS_TO_WORD[num]
    elif num < 100:
        if num % 10 == 0:
            return TENS_TO_WORD[(num // 10) * 10]
        else:
            return TENS_TO_WORD[(num // 10) * 10] + "-" + DIGIT_TO_WORD[num % 10]
    
    return str(num)

def hundreds2word(num):
    """Return positive integer 'num' as a word, provided it is less than a
    thousand. Does *not* use "and" ie
        hundreds2word(115) = one hundred fifteen
    """
    if num < 100:
        return tens2word(num)

    elif num % 100 == 0:
        return DIGIT_TO_WORD[num // 100] + " hundred"

    else:
        return DIGIT_TO_WORD[num // 100] + " hundred " + tens2word(num % 100)

def int2word(num):
    """Return integer 'num' as a word, provided it is greater than negative
    undecillion and smaller than positive undecillion.
    """
    if num < 0:
        return "negative " + int2word(-num)

    elif num == 0:
        return "zero"

    elif num < 100:
        return tens2word(num)

    elif num < 1000:
        # cannot invoke 'hundreds2word' because there would be no "and".
        if num % 100 == 0:
            return DIGIT_TO_WORD[num // 100] + " hundred"
        else:
            return DIGIT_TO_WORD[num // 100] + " hundred and " + tens2word(num % 100)

    else:
        magnitude = ((len(str(num)) - 1) // 3) * 3
        left_side = hundreds2word(num // 10**magnitude) + " " + MAGNITUDE[magnitude]
        remainder = num % 10 ** magnitude

        if remainder == 0:
            return left_side
        elif remainder < 100:
            return left_side + " and " + tens2word(remainder)
        else:
            return left_side + " " + int2word(remainder)

    return str(num)

def main():
    """Print the number of letters, no including spaces in hyphens, of all
    numbers from one to 'MAX_NUM' written out.
    """
    letters = 0
    for i in range(1, MAX_NUM + 1):
        word = int2word(i)
        clean_word = word.replace(" ", "").replace("-","")
        letters += len(clean_word)

    print(letters)


if __name__ == "__main__":
    main()
