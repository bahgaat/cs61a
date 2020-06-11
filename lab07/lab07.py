""" Lab 07: Generators, Linked Lists, and Trees """

# Generators
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    for i in s:
        result = i * k
        yield result




# Linked Lists

def link_to_list(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    # iterative solution
    list = []
    while link != Link.empty:
        list.append(link.first)
        link = link.rest
    return list + []

    # recursive solution
    if link == Link.empty:
        return []
    else:
        return [link.first] + link_to_list(link.rest)


# Trees

def cumulative_sum(t):
    """Mutates t so that each node's label becomes the sum of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """

    for b in t.branches:
        cumulative_sum(b)
    t.label = sum([leaf.label for leaf in t.branches]) + t.label



def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """

    list = []
    if t.is_leaf():
        list.append(True)
    if len(t.branches) == 2:
        list.append('has_more_than_one_child')
    for b in t.branches:
        if b.is_leaf():
            list.append(True)
        elif len(b.branches) == 1:
            if 'has_more_than_one_child' in list:
                if b.label >= b.branches[0].label:
                    list.append(True)
                else:
                    list.append(False)
            else:

                list.append(True)
        elif len(b.branches) == 2:
            list.append('has_more_than_one_child')
            if b.label >= b.branches[0].label:
                list.append(True)
            else:
                list.append(False)
            if b.label < b.branches[1].label:
                list.append(True)
            else:
                list.append(False)
        elif len(branches) > 2:
            list.append(False)
    if False in list :
        return False
    else:
        return True

# Link List Class
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
# Tree ADT

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
def is_palindrome(seq):
    """ Returns True if the sequence is a palindrome. A palindrome is a sequence
    that reads the same forwards as backwards
    >>> is_palindrome(Link("l", Link("i", Link("n", Link("k")))))
    False
    >>> is_palindrome(["l", "i", "n", "k"])
    False
    >>> is_palindrome("link")
    False
    >>> is_palindrome(Link.empty)
    True
    >>> is_palindrome([])
    True
    >>> is_palindrome("")
    True
    >>> is_palindrome(Link("a", Link("v", Link("a"))))
    True
    >>> is_palindrome(["a", "v", "a"])
    True
    >>> is_palindrome("ava")
    True
    """
    n = 1
    last_seq = len(seq) - n
    for i in range(len(seq)):
        if seq[0] != seq[last_seq]:
            return False
        n = n + 1
    return True

def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk.rest is Link.empty:
        return lnk.first
    else:
        print(lnk)
        return lnk.first + sum_nums(lnk.rest)

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    product = 1
    for link in lst_of_lnks:
        if link is Link.empty:
            return Link.empty
        else:
            product *= link.first
    lst_of_lnks_rests = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_lnks_rests))

def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest

def filter_no_iter(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> list(filter_no_iter(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    if link is Link.empty:
        return
    if f(link.first):
        yield link.first
    yield from filter_no_iter(link.rest, f)

def sum_paths_gen(t):
    """
    >>> t1 = Tree(5)
    >>> next(sum_paths_gen(t1))
    5
    >>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(9)])
    >>> sorted(sum_paths_gen(t2))
    [6, 7, 10]
    """
    # official answer
    if t.is_leaf():
        yield t.label
    for b in t.branches:
        for s in sum_paths_gen(b):
            yield s + t.label

    # my answer
    i = 0
    if t.is_leaf():
        yield t.label
    for child in t.branches:
        n = 0
        n += child.label
        if child.is_leaf():
            yield child.label + t.label
        for ancestor in child.branches:
            n -= i
            i = ancestor.label
            n += i
            yield n + t.label



def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    """
    for b in t.branches:
        make_even(b)
    if t.label % 2 != 0:
        t.label += 1

def fill_tree(t, n):
    """
    >>> t0 = Tree(0, [Tree(1), Tree(2)])
    >>> t1 = fill_tree(t0, 5)
    >>> t1
    Tree(5, [Tree(5), Tree(5)])
    """
    if t.is_leaf():
        return Tree(n)
    else:
        return Tree(n, [fill_tree(b, n)for b in t.branches])

def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    return Tree(combiner(t1.label, t2.label),[combine_tree(b1, b2, combiner)for b1, b2 in zip(t1.branches, t2.branches)])

