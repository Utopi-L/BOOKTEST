#include<iostream>
using namespace std;
int main()
{
    int i,&ri=i;
    i=5;
    ri=10;
    std::cout<<i<<" "<<ri<<endl;
}
// Output: 10 10
// Explanation: Here, ri is a reference to i. So, when we change the value of ri, it changes the value of i as well. So, the output is 10 10.