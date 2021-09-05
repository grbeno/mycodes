
# list of comma separated strings
strs = [ '217,139', '171,149', '187,210', '116,232', '182,575' ]

# with list comprehension
strs_to_float_li = [ float(i.replace(',','.')) for i in strs ]

# without loop, with map & lambda
strs_to_float_mp = map(lambda x: float(x.replace(',','.')), strs)

# results
print(strs_to_float_li)
print(list(strs_to_float_mp))

""" strs_to_float_li >> [217.139, 171.149, 187.21, 116.232, 182.575]
    list(strs_to_float_mp) >> [217.139, 171.149, 187.21, 116.232, 182.575] """