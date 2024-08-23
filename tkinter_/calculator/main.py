import tkinter as tk

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
        self.pack()
        self.create_homepage()

    def create_homepage(self):
        # 创建标签和文本框
        self.label = tk.Label(root, text="请输入你的名字：")
        self.label.pack()

        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        # 创建按钮
        hello_button = tk.Button(root, text="点击我", command=self.say_hello)
        hello_button.pack()

    def say_hello(self):
        self.label.config(text="Hello, " + self.name_entry.get() + "!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("TDengineGUI")
    center_window(root, 1200, 900)
    app = Application(master=root)
    app.mainloop()
