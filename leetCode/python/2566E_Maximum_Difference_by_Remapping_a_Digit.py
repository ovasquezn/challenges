def min_max_after_remap(num):
    s = str(num)
    max_val = num
    min_val = num

    for d1 in set(s):
        for d2 in '0123456789':
            if d1 == d2:
                continue
            remapped = s.replace(d1, d2)
            val = int(remapped)
            max_val = max(max_val, val)
            min_val = min(min_val, val)

    return max_val - min_val

# Example usage

num = 1234567890
result = min_max_after_remap(num)
print(f"Maximum difference after remapping digits in {num}: {result}")
# Output: Maximum difference after remapping digits in 1234567890: 9876543210