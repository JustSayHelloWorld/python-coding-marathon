"""Write a program that given an array of integers determines if it is sorted in "ascending" order, "descending" order or "not sorted" at all.

Example

For a = [10, 5, 4], the output should be
order(a) = "descending";
For a = [6, 20, 160, 420], the output should be
order(a) = "ascending";
For a = [1, 7, 0, 4, 8, 1], the output should be
order(a) = "not sorted".
[input] array.integer a

1 < a.length < 100, all of numbers are different

[output] string

"ascending", "descending" or "not sorted".
"""


def order(a):
    result = "not sorted"
    counter = 0
    previous_element = a[0]
    for i in range(1, len(a)):
        if a[i] > previous_element:
            counter += 1
        elif a[i] < previous_element:
            counter -= 1

        if i != abs(counter):
            return result
    if counter > 0:
        result = "ascending"
    else:
        result = "descending"

    return result