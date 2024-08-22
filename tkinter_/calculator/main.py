import tkinter as tk

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
root.mainloop()
