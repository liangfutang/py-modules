import tkinter as tk
from tkinter import font, filedialog, messagebox
import pandas as pd
from excel_cal import cal_total_score, sort_total_score, write_total_score

def center_window(root, width, height):
    # 获取屏幕尺寸
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # 计算窗口的开始位置
    x = (screen_width - width) / 2
    y = (screen_height - height) / 2
    # 设置窗口的位置
    root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True)
        self.create_homepage()

    def create_homepage(self):
        container = tk.Frame(self)
        container.pack(pady=10)
        # 选择需要计算的表格文件
        choose_but = tk.Button(container, text="选择文件", command=self.import_file)
        choose_but.grid(row=1, column=0, columnspan=2, pady=10)

    def say_hello(self):
        self.label.config(text="Hello, " + self.name_entry.get() + "!")

    def import_file(self):
        filetypes = (
            ('text files', '*.xlsx'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(
            title='选择一个需要清洗的表格文件',
            initialdir='/',
            filetypes=filetypes)
        if filename:
            askback = messagebox.askyesno('确认清洗', '清洗文件: ' + filename)
            if askback:
                xls = pd.ExcelFile(filename)
                sheet_names = xls.sheet_names
                data = pd.read_excel(filename, sheet_name=sheet_names[0])
                id2score = cal_total_score(data)
                id2sort = sort_total_score(id2score)
                write_total_score(id2score, id2sort, data, filename, sheet_names[0])
            else:
                print("False")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("数据清洗GUI系统 1.0")
    center_window(root, 800, 550)
    app = Application(master=root)
    app.mainloop()
