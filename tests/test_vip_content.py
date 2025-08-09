#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================
                    VIP章节内容获取测试
=================================================================
功能：测试VIP章节的内容获取功能

使用场景：
- 验证VIP章节是否能正确获取内容
- 检查VIP解密功能是否正常
- 调试后台编辑页面访问

测试内容：
- 指定VIP章节的内容获取
- 显示获取到的内容长度和预览
- 验证内容是否有效

注意：需要有效的Cookie和VIP章节权限
=================================================================
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jjwxc_col import JJWXCBackupTool

def test_vip_chapter():
    """测试VIP章节内容获取"""
    
    # 初始化工具
    tool = JJWXCBackupTool()
    
    # 测试参数 - 可根据需要修改
    novel_id = "9515272"  # 作品ID
    chapter_id = "17"     # VIP章节ID
    
    print("=" * 60)
    print("VIP章节内容获取测试")
    print("=" * 60)
    print(f"作品ID: {novel_id}")
    print(f"章节ID: {chapter_id}")
    
    # 构建VIP章节链接
    vip_link = f"https://my.jjwxc.net/onebook_vip.php?novelid={novel_id}&chapterid={chapter_id}"
    print(f"VIP链接: {vip_link}")
    
    # 获取VIP章节内容
    print("\n开始获取VIP章节内容...")
    content = tool.get_chapter_content(vip_link, is_vip=True)
    
    # 显示结果
    print("\n" + "=" * 60)
    print("获取结果：")
    print("=" * 60)
    print(f"内容长度: {len(content)} 字符")
    
    if len(content) > 100:
        print("✓ VIP章节内容获取成功")
        print(f"\n内容预览（前300字符）:")
        print("-" * 40)
        print(content[:300])
        print("-" * 40)
        
        # 检查是否包含作者有话说
        if '【作者有话说】' in content:
            print("✓ 包含作者有话说")
        else:
            print("- 不包含作者有话说")
            
    else:
        print("✗ VIP章节内容获取失败")
        print(f"错误内容: {content}")

if __name__ == "__main__":
    test_vip_chapter()
