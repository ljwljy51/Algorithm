// https://www.acmicpc.net/problem/17070
//  DFS로 풀어야 함은 인지했으나, 구체적인 구현 방안을 생각해내지 못함
//  (재귀호출에 익숙해지자). DP 구현 방법을 택했다. DP도...익숙해지자
//  https://velog.io/@twotwo28/%EB%B0%B1%EC%A4%80-17070-%ED%8C%8C%EC%9D%B4%ED%94%84-%EC%98%AE%EA%B8%B0%EA%B8%B0-1
//  위 코드를 참고했다.

#include <iostream>
#include <vector>
using namespace std;

int N;
bool isWall[16][16];  // 벽 존재 유무 체크
int cnt[16][16][3];   // dp 배열

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  // 입력받기
  cin >> N;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> isWall[i][j];
    }
  }

  cnt[0][1][0] = 1;  //(1,2) 위치에서 가로방향(0)으로 시작하는 파이프 1개
  // 0열, 1열 제외. 0행에 대한 초기화 진행
  for (int j = 2; j < N; j++) {
    if (!isWall[0][j]) {  // 벽 없는 경우 가로이동에 대해 미리 계산
      cnt[0][j][0] = cnt[0][j - 1][0];
    }
  }

  for (int y = 1; y < N; y++) {  // 1행 2열부터 값 계산
    for (int x = 2; x < N; x++) {
      if (!isWall[y][x]) {  // 이동 가능한 경우
        // 가로이동
        cnt[y][x][0] +=
            (cnt[y][x - 1][0] + cnt[y][x - 1][1]);  // 이전 파이프 방향이 가로
                                                    // 혹은 대각선일때만 가능
        // 세로이동
        cnt[y][x][2] +=
            (cnt[y - 1][x][1] + cnt[y - 1][x][2]);  // 이전 파이프 방향이 대각선
                                                    // 혹은 세로일 때 가능
        // 대각선 이동
        // 계산되는 위치 기준 왼쪽, 위쪽이 비어있어야 함
        if (isWall[y - 1][x] || isWall[y][x - 1]) {
          continue;
        }
        cnt[y][x][1] +=
            cnt[y - 1][x - 1][0] + cnt[y - 1][x - 1][1] + cnt[y - 1][x - 1][2];
      }
    }
  }

  // 목표 칸에 도착하는 모든 경우의 수 출력
  cout << cnt[N - 1][N - 1][0] + cnt[N - 1][N - 1][1] + cnt[N - 1][N - 1][2];
}