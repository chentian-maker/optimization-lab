#include <iostream>

// 1. 传值：value 是调用者变量的副本
void changeByValue(int value)
{
    value = 100;
    std::cout << "Inside changeByValue: value = "
              << value << '\n';
}

// 2. 传引用：value 是调用者变量的别名
void changeByReference(int& value)
{
    value = 100;
}

// 3. const 引用：能读取，但不能通过 value 修改原变量
void showByConstReference(const int& value)
{
    std::cout << "Read through const reference: "
              << value << '\n';

    // 取消下一行的注释会导致编译错误：
    // value = 100;
}

// 4. 交换两个原变量的值
void swap(int& first, int& second)
{
    int temp = first;
    first = second;
    second = temp;
}

// 5. 通过指针修改原变量
void modify(int* ptr)
{
    // nullptr 表示没有指向有效对象
    if (ptr == nullptr)
    {
        std::cout << "modify: nullptr, skipped\n";
        return;
    }

    *ptr = 999;
}

int main()
{
    int a = 10;

    std::cout << "[Pass by value]\n";
    std::cout << "Before: a = " << a << '\n';
    changeByValue(a);
    std::cout << "After: a = " << a << "\n\n";

    std::cout << "[Pass by reference]\n";
    std::cout << "Before: a = " << a << '\n';
    changeByReference(a);
    std::cout << "After: a = " << a << "\n\n";

    std::cout << "[Const reference]\n";
    showByConstReference(a);
    std::cout << '\n';

    int x = 10;
    int y = 20;

    std::cout << "[Swap]\n";
    std::cout << "Before: x = " << x
              << ", y = " << y << '\n';
    swap(x, y);
    std::cout << "After: x = " << x
              << ", y = " << y << "\n\n";

   int number = 30;

// 创建指针，保存 number 的地址
int* ptr = &number;

std::cout << "[Pointer]\n";

// 输出原变量的值
std::cout << "number = " << number << '\n';

// 输出原变量的地址
std::cout << "&number = " << &number << '\n';

// 输出指针保存的地址
std::cout << "ptr = " << ptr << '\n';

// 通过指针读取 number 的值
std::cout << "*ptr = " << *ptr << '\n';

// 通过指针修改 number
*ptr = 50;

std::cout << "After *ptr = 50: number = "
          << number << '\n';

// 把指针保存的地址传入函数
modify(ptr);

std::cout << "After modify(ptr): number = "
          << number << '\n';

// 测试空指针
modify(nullptr);
std::cout << "\n[Const reference experiment]\n";

int score = 60;
const int& view = score;

std::cout << "Before: score = " << score
          << ", view = " << view << '\n';

score = 90;

std::cout << "After: score = " << score
          << ", view = " << view << '\n';
    return 0;
}