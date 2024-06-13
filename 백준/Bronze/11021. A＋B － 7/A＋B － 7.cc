#include <iostream>
using namespace std;
int main(void) {
  int L;
  cin >> L; //cout << endl;
  for(int z = 0; z < L ; z += 1){
      int A;
      int B;
      cin >> A >> B;
      cout << "Case #" << z+1 <<  ": " ;
      cout << A + B  ;
      cout << endl;
    }
    
}
