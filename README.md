### Loading......
- 真·作家助手，用于帮助作家处理一些零碎的小事情。
尝试整理为一个完整的项目，目前只有一些简答的功能文件。

MY/                             # 项目根目录
├── backend/                    # Python后端
│   ├── app/                    # 核心代码
│   │   ├── api/                # 路由控制器
│   │   │   └── v1/             # 接口版本管理
│   │   │       ├── users.py    # 用户相关路由
│   │   │       └── items.py    # 业务相关路由
│   │   ├── models/             # 数据库模型
│   │   ├── schemas/            # Pydantic模型
│   │   ├── utils/              # 工具函数
│   │   ├── config.py           # 配置文件
│   │   └── main.py             # FastAPI入口
│   ├── tests/                  # 后端测试
│   ├── requirements.txt        # 生产依赖
│   └── requirements-dev.txt    # 开发依赖
│
├── frontend/                   # React前端
│   ├── public/                 # 静态资源
│   ├── src/
│   │   ├── api/                # 前端API请求封装
│   │   ├── assets/             # 图片/字体等
│   │   ├── components/         # 通用组件
│   │   ├── hooks/              # 自定义Hook
│   │   ├── pages/              # 页面组件
│   │   ├── stores/             # 状态管理
│   │   ├── styles/             # 全局样式
│   │   ├── utils/              # 工具函数
│   │   ├── App.tsx             # 主组件
│   │   └── main.tsx            # 入口文件
│   ├── tsconfig.json           # TypeScript配置
│   └── package.json            
│
├── mobile/                     # (可选)React Native移动端
│   ├── components/             # 复用前端组件需适配
│   └── ...                     # 类似frontend结构
│
├── scripts/                    # 自动化脚本
│   ├── deploy.sh               # 部署脚本
│   └── sync-translations.py    # 多语言同步脚本
│
├── .gitignore                  # 忽略规则
├── README.md                   # 项目说明
└── docker-compose.yml          # (可选)容器化配置