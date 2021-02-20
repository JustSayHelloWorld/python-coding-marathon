"""Numbers in the Morse code have the following pattern:

all digits consist of 5 characters;
the number of dots at the beginning indicates the numbers from 1 to 5, the remaining characters are dashes;
starting with the number 6, each dot is replaced by a dash and vise versa.
Write the function morse_number() for encryption of a number in a three-digit format in Morse code.



Attention!
Do not use any collection data like lists, tuples, dictionaries for holding Morse codes"""


def morse_number(number):
    converted_number = ""

    for i in range(0, len(number)):

        digit = int(number[i])

        if 6 <= int(digit) <= 9:

            chars = "-."
            digit = digit - 5

        else:
            chars = ".-"

        converted_number += chars[0] * digit
        converted_number += chars[1] * (5 - digit)
        converted_number += " "

    return converted_number