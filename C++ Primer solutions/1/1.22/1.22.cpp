#include <iostream>
#include "Sales_item.h"
using namespace std;
int main()
{
    Sales_item book, total;
    if (cin >> total)
    {
        while (cin >> book)
        {
            if (total.isbn() == book.isbn())
                total += book;
        }
        cout << total << endl;
    }
}