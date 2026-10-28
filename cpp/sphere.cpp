#include <iostream>
#include <vector>

double sphere(const std::vector<double>& x) {
    double s = 0.0;
    for (double xi : x) {
        s += xi * xi;
    }
    return s;
}

int main() {
    std::cout << sphere({1.0, -2.0, 3.0}) << '\n';
    return 0;
}
