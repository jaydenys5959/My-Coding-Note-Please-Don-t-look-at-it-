#include <iostream>
using namespace std;
int main(void) {
  int N;
  cin >> N; //cout << endl;
  for(int i = 1; i <= N; i += 1){ 
    for(int x = 0; x < i; x += 1){
      cout << "*";
    }    
    cout << endl;
  }
}