def prune_min(t):
    """Prune the tree mutatively from the bottom up.

    >>> t1 = Tree(6)
    >>> prune_min(t1)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_min(t2)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(3, [Tree(1), Tree(2)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_min(t3)
    >>> t3
    Tree(6, [Tree(3, [Tree(1)])])
    """
    if not t.is_leaf():
        if t.branches[0].label > t.branches[1].label:
            t.branches =  [t.branches[1]]
        else:
            t.branches =  [t.branches[0]]
        for b in t.branches:
            prune_min(b)

def eval_with_add ( t ):
    """ Evaluate an expression tree of * and + using only addition .
    >>> plus = Tree ( ’+ ’ , [ Tree (2) , Tree (3)])
    >>> eval_with_add ( plus )
    5
    >>> times = Tree ( ’* ’ , [ Tree (2) , Tree (3)])
    >>> eval_with_add ( times )
    6
    >>> deep = Tree ( ’* ’ , [ Tree (2) , plus , times ])
    >>> eval_with_add ( deep )
    60
    >>> eval_with_add ( Tree ( ’* ’))
    1
    """
    if t.label == '+':
        return sum([eval_with_add(b) for b in t.branches])
    elif t.label == '*':
        total = 1
        for b in t . branches :
            total, term = 0, eval_with_add(b)
            for _ in range(sum([eval_with_add(f) for f in t.branches[1:]])):
                total = total + term
        return total
    else :
        return t.label

# Tree Class
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

def is_palindrome(str):
    return  len(str) is len([str[i] for i in range(len(str)) if str[i] is str[len(str) - 1 - i]])

class TwoDIterator:
    def __init__(self, lst):
        self.lst = lst
        self.result = 0

    def __next__(self):
        if len(self.lst) == 0:
            raise StopIteration
        else:
            self.result = self.lst[0]
            if len(self.result) == 0:
                self.lst = self.lst[1:]
                return TwoDIterator.__next__(self)
            else:
                if len(self.lst[0][1:]) == 0:
                    self.lst = self.lst[1:]
                else:
                    self.lst = [self.lst[0][1:]] + self.lst[1:]
                return self.result[0]

    def __iter__(self):
        return self
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

def long_paths(tree, n):
    list = []
    if tree.is_leaf() and n <= 0:
        list.append(Link(tree.label))
    for b in tree.branches:
            for path in long_paths(b, n - 1):
                list.append(Link(tree.label, path))
    return list

def is_min_heap(t):
    for b in t.branches:
        if t.label > b.label:
            return False
    return False not in [is_min_heap(x) for x in t.branches]

class Network:
    """
    >>> cs61a_plus = Network()
    >>> cs61a_plus.add_friend('Robert', 'Jeffrey')
    >>> cs61a_plus.friends['Robert']
    ['Jeffrey']
    >>> cs61a_plus.friends['Jeffrey']
    ['Robert']
    >>> cs61a_plus.add_friend('Jessica', 'Robert')
    >>> cs61a_plus.friends['Robert']
    ['Jeffrey', 'Jessica']
    """
    def __init__(self):
        self.friends = {} # Maps users to a list of their friends
    def add_friend(self, user1, user2):
        if user1 not in self.friends:
            self.friends[user1] = []
        if user2 not in self.friends:
            self.friends[user2] = []
        self.friends[user1].append(user2)
        self.friends[user2].append(user1)

    def degrees(self, user1, user2, n):
        """
        >>> cs61a_plus = Network()
        >>> cs61a_plus.friends = {
        ... 'Robert': ['Jeffrey', 'Jessica'],
        ... 'Jeffrey': ['Robert', 'Jessica', 'Yulin'],
        ... 'Jessica': ['Robert', 'Jeffrey', 'Yulin'],
        ... 'Yulin': ['Jeffrey', 'Jessica'],
        ... 'Albert': []

        ... }
        >>> cs61a_plus.degrees('Robert', 'Yulin', 2) # Exactly 2 degrees
        True
        >>> cs61a_plus.degrees('Robert', 'Jessica', 2) # Less than 2 degrees
        True
        >>> cs61a_plus.degrees('Yulin', 'Robert', 1) # More than 1 degree
        False
        >>> cs61a_plus.degrees('Albert', 'Jessica', 10) # No friends!
        False
        """
        if user1 == user2:
            return True
        elif n <= 0 or user1 == 'Albert':
            return False
        for friend in self.friends[user1]:
            if friend == user2 and n >= 1:
                return True
        list = [Network.degrees(self, x, user2, n - 1) for x in self.friends[user1]]
        return any(list)



def triangle_sum( tri):


    tri = [ list( row) for row in tri ]
    rows = len( tri)
    r = rows - 2
    while rows > 1:
        for k in range (len( tri[r ])):
            tri[r][k] += max(tri[rows - 1][k], tri[rows - 1][k +1])
        r, rows = r - 1, rows - 1
    return tri [0][0]

class BinTree:
    empty = ()
    def __init__(self, label, left=empty, right=empty):
        self.label = label
        self.left = left
        self.right = right

