import cv2
import numpy as np

def pad_image_to_square(image):
    # 获取图片的高度和宽度
    height, width = image.shape[:2]

    # 计算需要填充的尺寸
    if height > width:
        # 高度大于宽度，左右填充
        pad_width = (height - width) // 2
        padding = ((0, 0), (pad_width, pad_width), (0, 0)) if len(image.shape) == 3 else ((0, 0), (pad_width, pad_width))
    else:
        # 宽度大于高度，上下填充
        pad_height = (width - height) // 2
        padding = ((pad_height, pad_height), (0, 0), (0, 0)) if len(image.shape) == 3 else ((pad_height, pad_height), (0, 0))

    # 使用白色填充图片
    padded_image = np.pad(image, padding, mode='constant', constant_values=255)

    return padded_image

# 读取图片
image_path = 'capture.png'  # 替换为你的图片路径
image = cv2.imread(image_path)

# 检查图片是否成功读取
if image is None:
    print("无法读取图片，请检查图片路径。")
else:
    # 补成正方形
    padded_image = pad_image_to_square(image)

    # 保存处理后的图片
    cv2.imwrite('capture.jpg', padded_image)
    print("处理后的图片已保存为 capture.jpg")