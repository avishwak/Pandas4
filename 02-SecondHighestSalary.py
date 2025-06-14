# Problem 2 : Second Highest Salary ( https://leetcode.com/problems/second-highest-salary/ )

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    distinct_salary = [s for s in set(employee['salary'])]
    distinct_salary.sort(reverse=True)
    SecondHighestSalary = [distinct_salary[1]] if len(distinct_salary)>1 else [None]
    return pd.DataFrame(SecondHighestSalary, columns = ['SecondHighestSalary'])