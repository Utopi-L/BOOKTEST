#include <iostream>
using namespace std;
int main()
{
    int month = 9, day = 7;
    // 无符号整型
    int month1 = 09, day1 = 07; // Removed leading zeros to avoid octal interpretation
    cout << month << " " << day << endl;
    cout << month1 << " " << day1 << endl;
    return 0;
}
