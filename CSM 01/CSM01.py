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
    elif n % 10 > n // 10 % 10 or n // 10 % 10 == 0:
        return False
    else:
        return is_sorted(n // 10)

def tree(label, branches=[]):

    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)
t = tree(1,
[tree(3,
[tree(4),
tree(5),
tree(6)]),
tree(2)])
x = tree('*', [tree(2), tree(3)])
def help(x):
    for b in branches(x):
        print(b)
    return b

def sqaure_tree(t):
    if is_leaf(t):
        if is_leaf(t):
            return  tree(label(t))
        else:
            return (label(t) ** 2 , [tree_max(b) for b in branches(t)])
sqaure_tree(t)

def eval_with_add(t):
    """Evaluate an expression tree of * and + using only
    addition.
    >>> plus = Tree('+', [Tree(2), Tree(3)])
    >>> eval_with_add(plus)
    5
    >>> times = Tree('*', [Tree(2), Tree(3)])
    >>> eval_with_add(times)
    6
    >>> deep = Tree('*', [Tree(2), plus, times])
    >>> eval_with_add(deep)
    60
    >>> eval_with_add(Tree('*'))
    1
    """
    if label(t) == '+':
        return sum([label(b) for b in branches(t)])
    elif label(t) == '*':
        total = 1
        for b in branches(t):
            total, term = 0, total
            for i in range(label(b)):
                total = total + term
        return total
    else:
        return label(t)

def height(t):
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(b)for b in branches(t)])
s = tree(4,[tree(5),tree(2)])
def find_path(tree, x):
    if label(tree) == x:
        return [label(tree)]
    paths = [find_path(b, x) for b in branches(tree)]
    for path in paths:
        if path:
            return [label(tree)] + path
t = [3,[1,[2]],[4]]
def tree_size(t):
    if is_leaf(t):
        return 1
    else:
        return 1 + [tree_size(branch)for branch in branches(t)]
def prune(t, k):
    if k == 0:
         return [label(t)]
    else:
        return [label(t)] + [prune(branch, k - 1)for branch in branches(t)]

class A():
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return self.x
    def __str__(self):
        return self.x * 2
class B():
    def __init__(self):
        print("boo!")
        self.a = []
    def add_a(self, a):
        self.a.append(a)
    def __repr__(self):
        print(len(self.a))
        ret = ""
        for a in self.a:
            ret += str(a)
        return ret
