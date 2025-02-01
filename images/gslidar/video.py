import cv2
import numpy as np

def pad_frame_to_square(frame):
    # 获取帧的高度和宽度
    height, width = frame.shape[:2]

    # 计算需要填充的尺寸
    if height > width:
        # 高度大于宽度，左右填充
        pad_width = (height - width) // 2
        padding = ((0, 0), (pad_width, pad_width), (0, 0)) if len(frame.shape) == 3 else ((0, 0), (pad_width, pad_width))
    else:
        # 宽度大于高度，上下填充
        pad_height = (width - height) // 2
        padding = ((pad_height, pad_height), (0, 0), (0, 0)) if len(frame.shape) == 3 else ((pad_height, pad_height), (0, 0))

    # 使用白色填充帧
    padded_frame = np.pad(frame, padding, mode='constant', constant_values=255)

    return padded_frame

# 输入视频文件路径
input_video_path = 'waymo.mp4'
# 输出视频文件路径
output_video_path = 'teaser.mp4'

# 打开输入视频文件
cap = cv2.VideoCapture(input_video_path)

# 检查视频是否成功打开
if not cap.isOpened():
    print("无法打开输入视频文件，请检查文件路径。")
    exit()

# 获取视频的帧率、宽度和高度
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 计算最大边长，作为输出视频的边长
max_side = max(width, height)

# 定义视频编码器（使用 H.264 编码）
fourcc = cv2.VideoWriter_fourcc(*'avc1')
# 创建视频写入对象
out = cv2.VideoWriter(output_video_path, fourcc, fps, (max_side, max_side))

while True:
    # 读取一帧视频
    ret, frame = cap.read()

    # 如果读取失败，退出循环
    if not ret:
        break

    # 将帧补成正方形
    padded_frame = pad_frame_to_square(frame)

    # 写入处理后的帧到输出视频文件
    out.write(padded_frame)

# 释放视频捕获对象和视频写入对象
cap.release()
out.release()

print("视频处理完成，处理后的视频已保存为", output_video_path)