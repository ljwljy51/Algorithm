// https://www.acmicpc.net/problem/7662
// https://please-amend.tistory.com/34
// C++ 큐를 오랜만에 다뤄봐서 위 코드를 참고했다 ㅜ.ㅜ
// PriorityQueue를 사용해 최소힙/최대힙 선언하는 방법에 주목!

// 우선순위 큐 라이브러리 사용

// map은 각 노드가 key와 value 쌍으로 이루어진 트리로, 중복을 허용하지 않는다.
// first가 key, second가 value
// 내부적으로 자동 정렬하며, key를 기준으로 오름차순으로 정렬

// 테스트케이스마다 상태 초기화해주기!!!!!!.

#include <iostream>
#include <map>
#include <queue>

using namespace std;

priority_queue<int, vector<int>, greater<int>> min_pq;  // 최소힙 선언
priority_queue<int, vector<int>, less<int>>
    max_pq;  // 최대힙 선언. 기본적으로 최대힙임
map<int, int> cnt;  // first는 특정 숫자를, second는 해당 숫자의 개수를 담도록.
                    // 양쪽 큐를 동기화하기 위함

void insert(int n) {  // 삽입
  min_pq.push(n);
  max_pq.push(n);
  cnt[n]++;
}

void deleteMin() {
  if (!min_pq.empty()) {
    cnt[min_pq.top()]--;  // 가장 상위 요소 pop
    min_pq.pop();
  }
}

void deleteMax() {
  if (!max_pq.empty()) {
    cnt[max_pq.top()]--;  // 가장 상위 요소 pop
    max_pq.pop();
  }
}

// 양쪽 큐를 동기화하기 위함.
void synchroPqs() {
  while (!min_pq.empty() && cnt[min_pq.top()] == 0) {
    min_pq.pop();
  }
  while (!max_pq.empty() && cnt[max_pq.top()] == 0) {
    max_pq.pop();
  }
}

void initStatus() {  // 새 테스트케이스마다 큐 초기화시켜주기 위함
  while (!min_pq.empty()) {
    min_pq.pop();
  }
  while (!max_pq.empty()) {
    max_pq.pop();
  }
  cnt.clear();  // map은 clear 지원. queue는 clear를 지원하지 않는다
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int T, n, k;
  char cmd;

  cin >> T;  // 테스트케이스 개수 입력
  while (T--) {
    initStatus();  // 테스트케이스마다 상태 초기화
    cin >> k;      // 커맨드 개수 입력
    for (int i = 0; i < k; i++) {
      cin >> cmd >> n;  // 커맨드 및 숫자 입력

      if (cmd == 'I') {
        insert(n);
      } else {         /// Delete 명령
        if (n == 1) {  // 최대값 삭제
          deleteMax();
        } else {  // 최소값 삭제
          deleteMin();
        }
        synchroPqs();  // 요소 삭제에 따른 큐 동기화
      }
    }

    if (max_pq.empty() || min_pq.empty()) {  // 둘중 한 큐라도 비어있는 경우
      cout << "EMPTY\n";
    } else {
      cout << max_pq.top() << " " << min_pq.top() << "\n";
    }
  }

  return 0;
}