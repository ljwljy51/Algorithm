#https://www.acmicpc.net/problem/1463
#DP
import sys
input = sys.stdin.readline
num = int(input())

data = [0]*(num+1)  # DP 위함

for i in range(2, num+1):
    data[i] = data[i-1]+1  # 이전 횟수+1. 1을 뺀 경우
    if i % 3 == 0:
        data[i] = min(data[i//3]+1, data[i])  # 현재 수에 대한 것과 3으로 나눈 수에 대한 것과 비교
    if i % 2 == 0:  # 둘 다 조건을 if로 해둬야 함. 그래야 둘 다 검사해보고 더 작은 것으로 선택
        data[i] = min(data[i//2]+1, data[i])

print(data[num])
