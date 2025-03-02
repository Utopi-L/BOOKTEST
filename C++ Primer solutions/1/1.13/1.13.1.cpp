#include <iostream>
using namespace std;
int main()
{
    int sum = 0;
    for (int i = 50; i <= 100; i++)
    {
        sum += i;
    }
    cout << "The sum of numbers from 50 to 100 is " << sum << endl;
}