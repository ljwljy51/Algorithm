//  https://school.programmers.co.kr/learn/courses/30/lessons/43165
// 왜인지는 모르겠으나.. 반복문 돌 때 q.size()값을 직접 넣어주면 시간초과가
// 떴었다. 따로 변수 선언해서 했더니 해결이 되긴 했으나, 왜 그런건지 아직도
// 헷갈림. 계속 내부 요소가 변경되어서 값이 변동적이라 그런 것 아닌가싶다.

#include <queue>
#include <vector>
using namespace std;

int solution(vector<int> numbers, int target) {
  queue<int> q;
  q.push(numbers[0]);
  q.push(-1 * numbers[0]);

  for (int i = 1; i < numbers.size(); i++) {
    int q_len = q.size();
    for (int j = 0; j < q_len; j++) {
      int tmp = q.front();
      q.pop();
      q.push(tmp + numbers[i]);
      q.push(tmp - numbers[i]);
    }
  }

  int answer = 0;
  int q_len = q.size();
  for (int i = 0; i < q_len; i++) {
    if (q.front() == target) {
      answer += 1;
    }
    q.pop();
  }
  return answer;
}