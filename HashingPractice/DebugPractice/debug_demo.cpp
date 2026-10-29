#include <iostream>
using namespace std;

int calculateAverage(int a, int b) {
    int result = (a + b) / 2;  // 故意制造一个错误
    return result;
}

int main() {
    int x = 10;
    int y = 20;

    int average = calculateAverage(x, y);

    cout << "x = " << x << '\n';
    cout << "y = " << y << '\n';
    cout << "average = " << average << '\n';

    return 0;
}