def average(t):
    """
    Returns the average value of all the labels in t.
    >>> t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
    >>> average(t0)
    1.5
    >>> t1 = Tree(8, [t0, Tree(4)])
    >>> average(t1)
    3.0
    """
    def helper(t, count):
        list = [t.label]
        for b in t.branches:
            print(list)
            print([])
            list.extend(helper(b, count + 1))
        return list
    return helper(t, 1)


def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    count = 1
    for b in t.branches:
        for leaf in alt_tree_map(b, map_fn):
            count += leaf
            print(count)
    return count

def is_min_heap(t):
    # one way
    x = [is_min_heap(b) if b.label > t.label else False for b in t.branches]
    if False in x:
        return False
    else:
        return True
    # second way
    for b in t.branches:
        list = []
        if b.label > t.label:
            list.append(is_min_heap(b))
        else:
            list.append(False)
        if False in list:
            return False
    return True

def largest_product_path(t):
    """
    >>> largest_product_path(None)
    0
    >>> largest_product_path(Tree(3))
    3
    >>> t = Tree(3, [Tree(7, [Tree(2)]), Tree(8, [Tree(1)]), Tree(4)])
    >>> largest_product_path(t)
    42
    """
    tree = t
    def helper(t):
        if not t:
            return 0
        result = t.label
        count = t.label
        list = []
        for b in t.branches:
            result = count * helper(b)
            list.append(result)
            print(list)
        if t == tree:
            if len(list) > 0:
                return max(list)
            else:
                return t.label
        else:
            return result
    return helper(t)

def largest_product_path_2(t):
    """
    >>> largest_product_path(None)
    0
    >>> largest_product_path(Tree(3))
    3
    >>> t = Tree(3, [Tree(7, [Tree(2)]), Tree(8, [Tree(1)]), Tree(4)])
    >>> largest_product_path_2(t)
    42
    """
    if not t:
        return 0
    elif t.is_leaf():
        return t.label
    else:
        paths = [largest_product_path_2(b) for b in t.branches]
        print(paths)
        return t.label * max(paths)

def largest_product_path_3(t):
    """
    >>> largest_product_path(None)
    0
    >>> largest_product_path(Tree(3))
    3
    >>> t = Tree(3, [Tree(7, [Tree(2)]), Tree(8, [Tree(1)]), Tree(4)])
    >>> largest_product_path_3(t)
    42
    """
    paths = []
    print([])
    if t.is_leaf():
        return t.label
    for b in t.branches:
        paths.append(largest_product_path_3(b))
        print(paths)
    if len(paths) > 0:
        return t.label * min(paths)
    else:
        return t.label

def contains(t, e):

    if t.label == e:
        return True
    for b in t.branches:
        if contains(b, e) == True:
            return True
        print(contains(b, e))
    return 2


def max_tree(t):
    """
    >>> max_tree(Tree(1, [Tree(5, [Tree(7)]),Tree(3,[Tree(9),Tree(4)]),Tree(6)]))
    Tree(9, [Tree(7, [Tree(7)]),Tree(9,[Tree(9),Tree(4)]),Tree(6)])
    """
    if t.is_leaf():
        return Tree(t.label)
    new_branches = [max_tree(b)for b in t.branches]
    new_label = max([t.label] + [leaf.label for leaf in new_branches])
    return Tree(new_label, new_branches)

def tree(t):

    list = []
    for b in t.branches:
        list.append(b.label)
        tree(b)
        print(list)
    return list

def level_order(t):
    def helper(t, count):
        if count == 1:
            list = [t.label]
        else:
            list = []
        for b in t.branches:
            list.append(b.label)
        for b in t.branches:
            list.extend(helper(b, count + 1))
        return list
    return helper(t, 1)


def all_paths(t):
    if t.is_leaf():
        return [[t.label]]
    list = []
    print(list)
    for b in t.branches:
        for s in all_paths(b):
            list.append([t.label] + s)
            print(list)
    return list

def all_paths_6(t):
    if t.is_leaf():
        return [t.label]
    list = []
    print(list)
    for b in t.branches:
        list.append([t.label] + all_paths_6(b))
        print(list)
    return list

