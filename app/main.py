import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(__file__))

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
    # 加载自定义CSS
    with open("app/styles/custom.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    # 渲染侧边栏
    page = render_sidebar()
    
    # 根据选择的页面渲染内容
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
