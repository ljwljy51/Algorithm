// 입력 범위가 너무 크면 이분탐색 고려하자

#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {
  int start = 1;  // 시작점의 돌 위치
  int end = distance;

  sort(rocks.begin(), rocks.end());
  rocks.push_back(distance);

  int mid, del_stone_cnt, current_stone, answer;
  while (start <= end) {
    mid = (start + end) / 2;
    del_stone_cnt = 0;
    current_stone = 0;
    for (int rock : rocks) {  // 벡터 내 요소 어떻게 받아오는가에 유의
      if (rock - current_stone < mid) {  // 거리가 기준값보다 작은 경우 돌 제거
        del_stone_cnt += 1;
      } else {  // 거리가 기준값보다 같거나 높을 경우 현재 돌을 새로운 기준으로
                // 둠
        current_stone = rock;
      }

      if (del_stone_cnt > n) {  // 돌을 더 많이 제거한 경우 for문 빠져나옴
        break;
      }
    }

    if (del_stone_cnt > n) {  // 돌을 더 많이 제거했을 경우 기준 낮춤
      end = mid - 1;
    } else {  // 돌을 딱 맞게, 혹은 더 제거했을 경우 기준 높임
      answer = mid;
      start = mid + 1;
    }
  }
  return answer;
}