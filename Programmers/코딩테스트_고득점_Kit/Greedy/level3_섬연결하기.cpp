// https://school.programmers.co.kr/learn/courses/30/lessons/42861
// 크루스칼 알고리즘
// mst

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> parent;  // 부모 노드 정보 담을 배열. 전역변수

int find_parent(int node) {
  if (parent[node] != node) {  // 부모 노드가 자신이 아닌 경우
    parent[node] = find_parent(parent[node]);  // 타고 올라가서 부모 찾고
  }
  return parent[node];
}

void union_parent(int start, int end) {
  start = find_parent(start);
  end = find_parent(end);
  if (start < end) {  // 부모 노드 번호에 따라 부모 노드 정보 갱신
    parent[end] = start;
  } else {
    parent[start] = end;
  }
}

bool cmp(vector<int> first, vector<int> second) {  // 정렬 기준 정하기 위함
  return first[2] < second[2];
}

int solution(int n, vector<vector<int>> costs) {
  int total_cost = 0;
  for (int i = 0; i < n; i++) {  // 부모 노드 정보 담는 벡터 초기화
    parent.push_back(i);
  }
  sort(costs.begin(), costs.end(), cmp);  // cost 기준으로 정렬

  for (int i = 0; i < costs.size(); i++) {  // edge 하나하나 접근
    int start = costs[i][0], end = costs[i][1], cost = costs[i][2];
    if (find_parent(start) !=
        find_parent(end)) {      // 두 노드 간 부모 노드가 다르면
      union_parent(start, end);  // 부모 노드 합치기
      total_cost += cost;        // 그래프에 해당 간선 포함
    }
  }
  return total_cost;
}