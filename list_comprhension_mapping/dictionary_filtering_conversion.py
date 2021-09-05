
coords = { 'coords': '12,45', 'test': '5,67' } 

# solution 1.
res = []  # list
for k,v in coords.items():
    elem = float(v.replace(',','.'))
    res.append(elem)  # add to list
res = tuple(res)
print(res)

# solution 2.
res2 = map(lambda v: float(v.replace(',','.')), coords.values())

# results
print(tuple(res2))

""" res >> (12.45, 5.67)
    tuple(res2) >> (12.45, 5.67) """