"""
2877. Create a DataFrame from a List

Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.

The result format is in the following example.

 

Example 1:

Input:
student_data:
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
Explanation:
A DataFrame was created on top of student_data, with two columns named student_id and age.

"""

from typing import List
import pandas as pd # type: ignore

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=["student_id", "age"])
    return df

# Example
student_data = [
    [1, 20],
    [2, 21],
    [3, 22]
]

df = createDataframe(student_data)
print(df)

"""
Function: createDataframe
Description
The createDataframe function takes a list of lists containing student data and converts it into a Pandas DataFrame. Each inner list represents a student's data, specifically their student ID and age.

Parameters
student_data (List[List[int]]): A list of lists where each inner list contains two integers. The first integer is the student ID, and the second integer is the student's age.
Returns
pd.DataFrame: A Pandas DataFrame with two columns: "student_id" and "age". Each row in the DataFrame corresponds to a student's data from the input list.
"""