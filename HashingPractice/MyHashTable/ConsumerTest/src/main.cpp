#include <iostream>
#include "MyHashTable.h"

int main()
{
    MyHashTable table(7);

    table.insert(100, 200);

    int value = 0;

    if (table.find(100, value))
    {
        std::cout << "Key: 100" << std::endl;
        std::cout << "Value: " << value << std::endl;
    }

    return 0;
}