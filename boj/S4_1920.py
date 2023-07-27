import sys
input = sys.stdin.readline
n = input()  # 숫자 개수
n_list = set(input().split())  # 입력받은 숫자들
num = input()
num_list = input().split()

for i in num_list:  # 집합의 성질 이용. 단순 존재 여부 검사면 집합or 딕셔너리를 활용해 시간복잡도 낮추기 가능
    print(1 if i in n_list else 0)
