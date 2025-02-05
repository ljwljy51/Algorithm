// https://www.acmicpc.net/problem/1918
// 전형적인 스택 사용 문제
// 전에 풀었던 괄호 오류찾기 부류의 문제와 비슷한듯
// 문제 자체는 간단하나, 조건 및 스택 조작 관련해 안꼬이게 조심

// 연산자 우선순위 고려

#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  string formula;
  stack<char> operators;
  cin >> formula;  // 식 입력받기

  for (int i = 0; i < formula.length(); i++) {
    // 피연산자인 경우
    if ((formula[i] >= 'A') && (formula[i] <= 'Z')) {
      cout << formula[i];  // 일단 출력
    }
    // 연산자인 경우
    else {
      if (formula[i] ==
          '(') {              // 괄호 있는 경우 이후 )나올때까지 스택에 넣어주기
        operators.push('(');  //
      }

      else {
        if (formula[i] == ')') {  // ( 나올때까지 연산자 출력
          while ((!operators.empty()) && (operators.top() != '(')) {
            cout << operators.top();
            operators.pop();
          }
          operators.pop();
        }

        else if ((formula[i] == '*') || (formula[i] == '/')) {
          while ((!operators.empty()) &&
                 ((operators.top() == '*') ||
                  (operators.top() == '/'))) {  // 기존 스택에 *./있는 경우
            cout << operators.top();
            operators.pop();
          }
          operators.push(formula[i]);
        }

        else if ((formula[i] == '-') || formula[i] == '+') {
          while ((!operators.empty()) &&
                 (operators.top() != '(')) {  // ( 만나기 전까지 출력
            cout << operators.top();
            operators.pop();
          }
          operators.push(formula[i]);
        }
      }
    }
  }

  while (!operators.empty()) {
    cout << operators.top();
    operators.pop();
  }

  return 0;
}