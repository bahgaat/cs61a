


def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print(link)
    <1 2 3>
    >>> insert(link, 9001, 0)
    >>> print(link)
    <9001 1 2 3>
    >>> insert(link, 100, 2)
    >>> print(link)
    <9001 1 100 2 3>
    >>> insert(link, 4, 5)
    IndexError
    """

    if index == 0:
        link.rest = Link(link.first, link.rest)
        link.first = value
    elif link.rest is Link.empty:
        raise IndexError
    else:
        insert(link.rest, value, index - 1)
# Link Class
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

def subset_sum(lst, k):
    if k == 0:
        return True
    elif len(lst) == 0 or k < 0:
        return False
    else:
        return subset_sum(lst[1:], k - lst[0]) or subset_sum(lst[1:], k)

def accumulate(iterable, f):
    it = iter(iterable)
    result = next(it)
    yield result
    for x in it:
        result = f(result, x)
        yield result

def leap ( pots ):
    """ Return the maximal value of collecting pots that are not adjacent .
    >>> leap ([2 , 4 , 3]) # Collect 2 and 3
    5
    >>> leap ([4 , 20 , 9 , 3 , 6 , 2]) # Collect 20 and 6
    26
    """
    if len(pots) <= 2:
        return max(pots)
    return max(pots[0] + max(pots[2:]), leap(pots[1:]))

def triangle_sum( tri):
    rows = len( tri)
    def partial_sum(r, k):
        if rows <= 0:
            return 0
        else:
            return tri[r][k] + max( partial_sum(r+1, k), partial_sum(r+1, k +1))
    return partial_sum(0, 0)

def pascal_row(s):
    """
    >>> a = Link.empty
    >>> for _ in range(5):
    ... a = pascal_row(a)
    ... print(a)
    <1>
    <1 1>
    <1 2 1>
    <1 3 3 1>
    <1 4 6 4 1>
    """
    if s is Link.empty:
        return Link(1)
    start = Link(1)
    last, current = start, s
    while current.rest is not Link.empty:
        start = Link(current.first + current.rest.first, last)
        last = start
        current = current.rest
    start = Link(1, start)
    return start

def scurry(f, n):
    """Return a function that calls f on a list of arguments after being called n times.
    >>> scurry(sum, 4)(1)(1)(3)(2) # equivalent to sum([1, 1, 3, 2])
    7
    >>> scurry(len, 3)(7)([8])(-9) # equivalent to len([7, [8], -9])
    3
    """
    def h(k, args_so_far):
        if k == 0:
            return f(args_so_far)
        return lambda x: h(k - 1, [x] + args_so_far)
    return lambda x: h(n - 1, [x])
