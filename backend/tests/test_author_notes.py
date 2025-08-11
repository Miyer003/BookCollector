#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================
                     作者有话说内容测试
=================================================================
功能：测试作者有话说内容的解析和格式保留

使用场景：
- 验证作者有话说是否能正确分离
- 检查作者有话说格式是否保留
- 调试作者有话说的显示效果

测试内容：
- 获取包含作者有话说的章节
- 分离并显示作者有话说部分
- 验证格式保留和换行处理

注意：需要选择包含作者有话说的章节进行测试
=================================================================
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jjwxc_col import JJWXCBackupTool

def test_author_notes():
    """测试作者有话说内容获取"""
    
    # 初始化工具
    tool = JJWXCBackupTool()
    
    # 测试参数 - 选择包含作者有话说的章节
    novel_id = "9515272"  # 作品ID
    chapter_id = "17"     # 包含作者有话说的章节ID
    
    print("=" * 60)
    print("作者有话说内容测试")
    print("=" * 60)
    print(f"作品ID: {novel_id}")
    print(f"章节ID: {chapter_id}")
    
    # 构建章节链接（根据VIP状态选择）
    is_vip = True  # 如果是VIP章节设为True
    if is_vip:
        chapter_link = f"https://my.jjwxc.net/onebook_vip.php?novelid={novel_id}&chapterid={chapter_id}"
    else:
        chapter_link = f"https://www.jjwxc.net/onebook.php?novelid={novel_id}&chapterid={chapter_id}"
    
    print(f"章节链接: {chapter_link}")
    print(f"VIP章节: {'是' if is_vip else '否'}")
    
    # 获取章节内容
    print("\n开始获取章节内容...")
    content = tool.get_chapter_content(chapter_link, is_vip=is_vip)
    
    # 分析内容
    print("\n" + "=" * 60)
    print("内容分析：")
    print("=" * 60)
    print(f"总内容长度: {len(content)} 字符")
    
    if '【作者有话说】' in content:
        print("✓ 找到作者有话说标记")
        
        # 分离正文和作者有话说
        parts = content.split('【作者有话说】', 1)
        main_text = parts[0].strip()
        author_notes = parts[1].strip() if len(parts) > 1 else ""
        
        print(f"正文长度: {len(main_text)} 字符")
        print(f"作者有话说长度: {len(author_notes)} 字符")
        
        if author_notes:
            print("\n" + "-" * 40)
            print("作者有话说内容预览:")
            print("-" * 40)
            # 显示前5行作为预览
            lines = author_notes.split('\n')
            for i, line in enumerate(lines[:5]):
                print(f"第{i+1}行: '{line}'")
            
            if len(lines) > 5:
                print(f"... (还有{len(lines)-5}行)")
            
            print(f"\n作者有话说统计:")
            print(f"- 总行数: {len(lines)}")
            print(f"- 空行数: {sum(1 for line in lines if not line.strip())}")
            print(f"- 非空行数: {sum(1 for line in lines if line.strip())}")
        else:
            print("✗ 作者有话说内容为空")
    else:
        print("✗ 未找到作者有话说标记")
        print("此章节可能不包含作者有话说")

if __name__ == "__main__":
    test_author_notes()
