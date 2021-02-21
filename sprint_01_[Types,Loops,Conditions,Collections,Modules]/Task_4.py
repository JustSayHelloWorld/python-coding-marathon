"""Given number n and two permutations p and q of length n. Find a permutation r, such that for every 1 <= i <= n, q[i] = p[r[i]].

Permutation of length n is an array consisting of distinct numbers from 1 to n in some order.

Example

Input:
n = 3, p = [3, 1, 2],  q = [2, 1, 3]

Output:
r = [3, 2, 1]
[input] integer n

length of the permutations

[input] array.integer p

[input] array.integer q

[output] array.integer

permutation r"""


def findPermutation(n, p, q):
    r = []
    for element in q:
        r.append(p.index(element)+1)
        n-=1
        if n==0:
            return r