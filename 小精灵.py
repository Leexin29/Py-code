print("小精灵：您好，欢迎光临古灵阁，请问您需要帮助吗？需要or不需要？")
answer1 = input("你：")

if answer1 == "需要":
    print("小精灵：请问你需要什么帮助呢？1、存取款；2、货币兑换；3、咨询")
    answer2 = int(input("你："))
    if answer2==2:
        print('''小精灵：金加隆和人民币的兑换率为1：51.3，即一金加隆=51.3人民币
        小精灵：请问您需要虽换多少金加隆呢？''')
        answer3 = input("你：")
        print("小精灵：好的，我知道了，您需要兑换"+answer3+"金加隆")
        print("小精灵：那么，您需要兑换"+str(int(answer3)*51.3)+"人民币")
        	
    elif answer2 == 1:
        print("小精灵：请您前去存取款窗口。谢谢配合！")
    elif answer2 == 3:
        print("小精灵：请你前去咨询窗口。谢谢配合！")
        
else:
    print("好的，再见")


print("\n\n\n谢谢光临，再见")
