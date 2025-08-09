#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================
                     作品列表获取测试
=================================================================
功能：测试作品列表的获取和解析功能

使用场景：
- 验证登录状态是否正常
- 检查作品列表获取是否成功
- 调试作品信息解析逻辑

测试内容：
- 检查Cookie登录状态
- 获取作者的所有作品列表
- 显示作品基本信息
- 验证作品链接格式

注意：需要有效的作者后台Cookie
=================================================================
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jjwxc_col import JJWXCBackupTool
import json

def test_novel_list():
    """测试作品列表获取"""
    
    # 初始化工具
    tool = JJWXCBackupTool()
    
    print("=" * 60)
    print("作品列表获取测试")
    print("=" * 60)
    
    # 检查登录状态
    print("1. 检查登录状态...")
    login_success = tool.check_login()
    
    if not login_success:
        print("✗ 登录失败，请检查Cookie是否有效")
        return
    
    print("✓ 登录成功")
    
    # 获取作品列表
    print("\n2. 获取作品列表...")
    novels = tool.get_novel_list()
    
    if not novels:
        print("✗ 作品列表获取失败")
        return
    
    print(f"✓ 成功获取 {len(novels)} 部作品")
    
    # 显示作品列表
    print("\n" + "=" * 60)
    print("作品列表详情：")
    print("=" * 60)
    
    for idx, novel in enumerate(novels):
        print(f"\n{idx+1:2d}. {novel.get('title', '未知标题')}")
        print(f"     ID: {novel.get('id', '未知')}")
        print(f"     分类: {novel.get('category', '未知')}")
        print(f"     状态: {novel.get('status', '未知')}")
        print(f"     字数: {novel.get('word_count', '未知')}")
        print(f"     章节数: {novel.get('chapter_count', '未知')}")
        print(f"     管理链接: {novel.get('link', '未知')}")
        print(f"     阅读链接: {novel.get('view_link', '未知')}")
    
    # 保存作品列表到测试目录
    test_output_path = os.path.join("tests", "novel_list_test.json")
    with open(test_output_path, "w", encoding="utf-8") as f:
        json.dump(novels, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ 作品列表已保存到: {test_output_path}")
    
    # 统计信息
    print("\n" + "=" * 60)
    print("统计信息：")
    print("=" * 60)
    print(f"总作品数: {len(novels)}")
    
    # 按状态统计
    status_count = {}
    for novel in novels:
        status = novel.get('status', '未知')
        status_count[status] = status_count.get(status, 0) + 1
    
    print("状态分布:")
    for status, count in status_count.items():
        print(f"  - {status}: {count}部")
    
    # 验证链接格式
    valid_links = 0
    for novel in novels:
        link = novel.get('link', '')
        if 'managenovel.php?novelid=' in link:
            valid_links += 1
    
    print(f"有效管理链接: {valid_links}/{len(novels)}")

if __name__ == "__main__":
    test_novel_list()
