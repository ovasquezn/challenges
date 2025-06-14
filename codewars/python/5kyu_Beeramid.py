# Codewars
# Beeramid (5 Kyu) 
# 10/06/25

# total_cans = 1500 // 2 = 750
# Niveles:
# 1^2 = 1 → quedan 749
# 2^2 = 4 → quedan 745
# 3^2 = 9 → quedan 736
# ...
# 12^2 = 144 → quedan 6
# 13^2 = 169 > 6 → no se puede

def beeramid(bonus, price):
    total = bonus // price
    level = 0
    while total >= (level + 1) ** 2:
        level += 1
        total -= level ** 2
    return level

print(
    beeramid(9,2),
    beeramid(11,2),
    beeramid(455,5)
)
