#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================
                     章节列表获取测试
=================================================================
功能：测试指定作品的章节列表获取功能

使用场景：
- 验证章节列表解析是否正确
- 检查VIP/免费章节识别
- 调试章节排序和编号

测试内容：
- 指定作品的章节列表获取
- 显示章节基本信息
- 统计VIP和免费章节数量
- 验证章节链接格式

注意：需要有效的作者后台Cookie
=================================================================
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jjwxc_col import JJWXCBackupTool
import json

def test_chapter_list():
    """测试章节列表获取"""
    
    # 初始化工具
    tool = JJWXCBackupTool()
    
    # 测试参数 - 可根据需要修改
    novel_id = "9515272"  # 作品ID
    novel_title = "摘花"   # 作品标题（用于显示）
    
    print("=" * 60)
    print("章节列表获取测试")
    print("=" * 60)
    print(f"作品ID: {novel_id}")
    print(f"作品标题: {novel_title}")
    
    # 构建作品管理链接
    novel_link = f"//my.jjwxc.net/backend/managenovel.php?novelid={novel_id}"
    print(f"管理链接: {novel_link}")
    
    # 获取章节列表
    print("\n开始获取章节列表...")
    chapters = tool.get_chapters(novel_link)
    
    if not chapters:
        print("✗ 章节列表获取失败")
        return
    
    print(f"✓ 成功获取 {len(chapters)} 个章节")
    
    # 显示章节列表
    print("\n" + "=" * 60)
    print("章节列表详情：")
    print("=" * 60)
    
    for idx, chapter in enumerate(chapters[:10]):  # 只显示前10章避免输出过长
        vip_mark = "[VIP]" if chapter.get('is_vip') else "[免费]"
        print(f"{idx+1:2d}. {vip_mark} 第{chapter.get('chapter_number', '?')}章 {chapter.get('title', '未知标题')}")
        print(f"     章节ID: {chapter.get('id', '未知')}")
        print(f"     链接: {chapter.get('link', '未知')}")
    
    if len(chapters) > 10:
        print(f"     ... (还有{len(chapters)-10}个章节)")
    
    # 统计信息
    print("\n" + "=" * 60)
    print("统计信息：")
    print("=" * 60)
    
    vip_chapters = [c for c in chapters if c.get('is_vip')]
    free_chapters = [c for c in chapters if not c.get('is_vip')]
    
    print(f"总章节数: {len(chapters)}")
    print(f"免费章节: {len(free_chapters)}章")
    print(f"VIP章节: {len(vip_chapters)}章")
    print(f"VIP比例: {len(vip_chapters)/len(chapters)*100:.1f}%")
    
    # 验证章节编号连续性
    chapter_numbers = [c.get('chapter_number', 0) for c in chapters]
    chapter_numbers.sort()
    
    print(f"章节编号范围: {min(chapter_numbers)} - {max(chapter_numbers)}")
    
    # 检查是否有缺失的章节编号
    expected_numbers = set(range(min(chapter_numbers), max(chapter_numbers) + 1))
    actual_numbers = set(chapter_numbers)
    missing_numbers = expected_numbers - actual_numbers
    
    if missing_numbers:
        print(f"缺失章节编号: {sorted(missing_numbers)}")
    else:
        print("章节编号连续，无缺失")
    
    # 验证链接格式
    vip_links = sum(1 for c in chapters if 'onebook_vip.php' in c.get('link', ''))
    free_links = sum(1 for c in chapters if 'onebook.php' in c.get('link', ''))
    
    print(f"VIP链接格式正确: {vip_links}/{len(vip_chapters)}")
    print(f"免费链接格式正确: {free_links}/{len(free_chapters)}")
    
    # 保存章节列表到测试目录
    test_output_path = os.path.join("tests", f"chapter_list_{novel_id}.json")
    with open(test_output_path, "w", encoding="utf-8") as f:
        json.dump(chapters, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ 章节列表已保存到: {test_output_path}")

if __name__ == "__main__":
    test_chapter_list()
