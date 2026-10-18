def convert(text):
    # 先把 :) 替换成笑脸，再把 :( 替换成哭脸
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    # 拿到用户输入，调用 convert 处理，然后打印结果
    user_input = input("Input: ")
    result = convert(user_input)
    print(result)


# 在文件底部调用 main，这样运行文件时程序才会启动
main()
