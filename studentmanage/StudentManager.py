
class StudentManager(object):
    def __init__(self):
        # 存储学生的列表
        self.student_list = []

    def run(self):
        # 加载学生信息
        self.load_student()

        while True:
            self.show_menu()
            num_menu = int(input('请输入您需要的功能序号:'))

            if num_menu == 1:
                self.add_student()
            elif num_menu == 2:
                self.del_student()

    # 加载学生信息
    def load_student(self):
        pass

    # 展示菜单
    def show_menu(self):
        pass

    # 新增学生信息
    def add_student(self):
        pass

    # 删除学生
    def del_student(self):
        pass
