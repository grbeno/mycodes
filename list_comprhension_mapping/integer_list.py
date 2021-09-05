
# list of integers
my_ints = [ 2, 3, 5, 6, 11, 3, 5, 1 ]

# with list comprehension
my_flts = [ float(i) for i in my_ints ]

# without loop, with map & lambda
my_mp = map(lambda x: float(x), my_ints)

# results
print(my_flts)
print(list(my_mp))

""" my_flts >> [2.0, 3.0, 5.0, 6.0, 11.0, 3.0, 5.0, 1.0] 
    list(my_mp) >> [2.0, 3.0, 5.0, 6.0, 11.0, 3.0, 5.0, 1.0] """