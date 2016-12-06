class Permutation(object):
    def __init__(self, arr):
        self.map = {}
        for i in arr:
            self.map[arr.index(i) + 1] = i
        self.size = len(arr)

    def __str__(self):
        left = [x + 1 for x in list(range(self.size))]
        out = ""
        while len(left) > 0:
            start = left.pop(0)
            out += "(" + str(start)
            current = self.map[start]
            while current != start:
                left.remove(current)
                out += " " + str(current)
                current = self.map[current]
            out += ")"
            if out[-3] == '(':
                out = out[:-3]
        if out == "":
            out = str("1")
        return out

    def __mul__(self, other):
        new_arr = [self.map[other.map[i]] for i in [x + 1 for x in list(
                range(self.size))]]
        return Permutation(new_arr)

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        out = 1
        for i in self.map.keys():
            out *= 9 * i + 27 * self.map[i]
        return out

    def is_even(self):
        current_num = 0
        for i in range(len(str(self))):
            if str(self)[i] == "(":
                num_spaces = 0
                while str(self)[i] != ")":
                    if str(self)[i] == " ":
                        num_spaces += 1
                    i += 1
                current_num += num_spaces
        return current_num % 2 == 0