def filter_tree(t, fn):
    """
    >>> t = Tree(1, [Tree(2), Tree(3, [Tree(4)]), Tree(6, [Tree(7)])])
    >>> filter_tree(t, lambda x: x % 2 != 0)
    >>> t
    tree(1, [Tree(3)])
    >>> t2 = Tree(2, [Tree(3), Tree(4), Tree(5)])
    >>> filter_tree(t2, lambda x: x != 2)
    >>> t2
    Tree(2)
    """

    if t.is_leaf():
        t.label = 0
    if not fn(t.label):
        t.label = 0
    for b in t.branches:
        filter_tree(b, fn)

def filter_tree_2(t, fn):

    if not fn(t.label):
        t.branches = []
    else:
        for b in t.branches[:]:
            print(b)
            print([])
            if not fn(b.label):
                t.branches.remove(b)
            elif b.is_leaf():
                t.branches.remove(b)
            else:
                filter_tree(b, fn)

def nth_level_tree_map(fn, tree, n):
    """Mutates a tree by mapping a function all the elements of a tree.
    >>> tree = Tree(1, [Tree(7, [Tree(3), Tree(4), Tree(5)]),
    Tree(2, [Tree(6), Tree(4)])])
    >>> nth_level_tree_map(lambda x: x + 1, tree, 2)
    >>> tree
    Tree(2, [Tree(7, [Tree(4), Tree(5), Tree(6)]),
    Tree(2, [Tree(7), Tree(5)])])
    """
    #tree.label = fn(tree.label)
    #def helper(tree, count):
        #print(count)
        #print([])
        #for b in tree.branches:
            #if count % n == 0:
                #b.label = fn(b.label)
            #helper(b, count + 1)
    #return helper(tree, 1)

    def helper(tree, level):
        if level % n == 0:
            print('label')
            print(tree.label)
            print('level')
            print(level)
            tree.label = fn(tree.label)
        for b in tree.branches:
            helper(b, level + 1)

    helper(tree, 0)

#def map_mut(f, L):
    """
    >>> L = [1, 2, 3, 4]
    >>> map_mut(lambda x: x**2, L)
    >>> L
    [1, 4, 9, 16]
    """
    #list = []
    #for i in L:
        #list.append(f(i))
    #return list
    #for i in L:
        #L[i] = f[L[i])


def make_max_finder():
    """
    >>> m = make_max_finder()
    >>> m([5, 6, 7])
    7
    >>> m([1, 2, 3])
    7
    >>> m([9])
    9
    >>> m2 = make_max_finder()
    >>> m2([1])
    1
    """
    counter = 0
    def helper(list):
        nonlocal counter
        max_num = max(list)
        if max_num > counter:
            counter = max_num
            return max_num
        else:
            return counter
    return helper


def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    def helper(link, sub_link):
        if sub_link is Link.empty:
            return False
        elif sub_link is link:
            return True
        else:
            return helper(link, sub_link.rest)
    return helper(link, link.rest)

def has_cycle_iteratively(link):
    original_link = link
    new_link = link.rest
    while new_link is not Link.empty:
        if new_link is original_link:
            return True
        new_link = new_link.rest
    return False

def seq_in_link(link, sub_link):
    """
    >>> lnk1 = Link(1, Link(2, Link(3, Link(4))))
    >>> lnk2 = Link(1, Link(4))
    >>> lnk3 = Link(4, Link(3, Link(2, Link(1))))
    >>> seq_in_link(lnk1, lnk2)
    True
    >>> seq_in_link(lnk1, lnk3)
    False
    """
    if sub_link is Link.empty:
        return True
    elif link is Link.empty:
        return False
    elif link.first != sub_link.first:
        return seq_in_link(link.rest, sub_link)
    elif link.first == sub_link.first:
        return seq_in_link(link.rest, sub_link.rest)

def infinity1(start):
    while True:
        start = start + 1
        return start
def infinity2(start):
    while True:
        start = start + 1
        yield start

def generate_constant(x):
    """A generator function that repeats the same value x forever.
    >>> area = generate_constant(51)
    >>> next(area)
    51
    >>> next(area)
    51
    >>> sum([next(area) for _ in range(100)])
    5100
    """
    while True:
        yield x

def black_hole(seq, trap):
    """A generator that yields items in SEQ until one of them matches TRAP, in which case that
    value should be repeatedly yielded forever.
    >>> trapped = black_hole([1, 2, 3], 2)
    >>> [next(trapped) for _ in range(6)]
    [1, 2, 2, 2, 2, 2]
    >>> list(black_hole(range(5), 7))
    [0, 1, 2, 3, 4]
    """
    for i in seq:
        if i == trap:
            x = generate_constant(i)
            return x
        else:
            yield i

