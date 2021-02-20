"""Given a string, check if its characters can be rearranged to form a palindrome. Where a palindrome is a string that reads the same left-to-right and right-to-left.

Example

"trueistrue" -> false;
"abcab" -> true because "abcba" is a palindrome
[input] string s (min 1 letters)

[output] boolean"""


def isPalindrome(str):
    lonely_char_counter = 0
    odd_counter = 0
    for element in str:
        if str.count(element) == 1:
            lonely_char_counter += 1
        elif str.count(element) % 2 != 0:
            odd_counter += 1

    if lonely_char_counter <= 1 and odd_counter <= 3:
        return True
    else:
        return False


