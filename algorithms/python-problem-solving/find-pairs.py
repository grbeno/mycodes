# HackerRank - 1 Month Interview Preparation Kit - Week 2 - Sales by Match

# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, 
# determine how many pairs of socks with matching colors there are.

# How many pairs are there?
# 3 solutions

ar = [10,20,20,10,10,30,50,10,20]
st = list(set(ar))
res = 0

for i in range(len(st)):
    res = res + int(ar.count(st[i])/2)
print(res)

res = map(lambda x: int(ar.count(x)/2),st)
print(sum(res))

res = sum(map(lambda x: int(ar.count(x)/2),st))
print(res)