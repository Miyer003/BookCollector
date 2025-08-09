#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================
                    统一章节获取方案测试
=================================================================
功能：测试新的统一后台章节获取方案

使用场景：
- 验证新的章节列表解析逻辑
- 测试统一的章节内容获取
- 对比免费和VIP章节处理效果

注意：测试之前有问题的作品
=================================================================
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jjwxc_col import JJWXCBackupTool

def test_unified_chapter_system():
    """测试统一章节获取方案"""
    
    # 初始化工具
    tool = JJWXCBackupTool()
    
    # 测试之前有问题的作品
    test_novels = [
        ("9095344", "引路人[单元]"),
        ("8839902", "匪"),
        ("8580593", "生生"),
        ("8419131", "无限"),
    ]
    
    print("=" * 60)
    print("统一章节获取方案测试")
    print("=" * 60)
    
    for novel_id, novel_title in test_novels:
        print(f"\n测试作品: {novel_title} (ID: {novel_id})")
        print("-" * 40)
        
        # 构建管理链接
        novel_link = f"//my.jjwxc.net/backend/managenovel.php?novelid={novel_id}"
        
        # 获取章节列表
        print("1. 获取章节列表...")
        chapters = tool.get_chapters(novel_link)
        
        if not chapters:
            print("✗ 章节列表获取失败")
            continue
        
        print(f"✓ 成功获取 {len(chapters)} 个章节")
        
        # 显示前几个章节信息
        print("\n章节列表预览:")
        for i, chapter in enumerate(chapters[:3]):  # 只显示前3个
            vip_mark = "[VIP]" if chapter.get('is_vip') else "[免费]"
            print(f"  {i+1}. {vip_mark} 第{chapter.get('chapter_number', '?')}章 {chapter.get('title', '未知标题')}")
        
        if len(chapters) > 3:
            print(f"  ... (还有{len(chapters)-3}个章节)")
        
        # 测试第一个章节的内容获取
        if chapters:
            print(f"\n2. 测试第一章节内容获取...")
            first_chapter = chapters[0]
            content = tool.get_chapter_content(first_chapter['link'])
            
            if content and not content.startswith("内容获取失败"):
                print(f"✓ 章节内容获取成功")
                print(f"内容长度: {len(content)} 字符")
                print(f"内容预览: {content[:100]}...")
                
                # 检查是否包含作者有话说
                if '【作者有话说】' in content:
                    print("✓ 包含作者有话说")
                else:
                    print("- 不包含作者有话说")
            else:
                print(f"✗ 章节内容获取失败: {content}")

if __name__ == "__main__":
    test_unified_chapter_system()
