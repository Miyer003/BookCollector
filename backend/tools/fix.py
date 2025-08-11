#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
章节标题格式化工具
功能：将三位阿拉伯数字章节标题转换为中文章节标题
例如：001 -> 第一章
"""

import re
import os

def number_to_chinese(num):
    """
    将阿拉伯数字转换为中文数字
    支持1-999的转换
    """
    chinese_nums = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    chinese_units = ['', '十', '百']
    
    if num == 0:
        return '零'
    
    result = ''
    num_str = str(num)
    length = len(num_str)
    
    for i, digit in enumerate(num_str):
        digit = int(digit)
        pos = length - i - 1  # 当前位数（个位为0，十位为1，百位为2）
        
        if digit != 0:
            # 特殊处理：10-19的情况，不说"一十"而说"十"
            if pos == 1 and digit == 1 and length == 2:
                result += chinese_units[pos]
            else:
                result += chinese_nums[digit] + chinese_units[pos]
        elif pos == 1 and length == 3 and result and int(num_str[i+1]) != 0:
            # 百位数中间有0的情况，如101，需要加"零"
            result += '零'
    
    return result

def fix_chapter_titles(input_file, output_file):
    """
    修复章节标题格式
    将三位数字章节标题转换为中文格式
    """
    try:
        # 读取原文件
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 使用正则表达式匹配三位数字开头的章节标题
        # 匹配模式：行首的三位数字，后面可能有空格和章节名
        pattern = r'^(\s*)(\d{3})(\s+)(.*)$'
        
        lines = content.split('\n')
        fixed_lines = []
        
        for line in lines:
            # 检查是否为三位数字开头的章节标题
            match = re.match(pattern, line)
            if match:
                prefix_space = match.group(1)  # 前面的空格
                number = int(match.group(2))   # 三位数字
                middle_space = match.group(3)  # 数字后的空格
                chapter_name = match.group(4)  # 章节名称
                
                # 转换为中文章节标题
                chinese_number = number_to_chinese(number)
                new_line = f"{prefix_space}第{chinese_number}章{middle_space}{chapter_name}"
                fixed_lines.append(new_line)
                print(f"转换: {match.group(2)} {chapter_name} -> 第{chinese_number}章 {chapter_name}")
            else:
                # 不是章节标题，保持原样
                fixed_lines.append(line)
        
        # 写入新文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(fixed_lines))
        
        print(f"\n✓ 处理完成！")
        print(f"输入文件: {input_file}")
        print(f"输出文件: {output_file}")
        
    except FileNotFoundError:
        print(f"❌ 错误：找不到文件 '{input_file}'")
        print("请确保 'mybook.txt' 文件存在于当前目录中")
    except Exception as e:
        print(f"❌ 处理过程中出现错误: {str(e)}")

def main():
    """主函数"""
    print("=" * 50)
    print("    章节标题格式化工具")
    print("    三位数字 -> 第X章")
    print("=" * 50)
    
    input_file = "mybook.txt"
    output_file = "fixed.txt"
    
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"❌ 错误：找不到文件 '{input_file}'")
        print("请将 'mybook.txt' 文件放置在脚本同目录下")
        return
    
    # 开始处理
    print(f"开始处理文件: {input_file}")
    print("正在转换章节标题...")
    print("-" * 30)
    
    fix_chapter_titles(input_file, output_file)

if __name__ == "__main__":
    main()
