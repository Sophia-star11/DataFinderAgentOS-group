# DataFinderAgentOS

某政务智能瞭望与智能问数系统 —— 基于 Web B/S 架构的数据智能采集与智能问数平台。

---

## 系统简介

DataFinderAgentOS 是一个面向政务场景的智能数据平台，融合了**数据采集（瞭望）、数据管理（仓库）、AI 对话（问数）、数字员工**四大核心能力。用户可以通过类 ChatGPT 的对话界面，与数据直接对话，实现智能问数、统计分析、报表生成等操作。

### 核心亮点

- **智能问数**：通过自然语言与数据对话，支持意图识别、数据库查询、统计分析
- **瞭望采集**：配置采集源规则，按关键词批量爬取网络数据（如百度新闻）
- **深度采集**：集成 crawl4ai 网页爬虫，通过数字员工-采集专员自动爬取并分析网页内容
- **数字员工**：支持 LLM 型（大模型+提示词+技能）和 API 型（HTTP 接口）两种形态
- **模型引擎**：对接 OpenAI 兼容 API，支持 SSE 流式对话、模型分类、参数调节
- **RBAC 权限**：用户-角色-功能三级权限体系，精细化控制菜单和功能访问

---

## 技术栈

| 层级 | 技术 |
|------|------|
| 后端框架 | Tornado 6.x（Python） |
| 数据库 | SQLite（本地单文件） |
| 前端框架 | Layui 2.9.x（主） + Bootstrap 5.3.8（辅） |
| AI 通信 | SSE（Server-Sent Events）代理到 OpenAI 兼容 API |
| 网页爬虫 | crawl4ai 0.9.1 + Playwright Chromium |
| 认证机制 | secure_cookie + PBKDF2-HMAC-SHA256 + XSRF |

---

## 快速开始

### 环境要求

| 项目 | 要求 |
|------|------|
| Python | 3.10+（推荐 3.13） |
| 操作系统 | Windows / Linux / macOS |
| 浏览器 | Chrome / Edge / Firefox 最新版 |

### 安装与启动

```bash
# 1. 克隆仓库
git clone https://github.com/Sophia-star11/DataFinderAgentOS-group.git
cd DataFinderAgentOS-group

# 2. 创建虚拟环境
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 启动服务
python run.py
```

启动成功后：
```
Server Started:http://localhost:10010/
```

### 访问系统

| 入口 | 地址 | 说明 |
|------|------|------|
| 管理侧后台 | http://localhost:10010/admin/ | 管理员登录 |
| 用户侧前台 | http://localhost:10010/ | 用户登录/注册 |

### 默认账号

| 用户名 | 密码 | 角色 |
|--------|------|------|
| admin | 123456 | 超级管理员（系统预置） |
| （自行注册） | （自行设置） | 普通用户 |

---

## 功能模块

### 管理侧（后台）

| 模块 | 说明 |
|------|------|
| 控制台 | 首页仪表盘，8 项统计指标实时刷新 |
| 用户管理 | 用户 CRUD、分页搜索、超管保护 |
| 角色管理 | 角色 CRUD、功能分配树、编辑弹窗 |
| 功能管理 | 功能 CRUD、父子层级、启用/禁用 |
| 菜单管理 | 菜单 CRUD、排序、预览、图标展示 |
| 瞭源管理 | 采集源 CRUD、URL 模板、请求头配置 |
| 瞭望采集 | 采集执行、橱窗展示、批量保存到仓库 |
| 数据仓库 | 数据列表、深度采集、批量操作 |
| 模型引擎 | 模型 CRUD、SSE 对话测试、分类筛选 |
| 数字员工 | 员工 CRUD、LLM/API 双型、测试功能 |

### 用户侧（前台）

| 模块 | 说明 |
|------|------|
| 登录/注册 | 双栏品牌布局、表单验证、XSRF 防护 |
| 智能对话 | 五区 ChatGPT 布局、SSE 流式输出、Markdown 渲染 |
| @技能命令 | @天气 / @新闻 / @音乐 / @电影 / @yummy |
| /快捷功能 | 生成报表 / 图表 / 数据分析 / 导出报告 |

---

## 项目结构

```
DataFinderAgentOS-group/
├── run.py                          # 项目入口（路由注册 + 初始化）
├── app/
│   ├── controllers/                # 控制层（16 个模块）
│   ├── models/                     # 模型层（13 个模块）
│   ├── static/                     # 静态资源（CSS/JS/第三方库）
│   │   ├── css/                    # 样式文件
│   │   ├── js/                     # 脚本文件
│   │   └── dist/                   # 本地化第三方组件（Layui/Bootstrap）
│   └── templates/                  # 模板目录
│       ├── *.html                  # 用户侧页面（5 个）
│       └── admin/*.html            # 后台管理侧页面（13 个）
├── config/                         # 配置目录（预留）
├── database/                       # 数据库目录
│   └── finderos.db                 # SQLite 数据库（自动创建）
├── data/                           # 数据存储目录
├── docs/                           # 开发文档
├── skills/                         # 技能目录（预留）
├── test/                           # 测试代码
└── requirements.txt                # Python 依赖
```

---

## 数据库

- **类型**：SQLite 单文件数据库
- **路径**：`database/finderos.db`
- **初始化**：首次启动 `run.py` 时自动创建表结构并填充初始数据
- **核心表**：users、roles、functions、menus、role_functions、watch_sources、watch_collected_data、data_warehouse、deep_collect_tasks、deep_collect_data、ai_models、digital_employees、conversations

---

## 配置说明

当前版本配置直接在 `run.py` 中，后续将迁移到 `config/` 目录。

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| 服务端口 | `10010` | `run.py` 第 651 行 |
| Cookie 密钥 | `datafinderagentos-token` | 会话加密密钥 |
| XSRF 防护 | `True` | 跨站请求伪造防护 |
| AI 模型 | （后台配置） | 模型引擎页面配置 API Base URL 和 API Key |

---

## 常见问题

**Q: 启动后菜单不完整？**
删除 `database/finderos.db`，重新启动 `run.py` 即可自动重建。

**Q: 对话报错 403？**
检查前端请求是否携带 XSRF token。

**Q: 深度采集不可用？**
安装 crawl4ai 和 Playwright：
```bash
pip install crawl4ai>=0.9.1
playwright install chromium
```

**Q: 模型对话无响应？**
登录后台 → 模型引擎 → 配置有效的 API Base URL 和 API Key。

**Q: 组员拉取后菜单缺失？**
`run.py` 已包含通用菜单保障循环，直接启动即可自动补全。

---

## 仓库信息

| 项目 | 内容 |
|------|------|
| 团队仓库 | https://github.com/Sophia-star11/DataFinderAgentOS-group |
| 个人仓库 | https://github.com/Sophia-star11/DataFinderAgentOSv1 |
| 默认分支 | main |
| 文档目录 | docs/（requirement.md / constraint.md / template.md / role.md / test_case.md / deployment.md） |

---

*v0.3 | 2026-07-15*
