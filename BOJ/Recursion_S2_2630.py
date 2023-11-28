import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt_white, cnt_blue = 0, 0


def cut(x, y, n):
    global cnt_white, cnt_blue
    stat = arr[x][y]  # 기준 설정
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != stat:  # 만약 색종이 잘라야 하면
                for k in range(2):
                    for l in range(2):  # 1/4 크기로 자름
                        cut(x + k * n // 2, y + l * n // 2, n // 2)
                return

    # 색종이 안잘라도 되면(모두 같은 색이면)
    if stat == 0:  # 하얀색이면
        cnt_white += 1
    else:
        cnt_blue += 1


cut(0, 0, n)

print(cnt_white)
print(cnt_blue)
