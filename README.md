# 股票回测系统

基于Streamlit构建的量化投资回测平台，支持动态/固定持仓策略分析，提供完整的交易数据验证和可视化分析功能。

## ✨ 功能特性

- **多策略支持**：固定持仓与动态持仓策略回测
- **数据校验**：自动验证交易日历、交易时间和数据频率
- **可视化分析**：交互式收益曲线与换手率分析
- **历史管理**：自动存储最近30天回测结果
- **数据库集成**：MongoDB存储回测结果与交易数据

## 🛠️ 环境依赖

- Python 3.8+
- MongoDB 4.4+
- 主要依赖库：
  ```bash
  pip install streamlit pymongo pandas numpy plotly loguru python-dotenv
  ```

## 📥 安装步骤

```bash
# 克隆仓库
git clone https://github.com/Derek-Grey/Stock_Backtest.git
cd Stock_Backtest

# 安装依赖
pip install -r requirements.txt

# 配置环境变量（复制模板文件）
copy config\.env.example config\.env
```

## ⚙️ 配置说明

编辑 `config/.env` 文件：

```ini
MONGO_URI=mongodb://username:password@host:port/
OUTPUT_DIR=./results
```

## 🚀 使用示例

```bash
# 启动前端界面
streamlit run src/frontend/pages/3_history.py

# 运行回测测试
python -m pytest tests/backtest/
```

## 📂 项目结构

```
stock_backtest/
├── config/              # 配置文件
├── src/
│   ├── backend/         # 回测核心逻辑
│   ├── frontend/        # Streamlit界面
│   └── data/            # 数据访问层
├── results/             # 回测结果存储
└── tests/               # 单元测试
```

## 📊 数据管理

- 自动忽略data目录下的.pkl文件（配置在`<mcfile name=".gitignore" path="d:\Derek\stock_backtest\.gitignore"></mcfile>`）
- 使用`<mcsymbol name="DataChecker" filename="portfolio_metrics.py" path="d:\Derek\stock_backtest\src\backtest\portfolio_metrics.py" startline="23" type="class"></mcsymbol>`进行数据验证
- MongoDB集合结构：
  ```python
  # 回测结果集合
  db.backtest_results.portfolio_metrics_minute
  db.backtest_results.portfolio_metrics_daily
  ```

## 🧑💻 贡献指南

1. 创建特性分支 `git checkout -b feature/new-feature`
2. 提交代码前运行测试：
   ```bash
   pytest tests/
   flake8 src/ --max-line-length=120
   ```
3. 发起Pull Request

## 📄 许可协议

MIT License © 2024 Derek Grey

```

**核心功能说明**：
1. 数据库连接配置参考了<mcsymbol name="get_client_U" filename="db_client.py" path="d:\Derek\stock_backtest\src\data\db_client.py" startline="18" type="function"></mcsymbol>实现
2. 结果存储路径由<mcfile name="settings.py" path="d:\Derek\stock_backtest\config\settings.py"></mcfile>配置
3. 前端界面入口为<mcfile name="3_history.py" path="d:\Derek\stock_backtest\src\frontend\pages\3_history.py"></mcfile>
```
