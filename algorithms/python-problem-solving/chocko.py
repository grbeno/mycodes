# HackerRank - 1 Month Interview Preparation Kit - Week 1 - Subarray Division 1

# Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
# Lily decides to share a contiguous segment of the bar selected such that:
# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.

# Az 's' tömb egy tábla csokit szemléltet, a számelemek pedig a kockákon olvashatók. Hány olyan folytonos sort (m=8 hosszú sor) törhetünk, amely a (d=26)-t adja eredményül, 
# vagyis a tömbnek hány olyan 8 elemű, folytonos résztömbje van, aminek az összege 26?
# 3 megoldás / 3 solution

s = [2, 3, 4, 4, 2, 1, 2, 5, 3, 4, 4, 3, 4, 1, 3, 5, 4, 5, 3, 1, 1, 5, 4, 3, 5, 3, 5, 3, 4, 4, 2, 4, 5, 2, 3, 2, 5, 3, 4, 2, 4, 3, 3, 4, 3, 5, 2, 5, 1, 3, 1, 4, 2, 2, 4, 3, 3, 3, 3, 4, 1, 1, 4, 3, 1, 5, 2, 5, 1, 3, 5, 4, 3, 3, 1, 5, 3, 3, 3, 4, 5, 2] #[2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
d = 26
m = 8

i,c,=0,0
while i < len(s):
    if sum(s[i:i+m]) == d:
        c+=1
    i+=1
print(c)

res = filter(lambda x: x==d, map(lambda x: sum(s[x:x+m]), range(len(s))))
print(len(list(res)))

test = len(list(filter(lambda x: x==d, [sum(s[i:i+m]) for i in range(len(s))])))
print(test)

test2 = list(map(lambda x: sum(s[x:x+m]) == d, range(len(s)))).count(True)
print(test2)