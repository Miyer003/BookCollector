#!/usr/bin/env python3
"""
VIP章节获取测试脚本
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jjwxc_col import JJWXCBackupTool

def test_vip_chapter():
    # 初始化工具
    tool = JJWXCBackupTool()
    
    # 测试VIP章节内容获取
    novel_id = "9515272"  # 摘花
    chapter_id = "17"     # 第17章 (VIP)
    
    print("测试VIP章节内容获取...")
    print(f"作品ID: {novel_id}")
    print(f"章节ID: {chapter_id}")
    
    # 构建VIP章节链接
    vip_link = f"https://my.jjwxc.net/onebook_vip.php?novelid={novel_id}&chapterid={chapter_id}"
    
    # 获取VIP章节内容
    content = tool.get_chapter_content(vip_link, is_vip=True)
    
    print(f"\n获取到的内容长度: {len(content)} 字符")
    print(f"内容预览（前500字符）:")
    print("-" * 50)
    print(content[:500])
    print("-" * 50)
    
    if len(content) > 100:
        print("✓ VIP章节内容获取成功")
    else:
        print("✗ VIP章节内容获取失败")
        print(f"完整内容: {content}")

if __name__ == "__main__":
    test_vip_chapter()
