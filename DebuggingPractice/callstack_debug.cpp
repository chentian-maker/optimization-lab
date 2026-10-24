
#include <iostream>

int calculate(int x)
{
    int result = x * 2;
    return result;
}

int main()
{
    int a = 10;
    int b = calculate(a);

    std::cout << "Result: " << b << '\n';
    return 0;
}
