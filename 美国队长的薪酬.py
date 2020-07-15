captain_salary = int(input("captain_salary:"))

if captain_salary<=500:
	print("欢迎进入史塔克穷人帮前三名")
	if captain_salary<=100:
		print("恭喜你荣获\"美元队长\"称号")
	else:
		print("请找弗瑞队长加薪")
elif 500<captain_salary <=1000:
	print("祝贺你至少可以温饱了")
elif captain_salary>1000:
	print("经济危机都难不倒您！")
elif 1000<captain_salary<=2000:
	print("您快比钢铁侠有钱了")
else:
	print("您是不是来自瓦坎达国？")
	
print("程序结束")


input("\n\n\nPress the enter key to exit")
