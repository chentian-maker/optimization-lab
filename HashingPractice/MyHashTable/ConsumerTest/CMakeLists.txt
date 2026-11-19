cmake_minimum_required(VERSION 3.20)

project(ConsumerTest LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 自动查找 MyHashTable
find_package(MyHashTable 1.0 CONFIG REQUIRED)

# 创建消费者程序
add_executable(consumer
    src/main.cpp
)

# 链接 MyHashTable
target_link_libraries(consumer
    PRIVATE MyHashTable::my_hash_table
)