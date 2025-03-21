"""
股票量化回测系统主页
"""
import streamlit as st
from pathlib import Path
import sys
import pymongo

# 设置页面配置
st.set_page_config(
    page_title="股票量化回测系统",
    page_icon="📈",
    layout="wide"
)

# 添加项目根目录到系统路径
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

# 添加自定义 CSS
st.markdown(
    """
    <style>
    .reportview-container {
        background: #F0FFF0; /* 浅绿色背景 */
    }
    .sidebar .sidebar-content {
        background: #FFFFFF; /* 白色背景 */
    }
    .stButton>button {
        color: #FFFFFF;
        background-color: #32CD32; /* 亮绿色按钮 */
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        transition: background-color 0.3s ease; /* 添加过渡效果 */
    }
    .stButton>button:hover {
        background-color: #3CB371; /* 鼠标悬停时的颜色 */
    }
    .stTitle {
        color: #333333; /* 深灰色标题 */
        font-weight: bold;
    }
    .stMarkdown h3 {
        color: #2E8B57; /* 深绿色小标题 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    # 修改侧边栏页面名称
    st.sidebar.markdown(
        """
        <style>
        [data-testid="stSidebarNav"] li div a {
            margin-left: 1rem;
            padding: 1rem;
            width: 100%;
            font-weight: normal;
        }
        [data-testid="stSidebarNav"] div button p {
            font-weight: normal;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # 更新系统名称和添加功能说明
    st.title("📈 股票量化回测系统")
    
    st.markdown("""
    ### 👋 欢迎使用股票量化回测系统
    """)
    
    # 系统说明 ================================
    with st.expander("📌 系统说明", expanded=True):
        st.markdown("""
        **🎯 系统特性**  
        • 多策略并行：支持股票/ETF/可转债多品种回测  
        • 智能风控：动态止盈止损/黑名单过滤机制  
        • 组合优化：MPT模型权重优化 + 风险平价模型
        
        **🔄 数据服务**  
        - 覆盖A股全市场5000+标的（1990-至今）  
        - 包含除权除息/分红送转完整数据  
        - 提供分钟级/日线级多粒度数据支持  
        """)
    
    # 功能模块说明 =================================
    with st.expander("📦 功能模块说明", expanded=True): 
        st.markdown("""
        * 📊 **策略回测**  
        - 固定持仓策略：按评分选取固定数量股票  
        - 动态调仓策略：按评分动态调整持仓比例
        
        * 📈 **数据查看**  
        - 行情数据：日线复权价格/成交量  
        - 状态数据：停复牌/ST/*ST标识  
        - 评分矩阵：多因子综合评分结果
        
        * 📝 **回测记录**  
        - 结果存档：自动保存最近回测记录  
        - 数据导出：支持CSV格式原始数据下载  
        - 对比分析：多策略绩效对比功能
        
        * ⚖️ **权重调整**  
        - 限制单日权重变化幅度（默认±5%）  
        - 自动归一化处理保证权重和为1  
        - 可视化权重变化轨迹
        
        * 🚀 **快速回测**  
        - 支持自定义滑点/手续费参数  
        - 实时计算年化收益率/波动率指标  
        - 可视化收益分布特征
        
        """)
        
    st.markdown("""
    请从左侧边栏选择功能开始使用。
    """)
    # 显示系统信息
    st.sidebar.markdown("### 系统信息")
    st.sidebar.info(
        f"""
        - 覆盖标的数: 5278 只
        - 系统版本: v1.1.0
        """
    )

if __name__ == "__main__":
    main()