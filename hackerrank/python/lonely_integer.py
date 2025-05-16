def lonelyinteger(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
    return None


L = [1,2,3,4,3,2,1]
print(lonelyinteger(L))



arr = ([[1,2,3],[4,5,6],[7,8,9]])



def test(arr):
    sum_diagonal_1 = 0
    sum_diagonal_2 = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                sum_diagonal_1 += arr[i][j]
            if i + j == len(arr) - 1:
                sum_diagonal_2 += arr[i][j]
    return abs(sum_diagonal_1 - sum_diagonal_2)
test(arr)