def weird_gen(x):
    if x % 2 == 0:
        yield x * 2

def greeter(x):
    while x % 2 != 0:
        print('hi')
        yield x
        print('bye')

def gen_inf(lst):
    while True:
        return lst

def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even))
    [0 , 2 , 4]
    >>> all_odd = (2*y-1 for y in range (5))
    >>> list(filter(all_odd, is_even))
    []
    >>> s = filter(naturals(), is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for i in iterable:
        if fn(i):
            yield i

def tree_sequence(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
    >>> print(list(tree_sequence(t)))
    [1, 2, 5, 3, 4]
    """
    yield t.label
    for b in t.branches:
        yield from tree_sequence(b)


def make_digit_getter(n):
    """ Returns a function that returns the next digit in n
    each time it is called, and the total value of all the integers
    once all the digits have been returned.
    >>> year = 8102
    >>> get_year_digit = make_digit_getter(year)
    >>> for _ in range(4):
    ... print(get_year_digit())
    2
    0
    1
    8
    >>> get_year_digit()
    11
    """
    sum = 0
    def function():
        nonlocal n
        p = n
        n = n // 10
        x = p % 10
        sum += x
        if n > 0:
            return x
        else:
            return sum
    return function


def max_leaf(t):
    """Create a new Tree with every node being the maximum distance away that node is from a leaf node.
    >>>t = Tree(3, [Tree(4), Tree(4, [Tree(1)])])
    >>>new_t = max_leaf(t)
    >>>new_t.entry
    2 # The 3 node was 2 away from the 1 node
    >>>[b.entry for b in new_t.branches]
    [0 1]
    """
    if t.is_leaf():
        return Tree(0)
    else:
        b = []
        for branch in t.branches:
            b.append(max_leaf(branch))
        print(b)
        return Tree(max(branch.label for branch in b ) + 1, b)

def contains(t, elm):
    """Return True if tree contains element, false otherwise.
    >>>t = Tree(4, [Tree(5), Tree(5, [Tree(6)])])
    >>>t = Tree(3, [Tree(4), Tree(4, [Tree(1)])])
    >>>contains(t, 6) == True
    True
    >>>contains(t, 1) == False
    True
    """
    if t.label == elm:
        return True
    list = []
    for b in t.branches:
        if contains(b, elm):
            return True
    return False

def all_paths(t):
    """
    >>>t = Tree(4, [Tree(5), Tree(5, [Tree(6)])])
    >>>t2 = Tree(3, [Tree(4), Tree(4, [t])])
    """
    if t.is_leaf():
        return [[t.label]]
    list = []
    for b in t.branches:
        for leaf in all_paths(b):
            list.append(leaf)
    print(list)
    print('w')
    return [t.label] + list

def count_nodes(t):

    return 1 + min([count_nodes(b)for b in t.branches])

def list_leaves(t):
    if t.is_leaf():
        return [t.label]
    list= []
    for b in t.branches:
        list.extend(list_leaves(b))
    return list

def print_tree(t, indent = 0 ):
    print('  '  *  indent + str(t.label))
    for b in t.branches:
        print_tree(b, indent + 1)

def sum_of_nodes(t):
    """
    >>> t = tree(...) # Tree from question 2.
    >>> sum_of_nodes(t) # 9 + 2 + 4 + 4 + 1 + 7 + 3 = 30
    30
    """
    sum = t.label
    for b in t.branches:
        sum += sum_of_nodes(b)
    return sum

def replace_x(t, x):
    branches = []
    for b in t.branches:
        branches += [replace_x(b, x)]
    if t.label == x:
        return Tree(0, branches)
    else:
        return Tree(t.label, branches)




def replace_leaves_sum(t):
    """
    >>> t = Tree(1, [Tree(3, [Tree(2), Tree(8)]), Tree(5)])
    >>> replace_leaves_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(6), Tree(12)]), Tree(6)])
    """
    def helper(t, list ):
        if t.is_leaf():
            t.label = sum(list) + t.label
        else:
            for b in t.branches:
                helper(b, list.append(t.label))
    return helper(t, [])


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
