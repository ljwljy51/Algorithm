// https://www.acmicpc.net/problem/1043
// 이진탐색 쓰면 될 줄 알았는데, 그래프 문제였음..
// 진실을 아는 사람과 같은 파티에 참석할 경우, 그 사람도 거짓말임을 알게 되는 걸
// 고려 못함.
// Union Find로 풀어야 한다고 한다. Union-Find알고리즘이란, 여러 개의
// 집합을 관리하면서 두 원소가 같은 집합에 속해 있는지 판단하는 알고리즘. 주로
// 그래프에서 연결 요소를 찾거나, MST를 구현할 때 사용됨

// 해당 문제의 경우, 각 파티마다 참여하는 사람들을 같은 그래프로 묶고, 진실을
// 아는 사람과 같은 그래프에 있는지 확인하면 되는 것
//  컴퓨터 바이러스 문제랑 비슷한듯

#include <iostream>
#include <vector>

using namespace std;
int N, M;
vector<int> parent(51);  // union find 수행하기 위한 부모 배열

// 경로 압축. find함수
int find(int num) {
  if (parent[num] == num) {  // 부모 노드 찾기
    return num;
  }
  return parent[num] = find(parent[num]);  // 경로압축
}

// union함수. 집합 병합 위함
void unite(int a, int b) {
  int rootA = find(a);
  int rootB = find(b);
  if (rootA != rootB) {
    parent[rootB] = rootA;
  }  // 부모노드 정보 갱신
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> N >> M;
  vector<vector<int>> party(M);  // 각 파티 당 참여 사람 목록 저장 위함
  int num_truth;
  cin >> num_truth;  // 진실 아는 사람의 수

  vector<bool> knowsTruth(51, false);  // 진실 아는 사람 여부 체크하기 위함

  vector<int> truthPeople(num_truth);    // 진실 아는 사람 목록
  for (int i = 0; i < num_truth; i++) {  // 진실 아는 사람 목록 추가 및 여부
                                         // 갱신
    cin >> truthPeople[i];
    knowsTruth[truthPeople[i]] = true;
  }

  // Union FInd 알고리즘 사용 위한 각 노드에 대한 부모 노드 설정
  for (int i = 1; i <= N; i++) {
    parent[i] = i;  // 초기엔 자기 자신이 부모
  }
  // 각 파티 정보 입력 후 같은 파티에 속한 사람들은 같은 집합으로 묶기
  for (int i = 0; i < M; i++) {
    int num_people;
    cin >> num_people;            // 파티 참여자 수 입력
    party[i].resize(num_people);  // 벡터 요소 직접 접근 위해 resize 필요
    for (int j = 0; j < num_people; j++) {
      cin >> party[i][j];
      if (j != 0) {  // 같은 파티 참여자인 경우 경로압축
        unite(party[i][j - 1], party[i][j]);
      }
    }
  }

  // 진실 아는 사람과 같은 집합에 속하는 사람의 경우, 그 사람들도 진실을 알게됨
  for (int person : truthPeople) {
    int root = find(person);  // 진실 아는 사람의 부모 노드 찾기
    for (int i = 0; i <= N; i++) {
      if (root == find(i)) {
        knowsTruth[i] = true;  // 진실 알게되는 경우 체크
      }
    }
  }

  // 진실 모르게 되는 파티 개수 세기
  int answer = 0;
  for (const auto& p : party) {
    bool has_truth = false;
    for (int person : p) {  // 진실 아는 사람 있는지 확인
      if (knowsTruth[person]) {
        has_truth = true;
        break;
      }
    }
    if (!has_truth) {
      answer++;  // 진실 아는 사람 없으면 추가
    }
  }

  cout << answer;
}
