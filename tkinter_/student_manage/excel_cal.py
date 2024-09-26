from openpyxl import load_workbook

# 计算总分并返回学号和姓名、学号和总分的字典
# id2deduct_score：key:学号，value:扣分
def cal_total_score(data):
    id2deduct_score = {}
    start, end = cal_deduct_score_range(data)
    print(start, end)
    for index, row in data.iterrows():
        # 过滤掉不是学号的列
        if not isinstance(row.values[0], int):
            continue
        # 统计每一个学号对应的分数
        deduct_points = row[start:end].sum()
        id2deduct_score[row.values[0]] = deduct_points
    return id2deduct_score

# 按照总分排序，并返回学号和排名的字典
# id2sort：分数排名：key:学号，value:排名位置
def sort_total_score(id2deduct_score):
    id2sort = {}
    # 按照分数降序排列
    sorted_students = sorted(id2deduct_score.items(), key=lambda item: item[1], reverse=False)
    last_score = None
    last_sort = 0
    for i, (student, score) in enumerate(sorted_students):
        if i==0 or score != last_score:
            last_score = score
            last_sort = i+1
        id2sort[student] = last_sort
    return id2sort

# 将总分和排名写回到表格中
def write_total_score(id2deduct_score, id2sort, data, filename, sheet_name):
    # 加载工作簿
    wb = load_workbook(filename)
    ws = wb[sheet_name]

    # 遍历每一行并在指定列写入数据
    for index, row in data.iterrows():
        # 过滤掉不是学号的列
        if not isinstance(row.values[0], int):
            continue
        # 假设我们将结果写入 'B' 列（Excel中的第2列）
        ws.cell(row=index + 2, column=16, value=id2deduct_score[row.values[0]])
        ws.cell(row=index + 2, column=17, value=100-id2deduct_score[row.values[0]])  # +2是因为 DataFrame 索引从 0 开始，Excel 从 1 开始，且第一行通常是表头
        ws.cell(row=index + 2, column=18, value=id2sort[row.values[0]])
    # 保存工作簿
    wb.save(filename)

# 检查文件找出统计扣分的列范围
def cal_deduct_score_range(data):
    start = 0
    end = 0
    title_row = data.iloc[0]
    for col_index, value in enumerate(title_row):
        if value == '姓名':
            start = col_index + 1
        if value == '扣分':
            end = col_index - 1
            break
    return start, end
