c2		#扫描端口脚本

j1		#创建1000jpg格式的图片

e1		#在excel表生成指定日期	并在右边那一行生成随机日期

a1		#读取excel表第一横行，将读取到的数据去重命名图片名字

w1		#读取excel和图片文件夹路径，用excel每一行分别去重命名图片名字	需要自定义路径

b64		#加解密base64编码

b32		#加解密base32编码

b58		#加解密base58编码

m5		#加密md5

p1		#指定图片爬取到本地

w2		#w1是最后保存到Excel表里，w2是保存到数组里		w2既生成数据，又能读取数据

php版本

```php
<?php

// 生成日期和时间数据的函数
function generate_dates_array() {
    // 创建一个空的数组
    $date_array = [];

    // 设置日期格式
    $date_format = 'Y-m-d';
    $time_format = 'H-i-s';

    // 设置初始日期和时间
    $start_date = new DateTime('2022-05-01');

    // 设置结束日期和时间
    $end_date = new DateTime('2023-05-31');

    // 写入日期和时间数据
    $current_date = clone $start_date;
    while ($current_date <= $end_date) {
        // 在早上8点到晚上8点之间随机生成三个时分秒数据
        for ($i = 0; $i < 3; $i++) {
            $random_hour = rand(8, 20);
            $random_minute = rand(0, 59);
            $random_second = rand(0, 59);

            // 将日期和时间合并为完整的DateTime对象
            $combined_datetime = clone $current_date;
            $combined_datetime->setTime($random_hour, $random_minute, $random_second);

            // 将日期和时间格式化为字符串
            $formatted_date = $current_date->format($date_format);
            $formatted_time = $combined_datetime->format($time_format);
            $all_datetime = DateTime::createFromFormat($date_format . ' ' . $time_format, $formatted_date . ' ' . $formatted_time);
            $unix_time = $all_datetime->getTimestamp();

            // 将日期和时间数据添加到数组中
            $date_array[] = [$formatted_date, $formatted_time, $unix_time];
        }

        // 增加一天，进行下一个日期的处理
        $current_date->add(new DateInterval('P1D'));
    }

    return $date_array;
}

// 重命名图片文件的函数
function rename_images($date_array) {
    // 获取当前文件夹路径
    $current_folder = getcwd();

    // 图片文件所在的文件夹路径
    $image_folder = $current_folder . "/old";
    $new_image_folder = $current_folder . "/new";

    // 遍历图片文件夹中的所有图片文件
    $files = scandir($image_folder);
    foreach ($files as $filename) {
        if ($filename == "." || $filename == "..") {
            continue;
        }

        $row_index = count($date_array);
        $data_a1 = $date_array[$row_index][0];
        $data_b2 = $date_array[$row_index][1];
        $data_b3 = $date_array[$row_index][2];

        // 构建完整的旧文件路径和新文件路径
        $old_path = $image_folder . "/" . $filename;
        $new_name = $data_a1 . " " . $data_b2 . " " . $filename;
        $new_path = $new_image_folder . "/" . $new_name;

        // 重命名文件
        copy($old_path, $new_path);
        echo "图片文件 " . $old_path . " 已重命名为 " . $new_path . "\n";

        // 修改文件时间
        touch($new_path, $data_b3);
    }

    echo "ok\n";
}

// 生成日期和时间数据的数组
$date_array = generate_dates_array();

// 重命名图片文件
rename_images($date_array);

```

pyinstxtractor	#反编译exe

g1			#更改后缀名
