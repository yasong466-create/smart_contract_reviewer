import streamlit as st
import sys
import os

# 保持这段代码不动，作为双重保险
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# --- 修改后的导入语句（添加 app. 前缀） ---
from app.components.sidebar import render_sidebar
from app.main_pages.analysis_page import render_analysis_page
from app.main_pages.upload_page import render_upload_page
from app.main_pages.report_page import render_report_page
from app.main_pages.progress_page import render_progress_page
from app.main_pages.budget_monitor import render_budget_monitor
from app.main_pages.price_library_manage import render_price_library

st.set_page_config(
    page_title="智能合同审查系统",
    page_icon="📄",
    layout="wide"
)

def main():
    # 动态获取 CSS 路径，解决不同环境下的路径差异
    css_path = os.path.join(current_dir, "styles", "custom.css")
    
    try:
        with open(css_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass # 如果没有 CSS 也不影响核心功能运行

    # 渲染页面
    page = render_sidebar()
    
    pages = {
        "上传合同": render_upload_page,
        "合同分析": render_analysis_page,
        "分析进度": render_progress_page,
        "审查报告": render_report_page,
        "预算监控": render_budget_monitor,
        "价格库管理": render_price_library
    }
    
    if page in pages:
        pages[page]()

if __name__ == "__main__":
    main()
