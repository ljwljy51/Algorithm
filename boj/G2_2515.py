import sys
input = sys.stdin.readline

N, S=map(int, input().split())
pictures=[list(map(int, input().split())) for _ in range(N)]  
pictures.sort()
            
dp=[0]

def upper_bound(height):
    left=0
    right=N-1
    
    while left<right:
        mid=(left+right)//2
        if pictures[mid][0]<=height:
            left=mid+1
        else:
            right=mid
    return right

for i in range(N):
    idx=upper_bound(pictures[i][0]-S)
    dp.append(max(dp[i], dp[idx]+pictures[i][1]))

print(dp[N])
