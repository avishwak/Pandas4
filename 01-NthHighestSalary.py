# Problem 1 : Nth Highest Salary (https://leetcode.com/problems/nth-highest-salary/solution/)


"""
if we want to drop the duplicates, it is n^2 time complexity, because we have to check each element with all the other elements.
so we use the set, it is O(n) time complexity, because we have to check each element with the set.
"""

import pandas as pd

# solution 1 using drop_duplicates and iloc
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee[['salary']].sort_values(by='salary', ascending=False)
    df.drop_duplicates(inplace=True)
    NthHighestSalary = df['salary'].iloc[N-1] if 0 < N <= len(df) else [None]
    return pd.DataFrame([NthHighestSalary], columns=[f"getNthHighestSalary({N})"])

# solution 2 using set 
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary_set = set()
    for s in employee['salary']:
        salary_set.add(s)
    salary_list = [s for s in salary_set]
    salary_list.sort(reverse=True)
    NthHighestSalary = [salary_list[N-1]] if 0 < N <= len(salary_list) else [None]
    return pd.DataFrame([NthHighestSalary], columns=[f"getNthHighestSalary({N})"])

# solution 3 
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee[['salary']].drop_duplicates()
    if N <= 0 or N > len(df):
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})

    return df.sort_values(by='salary', ascending=False).head(N).tail(1)[['salary']].rename(columns={'salary':f"getNthHighestSalary({N})"})