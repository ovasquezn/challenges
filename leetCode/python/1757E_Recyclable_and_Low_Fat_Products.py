"""
Problem: 1757. Recyclable and Low Fat Products (LeetCode – 30 Days of Pandas)

Table (DataFrame): Products
Columns:
- product_id (int, PK)
- low_fats (enum: 'Y'/'N')
- recyclable (enum: 'Y'/'N')

Task:
Return the product_id of products that are BOTH low fat AND recyclable.
Order can be arbitrary.

Example:
Input:
product_id  low_fats  recyclable
0           Y         N
1           Y         Y
2           N         Y
3           Y         Y
4           N         N

Output:
product_id
1
3

Approach:
- Filter rows where (low_fats == 'Y') AND (recyclable == 'Y').
- Select only ['product_id'] and return.

Time Complexity: O(n) over rows (vectorized boolean filtering).
Space Complexity: O(k) for the filtered subset (k ≤ n).
"""

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    mask = (products["low_fats"] == "Y") & (products["recyclable"] == "Y")
    return products.loc[mask, ["product_id"]]
