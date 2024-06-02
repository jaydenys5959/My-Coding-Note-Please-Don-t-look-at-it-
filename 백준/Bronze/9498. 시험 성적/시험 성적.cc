#include <iostream>
using namespace std;
int main(void) {
  int T;
  cin >> T;
  if(T >= 90 && T <= 100) {
      cout << "A";
  }
  else if(T >= 80 && T <= 89) {
      cout << "B";
  }
  else if(T >= 70 && T <= 79) {
      cout << "C";
  }
  else if(T >= 60 && T <= 69) {
      cout << "D";
    }
  else{
      cout << "F";
  }
}  
