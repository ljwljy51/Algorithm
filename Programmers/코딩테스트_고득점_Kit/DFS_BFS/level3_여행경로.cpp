// 역시나 솔루션 봄..ㅎ
// https://gyyeom.tistory.com/43
// 중간에 경로 끊긴 경우 대한 처리 부분에 주목
// 백트래킹 어떻게 하는지 주목

#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<string> answer;
bool visited[100001];
bool flag = false;
int cnt = 0;

void dfs(string start, vector<vector<string>> tickets) {
  if (cnt == tickets.size()) {
    flag = true;
  }
  answer.push_back(start);
  for (int i = 0; i < tickets.size(); i++) {
    if (!visited[i] &&
        tickets[i][0] == start) {  // 현재 티켓의 시작지가 인자값과 같으면
      visited[i] = true;            // 방문처리
      cnt++;                        // 카운트 증가
      dfs(tickets[i][1], tickets);  // 도착지 기준으로 다시 재귀함수 호출

      if (!flag) {
        answer.pop_back();
        visited[i] = false;  // 백트래킹
      }
    }
  }
}

vector<string> solution(vector<vector<string>> tickets) {
  sort(tickets.begin(), tickets.end());
  dfs("ICN", tickets);
  return answer;
}