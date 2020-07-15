# 需要的变量放到开头，明显一些。
number = 0
list_number = []

while True:
    number += 1
    a = input('A，你认罪吗？请回答认罪或者不认罪\n')
    b = input('B，你认罪吗？请回答认罪或者不认罪\n')
    list_number.append([a,b])
    # 需要将每一对实验者的选择存起来。
    # 用列表嵌套的方式来存放实验者的选择，也可用元组或字典

    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')        
    elif a == '不认罪' and b == '认罪':
        print('A判20年，B判1年，唉')
    elif a == '认罪' and b == '不认罪':
        print('A判1年，B判20年')
    else:
        print('都判3年，太棒了')
        break

        
print("\n\n这个实验中第",number,"对实验者做出了正确的选择。")
# 打印是第几对实验者做出了最优选择。
for i in range(number):
    print("\n\n实验中，第",i+1,"对实验者的选择是：",str(list_number[i]))
# 通过循环打印每一对实验者的选择。


