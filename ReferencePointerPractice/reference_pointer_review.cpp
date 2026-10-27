#include <iostream>

// 练习 1：交换两个原变量的值
void swap(int& first, int& second)
{
    int temp = first;
    first = second;
    second = temp;// 在这里补充代码
}

// 练习 2：把指针指向的整数增加 10
void modify(int* ptr)
{
    if (ptr == nullptr)
    {
        return;
    }

    *ptr += 10;
}

int main()
{
    int a = 3;
    int b = 8;

    std::cout << "Before swap: a = " << a
              << ", b = " << b << '\n';

    swap(a, b);

    std::cout << "After swap: a = " << a
              << ", b = " << b << '\n';

    modify(&a);

    std::cout << "After modify: a = " << a
              << ", b = " << b << '\n';

    modify(nullptr);

    std::cout << "After nullptr: program continues\n";

    return 0;
}
/*
今日学习记录：

1. int 参数接收副本，修改参数不影响原变量。
2. int& 参数引用原变量，修改参数会影响原变量。
3. const int& 可以读取原变量，不能通过该引用修改它。
4. int* 参数接收地址，通过 *ptr 修改指向的原变量。
5. 解引用之前，需要确保指针指向有效对象；
   本练习先排除 nullptr，传入的其他地址来自仍然存活的变量。

本次运行：
swap 前：a = 3，b = 8
swap 后：a = 8，b = 3
modify 后：a = 18，b = 3
*/