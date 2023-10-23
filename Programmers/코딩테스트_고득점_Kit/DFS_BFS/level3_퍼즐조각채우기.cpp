// https://jangcenter.tistory.com/40
// 함수에서 벡터를 인자로 전달하는 부분 어떻게 하는지에 주목
// memset함수 주목
// memset: 메모리 내용(값)을 원하는 크기만큼 특정 값으로 세팅할 수 있는 함수
// matching함수 내에서 벡터 내 벡터 요소 어떻게 받아와서 반복문 도는지에 주목

#include <cstring>
#include <queue>
#include <vector>

using namespace std;

vector<vector<pair<int, int>>> empties;  // 빈 공간
vector<vector<pair<int, int>>> puzzles;  // 블록들
bool visited[51][51];                    // 방문 여부 저장
int answer = 0;
int dy[] = {0, 1, 0, -1};
int dx[] = {1, 0, -1, 0};  // x, y축 방향
int N;

vector<pair<int, int>> repos_zero(
    vector<pair<int, int>> pos) {  // 위치정보들을 0,0이 기준이 되도록 변환
  int min_i = N;
  int min_j = N;
  for (int i = 0; i < pos.size(); i++) {
    min_i = min_i > pos[i].first ? pos[i].first : min_i;
    min_j = min_j > pos[i].second ? pos[i].second : min_j;
  }

  for (int i = 0; i < pos.size(); i++) {
    pos[i].first -= min_i;
    pos[i].second -= min_j;
  }
  return pos;
}

vector<pair<int, int>> bfs(vector<vector<int>> &map, int value, int i,
                           int j) {  // 인자로 받은 map에서 값에 맞는 위치 반환
  visited[i][j] = true;
  vector<pair<int, int>> v;  // 리턴할 벡터
  queue<pair<int, int>> q;   // bfs 위한 큐
  q.push(make_pair(i, j));
  v.push_back(make_pair(i, j));

  while (!q.empty()) {
    int y = q.front().first;
    int x = q.front().second;
    q.pop();

    for (int d = 0; d < 4; d++) {
      int new_y = y + dy[d];
      int new_x = x + dx[d];
      if (new_y >= 0 && new_y < N && new_x >= 0 &&
          new_x < N) {  // 인덱스 범위 확인
        if (!visited[new_y][new_x] && map[new_y][new_x] == value) {
          visited[new_y][new_x] = true;
          q.push(make_pair(new_y, new_x));
          v.push_back(make_pair(new_y, new_x));
        }
      }
    }
  }

  return v;
}

void rot(vector<pair<int, int>> &pos) {  // 시계방향으로 90도 회전
  int row = 0;
  for (int i = 0; i < pos.size(); i++) {
    row = row < pos[i].first ? pos[i].first : row;  // 행값중 최대값 추출
  }

  for (int i = 0; i < pos.size(); i++) {
    int y = pos[i].first;
    int x = pos[i].second;
    pos[i].first = x;
    pos[i].second = row - y;
  }
}

void matching() {
  vector<bool> puzzle_visited(puzzles.size(), false);

  for (vector<pair<int, int>> empty : empties) {
    for (int puzzle_idx = 0; puzzle_idx < puzzles.size(); puzzle_idx++) {
      if (puzzle_visited[puzzle_idx]) {  // 이미 사용한 퍼즈리면 continue
        continue;
      }

      vector<pair<int, int>> puzzle = puzzles[puzzle_idx];
      if (empty.size() !=
          puzzle.size()) {  // 퍼즐의 사이즈랑 빈칸의 사이즈가 안맞으면 continue
        continue;
      }

      bool flag = false;  // 퍼즐 조각 채워졌는지 확인 위함
      for (int r = 0; r < 4; r++) {
        int k = 0;  // 매칭된 개수 확인 위함
        for (int i = 0; i < empty.size(); i++) {  // 퍼즐과 빈칸 비교
          for (int j = 0; j < puzzle.size(); j++) {
            if (empty[i].first == puzzle[j].first &&
                empty[i].second ==
                    puzzle[j].second) {  // 퍼즐과 빈칸 위치 같으면
              k++;                       // 개수 추가
            }
          }
        }
        if (k != empty.size()) {  // 매칭된 개수 안맞으면 90도 회전 후 다시 확인
          rot(puzzle);
          continue;
        }

        // 해당 빈칸에 퍼즐 채울 수 있는 경우
        // 정보 갱신
        answer += empty.size();
        puzzle_visited[puzzle_idx] = true;
        flag = true;
        break;
      }
      if (flag) {  // 빈칸 채워진 경우
        break;
      }
    }
  }
}

int solution(vector<vector<int>> game_board, vector<vector<int>> table) {
  N = game_board.size();
  // 빈공간 확인, (0,0)이 기준이 되도록 위치 변환
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (game_board[i][j] == 0 && !visited[i][j]) {
        empties.push_back(repos_zero(bfs(game_board, 0, i, j)));
      }
    }
  }

  // 퍼즐 조각 확인, (0,0)이 기준이 되도록 위치 변환
  memset(visited, false, sizeof(visited));  // size가 아닌 sizeof함수 써야 함.
                                            // visited 배열 false로 초기화
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (table[i][j] == 1 && !visited[i][j]) {
        puzzles.push_back(repos_zero(bfs(table, 1, i, j)));
      }
    }
  }

  matching();  // 빈칸과 블럭 매치
  return answer;
}