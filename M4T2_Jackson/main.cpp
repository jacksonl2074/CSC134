// CSC 134
// M4T2 - Menus
// Version 2 -- started our character creator
// for Thudd
// Laura K. Jackson
// 2.27.23
#include <iostream>
#include <ctime>    // enables use of time() function
#include <cstdlib>  // enables rand(), srand()
using namespace std;

// menu functions
void option_one () {
    // count from 0 to 9
    cout << "Using while() to count" << endl;
    int num = 0;
    while (num < 10) {
        cout << num << " ";
        num++;
    }
    cout << endl;

    cout << "Using for() to count" << endl;
    for (int i=0; i<10; i++) {
        cout << i << " ";
    }
    cout << endl;
}

void option_two() {
    // dice roller
    int d6_1, d6_2, d6_3; // 3 dice (6 sided)
    int total; // 3d6
    int seed;
}
void option_three() {
    //  sum and average of dice
}
// There is not option 4 function, it's just quit.

// main  menu
int main()
{
    // display a menu
    // have the user choose 1, 2, 3,or 4.
    // do something based on the choice

    cout << "Welcome to the menu" << endl;
    cout << "Press 1 to count" << endl;
    cout << "Press 2 to sum up numbers" << endl;
    cout << "Press 3 to TODO" << endl;  // not implemented yet
    cout << "Choice: ";
    // input validation
    int choice;
    cin >> choice;
    // user must pick 1, 2, 3, or 4.
    while (choice < 1 || choice > 4) {
        cout << "Please choose 1, 2, 3, or 4: ";
        cin >> choice;
    }
    // if we get here, we know choice is valid
    if (choice == 1) {
        option_one();   // function call
    }
    cout << "Thanks for using the menu." << endl;
    return 0;
}
