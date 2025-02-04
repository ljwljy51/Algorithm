// https://www.acmicpc.net/problem/14500
// 접근방법 모두 생각해냈는데, 정작 구현에서 막혔다
// https://blog.thecloer.com/204?category=1054665

// 구조체로 테트로미노를 관리해 대칭,회전변환 수행하는 접근법
// 일부 하드코딩을 해준다

#include <iostream>
using namespace std;
const int TETROMINO_KIND = 5,
          TETROMINO_SIZE = 4;  // 톄트로미노의 종류 수 및 사이즈를 const로 정의

struct yx {
  int y, x;
};
struct tetromino {
  int w, h, flip, rotate;
  yx shape[TETROMINO_SIZE];
};

int N, M;
int answer = 0;
int board[500][500];

tetromino tetrominos[TETROMINO_KIND] = {
    {4, 1, 1, 2, {{0, 0}, {0, 1}, {0, 2}, {0, 3}}},  // ㅡ
    {2, 2, 1, 1, {{0, 0}, {0, 1}, {1, 0}, {1, 1}}},  // ㅁ
    {2, 3, 2, 4, {{0, 0}, {1, 0}, {2, 0}, {2, 1}}},  // ㄴ
    {2, 3, 2, 2, {{0, 0}, {1, 0}, {1, 1}, {2, 1}}},  // 늑
    {3, 2, 1, 4, {{0, 0}, {0, 1}, {0, 2}, {1, 1}}}   // ㅜ
};  // 테트로미노 배열 정의

int max(int &a, int &b) { return a > b ? a : b; }

void flip(tetromino &tetro) {
  for (yx &block : tetro.shape) {  // 각 블록에 대한 flip 적용(x축 기준 뒤집기)
    block.y = tetro.h - block.y - 1;
  }
}

void rotate90(
    tetromino &tetro) {  // 이 함수 구현이 까다로웠음. 시계방향으로 90도 회전
  int tmp = tetro.h;
  tetro.h = tetro.w;
  tetro.w = tmp;  // 기존 테트로미노 w,h값 swap

  for (yx &block : tetro.shape) {  // 블록 좌표값 수정
    tmp = block.x;
    block.x = tetro.w - block.y - 1;
    block.y = tmp;
  }
};

int getScore(
    int cur_y, int cur_x,
    tetromino &tetro) {  // 각 좌표에 테트로미노룰 놓았을 때 획득 점수 계산
  int score = 0;
  for (yx &block : tetro.shape) {
    score += board[cur_y + block.y][cur_x + block.x];
  }
  return score;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> N >> M;
  for (int i = 0; i < N; i++) {  // 칸별 점수 입력
    for (int j = 0; j < M; j++) {
      cin >> board[i][j];
    }
  }

  for (int tet_idx = 0; tet_idx < TETROMINO_KIND; tet_idx++) {
    tetromino &cur_tetro = tetrominos[tet_idx];
    for (int flip_cnt = 0; flip_cnt < cur_tetro.flip; flip_cnt++) {
      for (int rotate_cnt = 0; rotate_cnt < cur_tetro.rotate; rotate_cnt++) {
        for (int cur_y = 0; cur_y <= N - cur_tetro.h; cur_y++) {
          for (int cur_x = 0; cur_x <= M - cur_tetro.w; cur_x++) {
            answer = max(answer, getScore(cur_y, cur_x, cur_tetro));
          }
        }
        rotate90(cur_tetro);
      }
      flip(cur_tetro);
    }
  }
  cout << answer;
}