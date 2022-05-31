# HackerRank - 1 Month Interview Preparation Kit - Week 2 - Recursive Digit Sum

# In first recursion the x-length integer must be multipled by k! (e.g.) p = 9875 -> 9875987598759875
# Then we will get the sum of the digits of the n-integer (e.g.) 9+8+7+5 * 4 = 116
# 116 will be the next n, and the recursion have to continue until the n-integer consist of only one digit! <- 1+1+6 = 8. 8 is the superdigit!

def superDigit(n, k):
    s = str(n)
    if len(s) == 1:
        return n
    p = 0
    for d in s:
        p += int(d)        
    n = p * k
    k = 1
    return superDigit(n,k)

n = 9875 #148 #123
k = 4 #3 #3
print(superDigit(n,k))


    



