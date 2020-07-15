secret = 24  #设定秘密数字
while True:       
    guess = input('你来猜猜我的秘密数字是多少:')   #输入猜测数字
    if int(guess)==secret:  #数字对比
        print('正确！你很棒哦。') 
        break
    elif int(guess)>secret:
        print('你猜的太大了，请重新猜猜~')
    else:
        print('你猜的太小了，请重新猜猜~')






input("Press the enter key to exit.")
