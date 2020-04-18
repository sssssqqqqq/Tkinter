# 删除学生信息
import os
def delete():
    mark = True
    while(mark):
        studentId = input('请输入要删除学生的ID')
        if studentId is not '':
            if os.path.exists(filename):
                with open(filename,'r') as rfile:
                    studentId_old = rfile.readline()
            else:
                studentId_old = []
            ifdel = False
            if studentId_old:
                with open(filename,'w') as wfile:
                    d = {}
                    for list in studentId_old:
                        d = dict(eval(list))
                        if d['id'] != studentId:
                            wfile.write(str(d)+'\n')
                        else:
                            ifdel = True
                    if ifdel:
                        print('ID为%s 的学生信息已被删除...'% studentId)
                    else:
                        print('ID为%s 的学生信息未找到...' % studentId)
            else:
                print('无学生信息')
                break
            show()
            inputMark = input('是否继续删除？(y/n):')
            if inputMark == y:
                mark = True
            else:
                mark = False





