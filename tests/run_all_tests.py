#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================
                        测试套件主程序
=================================================================
功能：运行所有测试文件，提供统一的测试入口

使用方法：
python tests/run_all_tests.py

或者单独运行某个测试：
python tests/test_vip_content.py
python tests/test_free_content.py
python tests/test_author_notes.py
python tests/test_novel_list.py  
python tests/test_chapter_list.py
python tests/test_docx_format.py

测试说明：
1. test_novel_list - 测试作品列表获取
2. test_chapter_list - 测试章节列表获取  
3. test_free_content - 测试免费章节内容
4. test_vip_content - 测试VIP章节内容
5. test_author_notes - 测试作者有话说
6. test_docx_format - 测试DOCX文档生成

注意：需要有效的Cookie才能运行网络相关测试
=================================================================
"""
import os
import sys
import importlib.util

def run_test(test_name):
    """运行单个测试"""
    try:
        test_path = os.path.join(os.path.dirname(__file__), f"{test_name}.py")
        if not os.path.exists(test_path):
            print(f"✗ 测试文件不存在: {test_path}")
            return False
            
        # 动态导入测试模块
        spec = importlib.util.spec_from_file_location(test_name, test_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # 运行测试主函数
        if hasattr(module, 'main'):
            module.main()
        else:
            # 寻找以test_开头的函数
            test_functions = [name for name in dir(module) if name.startswith('test_')]
            if test_functions:
                for func_name in test_functions:
                    func = getattr(module, func_name)
                    if callable(func):
                        func()
            else:
                print(f"✗ 测试文件 {test_name} 中未找到测试函数")
                return False
        
        print(f"✓ 测试 {test_name} 完成\n")
        return True
        
    except Exception as e:
        print(f"✗ 测试 {test_name} 失败: {e}\n")
        return False

def main():
    """运行所有测试"""
    print("=" * 60)
    print("晋江文学城备份工具 - 测试套件")
    print("=" * 60)
    
    # 定义所有测试（按执行顺序）
    tests = [
        ("test_docx_format", "DOCX文档格式测试"),
        ("test_novel_list", "作品列表获取测试"),
        ("test_chapter_list", "章节列表获取测试"),
        ("test_free_content", "免费章节内容测试"),
        ("test_vip_content", "VIP章节内容测试"),
        ("test_author_notes", "作者有话说测试"),
    ]
    
    print(f"将运行 {len(tests)} 个测试:")
    for i, (test_name, description) in enumerate(tests, 1):
        print(f"{i}. {description}")
    
    print("\n" + "=" * 60)
    
    # 检查Cookie文件
    cookie_file = "my_cookie.txt"
    if not os.path.exists(cookie_file):
        print(f"⚠ 警告: 未找到 {cookie_file} 文件")
        print("网络相关测试可能会失败")
        print("如需完整测试，请先准备有效的Cookie文件\n")
    else:
        print(f"✓ 找到Cookie文件: {cookie_file}\n")
    
    # 运行测试
    passed = 0
    failed = 0
    
    for test_name, description in tests:
        print(f"运行测试: {description}")
        print("-" * 40)
        
        if run_test(test_name):
            passed += 1
        else:
            failed += 1
    
    # 显示结果总结
    print("=" * 60)
    print("测试结果总结")
    print("=" * 60)
    print(f"总测试数: {len(tests)}")
    print(f"通过: {passed}")
    print(f"失败: {failed}")
    
    if failed == 0:
        print("\n🎉 所有测试通过!")
    else:
        print(f"\n⚠ {failed} 个测试失败，请检查相关功能")

if __name__ == "__main__":
    main()
