#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================
                     章节列表解析调试工具
=================================================================
功能：调试章节列表解析问题，保存页面HTML并分析结构

使用场景：
- 当章节列表获取失败时使用
- 分析页面结构变化
- 调试章节解析逻辑

使用方法：
python tests/debug_chapter_parsing.py

注意：会保存页面HTML到tests目录，便于分析
=================================================================
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from jjwxc_col import JJWXCBackupTool
from bs4 import BeautifulSoup
import re

def debug_chapter_parsing():
    """调试章节列表解析"""
    
    # 初始化工具
    tool = JJWXCBackupTool()
    
    # 测试参数 - 已知有章节的作品
    test_novels = [
        ("9095344", "引路人[单元]"),
        ("8839902", "匪"),
        ("8580593", "生生"),
        ("8419131", "无限"),
        ("9515272", "摘花")  # 已知有章节的作品作为对照
    ]
    
    print("=" * 60)
    print("章节列表解析调试工具")
    print("=" * 60)
    
    for novel_id, novel_title in test_novels:
        print(f"\n调试作品: {novel_title} (ID: {novel_id})")
        print("-" * 40)
        
        # 构建后台URL
        backend_url = f"https://my.jjwxc.net/backend/managenovel.php?novelid={novel_id}"
        print(f"访问URL: {backend_url}")
        
        try:
            # 获取页面内容
            response = tool.session.get(backend_url, headers=tool.headers, timeout=30)
            response.encoding = 'gb18030'
            
            # 保存原始HTML
            html_file = os.path.join("tests", f"debug_novel_{novel_id}_{novel_title}.html")
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"✓ 页面已保存: {html_file}")
            
            # 解析页面
            soup = BeautifulSoup(response.content, 'html.parser', from_encoding='gb18030')
            
            # 分析页面结构
            print("\n页面结构分析:")
            
            # 查找所有表格
            tables = soup.find_all('table')
            print(f"找到 {len(tables)} 个表格")
            
            # 查找所有tr行
            all_trs = soup.find_all('tr')
            print(f"找到 {len(all_trs)} 个tr行")
            
            # 查找特定颜色的tr行
            green_trs = soup.find_all('tr', {'bgcolor': '#eefaee'})
            print(f"找到 {len(green_trs)} 个绿色tr行 (bgcolor=#eefaee)")
            
            # 查找包含chapterid的input
            chapter_inputs = soup.find_all('input', {'name': 'chapterid'})
            print(f"找到 {len(chapter_inputs)} 个章节ID输入框")
            
            # 查找所有链接
            all_links = soup.find_all('a', href=True)
            chapter_links = [a for a in all_links if 'onebook' in a.get('href', '')]
            print(f"找到 {len(chapter_links)} 个章节相关链接")
            
            # 如果找到章节ID输入框，分析其父元素结构
            if chapter_inputs:
                print(f"\n第一个章节ID输入框分析:")
                first_input = chapter_inputs[0]
                parent_tr = first_input.find_parent('tr')
                if parent_tr:
                    print(f"父tr的属性: {parent_tr.attrs}")
                    tds = parent_tr.find_all('td')
                    print(f"包含 {len(tds)} 个td")
                    for i, td in enumerate(tds):
                        print(f"  td[{i}]: {td.get_text(strip=True)[:50]}...")
            
            # 尝试不同的章节行查找方法
            print(f"\n尝试其他查找方法:")
            
            # 方法1：查找包含input[name=chapterid]的tr
            chapter_rows_method1 = []
            for input_elem in chapter_inputs:
                tr = input_elem.find_parent('tr')
                if tr and tr not in chapter_rows_method1:
                    chapter_rows_method1.append(tr)
            print(f"方法1 - 通过input查找: {len(chapter_rows_method1)} 行")
            
            # 方法2：查找其他可能的tr属性
            other_color_trs = soup.find_all('tr', {'bgcolor': True})
            colors = set()
            for tr in other_color_trs:
                colors.add(tr.get('bgcolor'))
            print(f"方法2 - 所有背景色: {colors}")
            
            # 方法3：查找包含onebook链接的tr
            chapter_rows_method3 = []
            for link in chapter_links:
                tr = link.find_parent('tr')
                if tr and tr not in chapter_rows_method3:
                    chapter_rows_method3.append(tr)
            print(f"方法3 - 通过链接查找: {len(chapter_rows_method3)} 行")
            
            print()
            
        except Exception as e:
            print(f"✗ 调试失败: {e}")
    
    print("\n" + "=" * 60)
    print("调试完成")
    print("请检查tests/目录下的HTML文件来分析页面结构")
    print("=" * 60)

if __name__ == "__main__":
    debug_chapter_parsing()
