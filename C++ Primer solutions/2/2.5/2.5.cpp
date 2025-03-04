#include <iostream>
#include <string>
#include <typeinfo>
using namespace std;

int main()
{
    // 字面值类型示例
    cout << "\nLiteral type examples:" << endl;
    cout << "'a' : " << typeid('a').name() << endl;
    cout << "L'a' : " << typeid(L'a').name() << endl;
    cout << "\"a\" : " << typeid("a").name() << endl;
    cout << "L\"a\" : " << typeid(L"a").name() << endl;
    cout << "10 : " << typeid(10).name() << endl;
    cout << "10u : " << typeid(10u).name() << endl;
    cout << "10L : " << typeid(10L).name() << endl;
    cout << "10uL : " << typeid(10uL).name() << endl;
    cout << "012 : " << typeid(012).name() << endl;
    cout << "0xC : " << typeid(0xC).name() << endl;
    cout << "3.14 : " << typeid(3.14).name() << endl;
    cout << "3.14f : " << typeid(3.14f).name() << endl;
    cout << "3.14L : " << typeid(3.14L).name() << endl;
    cout << "10. : " << typeid(10.).name() << endl;
    cout << "10e-2 : " << typeid(10e-2).name() << endl;
    cout << "0x10 : " << typeid(0x10).name() << endl;
    cout << "0x10u : " << typeid(0x10u).name() << endl;
    /*
    'a'      // char (on most systems, 4 bytes due to integer promotion)
    L'a'     // wchar_t (wide character)
    "a"      // const char[2] (string literal with null terminator)
    L"a"     // const wchar_t[2] (wide string literal)
    10       // int
    10u      // unsigned int
    10L      // long
    10uL     // unsigned long
    012      // int (octal literal, decimal value 10)
    0xC      // int (hexadecimal literal, decimal value 12)
    3.14     // double
    3.14f    // float
    3.14L    // long double
    10       // int (duplicate)
    10u      // unsigned int (duplicate)
    10.      // double (floating point without fractional part)
    10e-2    // double (scientific notation, value 0.1)
    0x10     // int (hexadecimal literal, decimal value 16)
    0x10u    // unsigned int (hexadecimal literal)
    */
    return 0;
}