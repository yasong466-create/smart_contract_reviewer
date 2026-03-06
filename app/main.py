import streamlit as st
import sys
import os

# --- 核心修复：强制注入路径 ---
# 获取当前 main.py 所在的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 重点：将 app 目录加入搜索路径的最前面
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# --- 现在导入绝对不会报错了 ---
from components.sidebar import render_sidebar
from main_pages.analysis_page import render_analysis_page
from main_pages.upload_page import render_upload_page
from main_pages.report_page import render_report_page
from main_pages.progress_page import render_progress_page
from main_pages.budget_monitor import render_budget_monitor
from main_pages.price_library_manage import render_price_library

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
