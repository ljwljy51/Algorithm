//https://school.programmers.co.kr/learn/courses/30/lessons/42860
#include <string>
#include <vector>

using namespace std;

int solution(string name) {
    int spell_move = 0;
    int n=name.length();
    int cursor_move=n-1; //좌우 이동
    for (int i=0; i<n; i++){
        spell_move+=min(name[i]-'A', 'Z'-name[i]+1); //상하 이동
        
        int next_idx=i+1;
        while (next_idx<n && name[next_idx]=='A'){
            next_idx+=1;
        }
    cursor_move=min(min(cursor_move, 2*i+(n-next_idx)), i+2*(n-next_idx));
    }
    return cursor_move+spell_move;
}