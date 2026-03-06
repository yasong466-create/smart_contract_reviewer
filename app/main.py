import streamlit as st
import sys
import os

# --- 1. 路径兼容处理 ---
# 获取当前 main.py 所在的绝对路径 (即 app/ 目录)
current_dir = os.path.dirname(os.path.abspath(__file__))

# 确保 Python 能找到当前目录下的 components 和 main_pages
if current_dir not in sys.path:
    sys.path.append(current_dir)

# --- 2. 导入自定义模块 ---
# 注意：因为上面处理了 sys.path，这里直接从文件夹名开始导入即可
from components.sidebar import render_sidebar
from main_pages.analysis_page import render_analysis_page
from main_pages.upload_page import render_upload_page
from main_pages.report_page import render_report_page
from main_pages.progress_page import render_progress_page
from main_pages.budget_monitor import render_budget_monitor
from main_pages.price_library_manage import render_price_library

# --- 3. 页面配置 ---
st.set_page_config(
    page_title="智能合同审查系统",
    page_icon="📄",
    layout="wide"
)

def main():
    # --- 4. 加载自定义CSS ---
    # 使用 os.path.join 自动处理不同系统的路径分隔符
    css_path = os.path.join(current_dir, "styles", "custom.css")
    
    try:
        with open(css_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        # 如果找不到 CSS，打印警告但允许程序继续运行
        st.warning(f"未找到 CSS 样式文件: {css_path}")

    # --- 5. 渲染侧边栏 ---
    page = render_sidebar()
    
    # --- 6. 路由逻辑 ---
    if page == "上传合同":
        render_upload_page()
    elif page == "合同分析":
        render_analysis_page()
    elif page == "分析进度":
        render_progress_page()
    elif page == "审查报告":
        render_report_page()
    elif page == "预算监控":
        render_budget_monitor()
    elif page == "价格库管理":
        render_price_library()

if __name__ == "__main__":
    main()
