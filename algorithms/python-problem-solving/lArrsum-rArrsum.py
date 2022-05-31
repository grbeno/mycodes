# HackerRank - 1 Month Interview Preparation Kit - Week 2 - Sherlock and Array

# Watson gives Sherlock an array of integers. 
# His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.

arr = [5,6,8,11] #[5,6,8,11] #[1,1,4,1,1] #[2,0,0,0] #[5,6,8,11]

# (left) arr[0] + arr[1] -> 5 + 6 = (right) arr[3] -> 11 ->> 11 = 11 !

c = sum(arr)

if arr[0] == c:
    print('YES')

l,r=0,0
y=0
for i in range(len(arr)-1):
    l = l + arr[i]
    r = c - l - arr[i+1]
    if l == r:
        y = 1

if y == 1:
    print('YES')
else:
    print('NO')
    



