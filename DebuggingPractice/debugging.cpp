#include <iostream>

int main()
{
    int a{10};
    int b{20};

    int average{(a + b) / 2};

    std::cout << "Expected average: 15\n";
    std::cout << "Actual average: " << average << '\n';

    return 0;
}