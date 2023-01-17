import sys
input = sys.stdin.readline

N, S=map(int, input().split()) 
pictures=[list(map(int, input().split())) for _ in range(N)]  #그림 당 높이와 가격 
pictures.sort() #오름차순으로 정렬
            
dp=[0] #dp 배열 초기화

def upper_bound(height): #이분탐색
    left=0
    right=N-1
    
    while left<right:
        mid=(left+right)//2
        if pictures[mid][0]<=height: #찾는 값이 절반 기준으로 오른쪽에 있으면
            left=mid+1
        else: #찾는 값이 절반 기준으로 왼쪽에 있으면
            right=mid
    return right #upper bound
print(pictures)

for i in range(N):
    idx=upper_bound(pictures[i][0]-S) #조건 만족하는 그림 중에서 가장 높이 낮은 것 찾음
    dp.append(max(dp[i], dp[idx]+pictures[i][1])) #지금까지의 최대값과 현재 그림 구매했을 떄의 경우 비교해 갱신

print(dp[N])