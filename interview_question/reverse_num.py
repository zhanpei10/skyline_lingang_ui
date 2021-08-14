# 反转数字

def reverse(number):
    str_num = str(number)
    str_num1 = str_num[::-1]

    return int(str_num1)


def reverse_three(number):
    num1 = number // 100
    num2 = number % 100 // 10
    num3 = number % 10
    return num3 * 100 + num2 * 10 + num1


if __name__ == '__main__':
    # print(reverse(123456789))
    print(reverse_three(901))