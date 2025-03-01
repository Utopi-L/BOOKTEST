#include<iostream>
using namespace std;
int main()
{
    cout<<"Enter two numbers: ";
    int v1=0,v2=0;
    cin>>v1>>v2;
    int sum=0;
    while(v1<(v2-1))
    {
        
        cout<<v1+1<<endl;
        v1++;
    }
    while(v2<(v1-1))
    {
        cout<<v2+1<<endl;
        v2++;
    }
}