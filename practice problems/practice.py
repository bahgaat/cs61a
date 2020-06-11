import itertools
from itertools import zip_longest

class BST:
    """
    >>> bst1 = BST(4, BST(2, BST(1)))
    >>> bst1.max()
    4
    >>> bst1.min()
    1
    >>> bst2 = BST(6, BST(2, BST(1), BST(4)), BST(7, BST.empty, BST(9)))
    >>> bst2.max()
    9
    >>> bst2.min()
    1
    >>> 9 in bst2
    True
    >>> 10 in bst2
    False
    >>> bst3 = BST(6, BST(2, BST(1), BST(4)), BST(8, BST(7), BST(9)))
    >>> 7 in bst3
    True
    >>> 10 in bst3
    False
    """
    empty = ()

    def __init__(self, label, left=empty, right=empty):
        assert left is BST.empty or isinstance(left, BST)
        assert right is BST.empty or isinstance(right, BST)

        self.label = label
        self.left, self.right = left, right

        if left is not BST.empty:
            assert left.max() <= label
        if right is not BST.empty:
            assert label < right.min()

    def is_leaf(self):
        return self.left is BST.empty and self.right is BST.empty

    def __repr__(self):
        if self.is_leaf():
            return 'BST({0})'.format(self.label)
        elif self.right is BST.empty:
            left = repr(self.left)
            return 'BST({0}, {1})'.format(self.label, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BST.empty:
                left = 'BST.empty'
            template = 'BST({0}, {1}, {2})'
            return template.format(self.label, left, right)

    def max(self):
        """Returns max element in BST."""
        if self.right is BST.empty:
            return self.label
        return self.right.max()

    def min(self):
        """Returns min element in BST."""
        if self.left is BST.empty:
            return self.label
        return self.left.min()

    def __contains__(self, e):
        if self.label == e:
            return True
        elif e > self.label and self.right is not BST.empty:
            return e in self.right
        elif self.left is not BST.empty:
            return e in self.left
        return False

def gcd(x, y):

    """
    >>> gcd(20, 4)
    4
    >>> gcd(21, 81)
    3
    """
    if x == y:
        return x
    elif x > y:
        return gcd(x - y, y)
    else:
        return gcd(x, y - x)

def binary_search(item, lst):
    """
    >>> l = [1, 4, 5, 8, 10, 12]
    >>> binary_search(4, l)
    True
    >>> binary_search(9, l)
    False
    """
    middle = len(lst) // 2
    if lst[middle] == item:
        return True
    if middle == 0:
        return False
    elif lst[middle] < item:
        return binary_search(item, lst[middle:])
    else:
        return binary_search(item, lst[:middle])




def merge_sort(lst):
    """
    Takes in a list and returns the sorted version of it.

    >>> p = [1, 34, 2, 5, 3]
    >>> merge_sort(p)
    [1, 2, 3, 5, 34]
    """
    length_list = len(lst)
    def helper(lst, counter):
        if counter + 1 == length_list:
            return lst
        for i in range(len(lst[counter:])):
            if lst[counter] > lst[i + counter]:
                lst[counter], lst[i + counter] = lst[i + counter], lst[counter]
        return helper(lst, counter + 1)
    return helper(lst, 0)

def merge(l1, l2):
    """
    Takes in two sorted lists and returns a single sorted
    list by merging the elements of both lists together.

    >>> r = [1, 3, 5, 6]
    >>> l = [1, 2, 4, 5]
    >>> merge(l, r)
    [1, 1, 2, 3, 4, 5, 5, 6]
    """
    return merge_sort(l1 + l2)


def mutable_reverse(lst):
    """
    >>> l = [1, 4, 5, 1, 4]
    >>> mutable_reverse(l)
    >>> l
    [4, 1, 5, 4, 1]
    >>> l = [1, 4, 5, 1, 4, 5]
    >>> mutable_reverse(l)
    >>> l
    [5, 4, 1, 5, 4, 1]
    """
    last_index = len(lst) - 1
    def helper(lst, counter):
        if last_index // 2 < counter:
            lst = lst
        else:
            lst[counter], lst[last_index - counter] = lst[last_index - counter], lst[counter]
            return helper(lst, counter + 1)
    return helper(lst, 0)



def subsetsum(array,num):
    """Return the first subset of array that adds to num, or 'NOPE' if none exist.
    >>>subsetsum([1,3,5,7], 9).sorted()
    [1,3,5]
    >>>subsetsum([1,3,5,7], 2)
    'NOPE'
    """
    print('array')
    print(array)
    print('num')
    print(num)

    if num < 0:
      return 'NOPE'
    elif len(array) == 0:
      return 'NOPE'
    else:
      if array[0] == num:
        return [array[0]]
      else:
        with_v = subsetsum(array[1:],(num - array[0]))
        if with_v != 'NOPE':
          return [array[0]] + with_v
        else:
          return subsetsum(array[1:],num)

def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps or jumps to reach the end of the level without ever landing in a Piranha plant. Assume that every level begins and ends with a dash.
    >>> mario_number('-P-P-')   # jump, jump
    1
    >>> mario_number('-P-P--')   # jump, jump, step
    1
    >>> mario_number('--P-P-')  # step, jump, jump
    1
    >>> mario_number('---P-P-') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number('-P-PP-')  # Mario cannot jump two plants
    0
    >>> mario_number('----')    # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number('----P----')
    9
    >>> mario_number('---P----P-P---P--P-P----P-----P-')
    180
    """
    print(level)
    print('')
    if len(level) == 0 or level[0] == 'P':
        return 0
    elif len(level) <= 2:
        return 1
    else:
        return mario_number(level[1:]) + mario_number(level[2:])

def can_win(number):
    """Returns True if the current player is guaranteed a win
    starting from the given state. It is impossible to win a game
    from an invalid game state.

    >>> can_win (-1) # invalid game state
    False
    >>> can_win (3) # take all three !
    True
    >>> can_win (4)
    False
    """
    print(number)
    print('')
    if number <= 0:
        return False
    action = 1
    while action <= 3:
        new_state = number - action
        if not can_win ( new_state ):
            return True
        action += 1
    return False


def geo_sum(a, r, n):
    """Returns the first n elements of a geometric series.

    >>> geo_sum(1, 1/2, 4)  # 1 + 1/2 + 1/4 + 1/8
    1.875
    >>> geo_sum(2, 2, 3)  # 2 + 4 + 8
    14
    """
    if n == 0:
        return 0
    else:
        return a + geo_sum(a * r, r, n - 1)

def num_primes(n):
    """
    Returns the number of primes less than or equal to n.

    >>> num_primes(6)   # 2, 3, 5
    3
    >>> num_primes(13)  # 2, 3, 5, 7, 11, 13
    6
    """
    def helper(n, count):
        if n == 1:
            return count
        else:
            if is_prime(n):
                return helper(n - 1, count + 1)
            else:
                return helper(n - 1, count)
    return helper(n, 0)

def is_prime(i):
    m = 2
    while m * m <= i:
        if i % m == 0:
            return False
        m += 1
    return True


def any(a, b, pred):
    """Returns True if any numbers from a to b inclusive satisfy
    pred.

    >>> any(2, 4, lambda x: x % 2 == 0)
    True
    >>> any(-5, 2, lambda x: x * x == -3 * x)   # -3 satisfies pred
    True
    >>> any(1, 6, lambda x: x % 7 == 0)
    False
    >>> any(0, 6, lambda x: x % 7 == 0)
    True
    """
    if a == b:
        return False
    elif pred(a):
        return True
    else:
        return any(a + 1, b, pred)

def any_2(a, b, pred):
    if a == b:
        return pred(a)
    else:
        return pred(b) or any(a, b - 1, pred)


class Tree_2:
    def __init__(self, label, branches=[]):
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
            tree_str = ' ' * indent + str(t.label) + '\n'
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

def replace_leaves_sum(t):
    """
    >>> t = Tree(1, [Tree(3, [Tree(2), Tree(8)]), Tree(5)])
    >>> replace_leaves_sum(t)
    >>> t
    Tree(1, [Tree(3, [Tree(6), Tree(12)]), Tree(6)])
    """
    def helper(t, total):
        if t.is_leaf():
            print(total)
            print('u')
            t.label = total + t.label
        else:
            for b in t.branches:
                helper(b, total + t.label )
    return helper(t, 0)

def delete_path_duplicates(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(1), Tree(1)])])
    >>> delete_path_duplicates(t)
    >>> t
    Tree(1, [Tree(2, [Tree(-1), Tree(-1)])])
    >>> t2 = Tree(1, [Tree(2), Tree(2, [Tree(2, [Tree(1)])])])
    >>> delete_path_duplicates(t2)
    >>> t2
    Tree(1, [Tree(2), Tree(2, [Tree(-1, [Tree(-1)])])])
    """
    def helper(t, list):
        if t.label in list:
            t.label = -1
        else:
            list += [t.label]
        for b in t.branches:
            helper(b, list)
    return helper(t, [])

def max_tree(t):
    if t.is_leaf():
        return Tree(t.label)
    new_branches = [max_tree(b)for b in t.branches]
    root = max([t.label] + [b.label for b in new_branches])
    return Tree(root, new_branches)

def size(t):
    """Returns the number of elements in a tree.

    >>> t1 = Tree(1,
    ...           [Tree(2, [Tree(4)]),
    ...            Tree(3)])
    >>> size(t1)
    4
    """
    if t.is_leaf():
        return 1
    else:
        return 1 + sum([size(b)for b in t.branches])

def same_shape(t1, t2):
    if t1 and not t2:
        return False
    if t2 and not t1:
        return False
    else:
        x = [same_shape(branch1, branch2) for branch1, branch2 in list(itertools.zip_longest(t1.branches, t2.branches))]
        if False in x:
            return False
        else:
            return True

def sprout_leaves(t, vals):
    if t.is_leaf():
        t.branches = [Tree(v)for v in vals]
    else:
        for b in t.branches:
            sprout_leaves(b, vals)


def prune_leaves(t, vals):

    if t.is_leaf():
        if t.label in vals:
            return None
        else:
            return Tree(t.label)
    else:
        branches = [prune_leaves(b, vals)for b in t.branches]
        for i in branches[:]:
            if i == None:
                branches.remove(i)
        return Tree(t.label, branches)


def leaves(t):
    """Returns a list of all the labels of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    if t.is_leaf():
        return [t.label]
    else:
        branches = []
        for b in t.branches:
            branches += leaves(b)
        return branches

def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    def helper(t, count):
        labels = [b.label for b in t.branches]
        for b in t.branches:
            if count % 2 == 0:
                b.label = labels.pop()
            helper(b, count + 1)
    return helper(t, 0)


def long_paths(t, n):
    """Return a list of all paths in t with length at least n.

    >>> long_paths(Tree(1), 0)
    [[1]]
    >>> long_paths(Tree(1), 1)
    []
    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> print(whole)
    0
      1
        2
        3
          4
          4
          5
      13
      6
        7
          8
        9
      11
        12
          13
            14
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    [0, 1, 2]
    [0, 1, 3, 4]
    [0, 1, 3, 4]
    [0, 1, 3, 5]
    [0, 6, 7, 8]
    [0, 6, 9]
    [0, 11, 12, 13, 14]
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    [0, 1, 3, 4]
    [0, 1, 3, 4]
    [0, 1, 3, 5]
    [0, 6, 7, 8]
    [0, 11, 12, 13, 14]
    >>> long_paths(whole, 4)
    [[0, 11, 12, 13, 14]]
    """
    if t.is_leaf():
        if n <= 0:
            return [[t.label]]
        else:
            return []
    list = []
    for b in t.branches:
        for leaf in long_paths(b, n - 1):
            list.append([t.label] + leaf)
    return list

def add_d_leaves(t, v):
    """Add d leaves containing v to each node at every depth d.

    >>>t1 = Tree(1, [Tree(3)])
    >>> add_d_leaves(t1, 4)
    >>> t1
    Tree(1, [Tree(3, [Tree(4)])])
    >>> t2 = Tree(2, [Tree(5), Tree(6)])
    >>> t3 = Tree(3, [t1, Tree(0), t2])
    >>> add_d_leaves(t3, 10)
    >>> print(t3)
    3
      1
        3
          4
            10
            10
            10
          10
          10
        10
      0
        10
      2
        5
          10
          10
        6
          10
          10
        10
    """
    def helper(t, degree):
        for b in t.branches:
            helper(b, degree + 1)
        list = [Tree(v) for _ in range(degree)]
        t.branches.extend(list)
    return helper(t, 0)

def find_path(t, x):
    """
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if t.label == x:
        return [t.label]
    else:
        list = []
        for b in t.branches:
            path = find_path(b, x)
            if path:
                return [t.label] + path

def level_order_2(t):
    """"
    >>> t = Tree(3, [Tree(7, [Tree(2, [Tree(8), Tree(1)]), Tree(5)])])
    >>> level_order(t)
    [3 7 5 2 8 1]
    >>> level_order(tree(3))
    [3]
    >>> level_order(None)
    []
    """
    if not t:
        return []
    current_level, next_level = [t.label], [t]
    while next_level:
        find_next = []
        for b in next_level:
            find_next.extend(b.branches)
        next_level = find_next
        current_level.extend([t.label for t in next_level])
    return current_level

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).
    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(Tree(2, [Tree(4, [Tree(6)])]))
    [2, 4, 6]
    """
    list = [t.label]
    for b in t.branches:
        list.extend(preorder(b))
    return list

class Tree(object):
    """ A tree with internal values. """

    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        args = repr(self.entry)
        if self.left or self.right:
            args += ', {0}, {1}'.format(repr(self.left), repr(self.right))
        return 'Tree({0})'.format(args)

    def print(self):
        def print_helper(tree, depth):
            if tree.right:
                print_helper(tree.right, depth + 1)
            print("{0}{1}".format("\t" * depth, tree.entry))
            if tree.left:
                print_helper(tree.left, depth + 1)
        print_helper(self, 0)


def flip_tree(tree):
    """ Swaps the left and right branches of a tree.
    Does not create a new tree and mutates the original.

    >>> t = Tree(5, Tree(1, None, Tree(4)), Tree(7, Tree(6), Tree(8)))
    >>> flip_tree(t)
    >>> t
    Tree(5, Tree(7, Tree(8), Tree(6)), Tree(1, Tree(4), None))
    """
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left
    flip_tree(tree.left)
    flip_tree(tree.right)


def in_order_traversal(t):
    """
    >>> t = Tree(5, Tree(1, None, Tree(4)), Tree(7, Tree(6), Tree(8)))
    >>> in_order_traversal(t)
    1
    4
    5
    6
    7
    8
    """
    if t.left is None:
        print(t.entry)
        return in_order_traversal(t.right)
    else:
        return in_order_traversal(t.right)
        print(t.entry)

def count_upt(n):
    if n == 1:
        print(1)
    else:
        print(n)
        count_upt(n - 1)

def multiply(m, n):
    if n == 1:
        return m
    else:
        return m + multiply(n - 1, m)

def  cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

def f(n):
    if n == 0:
        return 0
    else:
        return f(n - 1) + f(n - 1)

def iter_fib(n):
    x = 1
    prev = 0
    curr = 1
    while x < n:
        curr, prev = prev + curr, curr
        x += 1
    return curr

def count_stairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return count_stairs(n - 2) + count_stairs(n - 1)

def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """

    if n == 0:
        return 1
    if n < 0:
        return 0
    if k == 0:
        return 0
    return count_k(n - k, k ) + count_k(n, k - 1)

