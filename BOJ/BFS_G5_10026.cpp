// https://www.acmicpc.net/problem/10026
// 전형적인 BFS 문제
// 적록색약이 아닌 사람에 대한 결과값을 먼저 구한 뒤, 적록색약인 사람에 맞게
// 배열 조작 후 답을 새로 구하자

#include <iostream>
#include <queue>
#include <string>

using namespace std;

int dy[4] = {0, 0, -1, 1};
int dx[4] = {1, -1, 0, 0};

int N;
char paint[101][101];
bool visited[101][101];

void bfs(int y, int x) {    // 탐색시작점 받아와 bfs수행하는 함수
  queue<pair<int, int>> q;  // bfs를 위한 큐 생성
  q.push(make_pair(y, x));  // 시작점 push
  visited[y][x] = true;     // 방문처리

  while (!q.empty()) {            // 큐가 빌 때까지
    int cur_y = q.front().first;  // 현재 좌표값 pop
    int cur_x = q.front().second;
    q.pop();

    for (int i = 0; i < 4; i++) {
      int new_y = cur_y + dy[i];  // 새로운 좌표값 계산
      int new_x = cur_x + dx[i];

      if (new_y < 0 || new_y >= N ||
          new_x < 0 | new_x >= N) {  // 인덱스 벗어나는 경우
        continue;
      }
      if (!visited[new_y][new_x] &&
          (paint[y][x] ==
           paint[new_y][new_x])) {  // 방문하지 않았으면서 이전 좌표값과 새
                                    // 좌표값에 대한 색이 같은 경우
        q.push(make_pair(new_y, new_x));  // 큐에 넣고 방문처리
        visited[new_y][new_x] = true;
      }
    }
  }
}

int return_area_cnt() {
  int cnt = 0;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (!visited[i][j]) {
        cnt++;
        bfs(i, j);  // bfs 수행 시마다 area cnt+1
      }
    }
  }
  return cnt;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> N;  // 그림 크기 입력받음

  for (int i = 0; i < N; i++) {
    cin >> paint[i];  // 그림 색 정보 입력받음
  }

  int cnt_area_1 = return_area_cnt();  // 적록색약 없는 사람 기준 영역 수

  for (int i = 0; i < N; i++) {  // 적록색약 있는 사람에 대해 계산 위해
                                 // paint배열 및 visited 배열값 수정
    for (int j = 0; j < N; j++) {
      if (paint[i][j] == 'R') {
        paint[i][j] = 'G';
      }
      if (visited[i][j]) {
        visited[i][j] = false;
      }
    }
  }

  int cnt_area_2 = return_area_cnt();

  cout << cnt_area_1 << " " << cnt_area_2;
}