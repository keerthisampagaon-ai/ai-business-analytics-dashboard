import streamlit as st

def kpi_card(title, value, icon="📊", color="#4e73df"):

    html = f"""
    <div style="
        background: linear-gradient(135deg,{color},#224abe);
        padding:20px;
        border-radius:12px;
        color:white;
        text-align:center;
        box-shadow:0 4px 12px rgba(0,0,0,0.15);
        margin-bottom:10px;
    ">
        <div style="font-size:28px">{icon}</div>
        <div style="font-size:16px; opacity:0.9">{title}</div>
        <div style="font-size:32px; font-weight:bold">{value}</div>
    </div>
    """

    st.markdown(html, unsafe_allow_html=True)