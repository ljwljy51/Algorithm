#include <string>
#include <stack>

using namespace std;

string solution(string number, int k) {
    string answer = "";
    stack<int> nums_stack;
    
    for (int i=0; i<number.length(); i++){
        while (!nums_stack.empty() && nums_stack.top()<number[i] && k>0){
            nums_stack.pop();
            k-=1;
        }
        nums_stack.push(number[i]);
    }
    
    while (!nums_stack.empty()){ //스택에서 요소 제거하면서 문자열 생성
        answer=answer.insert(0, 1, nums_stack.top());
        nums_stack.pop();
    }
    return answer.substr(0, answer.length()-k);
}