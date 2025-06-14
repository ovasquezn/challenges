def solution(array_a, array_b):
    mean_square_error = []
    # zip combina los elementos de dos listas en tuplas
    for a,b in zip(array_a, array_b):
        mean_square_error.append((a-b)**2)
    return sum(mean_square_error) / len(array_a)

print(solution([1, 2, 3], [4, 5, 6]))  # Example usage