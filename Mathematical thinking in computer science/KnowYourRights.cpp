#include <iostream>

using namespace std;

int main() {
    int loop=0,loops=0;
    // for the two-digit number problem
    // effecient way
    for (int i = 10; i < 100; i++) {
        loops++;
      //  cout<<loops<<" " ;
        int x = i % 10;
        int y = i / 10;
        if (x * 7 == 10 * y + x) {
            cout<<endl;
            cout << i <<endl;
        }
    }
    
    // for the four-digit number problem
    // naive way
    for (int i = 10; i < 1000; i++) {
       int x = i%10;
       loop++;
        // cout<<loop<<" ";
        if (x * 7 == i) {
            cout<<endl;
            cout << i<<<<endl;
        }
    }

    return 0;
}
