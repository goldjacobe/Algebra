from prettytable import PrettyTable


class BinStruct(object):
    def __init__(self, the_set, rule):
        self.the_set = the_set
        self.rule = rule

    def is_associative(self):
        for a in self.the_set:
            for b in self.the_set:
                for c in self.the_set:
                    if not self.rule[(a, self.rule[(b, c)])] == self.rule[(
                            self.rule[(a, b)], c)]:
                        return False
        return True

    def get_identity(self):
        for e in self.the_set:
            for x in self.the_set:
                if self.rule[(e, x)] == x and self.rule[(x, e)] == x:
                    return e
        return None

    def has_identity(self):
        return self.get_identity is not None

    def get_inverse(self, x):
        if not self.has_identity():
            return None
        for y in self.the_set:
            if self.rule[(x, y)] == self.get_identity() and self.rule[(y,
                                                                       x)] ==\
                    self.get_identity():
                return y
        return None

    def has_inverse(self, x):
        return self.get_inverse(x) is not None

    def has_inverses(self):
        for x in self.the_set:
            if not self.has_inverse(x):
                return False
        return True

    def is_group(self):
        if self.is_associative() and self.has_identity() and \
                self.has_inverses():
            return True

    def cayley_table(self):
        x = PrettyTable()
        x.header = False
        l = list(self.the_set)
        if self.has_identity():
            i = l.index(self.get_identity())
            temp = l[0]
            l[0] = l[i]
            l[i] = temp
        x.add_row([""] + [str(x) for x in l])
        for a in l:
            x.add_row([str(a)] + [str(self.rule[(a, b)]) for b in l])
        print(x)
