# You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)
# Different sizes of alphabet rangoli are shown below:

# # size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# Solution

import string

def print_rangoli(size):
    n = size
    alphabet = string.ascii_lowercase
    width = 4 * n - 3

    for i in list(range(n))[::-1] + list(range(1, n)):
        print('-'.join(alphabet[n-1:i:-1] + alphabet[i:n]).center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)