import copy
import sys

eq = input()
eq2 = eq
eq_varnings = list()
eq = " " + eq + " "
eq = eq.replace("~", " not ")
eq = eq.replace("∨", " or ")
eq = eq.replace("∧", " and ")
eq = eq.replace("[", "(")
eq = eq.replace("]", ")")
eq = eq.replace("{", "(")
eq = eq.replace("}", ")")

for i in range(len(eq)):
    if eq[i] in " ()^":
        continue
    if eq[i + 1] in " ()" and eq[i - 1] in " ()" and eq[i] not in eq_varnings:
        eq_varnings.append(eq[i])

eq_varnings.sort()

for eqIndex in eq_varnings:
    sys.stdout.write(eqIndex + '\t')

print(eq2)
print()

for eqIndex in range(pow(2,len(eq_varnings))):
    vals = str(bin(eqIndex)).replace('0b','').zfill(len(eq_varnings))

    for value in vals:
        sys.stdout.write(value + '\t')

    eq_varnings_copy = copy.deepcopy(eq_varnings)
    for i in range(len(eq_varnings_copy)):
        eq_varnings_copy[i] += " = " + vals[i]
        exec(eq_varnings_copy[i])

    table = "result = eq"
    table = table.replace('eq', eq)
    exec(table)
    if result:
        print(1)
    else:
        print(0)