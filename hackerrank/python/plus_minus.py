# Plus Minus

def plus_minus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1

    print(f'{pos / len(arr):.6f}')
    print(f'{neg / len(arr):.6f}')
    print(f'{zero / len(arr):.6f}')
    # print(pos / len(arr))
    # print(neg / len(arr))
    # print(zero / len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)