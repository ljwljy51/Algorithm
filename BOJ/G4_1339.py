import sys

input = sys.stdin.readline

n = int(input())
word_lst = []

for i in range(n):
    word_lst.append(input().strip())

dict = {}
for i in range(n):  # 모든 단어에 대해
    for j in range(len(word_lst[i])):  # 단어 길이만큼
        if word_lst[i][j] in dict:  # 해당 알파벳이 딕셔너리에 있으면
            dict[word_lst[i][j]] += 10 ** (len(word_lst[i]) - j - 1)  # 가중치 더해줌
        else:  # 딕셔너리에 없는 경우
            dict[word_lst[i][j]] = 10 ** (len(word_lst[i]) - j - 1)

weight_lst = []
for n in dict.values():
    weight_lst.append(n)

weight_lst.sort(reverse=True)

num = 9  # 9~0 . 승수
answer = 0
for weight in weight_lst:
    answer += num * weight  # 수 계산
    num -= 1

print(answer)
