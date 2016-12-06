import group as g
import time
import permutation as p


print("Cayley table for Z/10Z")
g.create_additive_group(10).cayley_table()
print()
print("Cayley table for (Z/10Z)*")
g.create_multiplicative_group(10).cayley_table()
print()
print("Cayley table for S3")
g.create_symmetric_group(3).cayley_table()
print()
print("Cayley table for A4")
g.create_alternating_group(4).cayley_table()
print()
print("Check to see if Z/3Z and A3 are isomorphic")
print(g.create_additive_group(3) == g.create_alternating_group(3))
print()
print("Cayley tables for all proper subgroups of Z/6Z")
for h in g.create_additive_group(6).find_proper_subgroups():
    h.cayley_table()
print()
print("Cayley tables for all proper subgroups of S3")
for i in g.create_symmetric_group(3).find_proper_subgroups():
    i.cayley_table()
print()
start = time.time()
print("Cayley tables for all proper subgroups of A4")
for i in g.create_alternating_group(4).find_proper_subgroups():
    i.cayley_table()
end = time.time()
elapsed = end - start
print("Time to perform this operation: " + str(elapsed))
print("A Cayley graph for S3")
g.create_symmetric_group(3).cayley_graph(p.Permutation([2, 1, 3]),
                                         p.Permutation([3, 1, 2]))