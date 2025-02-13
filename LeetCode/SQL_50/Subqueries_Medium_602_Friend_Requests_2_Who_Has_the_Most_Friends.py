#https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/?envType=study-plan-v2&envId=top-sql-50
import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    tmp=pd.concat([request_accepted["requester_id"], request_accepted["accepter_id"]], axis=0).tolist()
    return pd.DataFrame({"id" : [mode(tmp)], "num" : [tmp.count(mode(tmp))]})
