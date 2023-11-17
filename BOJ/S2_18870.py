import sys

input = sys.stdin.readline

n = int(input())
num_lst = list(map(int, input().split()))  # 입력받음
num_sorted = sorted(list(set(num_lst)))  # 중복된 것 제거 후 정렬

idx_dict = {}
for i in range(len(num_sorted)):
    idx_dict[num_sorted[i]] = i  # 숫자에 대응하는 인덱스(순서) 저장

answer = []
for num in num_lst:
    answer.append(idx_dict[num])  # 답 추가

for a in answer:
    print(a, end=" ")  # 출력
