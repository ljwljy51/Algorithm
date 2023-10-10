// https://school.programmers.co.kr/learn/courses/30/lessons/43162
// C++에서는 배열 첫 선언 시 배열 크기를 지정해줘야 하는데, 이때 크기로 변수를
// 사용하면 안된다 이 부분에서 헤맸었음

#include <queue>
#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
  int answer = 0;
  bool visited[200] = {0};  // 각 노드 당 방문 여부 확인 위함
  queue<int> q;
  for (int i = 0; i < n; i++) {
    if (!visited[i]) {                 // 노드 방문 안했을 경우
      answer += 1;                     // 네트워크 수 추가
      visited[i] = 1;                  // 방문처리
      q.push(i);                       // 큐에 노드 추가
      while (!q.empty()) {             // 큐가 빌 때까지
        int current_node = q.front();  // 맨 앞 요소 가져옴
        q.pop();
        for (int j = 0; j < n; j++) {
          if (computers[current_node][j] == 1 &&
              !visited[j]) {  // 연결되어있고 방문 아직 안했을 경우
            visited[j] = 1;  // 방문 여부 갱신
            q.push(j);       // 큐에 노드 추가
          }
        }
      }
    }
  }
  return answer;
}