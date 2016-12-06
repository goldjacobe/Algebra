import group as g
import sys


def show_help():
    print("This is the command line interface for a group theory suite")
    print("There are three commands")
    print("$python3 main.py table [group]")
    print("$python3 main.py subgroups [group]")
    print("$python3 main.py cayley [group] [generators]")
    print("table prints the cayley table for the given group")
    print("subgroup prints the cayley tables for all proper subgroups")
    print("cayley prints the cayley graph, with generators as edges")
    print("the format for [group] is one of the following")
    print("Zn")
    print("Mn")
    print("Sn")
    print("An")
    print("Respectively, additive group of integers mod n, multiplicative "
          "group of integers mod n, symmetric group for n, alternating group "
          "for n")
    print("the format for [generators] of Zn or Mn are numbers separated by "
          "spaces")
    print("for Sn and An, enter permutations in python list notation")
    print('eg. "[4, 1, 3, 2]"')


def table(group):
    n = int(group[1:])
    grp = None
    if group[0] == "Z":
        grp = g.create_additive_group(n)
    elif group[0] == "M":
        grp = g.create_multiplicative_group(n)
    elif group[0] == "S":
        grp = g.create_symmetric_group(n)
    elif group[0] == "A":
        grp = g.create_alternating_group(n)
    grp.cayley_table()


def subgroups(group):
    n = int(group[1:])
    grp = None
    if group[0] == "Z":
        grp = g.create_additive_group(n)
    elif group[0] == "M":
        grp = g.create_multiplicative_group(n)
    elif group[0] == "S":
        grp = g.create_symmetric_group(n)
    elif group[0] == "A":
        grp = g.create_alternating_group(n)
    subs = grp.find_proper_subgroups()
    for sub in subs:
        sub.cayley_table()


def cayley(group, *gens):
    n = int(group[1:])
    grp = None
    if group[0] == "Z":
        grp = g.create_additive_group(n)
    elif group[0] == "M":
        grp = g.create_multiplicative_group(n)
    elif group[0] == "S":
        grp = g.create_symmetric_group(n)
    elif group[0] == "A":
        grp = g.create_alternating_group(n)
    grp.cayley_graph(*gens)


args = sys.argv

if args[1] == "help":
    show_help()
elif args[1] == "table":
    table(args[2])
elif args[1] == "subgroups":
    subgroups(args[2])
elif args[1] == "cayley":
    cayley(args[2], *map(int, args[3:]))