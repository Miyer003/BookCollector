### 项目简介
#### 注：本工具仅用于作者自助整理散落各地的作品，所需隐私信息由作者个人提供，仅个人保有，注意不要将隐私信息发布到公开网络

晋江文学城作品备份工具，支持免费和VIP章节的完整备份：
- `jjwxc_col.py`：晋江作者后台作品备份为 Word（docx）。
- `fix.py`：将行首三位数字章节号（001/002/…）转换为"第X章 …"。
- `tests/`：完整的测试套件，包含各功能模块的测试文件。

### 目录结构
```
BookCollector/
├── jjwxc_col.py          # 主程序
├── fix.py                # 章节标题格式化工具
├── my_cookie.txt         # Cookie文件（需要用户提供）
├── requirements.txt      # 依赖包列表
├── backup/              # 备份输出目录
│   └── YYYYMMDD_HHMMSS/ # 按时间戳分类的备份文件夹
│       ├── 作品1.docx   # 备份的DOCX文件
│       ├── 作品2.docx
│       └── 作品列表.json # 作品元数据
└── tests/               # 测试文件目录
    ├── run_all_tests.py      # 测试套件主程序
    ├── test_novel_list.py    # 作品列表测试
    ├── test_chapter_list.py  # 章节列表测试
    ├── test_free_content.py  # 免费章节测试
    ├── test_vip_content.py   # VIP章节测试
    ├── test_author_notes.py  # 作者有话说测试
    └── test_docx_format.py   # DOCX格式测试
```

### 环境与安装
1) 准备 Python 3.9+（建议虚拟环境）

```
cd BookCollector
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### jjwxc_col.py（晋江作品备份）
- **作用**：登录作者后台后，获取作者名下作品的所有章节内容（包括VIP），按作品生成 `.docx`，保存在 `backup/YYYYMMDD_HHMMSS/`。
- **前提**：在 `my_cookie.txt` 中粘贴浏览器获取的完整 Cookie（登录作者后台后，在开发者工具 Network 任一请求的 Request Headers 中复制 `Cookie` 字段）。

**核心功能**：
- **VIP章节解密**：通过作者后台编辑页面获取未加密的VIP章节内容
- **格式完整保留**：保持原文换行符、空行和特殊格式不丢失
- **作者有话说**：自动识别并独立格式化作者备注内容
- **实时保存**：边下载边保存，可随时查看进度和中断恢复

**使用**：
```
python jjwxc_col.py
```
- **交互选择**：
  - 输入数字选择单本（如 `1`）
  - 多本用逗号分隔（如 `1,3,5`）
  - 全部：`all` / `a`
  - 退出：`quit` / `q`
- **输出**：
  - `backup/YYYYMMDD_HHMMSS/*.docx` - 各作品的DOCX文件
  - `backup/YYYYMMDD_HHMMSS/作品列表.json` - 作品元数据
- **特性**：支持免费和VIP章节的完整内容获取

### 测试功能
提供完整的测试套件验证各项功能：

**运行所有测试**：
```
python tests/run_all_tests.py
```

**单独测试**：
```
python tests/test_vip_content.py     # VIP章节内容测试
python tests/test_free_content.py   # 免费章节内容测试
python tests/test_author_notes.py   # 作者有话说测试
python tests/test_novel_list.py     # 作品列表获取测试
python tests/test_chapter_list.py   # 章节列表获取测试
python tests/test_docx_format.py    # DOCX格式输出测试
```

测试功能说明：
- **网络测试**：验证Cookie有效性和内容获取
- **格式测试**：确认换行符和空行保留效果
- **VIP测试**：验证VIP章节解密功能
- **文档测试**：检查DOCX生成和格式化

### fix.py（章节标题格式化）
- **作用**：将文本中“行首三位数字+空格+标题”的章节行，转换为“第X章 标题”。如：`001 序章` → `第一章 序章`。
- **输入**：将待处理内容保存为 `mybook.txt`（与脚本同目录）。

**使用**：
```
python fix.py
```
- **输出**：生成 `fixed.txt`。
- **规则**：仅处理匹配 `^(\s*)(\d{3})(\s+)(.*)$` 的行；数字 1–999 会被转换为中文数字。

### 备注
- 网络与站点结构可能变化，如登录失败或抓取异常，请更新 Cookie 或稍后重试。