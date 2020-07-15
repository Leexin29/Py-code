import random

print("\t\t\t欢迎来到猜数字游戏！")
print("现在我想一个1-100之间的数字。")
print("试着猜猜看我想的是什么数字吧。")

a = random.randint(1, 100)

print("\n\n你有三次机会次猜测我心里想的数字")

for i in range(3):
    b = int(input("\n猜猜我心里想的数字："))
    if b == a:
        print("恭喜你，猜对了")
        break
    elif b < a:
        print("太小了，请重新猜一次")
    else:
        print("太大了，请重新猜一次")
        
else:
	print("抱歉，机会用完了哦。")


input("\n\n\nPress the enter key to exit")