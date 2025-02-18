// bfs 써서 풀면 될 줄 알았는데, 부르트포스+백트래킹잉었다.
// bfs 쓰면 시간초과됨
// '도시에 있는 치킨집 중에서 최대 M개를 고르고" 부분에서 조합을 써야 함을
// 눈치챘어야 함
// https://velog.io/@dianestar/%EB%B0%B1%EC%A4%80BOJ-15686%EB%B2%88-%EC%B9%98%ED%82%A8%EB%B0%B0%EB%8B%AC
// 위 코드 참고

#include <climits>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

struct House {
  int r, c;  // 집에 대한 정보
};
struct Chicken {  // 치킨집에 대한 정보
  int r, c;
  bool selected;
};
int N, M;
int minCityChickenDist = INT_MAX;
vector<House> house;
vector<Chicken> chicken;  // 집, 치킨에 대한 배열 생성

void cal_dist() {  // 각 집에 대해 선택된 M개의 치킨집과의 거리 중 최소값 구하기
  // 이를 모두 더해 도시 치킨거리를 구하고, 최소값 업데이트
  int cityChickenDist = 0;
  for (int i = 0; i < house.size(); i++) {
    // 각 집마다의 최소 치킨거리 구하기 위함
    int minChickenDist = INT_MAX;
    for (int j = 0; j < chicken.size(); j++) {
      if (chicken[j].selected) {
        int chickenDist =
            abs(house[i].r - chicken[j].r) + abs(house[i].c - chicken[j].c);
        minChickenDist =
            (chickenDist < minChickenDist) ? chickenDist : minChickenDist;
      }
    }
    cityChickenDist += minChickenDist;
  }
  minCityChickenDist = (cityChickenDist < minCityChickenDist)
                           ? cityChickenDist
                           : minCityChickenDist;
}

void select_Chicken(
    int idx, int cnt) {  // M개의 치킨집 조합을 구하는 과정. '조합'이므로 중복
                         // 선택을 막히 위해 기준 인덱스를 인자로 전달
  if (cnt == M) {
    cal_dist();  // 선택이 완료되었으면 거리 계산 수행
    return;
  }
  for (int i = idx; i < chicken.size(); i++) {
    if (!chicken[i].selected) {  // 선택되지 않은 경우
      chicken[i].selected = true;
      select_Chicken(i + 1, cnt + 1);  // 함수 재호출
      chicken[i].selected = false;     // 백트래킹
    }
  }
}

int main() {
  cin >> N >> M;
  int val;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> val;
      if (val == 1) {
        house.push_back({i, j});
      } else if (val == 2) {
        chicken.push_back({i, j, false});
      }
    }
  }  // 입력 받기

  select_Chicken(0, 0);
  cout << minCityChickenDist;

  return 0;
}