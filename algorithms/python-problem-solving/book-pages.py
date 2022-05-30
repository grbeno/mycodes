# HackerRank - 1 Month Interview Preparation Kit - Week 2 - Drawing Book

# n = pages of the book, p = the page to find <- you can turn the pages from the beginning or from the end of the book!

# 5,3 -> 1 # book with 5 pages, to find the 3rd! -> we have to turn at least 1 time!
# 4,4 -> 0
# 6,5 -> 1
# 6,2 -> 1
# 5,4 -> 0

n = 5
p = 4

if n % 2 != 0:
    n = n - 1
    
book = range(0,n)
from_begin, from_end = 0,0

for flip,i in enumerate(book):
    if i == p:
        from_begin = int(flip/2)

for flip,i in enumerate(book[::-1]):
    if i == p:
        from_end = int(flip/2)

if from_begin <= from_end:
    print(f"from begin: {from_begin}")
else:
    print(f"from end: {from_end+1}")