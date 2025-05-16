# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

# Sample Input
# 9 27
# Sample Output
# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------
# Explanation

# The center of the door mat has the design.
# Size: 9 x 27
# The welcome message is written in the center of the door mat.



# Solution:

n, m = map(int,input().split())
for i in range(1,n,2):
    print(('.|.'*i).center(m,'-'))
print('WELCOME'.center(m,'-'))
for i in range(n-2,-1,-2):
    print(('.|.'*i).center(m,'-'))

