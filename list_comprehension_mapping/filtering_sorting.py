
# list with condition, sorting 1st and 0 values
coords = [102.79, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.82, 21.31, 61.21, 13.27, 0.4, 0.0, 0.0, 0.0]

# with list comprehension
coords_li = [i for i in coords[1:] if i > 0]

# without loop, with filter & lambda
coords_fi = filter(lambda x: x > 0, coords[1:])

# results
print(sorted(coords_li))
print(list(sorted(coords_fi)))

""" sorted(coords_li) >> [0.4, 3.82, 13.27, 21.31, 61.21]
    list(sorted(coords_fi)) >> [0.4, 3.82, 13.27, 21.31, 61.21] """