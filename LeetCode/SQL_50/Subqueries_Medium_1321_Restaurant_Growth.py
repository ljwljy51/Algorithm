# https://leetcode.com/problems/restaurant-growth/?envType=study-plan-v2&envId=top-sql-50
# rolling 함수 사용 부분에 주뫀
import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    customer=customer.groupby("visited_on", as_index=False)["amount"].sum().rename(columns={"amount":"daily_amount"}) #일별 총합 계산
    # 문제에 따라 요구사항 충족
    # rolling함수 사용
    customer['rolling_sum']=customer['daily_amount'].rolling(window=7, min_periods=7).sum()
    customer['rolling_avg']=customer['daily_amount'].rolling(window=7, min_periods=7).mean().round(2)
    customer=customer.dropna()
    customer=customer.iloc[:, [0,2,3]].rename(columns={'rolling_sum':'amount', 'rolling_avg':'average_amount'})
    return customer