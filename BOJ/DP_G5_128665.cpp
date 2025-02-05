// https://www.acmicpc.net/problem/12865
// 주어진 조건 내 "최대가치"
// DP까지는 생각해냈으나, '배낭문제'를 쳐음 접해봄

// 0/1 Knapsack문제
// 최대 무게를 초과하지 않으면서 가치의 합을 최대로 하는 경우를 찾는 문제
// 각 물건을 한 개 넣거나, 또는 넣지 않거나 두 가지 선택만 가능하다는 것
// 즉, 물건을 나눠서 일부만 넣을 수 없음

// https://nanyoungkim.tistory.com/182
// 위 글 참고

#include <iostream>
using namespace std;

int N, K;
int DP[101][100001] = {0};  // row방향은 물건 idx를, col 방향은 무게 limit을
                            // 의미. 첫 행과 열은 0으로 초기화
int W[101];
int V[101];

int max(int &a, int &b) { return a > b ? a : b; }

void dp() {  // DP배열 계산 함수
  for (int limit = 1; limit <= K; limit++) {
    for (int idx = 1; idx <= N; idx++) {
      // 해당 물건 넣을 수 없는 경우
      if (W[idx] > limit) {
        DP[idx][limit] =
            DP[idx - 1][limit];  // 이전 물건까지에서의 최대가치 반영
      }
      // 해당 물건 넣을 수 있는 경우
      else {
        // 이전 물건까지에서의 최대가치, 이번 물건 넣었을 때의 최대가치 고려해
        // 최대값 반영
        DP[idx][limit] =
            max(DP[idx - 1][limit], DP[idx - 1][limit - W[idx]] + V[idx]);
      }
    }
  }
}

int main() {
  cin >> N >> K;
  for (int i = 1; i <= N; i++) {
    cin >> W[i] >> V[i];
  }

  dp();  // DP 배열 계산

  cout << DP[N][K];
}