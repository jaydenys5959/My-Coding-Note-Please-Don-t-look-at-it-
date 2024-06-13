#include <iostream>
using namespace std;
int main(void) {
  int A; // 시
  int B; // 분
  int C; // 요리가 걸리는 시간
  int D; // 요리가 걸리는 시간 + 분

  cin >> A >> B;
  cin >> C; 

  D = (A * 60) + B + C; //요리에 걸리는 시간 + 현재 시간을 분으로 바꾼 거 

  int hour = (D/60) % 24 ; 
  int min = D % 60;

  cout << hour << " " << min;
  

}