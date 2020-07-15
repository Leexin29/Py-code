students = ['小明','小红','小刚']
for i in range(3):
    student1 = students.pop(0)  # 运用pop()函数，同时完成提取和删除。
    students.append(student1)  # 将移除的student1安排到最后一个座位。
    print(students)
	
	
	
input("\n\nPress the enter key to exit.")
    
