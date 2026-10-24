
#include <iostream>

int main()
{
    int sum{0};

    for (int i{1}; i <= 10; ++i)
    {
        sum += i;

        if (sum > 20)
        {
            std::cout << "Sum exceeded 20!\n";
        }
    }

    std::cout << "Final sum: " << sum << '\n';
    return 0;
}
