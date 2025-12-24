#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from PIL import Image

def resize_images(source_folder, target_folder, target_height=430):
    """
    调整源文件夹中所有图片的高度为指定值，保持宽高比
    
    Args:
        source_folder: 源图片文件夹路径
        target_folder: 目标文件夹路径
        target_height: 目标高度（像素）
    """
    # 确保目标文件夹存在
    os.makedirs(target_folder, exist_ok=True)
    
    # 支持的图片格式
    supported_formats = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff')
    
    # 获取源文件夹中的所有文件
    files = os.listdir(source_folder)
    
    processed_count = 0
    skipped_count = 0
    
    for filename in files:
        # 检查文件扩展名是否为支持的图片格式
        if filename.lower().endswith(supported_formats):
            source_path = os.path.join(source_folder, filename)
            target_path = os.path.join(target_folder, filename)
            
            try:
                # 打开图片
                with Image.open(source_path) as img:
                    # 获取原始尺寸
                    original_width, original_height = img.size
                    
                    # 计算新的宽度，保持宽高比
                    width_ratio = target_height / original_height
                    new_width = int(original_width * width_ratio)
                    
                    # 调整图片大小
                    resized_img = img.resize((new_width, target_height), Image.Resampling.LANCZOS)
                    
                    # 保存调整后的图片
                    resized_img.save(target_path, quality=95)
                    
                    processed_count += 1
                    print(f"已处理: {filename} ({original_width}x{original_height} -> {new_width}x{target_height})")
                    
            except Exception as e:
                print(f"处理 {filename} 时出错: {e}")
                skipped_count += 1
        else:
            skipped_count += 1
            print(f"跳过非图片文件: {filename}")
    
    print(f"\n处理完成!")
    print(f"已处理图片数量: {processed_count}")
    print(f"跳过文件数量: {skipped_count}")

if __name__ == "__main__":
    # 设置源文件夹和目标文件夹
    source_folder = "JennieKim"
    target_folder = "JennieKim_430px"
    
    print("开始处理图片...")
    print(f"源文件夹: {source_folder}")
    print(f"目标文件夹: {target_folder}")
    print(f"目标高度: 430px")
    print("-" * 50)
    
    resize_images(source_folder, target_folder, target_height=430)