import tkinter as tk
from tkinter import ttk, Toplevel, filedialog, messagebox, Label, StringVar, Checkbutton, Button
from pandas import ExcelFile, read_excel
from excel_cal import cal_total_score, sort_total_score, write_total_score
import shutil
import os
import menu
from sort_show import SortShow
from openpyxl import load_workbook

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
        choose_but = tk.Button(container, text="成绩计算", command=self.import_file)
        choose_but.grid(row=2, column=0, columnspan=2, pady=10)
        # 成绩曲线展示
        choose_but = tk.Button(container, text="排名曲线", command=self.sort_show)
        choose_but.grid(row=3, column=0, columnspan=2, pady=10)

    def download_file(self):
        options_cal = ["数学成绩统计模板501.xlsx", "数学成绩统计模板502.xlsx"]
        options_sort = ["数学成绩排名模板501.xlsx", "数学成绩排名模板502.xlsx"]
        options = [options_cal, options_sort]
        # 回调函数处理用户的选择
        def handle_selection(selected):
            if selected:
                messagebox.showinfo("选择结果", f"您选择了: {', '.join(selected)}")
            else:
                messagebox.showinfo("选择结果", "您没有选择任何选项")
        dialog = MultiSelectDialog(self.master, "模板下载列表", options, handle_selection)
        self.master.wait_window(dialog)
        if not dialog.selected_options:
            return
        # 选择目标文件夹
        folder_path = filedialog.askdirectory(title="选择保存文件的文件夹")
        if folder_path:  # 如果用户选择了文件夹
            # 指定要下载的文件路径（项目中的文件）
            source_dir = os.path.join(os.path.abspath("."), "templates")

            try:
                # 将文件复制到目标文件夹
                for item in dialog.selected_options:
                    source_file = os.path.join(source_dir, item)
                    destination_file = os.path.join(folder_path, item)
                    shutil.copy(source_file, destination_file)
                messagebox.showinfo("下载", f"文件已保存到: {folder_path}")
            except Exception as e:
                messagebox.showerror("错误", f"文件下载失败: {e}")
    def import_file(self):
        filetypes = (
            ('text files', '*.xlsx'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(
            title='选择一个需要计算成绩的表格文件',
            initialdir='/',
            filetypes=filetypes)
        if filename:
            askback = messagebox.askyesno('确认统计', '统计文件: ' + filename)
            if askback:
                xls = ExcelFile(filename)
                sheet_names = xls.sheet_names
                data = read_excel(filename, sheet_name=sheet_names[0])
                # 加载 Excel 文件
                wb = load_workbook(filename)
                ws = wb[sheet_names[0]]
                id2deduct_score, id2name, row_start, row_end, col_start, col_end = cal_total_score(data, ws)
                id2sort = sort_total_score(id2deduct_score)
                try:
                    write_total_score(id2deduct_score, id2name, id2sort, data, filename, wb, ws, row_start, row_end, col_start, col_end)
                    messagebox.showinfo("success", "成绩统计完成")
                except PermissionError as e:
                    messagebox.showwarning("PermissionError", "文件正在被占用，请关闭文件后再试")
                except Exception as e:
                    messagebox.showerror("Error", "未知错误")
            else:
                print("False")

    def sort_show(self):
        filetypes = (
            ('text files', '*.xlsx'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(
            title='选择一个需要展示排名曲线的表格文件',
            initialdir='/',
            filetypes=filetypes)
        if filename:
            askback = messagebox.askyesno('确认展示', '展示文件: ' + filename)
            if askback:
                xls = ExcelFile(filename)
                sheet_names = xls.sheet_names
                data = read_excel(filename, sheet_name=sheet_names[0], header=None)
                try:
                    SortShow(data)
                except PermissionError as e:
                    messagebox.showwarning("PermissionError", "文件正在被占用，请关闭文件后再试")
                except Exception as e:
                    messagebox.showerror("Error", "未知错误")
def center_dialog(master, width, height):
    # 获取屏幕尺寸
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    # 计算窗口的开始位置
    x = (screen_width - width) / 2
    y = (screen_height - height) / 2
    return f"{width}x{height}+{int(x)}+{int(y)}"

class MultiSelectDialog(Toplevel):
    def __init__(self, parent, title, options, callback):
        super().__init__(parent)
        self.title(title)
        dialog_show = center_dialog(parent, 300, 235)
        self.geometry(dialog_show)
        self.callback = callback
        self.check_vars = []
        self.selected_options = []
        # 创建并放置标签
        label = Label(self, text="请选择一个或多个模板：", anchor='w')
        label.pack(fill=tk.X, padx=10, pady=10)
        # 创建并放置复选按钮
        separator_flag = 1
        for option_one_type in options:
            for option in option_one_type:
                var = StringVar()
                cb = Checkbutton(self, text=option, variable=var, onvalue=option, offvalue="")
                cb.deselect()  # 默认不选中
                cb.pack(anchor=tk.W)
                self.check_vars.append(var)
            if separator_flag == 1:
                ttk.Separator(self).pack(fill=tk.X, padx=10, pady=5)
                separator_flag += 1
        # 创建并放置确认和取消按钮
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        ok_button = Button(btn_frame, text="确认", command=self.on_ok)
        ok_button.pack(side=tk.LEFT, padx=5)

        cancel_button = Button(btn_frame, text="取消", command=self.destroy)
        cancel_button.pack(side=tk.RIGHT, padx=5)

    def on_ok(self):
        # 收集所有被选中的选项
        self.selected_options = [var.get() for var in self.check_vars if var.get()]
        if self.selected_options:
            messagebox.showinfo("选择结果", f"您选择了: {', '.join(self.selected_options)}")
        else:
            messagebox.showinfo("选择结果", "您没有选择任何选项")
        self.destroy()  # 关闭对话框

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Student Manager System 1.0")
    center_window(root, 800, 550)
    app = Application(master=root)
    app.mainloop()
