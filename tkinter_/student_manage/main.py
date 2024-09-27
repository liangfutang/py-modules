import tkinter as tk
from tkinter import font, filedialog, messagebox
import pandas as pd
from excel_cal import cal_total_score, sort_total_score, write_total_score
import shutil
import os
import sys
import menu

def center_window(root, width, height):
    # 获取屏幕尺寸
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # 计算窗口的开始位置
    x = (screen_width - width) / 2
    y = (screen_height - height) / 2
    # 设置窗口的位置
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    # 创建一个菜单栏
    menu.create_menu(root)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True)
        self.create_homepage()

    def create_homepage(self):
        container = tk.Frame(self)
        container.pack(pady=10)
        # 模板下载
        download_but = tk.Button(container, text="下载模板", command=self.download_file)
        download_but.grid(row=1, column=0, columnspan=2, pady=10)
        # 选择需要计算的表格文件
        choose_but = tk.Button(container, text="选择文件", command=self.import_file)
        choose_but.grid(row=2, column=0, columnspan=2, pady=10)

    def say_hello(self):
        self.label.config(text="Hello, " + self.name_entry.get() + "!")

    def resource_path(self, relative_path):
        """获取打包后文件的路径"""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)
    def download_file(self):
        # 选择目标文件夹
        folder_path = filedialog.askdirectory(title="选择保存文件的文件夹")
        if folder_path:  # 如果用户选择了文件夹
            # 指定要下载的文件路径（项目中的文件）
            source_file = self.resource_path("数学成绩统计模板.xlsx")

            # 构建目标文件的完整路径
            destination_file = os.path.join(folder_path, os.path.basename(source_file))

            try:
                # 将文件复制到目标文件夹
                shutil.copy(source_file, destination_file)
                messagebox.showinfo("下载", f"文件已保存到: {destination_file}")
            except Exception as e:
                messagebox.showerror("错误", f"文件下载失败: {e}")
    def import_file(self):
        filetypes = (
            ('text files', '*.xlsx'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(
            title='选择一个需要统计的表格文件',
            initialdir='/',
            filetypes=filetypes)
        if filename:
            askback = messagebox.askyesno('确认统计', '统计文件: ' + filename)
            if askback:
                xls = pd.ExcelFile(filename)
                sheet_names = xls.sheet_names
                data = pd.read_excel(filename, sheet_name=sheet_names[0])
                id2deduct_score, id2name = cal_total_score(data)
                id2sort = sort_total_score(id2deduct_score)
                try:
                    write_total_score(id2deduct_score, id2name, id2sort, data, filename, sheet_names[0])
                    messagebox.showinfo("success", "成绩统计完成")
                except PermissionError as e:
                    messagebox.showwarning("PermissionError", "文件正在被占用，请关闭文件后再试")
                except Exception as e:
                    messagebox.showerror("Error", "未知错误")
            else:
                print("False")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Student Manager System 1.0")
    center_window(root, 800, 550)
    app = Application(master=root)
    app.mainloop()
