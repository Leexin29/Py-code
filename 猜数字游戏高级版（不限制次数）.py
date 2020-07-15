import random

print("\t\t\t\t\t欢迎来到猜数字游戏！")
print("现在我心里想一个1-100之间的数字。")
print("试着猜一猜我心里想的是什么数字吧。")

number = random.randint(1 ,100)
tries = 1

while True:
    a = int(input("猜一猜我心里想的是什么数字："))
    if a>number:
        print("太大了")
        tries += 1
        continue
    elif a < number:
        print("太小了")
        tries += 1
        continue
    else:
        print("猜对了")
        tries += 1
        break
		
print("\n\n恭喜你猜出了数字，你总共猜测了",tries,"次")

input("\n\n\n\nPress the enter key to exit.")
