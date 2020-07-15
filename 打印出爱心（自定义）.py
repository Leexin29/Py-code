i= input("请输入你想打出的字符：")


print('\n'.join([''.join([(i[(x-y) % len(i)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))


input("Press the enter key to exit.")