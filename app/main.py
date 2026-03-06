import streamlit as st
import sys
import os

# --- 究极路径修复 ---
# 1. 获取当前文件 (main.py) 的绝对路径
current_file_path = os.path.abspath(__file__)
# 2. 获取 app 文件夹路径
app_dir = os.path.dirname(current_file_path)
# 3. 获取项目根目录 (smart_contract_reviewer)
root_dir = os.path.dirname(app_dir)

# 将根目录和 app 目录都以最高优先级加入
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)

# --- 导入逻辑 ---
# 既然已经把根目录加入了 sys.path，尝试使用带 app. 的全名导入
try:
    from app.components.sidebar import render_sidebar
    from app.main_pages.analysis_page import render_analysis_page
    from app.main_pages.upload_page import render_upload_page
    from app.main_pages.report_page import render_report_page
    from app.main_pages.progress_page import render_progress_page
    from app.main_pages.budget_monitor import render_budget_monitor
    from app.main_pages.price_library_manage import render_price_library
except ModuleNotFoundError:
    # 如果带 app. 失败，尝试不带 app. 的导入
    from components.sidebar import render_sidebar
    from main_pages.analysis_page import render_analysis_page
    from main_pages.upload_page import render_upload_page
    from main_pages.report_page import render_report_page
    from main_pages.progress_page import render_progress_page
    from main_pages.budget_monitor import render_budget_monitor
    from main_pages.price_library_manage import render_price_library

# 后面的 st.set_page_config 和 main() 函数保持不变...

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
