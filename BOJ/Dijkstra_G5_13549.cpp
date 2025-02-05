// https://www.acmicpc.net/problem/13549
//  다익스트라 알고리즘
//  "하나의 정점"에서 "다른 모든 정점"으로의 최단경로 구하기
// 가중치 존재 그래프에서 사용되며, 음의 가중치가 없는 경우에만 사용 가능
// 우선순위 큐를 사용하면 O(E log V)로 최적화할 수 있다.

#include <iostream>
#include <queue>
using namespace std;

int N, K;
bool visit[100001] = {false};  // 방문 여부 저장

void bfs(int n) {
  queue<pair<int, int>> q;
  q.push(make_pair(n, 0));  // 첫 번째 요소는 현재 위치, 두 번째 요소는 소요
                            // 시간
  while (!q.empty()) {
    int x = q.front().first;     // 시작 위치 가져옴
    int cnt = q.front().second;  // 소요 시간 가져옴
    q.pop();                     // 맨 앞 요소 삭제
    if (x == K) {                // 만약 도착 지점에 도달했으면
      cout << cnt;
      return;
    }
    // 도달 못한 경우. 이때, 탐색 순서 중요!!!!
    if (x * 2 >= 0 && x * 2 < 100001) {
      if (!visit[x * 2]) {
        visit[x * 2] = true;
        q.push(make_pair(x * 2, cnt));  // 순간이동엔 시간이 소요되지 않음
      }
    }
    if (x - 1 >= 0 && x - 1 < 100001) {
      if (!visit[x - 1]) {
        visit[x - 1] = true;
        q.push(make_pair(x - 1, cnt + 1));
      }
    }
    if (x + 1 >= 0 && x + 1 < 100001) {  // 배열 범위 안에 있는지 확인
      if (!visit[x + 1]) {               // 중복 방지 위해 방문 여부 확인
        visit[x + 1] = true;
        q.push(make_pair(x + 1, cnt + 1));
      }
    }
    // 가능한 좌표마다 모두 검사해야함
  }
}

int main() {
  ios::sync_with_stdio(NULL);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> K;  // 현재 위치, 도착 위치 입력받음
  bfs(N);         // 시작 지점을 전달

  return 0;
}