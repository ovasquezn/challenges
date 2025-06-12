# Codeforces 
# A. Team (231A)
# 10/06/25

n = int(input())
contador=0
for _ in range(n):
    a, b, c = map(int, input().split())
    list = [a,b,c]
    if a+b+c>=2:
        contador+=1
print(contador)
