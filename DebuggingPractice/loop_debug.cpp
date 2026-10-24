
#include <iostream>

int main()
{
    int target{15};
    int sum{0};

    for (int i{1}; i <= 5; ++i)
    {
        sum += i;
        std::cout << "i = " << i
                  << ", sum = " << sum << '\n';
    }

    std::cout << "Expected sum: 15\n";
    std::cout << "Actual sum: " << sum << '\n';

    if (sum != target)
    {
        std::cout << "BUG: incorrect sum!\n";
    }

    return 0;
}
