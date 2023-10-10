// https://school.programmers.co.kr/learn/courses/30/lessons/1844
#include <queue>
#include <vector>
using namespace std;

int solution(vector<vector<int>> maps) {
  int map_check[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};  // 상하좌우
  int n = maps.size();           // 세로 맵 길이
  int m = maps[0].size();        // 가로 맵 길이
  bool visited[101][101] = {0};  // visited 배열 초기화
  int distance[101][101] = {0};  // 거리 배열 초기화

  // bfs 사용
  queue<pair<int, int>> q;  // 큐 선언. pair를 요소로 가짐

  q.push(make_pair(0, 0));  // 시작점 대입
  visited[0][0] = 1;        // 방문 여부 및 거리정보 갱신
  distance[0][0] = 1;

  bool is_arrived = 0;  // 도착했을 경우, 빨리 끝내기 위한 플래그 설정
  while (!q.empty()) {
    int old_y = q.front().first;
    int old_x = q.front().second;

    q.pop();  // 원소 삭제

    for (int i = 0; i < 4; i++) {
      int new_x = old_x + map_check[i][1];  // 새로운 좌표 계산
      int new_y = old_y + map_check[i][0];

      if ((new_x >= 0 && new_x < m) &&
          (new_y >= 0 && new_y < n)) {  // 인덱스 범위 검사
        if (maps[new_y][new_x] == 1 &&
            visited[new_y][new_x] == 0) {  // 갈 수 있으면서 방문 안했을 경우
          q.push(make_pair(new_y, new_x));
          visited[new_y][new_x] = 1;
          distance[new_y][new_x] =
              distance[old_y][old_x] + 1;  // 방문처리 및 거리 계산

          if (new_y == n - 1 && new_x == m - 1) {  // 도착 지점 도달한 경우
            is_arrived = 1;                        // 플래그 갱신
            break;
          }
        }
      }
    }
    if (is_arrived) {
      break;
    }
  }
  int answer =
      (visited[n - 1][m - 1] == 1)
          ? distance[n - 1][m - 1]
          : -1;  // 마지막 지점 도달한 경우 거리값 반환, 도달 못한 경우 -1 반환
  return answer;
}