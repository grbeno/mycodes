import math

# HackerRank - 1 Month Interview Preparation Kit - Week 2 - Max Min

# min ( max(arr') - min(arr') )
# n elemű halmazból kiválasztott, k elemű részhalmaz-pár legkisebb különbségének megtalálása

arr = [1,2,3,4,10,20,30,40,100,200] # [100,200,300,350,400,401,402] -> 2; [1,4,7,2] -> 1; [1,2,3,4,10,20,30,40,100,200] -> 3
k = 4 # 3 # 2

arr.sort()
res=math.pow(10, 9) - 1 # 10^9 is the maximum of arr[i]!

i=0
while i <= len(arr) - k:
	unfairness = arr[i+k-1] - arr[i]
	if res > unfairness:
		res = unfairness # will be the smallest in the end
	i+=1

print(res)