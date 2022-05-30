# HackerRank - 1 Month Interview Preparation Kit - Week 1 - Mock Test - Find median

# https://en.wikipedia.org/wiki/Median

#arr = [2,3,5,3,4,5,1] # odd
arr = [5,6,7,1,1,12,8,10] # even

arr.sort()
if len(arr) % 2 == 0:
    print(round( (arr[round(len(arr)/2)] + arr[round(len(arr)/2)+1-1]) /2))
else:
    print(arr[round((len(arr)+1)/2)-1])