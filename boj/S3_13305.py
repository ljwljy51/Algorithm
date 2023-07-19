#https://www.acmicpc.net/problem/13305
import sys

input = sys.stdin.readline
num_city = int(input())  # 도시 개수 입력받음
road_lengths = list(map(int, input().split()))  # 도로 길이 입력받음
city_prices = list(map(int, input().split()))  # 도시 별 기름 가격 입력받음

total_cost = 0
min_city_price = city_prices[0]  # 탐색 시점 기준 최소 가격
for i in range(num_city-1):  # 각 마을 별로 주유 가격 확인
    if city_prices[i] < min_city_price:  # 현재 마을의 주유 가격이 지금까지의 최소 가격보다 낮으면
        min_city_price = city_prices[i]  # 최소 가격 값 갱신
    total_cost += min_city_price*road_lengths[i]  # 가격 계산

print(total_cost)
