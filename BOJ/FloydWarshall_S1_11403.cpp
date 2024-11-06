// https://www.acmicpc.net/problem/11403
// https://baebalja.tistory.com/328
// 오랜만의 C++이라 위 코드를 참고했다.

// 하나의 정점에서 출발해 다른 모든 정점으로의 최단 경로 구하기 -> Dijkstra
//  모든 정점에서 모든 정점으로의 최단 경로 구하기 -> Floyd Warshall

// 이 경우 플로이드 와샬 사용
// 가중치 없는 방향그래프

#include <iostream>
using namespace std;

int graph[101][101];  // 그래프 정보 담기 위함
int main() {
  int n;  // 노드 수
  cin >> n;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> graph[i][j];  // 그래프 정보 저장
    }
  }

  // 3중 for문사용
  for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (graph[i][k] &&
            graph[k][j]) {  // k노드를 통해 i노드->j노드 접근 가능한 경우
          graph[i][j] = 1;  // 연결정보 갱신
        }
      }
    }
  }

  // 결과 출력
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cout << graph[i][j] << " ";
    }
    cout << endl;
  }
}