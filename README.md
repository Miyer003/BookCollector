### 项目简介
#### 注：本工具仅用于作者自助整理散落各地的作品，所需隐私信息由作者个人提供，仅个人保有，注意不要将隐私信息发布到公开网络
收集与整理文本的两个脚本：
- `jjwxc_col.py`：晋江作者后台作品备份为 Word（docx）。
- `fix.py`：将行首三位数字章节号（001/002/…）转换为“第X章 …”。

### 环境与安装
1) 准备 Python 3.9+（建议虚拟环境）

```
cd BookCollector
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### jjwxc_col.py（晋江作品备份）
- **作用**：登录作者后台后，获取作者名下作品公开章节内容，按作品生成 `.docx`，保存在 `backup_YYYYMMDD_HHMMSS/`。
- **前提**：在 `my_cookie.txt` 中粘贴浏览器获取的完整 Cookie（登录作者后台后，在开发者工具 Network 任一请求的 Request Headers 中复制 `Cookie` 字段）。

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
  - `backup_YYYYMMDD_HHMMSS/*.docx`
  - `backup_YYYYMMDD_HHMMSS/作品列表.json`
  - 调试文件（如登录验证页面快照）同目录保存
- **限制**：当前仅抓取公开免费章节。

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