""" Lab 3: Recursion and Midterm Review """

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if b > a:
        b, a = a, b
    if b % a == 0:
        return b
    else:
        return gcd(a - b, b)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    if n == 1:
        print(n)
        return n
    elif n % 2 == 0:
        print(n)
        n = n // 2
    else:
        print(n)
        n = (n * 3) + 1
    return hailstone(n) + n // n
