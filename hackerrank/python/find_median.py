import math
import os
import random
import re
import sys

def findMedian(arr):
    arr.sort()
    return arr[int((len(arr)-1)/2)]

L = [1,2,4,5,6,4,3]

print(findMedian(L))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = findMedian(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()