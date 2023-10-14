// C++에서는 조건을 줄 때 3<x<5 이런 식으로 하는 게 안된다.
// 이걸 까먹었어서 몇 시간 날렸다 ^^~
// 항상 같은 로직으로 짰는데 답이 이상하면 언어에 따른 문법 오류가 있는지
// 체크하자..........

#include <string>
#include <vector>

using namespace std;

int map[102][102] = {0};
int visited[102][102] = {0};
int directions[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

int bfs(int character_x, int character_y, int item_x, int item_y) {
  vector<pair<int, int>> q;
  q.push_back(make_pair(character_y, character_x));
  visited[character_y][character_x] = 1;

  while (!q.empty()) {
    int current_y = q.front().first, current_x = q.front().second;
    q.erase(q.begin());  // pop
    for (int i = 0; i < 4; i++) {
      int new_y = current_y + directions[i][0],
          new_x = current_x + directions[i][1];
      if (visited[new_y][new_x] == 0 && map[new_y][new_x] == 1) {
        visited[new_y][new_x] = visited[current_y][current_x] + 1;
        q.push_back(make_pair(new_y, new_x));
      }
      if (new_y == item_y && new_x == item_x) {
        break;
      }
    }
  }
  return (visited[item_y][item_x] - 1) / 2;
}

int solution(vector<vector<int>> rectangle, int characterX, int characterY,
             int itemX, int itemY) {
  for (int i = 0; i < rectangle.size(); i++) {
    int bottom_left_x = rectangle[i][0] * 2,
        bottom_left_y = rectangle[i][1] * 2, top_right_x = rectangle[i][2] * 2,
        top_right_y = rectangle[i][3] * 2;

    for (int y = bottom_left_y; y < top_right_y + 1; y++) {
      for (int x = bottom_left_x; x < top_right_x + 1; x++) {
        if ((bottom_left_x < x && x < top_right_x) &&
            (bottom_left_y < y && y < top_right_y)) {
          map[y][x] = 2;  // 직사각형 내부
        } else if (map[y][x] != 2) {
          map[y][x] = 1;  // boundary
        }
      }
    }
  }

  int answer = bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2);
  return answer;
}