#Craps Roller
#演示随机数的生成

import random
	#用于加载random模块

    #生成1到6之间的随机数
die1 = random.randint(1,6)
    #randint()函数用于产生随机数，需要两个整数参数值，然后回返回这两个值之间的一个随机整数（其范围包括给定的参数值）。
die2 = random.randrange(6) + 1

'''#randrange()函数也可以产生随机整数，用这种方式进行调用的话，函数会返回一个0（包括）到参数值（之间的随机整数）。
    所以，调用random.randrange(6)将会得到0、1、2、3、4、5之间的一个值。
    randrange()确实是在六个数字中随机条一个数字只不过这些数字都是从0开始的。'''
	

total = die1 + die2

print("You roalled a",die1,"and a",die2,"for a total of",total)

input("\n\nPress the enter key to exit")
