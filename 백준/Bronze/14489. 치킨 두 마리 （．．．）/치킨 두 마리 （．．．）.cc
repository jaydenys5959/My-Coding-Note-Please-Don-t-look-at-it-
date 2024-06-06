#include <iostream>
using namespace std;
int main(void) {
  int A;
  int B;
  int C;
  cin >> A >> B >> C;
  int D = A + B;
  int E = C * 2;
  if(D < E){
    cout << D;
  }
  else{
    int w = D - E;
    cout << w;
  }
  
}
  