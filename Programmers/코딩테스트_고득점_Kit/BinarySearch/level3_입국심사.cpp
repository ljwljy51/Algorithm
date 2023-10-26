// 벡터 정렬, 마지막 요소값 참조하는 부분 주목
// for문에서 요소 어떻게 하나하나 받아오는지 주목
// 타입캐스팅

#include <algorithm>
#include <string>
#include <vector>

using namespace std;

long long solution(int n, vector<int> times) {
  sort(times.begin(), times.end());
  long long answer = 0;
  long long left = 1;
  long long right = (long long)times.back() * n;
  long long mid;
  long long people = 0;

  while (left <= right) {
    mid = (left + right) / 2;
    people = 0;
    for (long long time : times) {
      people += (mid / time);
      if (people >= n) {
        break;
      }
    }
    if (people >= n) {
      answer = mid;
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return answer;
}