def print_column(tree , col):
    """ Print the labels of the nodes in column COL of BinTree TREE ,
    in any order , one per line.
    >>> e = BinTree. empty
    >>> tree = BinTree(6,
    ... BinTree(3,
    ... BinTree(5, BinTree(9) , BinTree(2, e, BinTree(7))) ,
    ... BinTree(1)) ,
    ... BinTree(4, e, BinTree(0, BinTree(8))))
    >>> print_column(tree , -1)
    3
    2
    >>> print_column(tree , 2)
    0 """
    if tree is BinTree. empty :
        return
    if col == 0:
        print(tree.label)
    left = print_column(tree.left, col + 1)
    right = print_column(tree.right, col - 1)

def min_leaf_depth (t):
    """
    >>> t1 = Tree (2)
    >>> min_leaf_depth (t1)
    0
    >>> t2 = Tree (2, [ Tree (0) , Tree (1) , Tree (6)])
    >>> min_leaf_depth (t2)
    1
    >>> t3 = Tree (2, [ Tree (0) , t2 ])
    >>> min_leaf_depth (t3)
    1
    >>> t4 = Tree (2, [t2 , t3 ])
    >>> min_leaf_depth (t4)
    2
    """
    if t. is_leaf ():
        return 0
    else :
        c_depths = [ 1 + min_leaf_depth (c) for c in t. branches ]
        return  min ( c_depths)


class upseq_iter:
    def __init__(self , L):
        self.list = L

    def __iter__( self ): return self
    def __next__( self ):
        if not self.list:
            raise StopIteration
        r = self.list[0]
        self.list = self.list[1:]
        while self.list and self.list[0] < r:
            self.list = self.list[1:]
        return r
def upsubseq(L):
    """
    >>> list( upsubseq([4 , 2, 3, 6, 6, 5, 7, 1, 3]))
    [4, 6, 6, 7]
    >>> list( upsubseq([]))
    []
    """
    return upseq_iter(L)

class LoopJoin:
    """A database join iterator that takes in two iterables and joins their rows.
    >>> users = [(1, 'Kevin', '2017-05-19'), (2, 'Stan', '2017-06-20')]
    >>> sales = [('2017-07-20', 9580, 2), ('2017-07-24', 8483, 2)]
    >>> for row in LoopJoin(users, sales):
    ... print(row)
    (1, 'Kevin', '2017-05-19', '2017-07-20', 9580, 2)
    (1, 'Kevin', '2017-05-19', '2017-07-24', 8483, 2)
    (2, 'Stan', '2017-06-20', '2017-07-20', 9580, 2)
    (2, 'Stan', '2017-06-20', '2017-07-24', 8483, 2)
    """
    def __init__(self, left_iterable, right_iterable):
        self.left_iterator = iter(left_iterable)
        self.right_iterator = iter(right_iterable)
        self.left = next(self.left_iterator)
        self.right_iterable = right_iterable
    def __iter__(self):
        return self
    def __next__(self):
        try:
            right = next(self.right_iterator)
            row = self.left + right
            return row

        except StopIteration:
            self.right_iterator = iter(self.right_iterable)
            self.left = next(self.left_iterator)
        return next(self)

def split(s, pred):
    """Mutatively split s, returning one with elements that satisfy pred and one without.
    >>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> evens, odds = split(s, lambda x: x % 2 == 0)
    >>> evens
    Link(4, Link(2))
    >>> odds
    Link(5, Link(3, Link(1)))
    """
    satisfy, not_satisfy = Link.empty, Link.empty
    while s is not Link.empty:
        rest = s.rest
        if pred(s.first):
            result = satisfy
            satisfy = s
            satisfy.rest = result
        else:
            result = not_satisfy
            not_satisfy = s
            not_satisfy.rest = result
        s = rest
    return satisfy, not_satisfy


def same_level_order(tree, s):
    """Return True if and only if list s
    ontains the labels of tree in level order.
    >>> t = Tree(1, [Tree(2, [Tree(3), Tree(4)℄), Tree(5)℄)
    >>> same_level_order(t, [1, 2, 5, 3, 4℄)
    True
    >>> same_level_order(t, [1, 2, 3, 4, 5℄)
    False
    >>> same_level_order(t, [1, 2, 5, 3, 4, 6℄)
    False
    >>> same_level_order(t, [1, 2, 5, 3℄)
    False
    """
    k = 1
    for label in t.branches:
        if label.label != s[k] or not same_level_order(label, s[k:]):
             return False
        print(label.label)
        print("#")
        k += 1
    return True

def runts(t):
    """Return a list in any order of the labels of all runt nodes in t.
    >>> sorted(runts(Tree(9, [Tree(3), Tree(4, [Tree(5, [Tree(6)]), Tree(7)]), Tree(2)])))
    [2, 5, 6, 9]
    """
    result = []
    def g(node):
         if len(node.branches) >= 1:
             result.append(min([c.label for c in node.branches]))
    apply_to_nodes(g, t)
    return result + [t.label]
def apply_to_nodes(f, t):
    """Apply a function f to each node in a Tree instance t."""
    f(t)
    for b in t.branches:
        apply_to_nodes(f, b)

def max_label(t):
    """Return the largest label in t.
    >>> max_label(Tree(4, [Tree(5), Tree(3, [Tree(6, [Tree(1), Tree(2)])])]))
    6
    """

    def f(node):
        nonlocal t
        t = max(t, node, key=lambda n: n.label)
    apply_to_nodes(f, t)
    return t.label
