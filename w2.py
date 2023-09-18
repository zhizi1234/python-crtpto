import os
import shutil
from datetime import datetime, timedelta
from random import randint
import time

# 生成日期和时间数据的函数
def generate_dates_array():
    # 创建一个空的数组
    date_array = []

    # 设置日期格式
    date_format = '%Y-%m-%d'
    time_format = '%H-%M-%S'

    # 设置初始日期和时间
    start_date = datetime(2022, 5, 1)

    # 设置结束日期和时间
    end_date = datetime(2023, 5, 31)

    # 写入日期和时间数据
    current_date = start_date.date()
    while current_date <= end_date.date():
        # 在早上8点到晚上8点之间随机生成三个时分秒数据
        for i in range(3):
            random_hour = randint(8, 20)
            random_minute = randint(0, 59)
            random_second = randint(0, 59)

            # 将日期和时间合并为完整的datetime对象
            combined_datetime = datetime.combine(current_date, datetime.min.time()) + \
                                timedelta(hours=random_hour, minutes=random_minute, seconds=random_second)

            # 将日期和时间格式化为字符串
            formatted_date = current_date.strftime(date_format)
            formatted_time = combined_datetime.strftime(time_format)
            all_datetime = datetime.strptime(formatted_date + " " + formatted_time, '%Y-%m-%d %H-%M-%S')
            unix_time = time.mktime(all_datetime.timetuple())

            # 将日期和时间数据添加到数组中
            date_array.append([formatted_date, formatted_time, unix_time])

        # 增加一天，进行下一个日期的处理
        current_date += timedelta(days=1)

    return date_array

# 重命名图片文件的函数
def rename_images(date_array):
    # 获取当前文件夹路径
    current_folder = os.getcwd()

    # 图片文件所在的文件夹路径
    image_folder = current_folder + "\\old"
    new_image_folder = current_folder + "\\new"

    # 遍历图片文件夹中的所有图片文件
    for row_index, filename in enumerate(os.listdir(image_folder)):
        data_a1 = date_array[row_index][0]
        data_b2 = date_array[row_index][1]
        data_b3 = date_array[row_index][2]

        # 构建完整的旧文件路径和新文件路径
        old_path = os.path.join(image_folder, filename)
        new_name = str(data_a1) + " " + str(data_b2) + " " + filename
        new_path = os.path.join(new_image_folder, new_name)

        # 重命名文件
        shutil.copyfile(old_path, new_path)
        print(f'图片文件 {old_path} 已重命名为 {new_path}')

        # 修改文件时间
        os.utime(new_path, (data_b3, data_b3))

    print('ok')

# 生成日期和时间数据的数组
date_array = generate_dates_array()

# 重命名图片文件
rename_images(date_array)
