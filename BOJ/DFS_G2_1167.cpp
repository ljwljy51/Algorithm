// https://www.acmicpc.net/problem/1167

// https://www.acmicpc.net/problem/1967
// 위 문제와 거의 비슷하다. 입력을 어떻게 처리하는지에 주목

#include <string.h>

#include <iostream>
#include <vector>
using namespace std;

int N, node_num;
int answer = 0;
bool is_visited[100001] = {false};
vector<pair<int, int>> graph[100001];

void DFS(int start_node, int dist) {
  is_visited[start_node] = true;  // 방문처리

  if (answer < dist) {  // 현재 거리가 더 먼 경우 거리정보 갱신 및 노드 번호
                        // 저장
    answer = dist;
    node_num = start_node;
  }

  for (int i = 0; i < graph[start_node].size();
       i++) {  // 방문 가능한 노드에 대한 dfs 처리
    int next_node = graph[start_node][i].first;
    int next_dist = graph[start_node][i].second + dist;
    if (!is_visited[next_node]) {  // 다음 노드 방문 안한 경우 dfs 수행
      DFS(next_node, next_dist);
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> N;
  int start, end, weight;
  for (int i = 1; i <= N; i++) {  // 그래프정보 저장
    cin >> start >> end;
    while (end != -1) {
      cin >> weight;
      graph[start].push_back({end, weight});
      graph[end].push_back({start, weight});
      cin >> end;
    }
  }

  DFS(1, 0);  // 우선 루트 기준으로 가장 먼 노드 구하기

  // 구해진 노드 기준 가장 먼 노드와의 거리 구하기 위해 다시 DFS 수행
  // 과거 사용 데이터 초기화 필요
  answer = 0;
  memset(is_visited, false, sizeof(is_visited));

  DFS(node_num, 0);  // 새로운 노드 기준 최장거리 구하기
  cout << answer;
}
