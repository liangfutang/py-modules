import tkinter as tk
from tkinter import messagebox

def create_menu(root):
    # 创建一个菜单栏
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    # 创建菜单项---文件
    file_menu = tk.Menu(menu_bar, tearoff=False)
    file_menu.add_command(label="待解锁", command=on_hello)
    file_menu.add_separator()
    file_menu.add_command(label="Quit", command=root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)
    # 创建菜单项---help
    help_menu = tk.Menu(menu_bar, tearoff=False)
    help_menu.add_command(label="待解锁", command=on_hello)
    help_menu.add_separator()
    help_menu.add_command(label="About", command=about)
    menu_bar.add_cascade(label="Help", menu=help_menu)

def on_hello():
    pass

def about():
    messagebox.showinfo("About Software", "This is a system to manage students info.")
