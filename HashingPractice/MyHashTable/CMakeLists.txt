
cmake_minimum_required(VERSION 3.20)

project(MyHashTable LANGUAGES CXX)

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# 创建 MyHashTable 核心库
add_library(my_hash_table
    src/MyHashTable.cpp
)
# 开启 GCC/Clang 编译警告
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    target_compile_options(my_hash_table PRIVATE
        -Wall
        -Wextra
        -Wpedantic
    )
endif()
# 配置头文件搜索目录
target_include_directories(my_hash_table PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)
# 创建基础测试程序
add_executable(basic_test
    tests/basic_test.cpp
)

target_link_libraries(basic_test PRIVATE my_hash_table)

# 创建完整测试程序
add_executable(test_hash_table
    tests/test.cpp
)

target_link_libraries(test_hash_table PRIVATE my_hash_table)

# 创建性能测试程序
add_executable(benchmark
    tests/benchmark.cpp
)

target_link_libraries(benchmark PRIVATE my_hash_table)
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    target_compile_options(basic_test PRIVATE
        -Wall -Wextra -Wpedantic
    )

    target_compile_options(test_hash_table PRIVATE
        -Wall -Wextra -Wpedantic
    )

    target_compile_options(benchmark PRIVATE
        -Wall -Wextra -Wpedantic
    )
endif()
# ==============================
# CTest 自动化测试配置
# ==============================

# 启用 CTest
include(CTest)

# 注册基础测试
add_test(
    NAME BasicTest
    COMMAND basic_test
)

# 注册完整自动化测试
add_test(
    NAME HashTableTest
    COMMAND test_hash_table
)
# ==============================
# 安装与库导出配置
# ==============================

include(GNUInstallDirs)

# 安装静态库
install(
    TARGETS my_hash_table
    EXPORT MyHashTableTargets
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

# 安装头文件
install(
    FILES include/MyHashTable.h
    DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

# 导出 CMake Targets
install(
    EXPORT MyHashTableTargets
    FILE MyHashTableTargets.cmake
    NAMESPACE MyHashTable::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/MyHashTable
)

# ==============================
# CMake Package Configuration
# ==============================

include(CMakePackageConfigHelpers)

# 生成 MyHashTableConfig.cmake
configure_package_config_file(
    "${CMAKE_CURRENT_SOURCE_DIR}/cmake/MyHashTableConfig.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/MyHashTableConfig.cmake"
    INSTALL_DESTINATION lib/cmake/MyHashTable
)

# 生成版本配置文件
write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/MyHashTableConfigVersion.cmake"
    VERSION 1.0.0
    COMPATIBILITY SameMajorVersion
)

# 安装配置文件
install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/MyHashTableConfig.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/MyHashTableConfigVersion.cmake"
    DESTINATION lib/cmake/MyHashTable
)