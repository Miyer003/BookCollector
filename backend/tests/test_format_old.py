#!/usr/bin/env python3
"""
VIP章节格式测试脚本
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jjwxc_col import JJWXCBackupTool

def test_vip_format():
    # 初始化工具
    tool = JJWXCBackupTool()
    
    # 测试VIP章节内容格式
    novel_id = "9515272"  # 摘花
    chapter_id = "17"     # 第17章 (VIP)
    
    print("测试VIP章节格式保留...")
    print(f"作品ID: {novel_id}")
    print(f"章节ID: {chapter_id}")
    
    # 构建VIP章节链接
    vip_link = f"https://my.jjwxc.net/onebook_vip.php?novelid={novel_id}&chapterid={chapter_id}"
    
    # 获取VIP章节内容
    content = tool.get_chapter_content(vip_link, is_vip=True)
    
    print(f"\n获取到的内容长度: {len(content)} 字符")
    print("\n原始格式内容（显示换行符）:")
    print("-" * 60)
    
    # 显示原始内容的前20行，包括换行符
    lines = content.split('\n')
    for i, line in enumerate(lines[:20]):
        print(f"第{i+1:2d}行: '{line}'")
    
    print("-" * 60)
    print(f"总共 {len(lines)} 行")
    
    # 检查空行数量
    empty_lines = sum(1 for line in lines if not line.strip())
    print(f"空行数量: {empty_lines}")
    
    # 检查是否包含作者有话说
    if '【作者有话说】' in content:
        print("✓ 包含作者有话说")
        # 找到作者有话说的位置
        author_note_start = content.find('【作者有话说】')
        author_note_content = content[author_note_start:]
        author_lines = author_note_content.split('\n')
        print(f"作者有话说部分有 {len(author_lines)} 行")
    else:
        print("✗ 不包含作者有话说")

if __name__ == "__main__":
    test_vip_format()
