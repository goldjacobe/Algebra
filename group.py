from binstruct import BinStruct
from math import gcd
from permutation import Permutation
import itertools as it
import graphviz as gv


class Group(BinStruct):
    def __init__(self, the_set, rule):
        BinStruct.__init__(self, the_set, rule)
        if not self.is_group():
            raise ValueError("not a group")
        self.size = len(the_set)
        self.orders = {}
        for x in the_set:
            self.orders[x] = self.find_order(x)
        self.generators = [x for x in self.the_set if self.orders[x] ==
                           self.size]

    def find_order(self, x):
        counter = 1
        current = x
        while current != self.get_identity():
            current = self.rule[current, x]
            counter += 1
        return counter

    def find_subsets_order(self, n):
        l = [x for x in map(set, it.combinations(self.the_set, n)) if
             self.get_identity() in x]
        return l

    def find_divisors(self):
        l = []
        for i in range(1, len(self.the_set)):
            if len(self.the_set) % i == 0:
                l.append(i)
        return l

    def find_proper_subgroups(self):
        s = []
        l = self.find_divisors()
        for d in l:
            m = self.find_subsets_order(d)
            for h in m:
                is_sg = True
                for a in h:
                    for b in h:
                        if self.rule[(a, self.get_inverse(b))] not in h:
                            is_sg = False
                if is_sg:
                    s.append(Group(h, self.rule))
        return s

    def is_abelian(self):
        for a in self.the_set:
            for b in self.the_set:
                if self.rule[a, b] != self.rule[b, a]:
                    return False
        return True

    def is_cyclic(self):
        if len(self.generators) > 0:
            return True
        return False

    def __eq__(self, other):
        if len(self.the_set) != len(other.the_set):
            return False
        l = list(self.the_set)
        i = l.index(self.get_identity())
        temp = l[0]
        l[0] = l[i]
        l[i] = temp
        m = list(other.the_set)
        i = m.index(other.get_identity())
        temp = m[0]
        m[0] = m[i]
        m[i] = temp
        for x in create_symmetric_group(len(l)).the_set:
            is_isom = True
            if x.map[1] == 1:
                fun = {l[j]: m[x.map[j + 1] - 1] for j in range(len(l))}
                for o in l:
                    for p in l:
                        if fun[self.rule[(o, p)]] != other.rule[(fun[o],
                                                                 fun[p])]:
                            is_isom = False,
                if is_isom:
                    return True
        return False

    def cayley_graph(self, *gens):
        g = gv.Digraph(format='png')
        for x in self.the_set:
            g.node(str(x))
        for gen in gens:
            for y in self.the_set:
                for z in self.the_set:
                    if z == self.rule[y, gen]:
                        g.edge(str(y), str(z), label=str(gen))
        g.render("img/g", view=True)




def create_additive_group(n):
    the_set = set(range(n))
    rule = {(a, b): ((a + b) % n) for a in the_set for b in the_set}
    return Group(the_set, rule)


def create_multiplicative_group(n):
    the_set = set([x for x in range(n) if gcd(x, n) == 1])
    rule = {(a, b): ((a * b) % n) for a in the_set for b in the_set}
    return Group(the_set, rule)


def gen_perm_arrs(n):
    if n == 1:
        return [[1]]
    else:
        out = []
        one_lower = gen_perm_arrs(n-1)
        for perm in one_lower:
            for i in range(n):
                out.append(perm[0:i] + [n] + perm[i:n-1])
        return out


def create_symmetric_group(n):
    the_set = set([Permutation(x) for x in gen_perm_arrs(n)])
    rule = {(a, b): a * b for a in the_set for b in the_set}
    return Group(the_set, rule)


def create_alternating_group(n):
    the_set = set([Permutation(x) for x in gen_perm_arrs(n) if Permutation(
        x).is_even()])
    rule = {(a, b): a * b for a in the_set for b in the_set}
    return Group(the_set, rule)