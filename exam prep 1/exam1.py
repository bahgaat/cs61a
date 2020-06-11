# Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)
def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
# Selectors
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
# For convenience
def is_leaf(tree):
    return not branches(tree)
t = tree(1,
[tree(3,
[tree(4),
tree(5)]),
tree(2)])
def sum_range(t):
    def helper(t):
        if is_leaf(t):
            return [label(t),label(t)]
        else:
            a = min([helper(branch)for branch in branches(t)])
            b = max([helper(branch)for branch in branches(t)])
            x = label(t)
            print(a)
            print(b)
            print(x)
            return [b + x, a + x]
    x, y = helper(t)
    return x - y

def no_eleven(n):
    """Return a list of lists of 1's and 6's that do not
    contain 1 after 1.
    >>> no_eleven(2)
    [[6, 6], [6, 1], [1, 6]]
    >>> no_eleven(3)
    [[6, 6, 6], [6, 6, 1], [6, 1, 6], [1, 6, 6], [1, 6, 1]]
    >>> no_eleven(4)[:4] # first half
    [[6, 6, 6, 6], [6, 6, 6, 1], [6, 6, 1, 6], [6, 1, 6, 6]]
    >>> no_eleven(4)[4:] # second half
    [[6, 1, 6, 1], [1, 6, 6, 6], [1, 6, 6, 1], [1, 6, 1, 6]]
    """
    if n == 0:
        return [[]]
    elif n == 1:
        return [[6],[1]]
    else:
        a, b = no_eleven( n - 1), no_eleven(n - 2)
        return [ [6] + s for s in a] + [[1] + [6]for s in b]

def combo(a, b):
    """Return the smallest integer with all of the digits of a and b (in order).
    >>> combo(531, 432) # 45312 contains both _531_ and 4_3_2.
    45312
    >>> combo(531, 4321) # 45321 contains both _53_1 and 4_321.
    45321
    >>> combo(1234, 9123) # 91234 contains both _1234 and 9123_.
    91234
    >>> combo(0, 321) # The number 0 has no digits, so 0 is not in the result.
    321
    """
    if a == 0 or b == 0:
        return a + b
    elif a % 10 == b % 10:
        return combo( a//10, b//10) * 10 + a % 10
    else:
        return min(combo(a // 10, b ) * 10 + a % 10,combo( a , b // 10)  * 10 +  b % 10)

def subset_sum(target , lst):
    """ Returns True if it is possible to add some of the integers in lst
    to get target .
    >>> subset_sum(10 , [-1, 5, 4, 6])
    True
    >>> subset_sum(4, [5, -2, 12])
    False
    >>> subset_sum(-3, [5, -2, 2, -2, 1])
    True
    >>> subset_sum(0, [-1, -3, 15]) # Sum up no numbers to get 0
    True
    """
    if target == 0:
        return True
    elif not lst:
        return False
    else:
        a = subset_sum(target - lst[0], lst[1:])
        b = subset_sum(target, lst[1:])
        return a or b

def ways(start, end, k, actions):
    """Return the number of ways of rea
    hing end from start by taking up to k a
    tions.
    >>> ways(-1, 1, 5, [abs, lambda x: x+2]) # abs(-1) or -1+2, but not abs(abs(-1))
    2
    >>> ways(1, 10, 5, [lambda x: x+1, lambda x: x+4]) # 1+1+4+4, 1+4+4+1, or 1+4+1+4
    3
    >>> ways(1, 20, 5, [lambda x: x+1, lambda x: x+4])
    0
    >>> ways([3, [2, 3, 2, 3, 4, [lambda x: [2+x, lambda x: 2*x, lambda x: x[:-1℄℄)
    3
    """
    if start == end:
        return 1
    elif k == 0:
        return 0
    return sum([ways(f(start), end, k - 1, actions) for f in actions])

def sums(n, k):
    """ Return the ways in which K positive integers can sum to N.
    >>> sums (2, 2)
    [[1 , 1]]
    >>> sums (2, 3)
    []
    >>> sums (4, 2)
    [[3 , 1], [2, 2], [1, 3]]
    >>> sums (5, 3)
    [[3 , 1, 1], [2, 2, 1], [1, 3, 1], [2, 1, 2], [1, 2, 2], [1, 1, 3]]
    """
    if k > n :
       return []
    y = []
    for x in range(k):
        y.extend ([ s + [1] for s in sums( n - 1, k - 1 )])
    return y

def repeat_digits(n):
    """Given a positive integer N, returns a number with each digit repeated.
    >>> repeat_digits(1234)
    11223344
    """
    last, rest = n % 10, n // 10
    if n == 0 :
        return 0
    return repeat_digits(rest) * 100 + last * 11

def thanos_messenger(word):
    """A messenger function that discards every other word.
    >>> thanos_messenger("I")("don't")("feel")("so")("good")(".")
    'I feel good.'
    >>> thanos_messenger("Thanos")("always")("kills")("half")(".")
    'Thanos kills.'
    """
    assert word != '.', 'No words provided!'
    def make_new_messenger(message, skip_next):
        def new_messenger(word):
            if word == '.':
                return message + word
            if skip_next % 2 == 0 :
                return make_new_messenger(message, skip_next + 1)
            return make_new_messenger(message + " " + word, skip_next + 1)
        return new_messenger
    return make_new_messenger(word,0)

def compress(lst):
    """Given a deep list of integers, return a new list compressing all neighboring integers.
    >>> compress([])
    []
    >>> compress([1, 2, 3])
    [6]
    >>> compress([0, 0, 0, 0])
    [0]
    >>> compress([1, 2, [3, 4]])
    [3, [7]]
    >>> compress([[11, 12], 3, 4, [1, 2], [5, 6], 7, 8, [9, 10]])
    [[23], 7, [3], [11], 15, [19]]
    >>> compress([1, 2, [3, [4, 5, 6], [7, 8], 9, 10], 11, 12])
    [3, [3, [15], [15], 19], 23]
    """
    total = 0
    result = []
    store = False
    for element in lst:
        if type(element) == int:
            total += element
            result += [total]
            #total = 0
        else:
            result += [compress(element)]
    #if store:
        #result += [total]
    return result


def decrypt (s , d ):
    """ List all possible decoded strings of s.
    >>> codes = {
    ... ’alan ’: ’spooky ’,
    ... ’al ’: ’drink ’,
    ... ’antu ’: ’your ’,
    ... ’turing ’: ’ghosts ’,
    ... ’tur ’: ’scary ’,
    ... ’ing ’: ’skeletons ’,
    ... ’ring ’: ’ovaltine ’
    ... }
    >>> decrypt ( ’ alanturing ’, codes )
    [ ’ drink your ovaltine ’, ’spooky ghosts ’, ’spooky scary skeletons ’]
    """
    if s == ’’:
        return []
    ms = []
    if s in d:
        ms.append (d[s])
    for k in range(1, len(s) + 1) :
        first , suffix = s [: k ] , s [ k :]
        if first in d:
            for rest in decrypt(suffix, d) :
                ms . append (d[first] + " " + rest)
    return ms

class Counter:
    """
    >>> dog = Counter([’ this ’, ’is ’, ’spot ’, ’see’, ’spot ’, ’run ’])
    >>> dog. counts [’ this ’]
    1
    >>> dog. counts [’ spot ’]
    2
    >>> ’catdog ’ in dog. counts
    False
    """
    def __init__(self , lst):
        self. counts = {}
        for i in lst:
            if i in self.counts:
                self.counts[i] = self.counts[i] + 1
            else:
                self.counts[i] = 1
        self.counts
