
#include <iostream>

double calculate_average(int sum, int count)
{
    return sum / count;
}

double calculate_score(int a, int b, int c)
{
    int sum = a + b + c;
    return calculate_average(sum, 3);  // 故意留下错误
}

int main()
{
    int a = 10;
    int b = 20;
    int c = 30;

    double score = calculate_score(a, b, c);

    std::cout << "Expected average: 20\n";
    std::cout << "Actual average: " << score << '\n';

    return 0;
}
