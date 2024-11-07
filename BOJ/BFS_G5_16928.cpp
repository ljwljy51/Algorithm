// https://www.acmicpc.net/problem/16928
// https://hagisilecoding.tistory.com/85
// DP문제로 생각했는데, BFS 문제였다..!
// 이 문제의 경우, DP의 최적부분구조를 위반한다.
//  즉, 작은 부분문제에서 구한 최적의 답으로 합쳐진 큰 문제의 최적의 답을 구할
//  수 없음 (뱀 변수..)
// DP가 불가한 경우 BFS를 고려해보자

#include <iostream>
#include <queue>
using namespace std;
int map[102] = {0};  // 맵 배열
bool isVisited[102] = {0};  // 방문 여부 확인 위함 (최소횟수 구하는 것이므로,
                            // 중복된 칸에 대해 다시 계산할 필요 없음)

void bfs(int start, int cnt) {
  queue<pair<int, int>> q;  // bfs 큐 생성
  q.push(make_pair(start, cnt));
  while (!q.empty()) {
    int cur_start = q.front().first;  // 현재 위치
    int cur_cnt = q.front().second;   // 주사위 굴린 횟수
    q.pop();

    for (int i = 1; i <= 6; i++) {     // 주사위 눈 수마다 계산
      int next_start = cur_start + i;  // 다음 좌표 계산
      if (next_start == 100) {         // 딱 100번째 칸에 도착한 경우
        cout << cur_cnt + 1;           // 주사위 굴린 수 출력
        return;
      } else if (next_start <
                 100) {  // 다음 좌표가 100 미만인 경우에만 다시 이동 가능
        while (map[next_start] !=
               0) {  // 다음 좌표가 사다리 혹은 뱀에 해당하는 경우
          next_start = map[next_start];  // 이동해야 하는 칸으로 이동
        }
        if (!isVisited[next_start]) {  // 방문하지 않은 경우
          q.push(make_pair(next_start, cur_cnt + 1));  // 큐에 넣음
          isVisited[next_start] = true;                // 방문처리
        }
      }
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int N, M, start, end;

  cin >> N >> M;
  for (int i = 0; i < N; i++) {
    cin >> start >> end;
    map[start] = end;  // 사다리정보 맵에 저장
  }

  for (int i = 0; i < M; i++) {
    cin >> start >> end;
    map[start] = end;  // 뱀 정보 맵에 저장
  }

  bfs(1, 0);  // 1번칸에서 시작, 주사위 굴린 횟수 전달
  return 0;
}
