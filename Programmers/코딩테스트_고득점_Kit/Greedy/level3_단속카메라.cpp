// https://school.programmers.co.kr/learn/courses/30/lessons/42884?language=cpp
#include <algorithm>
#include <vector>
using namespace std;

bool cmp(vector<int> a, vector<int> b) {
  return a[1] < b[1];  // 도착점 기준 오름차순 정렬
}

int solution(vector<vector<int>> routes) {
  sort(routes.begin(), routes.end(), cmp);
  int cnt_camera = 1;
  int current_arrival = routes[0][1];  // 초기값 지정
  for (int i = 1; i < routes.size(); i++) {
    if (routes[i][0] > current_arrival) {
      cnt_camera += 1;
      current_arrival = routes[i][1];
    }
  }
  return cnt_camera;
}