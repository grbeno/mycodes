
# long dict
coords = { 'coords': [ '132,34', '147,87', '206,86', '217,139', '171,149', '187,210', '116,232', '182,575', '436,497', '281,79' ] }

# get 'coords' key values and split them to tuples
split_coords_to_int = [ tuple(map(int, i.split(','))) for i in coords['coords'] ]

# results
print(split_coords_to_int)

" split_coords_to_int >> [(132, 34), (147, 87), (206, 86), (217, 139), (171, 149), (187, 210), (116, 232), (182, 575), (436, 497), (281, 79)] "