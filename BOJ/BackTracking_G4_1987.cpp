// https://www.acmicpc.net/problem/1987
//  백트래킹문제..!
// 이번에도 BFS인 줄 알았는데 DFS+백트래킹이었다.
//'지금까지의 경로에서 한 번 방문한 종류의 알파벳은 다시 사용할 수 없다"는
// 점에서 DFS+백트래킹임을 인지했어야 함 BFS의 경우, 이전 경로의 정보를 담기
// 힘들다. https://ansohxxn.github.io/boj/1987/ 위 코드를 참고했다.

#include <iostream>
using namespace std;

int R, C, answer;
int dy[4] = {0, 0, -1, 1};
int dx[4] = {1, -1, 0, 0};
char board[20][20];  // 보드 최대 20칸
bool visited[26];    // 알파벳 방문여부 체크

inline bool idx_check(int y, int x) {
  return ((y >= 0) && (y < R) && (x >= 0) && (x < C));
}

void dfs(int y, int x, int cnt) {
  answer = (cnt > answer) ? cnt : answer;  // cnt 최대값 갱신
  // 네 방향으로 인덱스 체크
  for (int i = 0; i < 4; i++) {
    int new_y = y + dy[i];
    int new_x = x + dx[i];
    if (idx_check(new_y, new_x)) {  // 인덱스 유효한 경우
      int next_char_idx = board[new_y][new_x] - 'A';
      if (!visited[next_char_idx]) {    // 아직 방문하지 않은 경우
        visited[next_char_idx] = true;  // 방문처리
        dfs(new_y, new_x, cnt + 1);
        visited[next_char_idx] = false;  // 백트래킹
      }
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> R >> C;
  for (int i = 0; i < R; i++) {
    for (int j = 0; j < C; j++) {
      cin >> board[i][j];
    }
  }  // 입력받기

  visited[board[0][0] - 'A'] = true;  // 시작지점방문 체크
  dfs(0, 0, 1);  // 시작점을 기준으로 dfs 수행. 현재 카운트 포함시켜야 하므로
                 // cnt 1로 시작

  cout << answer;
  return 0;
}