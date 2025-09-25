"""
Problem: 595. Big Countries (LeetCode – 30 Days of Pandas)

Table (DataFrame): World
Columns:
- name (varchar, PK)
- continent (varchar)
- area (int)
- population (int)
- gdp (bigint)

A country is considered "big" if:
- area >= 3,000,000 OR
- population >= 25,000,000

Task:
Return a DataFrame with columns ['name', 'population', 'area'] 
for the countries that satisfy the condition. Order can be arbitrary.

Examples:
Input sample (World):
name        continent  area     population   gdp
------------------------------------------------
Afghanistan Asia       652230   25500100     20343000000
Albania     Europe     28748    2831741      12960000000
Algeria     Africa     2381741  37100000     188681000000
Andorra     Europe     468      78115        3712000000
Angola      Africa     1246700  20609294     100990000000

Output:
name         population   area
------------------------------
Afghanistan  25500100     652230
Algeria      37100000     2381741

Approach:
- Filter rows where (area >= 3_000_000) OR (population >= 25_000_000).
- Select only the required columns ['name', 'population', 'area'].
- Return the resulting DataFrame.

Time Complexity: O(n) over number of rows (vectorized filtering).
Space Complexity: O(k) for the filtered subset (≤ n rows).
"""

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    mask = (world["area"] >= 3_000_000) | (world["population"] >= 25_000_000)
    return world.loc[mask, ["name", "population", "area"]]