odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    ascci_sum_of_names = sum(ord(el) for el in input()) // row

    if ascci_sum_of_names % 2 == 0:
        even_set.add(ascci_sum_of_names)

    else:
        odd_set.add(ascci_sum_of_names)

sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)

if sum_even_set == sum_odd_set:
    print(*odd_set.union(even_set), sep=', ')
elif sum_even_set < sum_odd_set:
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')
