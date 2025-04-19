# -*- coding: utf-8 -*-
# title: 数据查看
"""
数据查看页面
"""
import streamlit as st
import pandas as pd
from pathlib import Path
import sys
import pymongo

# 添加项目根目录到系统路径
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

from src.data.load_data import LoadData

def data_view_page():
    st.title("📊 数据查看")
    
    # 新增核心功能说明 ================================
    with st.expander("📌 数据说明", expanded=True):
        st.markdown("""
        ### 数据范围说明
        
        **📈 核心数据集**  
        1. **股票数据**：全市场日线行情（复权价格）  
        2. **交易状态**：停复牌、退市等状态标记  
        3. **风险警示**：ST/*ST等特殊处理标识  
        4. **涨跌停**：每日涨跌停价及状态  
        5. **评分矩阵**：基于量价特征的综合评分
        
        ### 使用建议
        - 日期范围建议不超过5年（数据量过大会影响加载速度）
        - 评分矩阵数据每日更新（T+1模式）
        - 风险警示数据可用于过滤标的
        """)
    # ==============================================

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
            font-size: 16px;
        }
        .stDateInput>div {
            border-radius: 8px;
        }
        .main-title {
            font-size: 2rem;  /* Unified font size */
        }
        </style>
        """, unsafe_allow_html=True
    )
    
    # 在原有组件添加说明提示
    st.markdown("### 选择数据类型")
    data_type = st.selectbox(
        "",
        ["股票数据", "交易状态", "风险警示", "涨跌停", "评分矩阵"],
        help="选择要查看的数据类型，不同数据集更新频率不同"
    )
    
    # 在日期选择器添加帮助提示
    # 使用列布局 (必须保留此部分)
    col1, col2 = st.columns(2)
    
    with col1:
        date_s = st.date_input(
            "选择开始日期", 
            value=pd.to_datetime("2010-01-01"),
            help="建议起始日期不早于2010年（早期数据不完整）"
        )
    
    with col2:
        date_e = st.date_input(
            "选择结束日期", 
            value=pd.to_datetime("2024-12-31"),
            help="默认显示最新可用数据"
        )
    
    # 在查询结果后添加技术说明
    if st.button("🔍 确认查询"):
        try:
            with st.spinner('加载数据中，请稍候...'):
                # 创建数据加载器实例
                data_loader = LoadData(
                    date_s=str(date_s),
                    date_e=str(date_e),
                    data_folder=str(ROOT_DIR / "data")
                )
                
                if data_type == "股票数据":
                    df_stocks, _, _, _ = data_loader.get_stocks_info()
                    st.dataframe(df_stocks)
                    
                elif data_type == "交易状态":
                    _, trade_status, _, _ = data_loader.get_stocks_info()
                    st.dataframe(trade_status)
                    
                elif data_type == "风险警示":
                    _, _, risk_warning, _ = data_loader.get_stocks_info()
                    st.dataframe(risk_warning)
                    
                elif data_type == "涨跌停":
                    _, _, _, limit = data_loader.get_stocks_info()
                    st.dataframe(limit)
                    
                elif data_type == "评分矩阵":
                    score_matrix = data_loader.generate_score_matrix('stra_V3_11.csv')
                    st.dataframe(score_matrix)
                
                # 新增数据源说明
                with st.expander("🔧 数据源说明"):
                    st.markdown("""
                    **数据更新机制**  
                    - 基础数据：每日18:00更新（交易所清算后）  
                    - 评分矩阵：每日22:00更新（模型计算批次结果）  
                    
                    **数据精度**  
                    - 价格数据：保留4位小数  
                    - 评分数据：标准化至[0,1]区间  
                    """)
        except Exception as e:
            st.error(f"加载数据时出错: {str(e)}")

if __name__ == "__main__":
    data_view_page()