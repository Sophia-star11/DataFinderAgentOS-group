# DataFinderAgentOS-group — 智能瞭望与问数系统

## Task 1: 数智大屏 3D 地球（替换桑基图）
- 移除中央桑基图「数据流水线」，替换为 ECharts GL 3D 地球「数据源星球」
- 数据源节点通过斐波那契球面算法均匀分布在球体表面，节点大小 = 数据量
- 弧线从各节点流向球心，表示数据流入平台
- 悬停/点击显示数据来源名称 + 数据量
- 地球支持拖拽旋转、缩放、自动旋转
- 加载 `echarts-gl.min.js`（项目已有，原未使用）

## Task 2: 数智大屏深色主题
- 整体页面背景改为深色（`#0a1628`）
- 面板改为深色渐变（`#0f1f3a → #0a1628`），边框使用科技蓝半透明（`rgba(56,189,248,0.12)`）
- 面板标题 + 所有图表文字颜色调整为浅色（`#94a3b8` / `#cbd5e1` / `#e2e8f0`）
- 地球标签使用白色 + 文字阴影（`textShadowColor: rgba(0,0,0,0.8)`）确保可读

## Task 3: 饼图替换为数据状态分布
- 左栏饼图从「数据来源分布」改为「数据状态分布」
- 显示两个状态：普通采集（`is_deep_collected=0`）、深度采集（`is_deep_collected=1`）
- 新增 API `/api/data-screen/status`，从 `data_warehouse` 统计
- 颜色映射：普通采集=`#3b82f6`(蓝)、深度采集=`#22c55e`(绿)
- 去掉原「未采集」项（与普通采集重叠，意义不明确）

## Task 4: SSRF 防护
- 在 `app/controllers/base.py` 新增 `check_ssrf(url)` 公共函数
  - 只允许 `http/https` 协议
  - DNS 解析后检查目标 IP 是否为内网/保留地址（127、10、172.16-31、192.168、169.254、0.x、组播）
  - 抛出 `ValueError`，上层捕获后返回友好提示
- 在 6 个文件 8 个入口点加入 SSRF 校验：
  - **配置时**：`admin_model.py` 创建/更新模型时校验 `api_base_url`
  - **运行时**：`user_chat.py` 调 LLM 前 + 调 API 数字员工前
  - **运行时**：`admin_digital_employee.py` 测试 LLM/API 员工前
  - **运行时**：`admin_warehouse.py` 深度采集 LLM/API 调用前
  - **运行时**：`skill_executor.py` 技能 API 调用前

## Task 5: 修复 auth.py role_code 查询错误
- `AdminLoginHandler.post()` 中 `user.get("role_code")` 报错 — `sqlite3.Row` 在 Python 3.8 无 `.get()` 方法
- 修复为 `dict(user).get("role_code")`

## Task 6: 舆情大屏功能增强
- **批量操作**：表格添加复选框 → 选中后出现「批量删除」按钮，支持一次性删除多条预警
- **重新审核**：新增「重新审核」按钮，对全部预警重新执行 AI 分析（`force: true`）
- **查看对话**：点击「查看对话」弹窗展示完整对话内容（从 `/api/admin/conversations/messages` 获取）
- **无害级别**：严重度选项增加「无害」(harmless)，对应低危标签展示
- **误报标记优化**：误报确认文案改为「确认将该预警标记为误报？」
- **批量审核反馈优化**：显示审核进度（如 已完成 3/10 条审核）
