#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================
                    免费章节内容获取测试
=================================================================
功能：测试免费章节的内容获取功能

使用场景：
- 验证免费章节内容获取是否正常
- 检查内容格式是否正确保留
- 调试免费章节解析逻辑

测试内容：
- 指定免费章节的内容获取
- 显示获取到的内容长度和预览
- 验证换行符和格式保留

注意：免费章节无需特殊权限，但需要有效的基础Cookie
=================================================================
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jjwxc_col import JJWXCBackupTool

def test_free_chapter():
    """测试免费章节内容获取"""
    
    # 初始化工具
    tool = JJWXCBackupTool()
    
    # 测试参数 - 可根据需要修改
    novel_id = "9515272"  # 作品ID
    chapter_id = "1"      # 免费章节ID
    
    print("=" * 60)
    print("免费章节内容获取测试")
    print("=" * 60)
    print(f"作品ID: {novel_id}")
    print(f"章节ID: {chapter_id}")
    
    # 构建免费章节链接
    free_link = f"https://www.jjwxc.net/onebook.php?novelid={novel_id}&chapterid={chapter_id}"
    print(f"免费链接: {free_link}")
    
    # 获取免费章节内容
    print("\n开始获取免费章节内容...")
    content = tool.get_chapter_content(free_link, is_vip=False)
    
    # 显示结果
    print("\n" + "=" * 60)
    print("获取结果：")
    print("=" * 60)
    print(f"内容长度: {len(content)} 字符")
    
    if len(content) > 100:
        print("✓ 免费章节内容获取成功")
        print(f"\n内容预览（前300字符）:")
        print("-" * 40)
        print(content[:300])
        print("-" * 40)
        
        # 检查是否包含作者有话说
        if '【作者有话说】' in content:
            print("✓ 包含作者有话说")
        else:
            print("- 不包含作者有话说")
            
        # 检查换行符保留
        lines = content.split('\n')
        print(f"内容行数: {len(lines)}")
        empty_lines = sum(1 for line in lines if not line.strip())
        print(f"空行数量: {empty_lines}")
        
    else:
        print("✗ 免费章节内容获取失败")
        print(f"错误内容: {content}")

if __name__ == "__main__":
    test_free_chapter()
