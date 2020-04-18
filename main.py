import re
import menu
def main():
    ctrl = True
    while(ctrl):
        menu()
        option = input('请选择')
        option_str = re.sub('\D','',option)
        if option_str in ['0','1','2','3','4','5','6','7']:
            option_int = int(option_str)
        if option_int == 0:       # 退出
            exit()
        elif option_int == 1:     # 录入学生信息
            insert()
        elif option_int == 2:     # 查询学生成绩
            search()
        elif option_int == 3:     # 删除学生成绩
            delete()
        elif option_int == 4:     # 修改学生成绩
            alter()
        elif option_int == 5:     # 对学生成绩进行排序
            sort()
        elif option_int == 6:     # 统计学生人数
            total()
        elif option_int == 7:     # 显示所有学生信息
            show()
if __naame__ == '__main__':
    main()


