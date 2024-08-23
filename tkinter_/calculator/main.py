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

def say_hello():
    label.config(text="Hello, " + name_entry.get() + "!")

# 创建主窗口
root = tk.Tk()
root.title("计算器")

# 创建标签和文本框
label = tk.Label(root, text="请输入你的名字：")
label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

# 创建按钮
hello_button = tk.Button(root, text="点击我", command=say_hello)
hello_button.pack()

# 启动Tkinter主事件循环
center_window(root, 400, 300)
root.mainloop()