def mystery(n):
    if n == 0:
        return 0
    else:
        return n + mystery(n - 1)

def foo(n):
    if n < 0:
        return 0
    return foo(n - 2) + foo(n - 1)

def fooply(n):
    if n < 0:
        return 0
    return fooply(n) + fooply(n - 1)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False
    otherwise.
    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def mario_number(level):
    if level == 1:
        return 1
    elif level % 10  == 0:
        return 0
    else:
        return mario_number(level // 10) + mario_number(level // 100)

def all_true(lst):
    """
    >>> all_true([True, 1, "True"])
    True
    >>> all_true([1, 0, 1])
    False
    >>> all_true([])
    True
    """
    if lst == []:
        return True
    elif lst[0] == False or lst[0] == 0:
        return False
    else:
        return all_true(lst[1:])

def is_sorted(n):
    """
    >>> is_sorted(2)
    True
    >>> is_sorted(22222)
    True
    >>> is_sorted(9876543210)
    True
    >>> is_sorted(9087654321)
    False
    """
    if n < 10:
        return True
    elif n % 10 > n // 10 % 10:
        return False
    else:
        return is_sorted(n // 10)

def add_up(n, lst):
    """
    >>> add_up(6, [1, 2, 3, 4, 5])
    True
    >>> add_up(8, [2, 1, 5, 4, 3])
    True
    >>> add_up(-1, [1, 2, 3, 4, 5])
    False
    >>> add_up(100, [1, 2, 3, 4, 5])
    False
    """
    if sum([i for i in lst]) == n:
        return True
    if lst == []:
        return False
    else:
        first, rest = add_up(n, lst[1:]), add_up(n, lst[0:len(lst) - 1])
        return first or rest

def repeat_digits(n):
    """Given a positive integer N, returns a number with each digit repeated.
    >>> repeat_digits(1234)
    11223344
    """
    last, rest = n % 10, n // 10
    if last == 0:
        return 0
    else:
        return repeat_digits(rest) * 100 + last * 11

def make_editor(n, pr):
    """Return an editor for N.
    >>> f = make_editor(2018, lambda n: print('n is now', n))
    >>> f = f(delete(3)) # delete the last 3 digits from the end of 2018
    n is now 2
    >>> f = f(insert(4, 0)) # insert digit 4 at the end of 2 (position 0)
    n is now 24
    >>> f = f(insert(3, 1)) # insert digit 3 in the middle of 24 (position 1)
    n is now 234
    >>> f = f(insert(1, 3)) # insert digit 1 at the start of 234 (position 3)
    n is now 1234
    >>> f = make_editor(123, print)(delete(10)) # delete 10 digits from the end of 123
    0
    """
    def editor(edit):
        result = edit(n)
        print(pr(result))
        return make_editor(result, pr)
    return editor

def insert(d, k):
    def edit(n):
        if k == 0:
            return n + 10 * d
        else:
            return n + 10 * insert(d, k -1)(n // 10)
    return edit
delete = lambda k :  n // 10 ** k


def collapse(n):
    """For non-negative N, the result of removing all digits that are equal
    to the digit on their right, so that no adjacent digits are the same.
    >>> collapse(1234)
    1234
    >>> collapse(12234441)
    12341
    >>> collapse(0)
    0
    >>> collapse(3)
    3
    >>> collapse(11200000013333)
    12013
    """
    left, last = n // 10, n % 10
    if n < 10:
        return last
    elif last == left % 10:
        return collapse(n // 10)
    else:
        return collapse(n // 10) * 10 + last

def confirmer(code):
    """Return a confirming function for CODE.
    >>> confirmer(204)(2)(0)(4) # The digits of 204 are 2, then 0, then 4.
    True
    >>> confirmer(204)(2)(0)(0) # The third digit of 204 is not 0.
    False
    >>> confirmer(204)(2)(1) # The second digit of 204 is not 1.
    False
    >>> confirmer(204)(20) # The first digit of 204 is not 20.
    False
    """
    def confirm1(d, t):
        def result(digit):
            if d == digit:
                return t
            else:
                return False
        return result
    def extend(prefix, rest):
        """Return a confirming function that returns REST when given the digits of PREFIX.
        For example, if c = extend(12, confirmer(34)), then c(1)(2) returns confirmer(34),
        so that c is a confirming function for 1234."""
        left, last = prefix // 10, prefix % 10
        if prefix < 10 :
            return confirm1(prefix, rest)
        else:
            return extend(left, confirm1(last, rest))
    return extend(code, True)

def decode(f, y=0):
    """Return the code for a confirming function f.
    >>> decode(confirmer(12001))
    12001
    >>> decode(confirmer(56789))
    56789
    """
    d = 0
    while d < 10:
        x, code = f(d), y * 10 + d
        if x == True:
            return code
        elif x == False:
            d += 1
        else:
            return decode(x, code)

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
    x = 0
    for element in lst:
        if type(element) == int:
            if element - x == 1 or x == 0:
                x, total = element, total + element
        else:
            result.append(compress(element))
    result.append(total)
    return result
def correspond(A , B , M ):
    """ Assuming A and B are lists of strings with len(A) == len(B), and M
    is an integer , returns true iff there is a sequence of indices into A
    and B , (i1 , i2 , ... , im ) , where 1 <= m <= M , such that
    A[ i1] + A [ i2 ] + ... + A[ im ] == B [ i1 ] + B[ i2 ] + ... + B[ im ].
    """
    N = len( A)
    def can_correspond (sa , sb , M, count ):
        if M <= 0:
            return False
        else :
            for i in range(N):
                ta = sa + A[i]
                tb = sb + B[i]
                if ta == tb :
                    return True
                elif can_correspond ( ta, tb , M - 1 ):
                    return True
            return False
    return can_correspond (" " , "" , M)


def subsequence (l , s ):
    """
    Returns true if s is a subsequence of l.
    >>> subsequence ([9 , 1 , 4 , 5 , 6] , [4 , 5 , 6])
    True
    >>> subsequence ([3 , 5 , 0 , 3 , 4 , 3 , 7 , 9 , 3 , 2] , [3 , 3 , 9 , 2])
    True
    >>> # Below , the numbers in seq2 appear in seq1 ,
    >>> # but not in the same order .
    >>> subsequence ([3 , 5 , 5 , 8 , 3] , [8 , 5 , 3])
    False
    >>> # Below , not all the numbers in seq2 are present in seq1 .
    >>> subsequence ([3 , 5 , 5 , 8 , 3] , [3 , 2 , 8])
    False
    >>> subsequence ([3 , 2 , 57 , 8] , [3 , 5 , 7])
    False
    """
    if s == []:
        return True
    elif l == []:
        return False
    elif l[0] == s[0] :
        return subsequence ( l[1:] , s[1:] )
    else :
        return subsequence ( l[1:] , s )

def significant (n , k ):
    """ Return the K most significant digits of N.
    >>> significant (12345 , 3)
    123
    >>> significant (12345 , 7)
    12345
    """
    if 10 ** k > n:
        return n
    return significant ( n // 10 , k)

def multiadder ( n ):
    """ Return a function that takes N arguments , one at a time , and adds them .
    >>> f = multiadder (3)
    >>> f (5)(6)(7) # 5 + 6 + 7
    18
    >>> multiadder (1)(5)
    5
    >>> multiadder (2)(5)(6) # 5 + 6
    11
    >>> multiadder (4)(5)(6)(7)(8) # 5 + 6 + 7 + 8
    26
    """

    assert n > 0
    if n == 1:
        return lambda x : x
    else :
        return lambda a: lambda b: multiadder(n - 1) (a + b)

def decompose1 (f , h ):
    """ Return g such that h(x) equals f(g(x)) for any non - negative integer x.
    >>> add_one = lambda x: x + 1
    >>> square_then_add_one = lambda x: x * x + 1
    >>> g = decompose1 ( add_one , square_then_add_one )
    >>> g (5)
    25
    >>> g (10)
    100
    """
    def g ( x ):
        def r ( y ):
            if y == x:
                return h(x) - f(x) + y
            else:
                return r(y + 1)
        return r(0)
    return

from operator import add , mul
def combine (n , f , result ):
    """ Combine the digits in non - negative integer n using f.
    >>> combine (3 , mul , 2) # mul (3 , 2)
    6
    >>> combine (43 , mul , 2) # mul (4 , mul (3 , 2))
    24
    >>> combine (6502 , add , 3) # add (6 , add (5 , add (0 , add (2 , 3)))
    16
    >>> combine (239 , pow , 0) # pow (2 , pow (3 , pow (9 , 0)))
    8
    """
    if n == 0:
        return result
    else :
        return combine ( n // 10, f ,f(n % 10, result) )

square = lambda x : x * x
double = lambda x : 2 * x
def memory (x , f ):
    """ Return a higher - order function that prints its memories .
    >>> f = memory (3 , lambda x: x)
    >>> f = f( square )
    3
    >>> f = f( double )
    9
    >>> f = f( print )
    6
    >>> f = f( square )
    3
    None
    """
    def g ( h ):
        print ( f(x) )
        return memory(x, h)
    return g

def decrypt (s , d ):
    """ List all possible decoded strings of s.
    >>> codes = {
    ... 'alan ’: ’spooky ’,
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
    if s == "":
        return []
    ms = []
    if s == d.key():
        ms . append ( d[s] )
        for k in s:
            first , suffix = s [: k ] , s [ k :]
            if first == d.key() :
                for rest in suffix :
                    ms.append ( d[first] + decrypt(rest, d) )
        return ms

def kbonacci(n, k):
    """ Return element N of a K- bonacci sequence .
    >>> kbonacci (3, 4)
    1
    >>> kbonacci (9, 4)
    29
    >>> kbonacci (4, 2)
    3
    >>> kbonacci (8, 2)
    21
    """
    if n < k - 1:
        return 0
    elif n == k - 1:
        return 1
    else:
        total = 0
        i = 1
        while i < n:
            total = total + kbonacci(n - i, k )
            i=i+1
        return total
def combine(left , right):
    """ Return all of LEFT ’s digits followed by all of RIGHT ’s digits ."""
    factor = 1
    while factor <= right:
        factor = factor * 10
    return left * factor + right
def reverse(n):
    """ Return the digits of N in reverse .
    >>> reverse (122543)
    345221
    """
    if n < 10:
        return n
    else:
        return combine( n % 10, reverse(n // 10))
def remove(n, digit):
    """ Return all digits of N that are not DIGIT , for DIGIT less than 10.
    >>> remove (243132, 3)
    2412
    >>> remove (243132, 2)
    4313
    >>> remove ( remove (243132, 1), 2)
    433
    """
    removed = 0
    while n != 0:
        y, n = n % 10, n // 10
        if y != digit :
            removed = removed * 10 + y
    return reverse(removed)

def if_fn(condition):
    if condition:
        return lambda a, b: a
    else:
        return lambda a, b: b
def factorial(n):
    """ Compute N! for non - negative N. N! = 1 * 2 * 3 * ... * N.
    >>> factorial (3)
    6
    >>> factorial (5)
    120
    >>> factorial (0)
    1
    """
    def base():
        return 1
    def recursive():
        return n * factorial(n-1)
    return if_fn(n)(recursive, base)()

def sabacc_winner(cards, player0, player1):
    """Returns the winner of a game of Sabacc if players can take 1 or 2 cards
    per turn and both players play optimally. Assume that it is player0's turn.
    >>> sabacc_winner(0, 'Han', 'Lando')
    'Han'
    >>> sabacc_winner(1, 'Han', 'Lando')
    'Lando'
    >>> sabacc_winner(2, 'Han', 'Lando')
    'Han'
    >>> sabacc_winner(3, 'Han', 'Lando')
    'Han'
    >>> sabacc_winner(4, 'Han', 'Lando')
    'Lando'
    """
    if cards == 0:
        return player0
    if cards == 1:
        return player1
    one_card = sabacc_winner(cards - 1, player1, player0)
    two_card = sabacc_winner(cards - 2, player1, player0)
    if one_card == player0 or two_card == player0:
        return player0
    return player1

def sum_largest(n, k):
    """Return the sum of the K largest digits of N.
    >>> sum_largest(2018, 2) # 2 and 8 are the two largest digits (larger than 0 and 1).
    10
    >>> sum_largest(12345, 10) # There are only five digits, so all are included in the sum.
    15
    """
    if k == 0 or n == 0:
        return 0
    a = sum_largest(n // 10 , k -1) + n % 10
    b = sum_largest(n // 10, k)
    print("a")
    print(a)
    print("b")
    print(b)
    return max(a, b)
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
    elif a % 10 == b % 10  :
        return combo(a // 10, b // 10) * 10 + a % 10
    return min(combo(a , b // 10) * 10 + b % 10, combo(a // 10, b ) * 10 + a % 10)

def ways(start, end, k, actions):
    if start == end:
        return 1
    elif k == 0:
        return 0
    return sum([ways(f(start), end, k -1, actions) for f in actions])

def sums (n , k ):
    """ Return the ways in which K positive integers can sum to N.
    >>> sums (2 , 2)
    [[1 , 1]]
    >>> sums (2 , 3)
    []
    >>> sums (4 , 2)
    [[3 , 1] , [2 , 2] , [1 , 3]]
    >>> sums (5 , 3)
    [[3 , 1 , 1] , [2 , 2 , 1] , [1 , 3 , 1] , [2 , 1 , 2] , [1 , 2 , 2] , [1 , 1 , 3]]
    """
    if k == 1:
        return [[n]]
    y = []
    for x in range(1,n) :
        y . extend ([ s + [x] for s in sums ( n - x, k - 1 )])
    return y

def count_groupings(n):
    if n == 1:
        return 1
    total = 0
    i = 1
    while n > i:
        total += count_groupings(n - i) * count_groupings(i)
        i += 1
    return total

def no_eleven(n):
    """ Return a list of lists of 1 ’s and 6 ’s that do not contain 1 after 1.
    >>> no_eleven (2)
    [[6, 6], [6, 1], [1, 6]]
    >>> no_eleven (3)
    [[6, 6 , 6], [6, 6 , 1], [6, 1 , 6], [1, 6 , 6], [1, 6 , 1]]
    >>> no_eleven (4)[:4] # first half
    [[6, 6 , 6 , 6], [6, 6 , 6 , 1], [6, 6 , 1 , 6], [6, 1 , 6 , 6]]
    >>> no_eleven (4)[4:] # second half
    [[6, 1 , 6 , 1], [1, 6 , 6 , 6], [1, 6 , 6 , 1], [1, 6 , 1 , 6]]
    """
    if n == 0:
        return [[]]
    elif n == 1:
        return [[6],[1]]
    else:
        a, b = no_eleven(n - 1), no_eleven( n - 2 )
        return [[6] + s for s in a] + [  [1,6] + s for s in b]

from operator import mul
def square(x):
    return mul(x, x)
def print_square(x):
    print(mul(x, x))
def g(d):
    return print(d)

def alt (f , g , z ):
    while g ( z ) > 0 and z != 5:
        f , g = g , f
        z = g ( z )
    return z
def grow ( x ):
    return int (( x * 3) / 2)
def shrink ( x ):
    return x - 2
def flip ( x ):
    return int (10 / (x -2))


def make_zipper(f1, f2, sequence):
    """ Return a function of f1 and f2 composed based on sequence.
    >>> def increment(x):
    return x + 1
    >>> def square(x):
    return x * x
    >>> do_nothing = make_zipper(increment, square, 0)
    >>> do_nothing(2) # Don't call either f1 or f2, just return your input untouched
    2
    >>> incincsq = make_zipper(increment, square, 112)
    >>> incincsq(2) # increment(increment(square(2))), so 2 -> 4 -> 5 -> 6
    6
    >>> sqincsqinc = make_zipper(increment, square, 2121)
    >>> sqincsqinc(2) # square(increment(square(increment(2)))), so 2 -> 3 -> 9 -> 10 -> 100
    100
    """
    zipper = lambda x: x
    helper = lambda f, g: lambda x: f(g(x))
    print(helper)
    print("#")
    while sequence != 0:
        if sequence % 10 == 1:
            zipper = helper(f1, zipper)
        else:
            zipper = helper(f2, zipper)
        sequence = sequence // 10
    return zipper

def f(g):
    if g == 0:
        return 1
    else:
        return

def rect(area, perimeter):
    """Return the longest side of a rectangle with AREA and PERIMETER that has integer sides.
    >>> rect(10, 14) # A 2 x 5 rectangle
    5
    >>> rect(5, 12) # A 1 x 5 rectangle
    5
    >>> rect(25, 20) # A 5 x 5 rectangle
    5
    >>> rect(25, 25) # A 2.5 x 10 rectangle doesn't count because sides are not integers
    False
    >>> rect(25, 29) # A 2 x 12.5 rectangle doesn't count because sides are not integers
    False
    >>> rect(100, 50) # A 5 x 20 rectangle
    20
    >>> rect(5, 11)
    False
    >>> rect(4, 11)
    False
    """
    side = 1
    while side * side <= area:
        other = round(area / side)
        if 2 * (side + other) == perimeter:
            return other
        side = side + 1
    return False

def repeat(k):
    """When called repeatedly, print each repeated argument.
    >>> f = repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    """
    return lambda i : lambda x: detector(k)(i)(k)

def detector(f):
    def g(i):
        if lambda k: f % 10 == i or f == 0:
            print(k)
            if f == 0:
                return repeat(k * 10 + i)
            else:
                print(i)
                return repeat(k * 10 + i)
        return detector(f // 10)(i)(k)
    return g
def eight_path(t):
    """Returns a path of the labels from the root to a leaf whose sum is a multiple of eight,
    or return None if no path exists.
    >>> t1 = tree(5, [tree(2),
    tree(1, [tree(3),
    tree(2)])
    ])
    >>> eight_path(t1)
    [5, 1, 2]
    >>> t2 = tree(9, [t1])
    >>> eight_path(t2)
    [9, 5, 2]
    """
    def helper(t, path_so_far):
        path_so_far += [t.label]
        if t.is_leaf():
            return path_so_far
        for b in t.branches:
            result = sum(helper(t, result) % 8) == 0
            if result:
                return path_so_far
    return helper(t, [])

def siblings(t):
    """Return a list of the labels of all nodes that have siblings in t.
    >>> a = Tree_2(4, [Tree_2(5), Tree_2(6), Tree_2(7, [Tree_2(8)])])
    >>> siblings(Tree_2(1, [Tree_2(3, [a]), Tree_2(9, [Tree_2(10)])])
    [3, 9, 5, 6, 7]
    """
    result = [b.label for b in t.branches if len(t.branches) >= 2 ]
    for b in t.branches:
        result += siblings(b)
    return result



class Sib(Tree_2):
    """A tree that knows how many siblings it has.
    >>> a = Sib(4, [Sib(5), Sib(6), Sib(7, [Sib(8)])])
    >>> a.label
    4
    >>> a.branches[1].label
    6
    >>> a.siblings
    0
    >>> a.branches[1].siblings
    2
    """
    def __init__(self, label, branches=[]):
        self.siblings = 0
        for b in branches:
            b.siblings += len(branches) - 1
        Tree_2.__init__(self, label, branches)

def longest_seq(t):
    """ The length of the longest downward sequence of nodes in T whose
    labels are consecutive integers.
    >>> t = Tree(1, [ Tree (2) , Tree(1, [ Tree (2, [ Tree(3, [ Tree (0)])])])])
    >>> longest_seq(t) # 1 -> 2 -> 3
    3
    >>> t = Tree (1)
    >>> longest_seq(t)
    1
    """
    max_len = 1
    def longest(t):
        nonlocal max_len
        n = 1
        if not t.is_leaf():
            for b in t.branches:
                longest(b)
                if b.label > t.label:
                    n = n + 1
            max_len = max(n, max_len)
        return n
    longest(t)
    return max_len
def complete(t, d, k):
    """ Return whether t is d-k-complete.
    >>> complete(Tree (1), 0, 5)
    True
    >>> u = Tree(1, [Tree (1), Tree (1), Tree (1)])
    >>> [ complete(u, 1, 3) , complete(u, 1, 2) , complete(u, 2, 3) ]
    [True , False , False]
    >>> complete(Tree(1, [u, u, u]), 2, 3)
    True
    """
    if not t.branches:
        return d == 0
    bs = [ complete(b ,d - 1, k) for b in t.branches]
    return k == len(bs) and all(bs)

def closest (t):

    diff = abs (sum([b for b in t.branches]))
    return min( diff,[closest(b)for b in t.branches])


def count_ways(t, total):
    """Return the number of ways that any sequence of consecutive nodes in a root-to-leaf path
    can sum to total.
    >>> t1 = Tree_2(5, [Tree_2(1, [Tree_2(2, [Tree_2(1)]),
    ... Tree_2(1, [Tree_2(4, [Tree_2(2, [Tree_2(2)])])])]),
    ... Tree_2(3, [Tree_2(2, [Tree_2(2),
    ... Tree_2(3)])]),
    ... Tree_2(3, [Tree_2(1, [Tree_2(3)])])])
    >>> count_ways(t1, 7)
    4
    >>> count_ways(t1, 4)
    6
    >>> t2 = tree(2, [tree(-10, [tree(12)]),
    ... tree(1, [tree(1),
    ... tree(-1, [tree(2)])])])
    >>> count_ways(t2, 2)
    6
    >>> count_ways(t2, 4)
    3
    """
    def paths(sub_t, sub_total, original_t, original_total):
        ways = 0
        if sub_total == 0:
            return 1
        ways += sum([paths(b, sub_total - t.label, t, total) for b in sub_t.branches])
        print(ways)
        if not original_t.is_leaf():
            ways+= [paths(b, total, b, total)for b in t.branches]
        return ways
    return paths(t, total, t, total)

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

def double1(L):
    """ Returns a list in which each item in L appears twice in sequence.
    It is non - destructive.
    >>> Q = Link(3, Link(4, Link (1)))
    >>> double1(Q)
    Link (3, Link(3, Link(4, Link(4, Link(1, Link (1))))))
    >>> Q
    Link (3, Link(4, Link (1)))
    >>> double1( Link. empty)
    ()
    """
    result = Link.empty
    last = None
    while L is not Link.empty:
        if last is None:
            result = Link(L.first, result)
            result, last = Link(L.first, result), 1
        else:
            result = Link(result, Link(L.first))
            result = Link(result, Link(L.first))
        L = L.rest
    return result


def double2(L):
    """ Destructively modifies L to insert duplicates of each item immediately
    following the item , returning the result .
    >>> Q = Link(3, Link(4, Link (1)))
    >>> double2(Q)
    Link (3, Link(3, Link(4, Link(4, Link(1, Link (1))))))
    >>> Q
    Link (3, Link(3, Link(4, Link(4, Link(1, Link (1))))))
    """
    result = L
    while L is not Link. empty:
        L.rest =  Link(L.first, L.rest)
        L = L.rest.rest
    return L

def naturals():
    i = 1
    while True:
        yield i
        i += 1

class Filter:
    def __init__(self , iterable , fn ):
        self.fn = fn
        self.iterator = iter(iterable)
    def __iter__( self ):
        return self
    def __next__( self ):
        for elem in self.iterator:
            if self.fn(elem):
                return elem

def expand(g, h, w, fill):
    for row in g:
        row.extend([fill for i in range(len(row), w)])
        print(row)
    for k in range(len(g), h):
        g.append([fill for i in range(w)])

    return g
tri = [
[ 1 ],
[ 2 , 1],
[-2, -1, 1],
[ 3, 3 , 1, 1]
]
def triangle_sum(tri):
    rows = len(tri)
    def partial_sum(r, k):
        if len(r) == 1:
            return r[0][k]
        else:
            return r[0][k] + max(partial_sum(r[1:], k), partial_sum(r[1:], k + 1))
    return partial_sum(tri , 0)
def leap(pots):
    if pots == []:
        return 0
    return max(max([pots[0] + b if b else 0 for b in pots[2:]]), leap(pots[1:]))


class Poll:
    s = []
    def __init__(self, n):
        self.name = n
        self.votes = {}
        Poll.s.append(self.votes)
    def vote(self, choice):
        self.votes[(self.name, choice)] = self.votes.get(self.name, 0) + 1 or 1

def tally(c):
    return [(pair[0][0], pair[1]) for pair in Poll.s if pair[0][1] == c]

def is_subseq(w1, w2):
    """ Returns True if w1 is a subsequence of w2 and False otherwise.
    >>> is_subseq("word", "word")
    True
    >>> is_subseq("compute", "computer")
    True
    >>> is_subseq("put", "computer")
    True
    >>> is_subseq("computer", "put")
    False
    >>> is_subseq("sin", "science")
    True
    >>> is_subseq("nice", "science")
    False
    is_subseq("boot", "bottle")
    False
    """
    print(w2)
    print("exit")
    if w1 == w2:
        return True
    elif w2 == "":
        return False
    else:
        with_elem =  True in [is_subseq(w1, w2[0:i] + w2[i + 1:])for i in range(len(w2)-1)if i > 0]
        without_elem = is_subseq(w1, w2[1:])
        return with_elem or without_elem

def tree(label, branches=[]):
    return [label] + list(branches)

def label(t):
    return t[0]

def is_leaf(t):
    return not branches(t)

def branches(t):
    return t[1:]

def max_path(t, k):
    """ Return a list of the labels on any path in tree t of length at most k with the greatest sum
    >>> t1 = tree(6, [tree(3, [tree(8)]), tree(1, [tree(9), tree(3)])])
    >>> max_path(t1, 3)
    [6, 3, 8]
    >>> max_path(t1, 2)
    [3, 8]
    >>> t2 = tree(5, [t1, tree(7)])
    >>> max_path(t2, 1)
    [9]
    >>> max_path(t2, 2)
    [5, 7]
    >>> max_path(t2, 3)
    [6, 3, 8]
    >>> max_path(t1, 4)
    [6, 3, 8]
    """
    def helper(t, k, on_path):

        if k == 0:
            return []
        elif is_leaf(t):
            return [label(t)]
        a = [[label(t)] + helper(b, k - 1, True) for b in branches(t)]
        #print(a)
        #print("exit")
        if on_path:
            #print("path")
            #print("eXit")
            return max(a , key = sum)
        else:
            b = [ helper(b, k, False)for b in branches(t) ]
            #print(b)
            #print("Exit")
            return max(a + b, key = sum)
    print("a7a")
    return helper(t, k, False)
def count_ways(t, total):
    """Return the number of ways that any sequence of consecutive nodes in a root-to-leaf path
    can sum to total.
    >>> t1 = tree(5, [tree(1, [tree(2, [tree(1)]),
    ... tree(1, [tree(4, [tree(2, [tree(2)])])])]),
    ... tree(3, [tree(2, [tree(2),
    ... tree(3)])]),
    ... tree(3, [tree(1, [tree(3)])])])
    >>> count_ways(t1, 7)
    4
    >>> count_ways(t1, 4)
    6
    >>> t2 = tree(2, [tree(-10, [tree(12)]),
    ... tree(1, [tree(1),
    ... tree(-1, [tree(2)])])])
    >>> count_ways(t2, 2)
    6
    >>> count_ways(t2, 4)
    3
    """
    def paths(t, total, can_skip):
        ways = []
        if total == label(t):
            ways.append(label(t))
        ways.append([[label(t)] + paths(b, total - label(t), False) for b in branches(t)])
        if can_skip:
            ways.extend ([paths(b, total, True) for b in branches(t)])
        return ways
    return paths(t, total, True)

def stable(s, k, n):
    """Return whether all pairs of elements of S within distance K differ by at most N.
    >>> stable([1, 2, 3, 5, 6], 1, 2) # All adjacent values differ by at most 2.
    True
    >>> stable([1, 2, 3, 5, 6], 2, 2) # abs(5-2) is a difference of 3.
    False
    >>> stable([1, 5, 1, 5, 1], 2, 2) # abs(5-1) is a difference of 4.
    False
    """
    for i in range(len(s)):
        near = range(i - k - 1, i)
        if True in ([True for j in near if abs(s[i] - s[j]) > n]):
            return False
    return True
