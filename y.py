import random
secret_number=random.randint(1,100)
print("欢迎来到猜数字游戏！")
print("我已经想好了一个1到100的数，快猜猜看吧！")
guess=None
while guess !=secret_number:
    guess=int(input("请输入您的猜测（1-100）："))
    if guess==secret_number:
        print("恭喜你，答对了！")
        break
    elif guess>secret_number:
        print("大了!")
    else:
        print("小了！")