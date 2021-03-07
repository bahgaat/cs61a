"""Lab 1: Expressions and Control Structures"""
from operator import add

# Coding Practice

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    "*** YOUR CODE HERE ***"
    def square(x):
        return x * x
    while n!= 0:
        new_square = square(x)
        x = new_square
        n = n - 1
    return x

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    list_of_int = []
    convert_int_to_str = str(n)
    convert_str_to_list = list(convert_int_to_str.strip())
    for letter in convert_str_to_list :
        convert_letter_to_int = int(letter)
        list_of_int.append(convert_letter_to_int)
    sum_list = sum(list_of_int)
    return sum_list



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    former_int = 0
    convert_int_to_str = str(n)
    convert_str_to_list = list(convert_int_to_str.strip())
    for letter in convert_str_to_list:
        convert_letter_to_int = int(letter)
        new_int = convert_letter_to_int
        if new_int and former_int == 8:
            former_int = new_int
            return True
        else:
            former_int = new_int
    return False
