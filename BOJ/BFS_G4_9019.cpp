// https://www.acmicpc.net/problem/9019
//  접근방법은 구상해냈으나, 반례처리 못함
// https://donggoolosori.github.io/2020/10/05/boj-9019/
//  반례 처리부분에 주목
//  visited 배열 다루는 부분에 주목

#include <string.h>  //memset함수 사용 위함

#include <iostream>
#include <queue>

using namespace std;

int A, B;
bool visited[10000];  // bfs 사용

void bfs(int a, int b) {
  queue<pair<int, string>> q;  // 연산 후 숫자값 및 연산내역 저장 위함
  q.push(make_pair(a, ""));
  visited[a] = true;

  while (!q.empty()) {
    int cur_num = q.front().first;
    string cur_op = q.front().second;
    q.pop();

    if (cur_num == b) {  // 타겟값 찾은 경우
      cout << cur_op << '\n';
      return;
    }

    int D, S, L, R;

    D = (cur_num * 2) % 10000;
    if (!visited[D]) {
      visited[D] = true;
      q.push(make_pair(D, cur_op + "D"));
    }

    S = (cur_num - 1 < 0) ? 9999 : cur_num - 1;
    if (!visited[S]) {
      visited[S] = true;
      q.push(make_pair(S, cur_op + "S"));
    }

    L = (cur_num % 1000) * 10 + (cur_num / 1000);  // L,R연산방법에 주목
    if (!visited[L]) {
      visited[L] = true;
      q.push(make_pair(L, cur_op + "L"));
    }

    R = cur_num / 10 + (cur_num % 10) * 1000;
    if (!visited[R]) {
      visited[R] = true;
      q.push(make_pair(R, cur_op + "R"));
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int T;
  cin >> T;
  while (T--) {
    cin >> A >> B;
    memset(visited, false, sizeof(visited));  // 매 테스트케이스마다 초기화해줌
    bfs(A, B);
  }

  return 0;
}