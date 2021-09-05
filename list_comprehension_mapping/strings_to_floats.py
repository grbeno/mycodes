
# list of strings
my_str = [ '2.12', '1.1', '3.14', '2.0', '4.566' ]

# with list comprehension
my_flts2 = [ float(i) for i in my_str ]

# without loop, with map & lambda
my_mp2 = map(lambda x: float(x), my_str)

# results
print(my_flts2)
print(list(my_mp2))

""" my_flts2 >> [2.12, 1.1, 3.14, 2.0, 4.566]
list(my_mp2) >> [2.12, 1.1, 3.14, 2.0, 4.566] """