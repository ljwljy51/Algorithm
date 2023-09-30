// sort 방식, 변수 할당 방법, 벡터 요소 접근 방법 유의

#include <algorithm>  //sort 사용 위함
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> people, int limit) {
  sort(people.begin(), people.end());
  int start = 0, end = people.size() - 1;  // 변수 할당 방식 유의
  int boat_cnt = 0;
  while (start <= end) {
    boat_cnt += 1;
    if (people[start] + people[end] <=
        limit) {  // 가장 가벼운 사람과 가장 무거운 사람 먼저 태움
      start += 1;  // 투포인터
      end -= 1;
    } else {  // 무거운 사람 한 명만 태움 (그래야 효율적)
      end -= 1;
    }
  }
  return boat_cnt;
}