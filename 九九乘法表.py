for i in range(1,10):
    for n in range(1,i+1):
        print( '%d X %d = %d' % (n,i,i*n),end = '  ' )#end()使得print函数不换行，用来控制换行行数和结尾字符
    print('  ')
#用print来换行

