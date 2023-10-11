// 큐는 front, back 요소 말고는 내부 값 탐색 불가. 내부 값 보고싶으면 일일이
// pop해서 확인해야함 위 내용 몰라서 엄청 헤맴 왜인지 모르겠으나, 파이썬 로직
// 그대로 짜도 계속 테스트 케이스가 틀렸었음. 조건문 변수 부분에 오류가 있었던 거였음
// 조건문에서 조건이 변수로 주어지는 경우, 어떻게 처리되는지 잘 파악해야 할듯

#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(string begin, string target, vector<string> words) {
  vector<string> q;
  q.push_back(begin);
  int cnt = 0;
  while (!q.empty()) {
    cnt += 1;
    int len_q = q.size();  // 이 부분이 핵심!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    // 조건문 쓸 때 변수를 조건으로 사용하지 말자..........2시간 버림
    for (int i = 0; i < len_q; i++) {
      begin = q.front();
      q.erase(q.begin());
      for (int j = 0; j < words.size(); j++) {
        int diff_cnt = 0;
        for (int k = 0; k < begin.length(); k++) {
          if (begin[k] != words[j][k]) {
            diff_cnt += 1;
          }
        }

        if (diff_cnt == 1) {
          q.push_back(words[j]);
          words.erase(words.begin() + j);
        }
      }
    }

    if (find(q.begin(), q.end(), target) != q.end()) {  // 큐 안에 타겟 있을
                                                        // 경우
      return cnt;
    }
  }

  return 0;
}
