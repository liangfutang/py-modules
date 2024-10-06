import tkinter as tk
import menu
import pandas as pd

def SortShow(frame, data):
    # 清除现有内容
    for widget in frame.winfo_children():
        widget.destroy()
    # 读取数据模型
    id2name, id2sortList = data_model(data)
    # 检索展示折线图

# 统计表格中的数据模式
def data_model(data):
    id2name = {}
    id2sortList = {}
    for index, row in data.iterrows():
        # 过滤掉不是学号的列
        if not isinstance(row.values[0], int):
            continue
        # 统计学号和姓名的关系
        id2name[row.values[0]] = row.values[1]
        # 统计该学生的学号和所有单元的排名
        sort_list = []
        for col_index, column in enumerate(data.columns):
            # 过滤掉 学号和姓名
            if col_index < 2:
                continue
            value = row[column]
            if not isinstance(value, int):
                sort_list.append(None)
            else:
                sort_list.append(value)
        id2sortList[row.values[0]] = sort_list
    return id2name, id2sortList

# 检索展示成绩排名
def search_show(data):
    pass
