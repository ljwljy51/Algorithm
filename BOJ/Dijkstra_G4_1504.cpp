// https://www.acmicpc.net/problem/1504
// 다익스트라 알고리즘
//"하나의 정점"에서 "다른 모든 정점"으로의 최단경로 구하기
// 가중치 존재 그래프에서 사용되며, 음의 가중치가 없는 경우에만 사용 가능

// 1번 노드에서 N번 노드까지 가는 최단 거리를 구하되, 필수 경유 두 노드 들러야
// 함
// https://m.blog.naver.com/fbfbf1/222662098136
// 위 코드를 참고함

// INT_MAX값 썼다가 오버플로우 나서 계속 틀려서 헤맸다..^^... 다음부턴 거리값
// 초기화 적당히 큰 값으로 해주도록 하자
#include <iostream>
#include <queue>  // 다익스트라 사용 위함
#include <vector>
using namespace std;

int N, E;
const int MAX_INT = 1e9;

vector<pair<int, int>>
    graph[801];     // 인접 노드 및 거리 저장. 거리, 노드 순으로 저장
int min_dist[801];  // 최단거리 저장 배열. 시작 정점으로부터 i번노드까지의
                    // 최단거리
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>>
    pq;  // 다익스트라 사용 위한 우선순위 큐 정의

void bfs(int start_node) {
  // 거리값 초기화
  fill(min_dist, min_dist + N + 1, MAX_INT);

  // 시작 정점 거리 0으로 설정
  min_dist[start_node] = 0;
  // 큐에 요소(거리, 노드 순) 삽입
  pq.push({min_dist[start_node], start_node});

  while (!pq.empty()) {
    // 방문 정점 추출(거리, 노드)
    auto cur = pq.top();
    pq.pop();

    // 기존에 저장된 최단거리보다 큰 경우 무시
    if (min_dist[cur.second] < cur.first) {
      continue;
    }

    for (auto nxt :
         graph[cur.second]) {  // 현재 정점과 연결된 모든 인접 노드 탐색
      // 더 짧은 경로 발견 시 거리값 갱신
      if (min_dist[nxt.second] > min_dist[cur.second] + nxt.first) {
        min_dist[nxt.second] = min_dist[cur.second] + nxt.first;
        pq.push({min_dist[nxt.second], nxt.second});  // 우선순위 큐 삽입
      }
    }
  }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> N >> E;

  for (int i = 0; i < E; i++) {
    int start_node, end_node, dist;
    cin >> start_node >> end_node >> dist;

    // 무방향그래프이므로 양측 연결
    graph[start_node].push_back({dist, end_node});
    graph[end_node].push_back({dist, start_node});
  }

  // 반드시 거쳐야 하는 두 노드값 입력
  int v1, v2;
  cin >> v1 >> v2;

  // 전체 가능 경로는 1->v1->v2->N or
  // 1->v2->v1->N
  // 위 두 경로에 대한 최단경로 구하기 위해 아래 로직 수행
  bfs(1);                        // 1번노드에서 각 노드까지의 최단거리 구함
  int one_to_v1 = min_dist[v1];  // 1->v1 최단거리
  int one_to_v2 = min_dist[v2];

  // v1번 노드에서 출발하는 최단 경로 계산
  bfs(v1);
  int v1_to_v2 = min_dist[v2];
  int v1_to_N = min_dist[N];

  bfs(v2);
  int v2_to_v1 = min_dist[v1];
  int v2_to_N = min_dist[N];

  // 가능한 두 경로 중 최소값 선택
  int sum_1 = one_to_v1 + v1_to_v2 + v2_to_N;
  int sum_2 = one_to_v2 + v2_to_v1 + v1_to_N;

  int answer = (sum_1 > sum_2) ? sum_2 : sum_1;
  if (answer >= MAX_INT || answer < 0) {
    cout << -1;
    return 0;
  }
  cout << answer;
  return 0;
}
