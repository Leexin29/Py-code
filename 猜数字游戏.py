jls_extract_var = '''temp=input("不妨猜一下我心里想的是哪个数字:")

guess=int(temp)

if guess == 8:

    print("恭喜你，猜对了！！")

    print("哼，猜对了也没有奖励")

else:

    print("猜错了，我心里想的是8")

print("游戏结束喽，不玩了")

'''





def guess_number():

    answer = random.randint(1, 10)

    while True:

        try:

            guess = int(input("不妨猜一下我心里想的是哪个数字（1-10之间）："))

            if guess == answer:

                print("恭喜你，猜对了！")

                break

            else:

                print("猜错了，再试一次吧！")

        except ValueError:

            print("请输入数字！")


    print("游戏结束，再见！")


if __name__ == '__main__':

    guess_number()