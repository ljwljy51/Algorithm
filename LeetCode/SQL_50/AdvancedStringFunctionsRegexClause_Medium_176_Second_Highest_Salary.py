#https://leetcode.com/problems/second-highest-salary/submissions/1541378191/?envType=study-plan-v2&envId=top-sql-50
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries=employee['salary'].drop_duplicates()
    print(unique_salaries)
    second_highest=unique_salaries.nlargest(2).iloc[-1] if len(unique_salaries)>=2 else None
    if second_highest is None:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    else:
        return pd.DataFrame({'SecondHighestSalary':[second_highest]})