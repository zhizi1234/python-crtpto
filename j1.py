from PIL import Image
import os

# 创建保存图片的文件夹
os.makedirs("图片", exist_ok=True)

for i in range(1, 1001):
    # 创建一个新的RGB图像对象，大小为100x100像素
    image = Image.new("RGB", (100, 100), (255, 255, 255))
    
    # 设置文件路径和文件名，例如：图片/image_001.jpg, 图片/image_002.jpg, ...
    filename = f"图片/image_{str(i).zfill(3)}.jpg"
    
    # 保存图像为JPEG格式
    image.save(filename, "JPEG")
