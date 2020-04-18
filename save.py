# 保存学生信息
def save(student):
    try:
        students_txt = open(filename,'a')      # 以追加模式打开
    except Exception as e:
        students_txt = open(filename,'w')      # 如果文件不存在，创建文件并打开文件
    for info in student:
        students_txt.writelines(str(info))     # 按行写入
    students_txt.close()                       # 关闭文件
