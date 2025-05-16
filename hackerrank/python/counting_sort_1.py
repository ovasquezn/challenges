# Comparison Sorting
# Quicksort usually has a running time of , but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat  (worst-case) running time, since represents the minimum number of comparisons needed to know where to place each element. For more details, you can see these notes (PDF).

def counting_sort(arr):
    count = [0] * 4
    for i in arr:
        count[i] += 1
    return count

print(counting_sort([1,2,3,4,3,2,1]))

arr = [1,2,3,4,3,2,1]
print(max(arr) - min(arr) + 1)