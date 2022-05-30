# HackerRank - 1 Month Interview Preparation Kit - Week 2 - Grid Challenge

# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. 
# Determine if the columns are also in ascending alphabetical order, top to bottom. 
# Return YES if they are or NO if they are not.

grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
n = len(grid)

# O(n^2) solution:

no=0
for i in range(n):
    l,col = '',''
    for s in grid:
        asc = ''.join(sorted(s))
        col = l + asc[i]
        l = col
    if ''.join(sorted(col)) != col:
        no = 1

# Evaluation
if no == 1:
    print('NO')
else:
    print('YES')

# O(n) solution:
rows = []
for s in grid:
    if ''.join(sorted(s)) != s: # check if it is not ordered ?
        s = ''.join(sorted(s))
    rows.append(s)

cols = zip(*rows) # transpose the array

no=0
for c in cols:
    if ''.join(sorted(c)) != ''.join(c): # check if it is not ordered
        no = 1

# Evaluation
if no == 1:
    print('NO')
else:
    print('YES')

