"""Create function-generator divisor that should return all divisors of the positive number.
If there are no divisors left function should return None.
three = divisor(3)
next(three) => 1
next(three) => 3
next(three) => None"""


def divisor(divised_num):
    n = 1
    divisors = []
    while n <= divised_num:
        if divised_num % n == 0:
            divisors.append(n)
        n += 1

    i = 0
    while True:
        if i < len(divisors):
            yield divisors[i]
            i += 1
        else:
            yield None