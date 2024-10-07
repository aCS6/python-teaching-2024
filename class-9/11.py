ls = [8,7,4,3,10]

#  Only reverse (no sorting)
ls2 = list(reversed(ls))
# print(ls2)

# sort
ls1 = sorted(ls)

# Ascending order (from smaller to greater)
# print(ls1)

# Descending order (from greater to smaller)

# Approach-1
ls3 = list(reversed(ls1))
# print(ls3)

# Approach-2
ls4 = sorted(ls, reverse=True)
print(ls4)

