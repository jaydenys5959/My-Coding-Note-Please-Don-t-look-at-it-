#include <iostream>
using namespace std;
int main(void) {
  int A;
  int B;
  cin >> A;
  cin >> B;
if(A == B){
    cout << "==";
}
else if(A > B){
    cout << ">";
}
else{
    cout << "<";  
  }
}
