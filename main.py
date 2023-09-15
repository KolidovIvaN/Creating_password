import random


def CreatePassword(length):
    lower_case = "qwertyuiopasdfghjklzxcvbnm"
    upper_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
    numbers = "1234567890"
    symbol = "!@#$%^&*()_=+-[]{};:\"|,.<>\/?"
    summa = lower_case + upper_case + numbers + symbol
    password = "".join(random.sample(summa, length))
    # print(len(summa)) # 91
    print(f"Your password: {password}")


def main():
    print("Enter the password length (max 91):")
    length = int(input())
    CreatePassword(length)


if __name__ == '__main__':
    main()
