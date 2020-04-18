# 录入学生信息
import save
def insert():
    Studentlist = []
    mark = True
    while mark:
        id = input('请输入学号： ')
        if not id:
            break
        name = input('请输入学生姓名： ')
        if not name:
            break
        english = int(input('请输入英语成绩： '))
        math = int(input('请输入数学成绩： '))
        c = int(input('请输入c语言成绩： '))
        student = {'id':id,'name':name,'english':english,'math':math,'c':c}
        Studentlist.append(student)
        if inputMrak == 'y':
            mark = True
        else:
            mark = False
        save(Studentlist)
        print('学生信息录入完毕')


