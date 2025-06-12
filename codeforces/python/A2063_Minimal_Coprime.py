
# Today, Little John used all his savings to buy a segment. He wants to build a house on this segment.
# A segment of positive integers [𝑙,𝑟] is called coprime if 𝑙 and 𝑟 are coprime∗.

# A coprime segment [𝑙,𝑟] is called minimal coprime if it does not contain† any coprime segment not equal to itself. To better understand this statement, you can refer to the notes.

# Given [𝑙,𝑟], a segment of positive integers, find the number of minimal coprime segments contained in [𝑙,𝑟].

# ∗Two integers 𝑎 and 𝑏 are coprime if they share only one positive common divisor. For example, the numbers 2 and 4 are not coprime because they are both divided by 2 and 1, but the numbers 7 and 9 are coprime because their only positive common divisor is 1.
# †A segment [𝑙′,𝑟′] is contained in the segment [𝑙,𝑟] if and only if 𝑙≤𝑙′≤𝑟′≤𝑟.
# Input
# Each test contains multiple test cases. The first line contains the number of test cases 𝑡 (1≤𝑡≤100). The description of the test cases follows.

# The only line of each test case consists of two integers 𝑙 and 𝑟 (1≤𝑙≤𝑟≤109).

# Output
# For each test case, output the number of minimal coprime segments contained in [𝑙,𝑟], on a separate line.

# Example
# inputCopy
# 6
# 1 2
# 1 10
# 49 49
# 69 420
# 1 1
# 9982 44353
# outputCopy
# 1
# 9
# 0
# 351
# 1
# 34371

# Note
# In the first test case, the only minimal coprime segment is [1,2].

# In the second test case, the minimal coprime segments are [1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10].

# In the third test case, there are no minimal coprime segments contained in [49,49].

# In the fourth test case, the minimal coprime segments are [69,70],[69,71],[69,72],...,[69,420].

# In the fifth test case, the only minimal coprime segment is [1,1].

# Solution

# Let's consider the segment [l,r]. We can see that the number of minimal coprime segments contained in [l,r] is equal to the number of minimal coprime segments contained in [1,r] minus the number of minimal coprime segments contained in [1,l−1].

# Let's consider the segment [1,r]. We can see that the number of minimal coprime segments contained in [1,r] is equal to the number of minimal coprime segments contained in [1,r−1] plus the number of minimal coprime segments that end at r.

# Let's consider the number of minimal coprime segments that end at r. We can see that the number of minimal coprime segments that end at r is equal to the number of minimal coprime segments that end at r−1 plus the number of minimal coprime segments that start at r.

# Let's consider the number of minimal coprime segments that start at r. We can see that the number of minimal coprime segments that start at r is equal to the number of minimal coprime segments that start at r−1 minus the number of minimal coprime segments that start at r−2.

# Let's consider the number of minimal coprime segments that start at r−1. We can see that the number of minimal coprime segments that start at r−1 is equal to the number of minimal coprime segments that start at r−2 plus the number of minimal coprime segments that end at r−1.

# Let's consider the number of minimal coprime segments that end at r−1. We can see that the number of minimal coprime segments that end at r−1 is equal to the number of minimal coprime segments that end at r−2 plus the number of minimal coprime segments that start at r−1.

# Let's consider the number of minimal coprime segments that start at r−2. We can see that the number of minimal coprime segments that start at r−2 is equal to the number of minimal coprime segments that start at r−3 minus the number of minimal coprime segments that start at r−4.

# Let's consider the number of minimal coprime segments that start at r−3. We can see that the number of minimal coprime segments that start at r−3 is equal to the number of minimal coprime segments that start at r−4 plus the number of minimal coprime segments that end at r−3.

# Let's consider the number of minimal coprime segments that end at r−3. We can see that the number of minimal coprime segments that end at r−3 is equal to the number of minimal coprime segments that end at r−4 plus the number of minimal coprime segments that start at r−3.

# Let's consider the number of minimal coprime segments that end at r−4. We can see that the number of minimal coprime segments that end at r−4 is equal to the number of minimal coprime segments that end at r−5 plus the number of minimal coprime segments that start at r−4.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_minimal_coprime_segments(l, r):
    count = 0
    for x in range(l, r + 1):  # Iteramos desde l hasta r
        for y in range(x, r + 1):  # Buscamos el primer r' tal que gcd(x, y) == 1
            if gcd(x, y) == 1:
                count += 1
                break  # Al encontrar un segmento mínimo, pasamos al siguiente x
    return count

# Leer número de casos de prueba
t = int(input().strip())

# Procesar cada caso
for _ in range(t):
    l, r = map(int, input().split())
    print(count_minimal_coprime_segments(l, r))
    
print(count_minimal_coprime_segments(1, 2))  # 1
print(count_minimal_coprime_segments(1, 10))  # 9
print(count_minimal_coprime_segments(49, 49))  # 0
print(count_minimal_coprime_segments(69, 420))  # 351
print(count_minimal_coprime_segments(1, 1))  # 1
print(count_minimal_coprime_segments(9982, 44353))  # 34371