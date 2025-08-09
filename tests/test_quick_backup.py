#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================
                    快速备份测试脚本
=================================================================
功能：测试统一方案的完整备份流程

注意：只备份前几章节以节省时间
=================================================================
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jjwxc_col import JJWXCBackupTool

def test_quick_backup():
    """快速备份测试"""
    
    # 初始化工具
    tool = JJWXCBackupTool()
    
    # 测试一本之前有问题的书
    novel_id = "8419131"
    novel_title = "无限"
    
    print("=" * 60)
    print(f"快速备份测试: {novel_title}")
    print("=" * 60)
    
    # 手动构建作品信息
    novel = {
        'id': novel_id,
        'title': novel_title,
        'link': f"//my.jjwxc.net/backend/managenovel.php?novelid={novel_id}",
        'status': '测试',
        'word_count': '未知',
        'chapter_count': '未知',
        'category': '测试'
    }
    
    # 获取章节列表
    print("1. 获取章节列表...")
    chapters = tool.get_chapters(novel['link'])
    
    if not chapters:
        print("✗ 章节列表获取失败")
        return
    
    print(f"✓ 成功获取 {len(chapters)} 个章节")
    
    # 只备份前3章以节省时间
    test_chapters = chapters[:3]
    print(f"测试备份前 {len(test_chapters)} 章")
    
    # 创建DOCX文档
    print("\n2. 创建DOCX文档...")
    tool.create_docx_with_realtime_save(novel, test_chapters)
    
    print("\n✓ 快速备份测试完成！")

if __name__ == "__main__":
    test_quick_backup()
