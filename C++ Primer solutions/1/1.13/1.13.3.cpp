#include <iostream>
using namespace std;
int main()
{
    cout << "Enter two numbers: ";
    int v1 = 0, v2 = 0;
    cin >> v1 >> v2;
    int sum = 0;
    for (int i = v1; i < v2 - 1; i++)
    {
        cout << i + 1 << endl;
    }
    for (int i = v2; i < v1 - 1; i++)
    {
        cout << i + 1 << endl;
    }
}