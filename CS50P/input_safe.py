
def get_integer():
    while True:
        try:
            number = int(input("请输入一个整数："))
            return number
        except ValueError:
            print("输入错误！请不要输入字母或小数，请重新输入。")


def main():
    number = get_integer()
    print(f"输入成功！你输入的整数是：{number}")


if __name__ == "__main__":
    main()
