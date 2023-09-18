import os
from openpyxl import load_workbook

# 加载Excel文件
workbook = load_workbook('./1.xlsx')
sheet = workbook.active

# 读取A1单元格的数据
new_name1 = sheet['A1'].value
new_name2 = sheet['B1'].value

# 定义旧文件名和新文件名
old_name = '1.jpg'
file_path = './'  # 图片文件的目录路径

# 构建完整的旧文件路径和新文件路径
old_path = os.path.join(file_path, old_name)
new_path = os.path.join(file_path, new_name1+new_name2 + '.jpg')

# 检查旧文件是否存在
if not os.path.exists(old_path):
    print('图片文件不存在。')
    exit()

# 重命名文件
os.rename(old_path, new_path)

print('图片文件名已更改为：', new_name1+new_name2)
