"""For the given integer n, consider an increasing sequence consisting of all positive integers that are either powers of n, or sums of distinct powers of n.
Your task is to find the kth (1-based) number in this sequence.

Example

For n = 3 and k = 4, the output should be
kthTerm(n, k) = 9.

For n = 3, the sequence described above begins as follows: 1, 3, 4, 9, 10, 12, 13...
[3**0] => [1]
[1, 3**1, 3**1 +1] => [1, 3, 4]
[1, 3, 4, 3**2, 3**2 +1, 3**2 +3, 3**2 +4] => [1, 3, 4, 9, 10, 12, 13]
...

The 4th number in this sequence is 9, which is the answer.

Input/Output

[input] integer n

The number to build the sequence by.

Constraints:
2 ≤ n ≤ 30.

[input] integer k

The 1-based index of the number in the sequence.

Constraints:
1 ≤ k ≤ 100.

[output] integer

The kth element of the sequence.
"""
def kthTerm(n, k):
    result_sequence: list = []
    power_counter = 0

    while len(result_sequence) <= k:

        if len(result_sequence) > 0:
            sequence_part_for_sum = result_sequence.copy()
            result_sequence.append(n ** power_counter)
            for element in sequence_part_for_sum:
                result_sequence.append(n ** power_counter + element)
        else:
            result_sequence.append(n ** power_counter)
        power_counter +=1
    return result_sequence[k-1]