import streamlit as st

def kpi_card(title,value):

    html = f"""
    <div class="card">
        <h3>{title}</h3>
        <h1>{value}</h1>
    </div>
    """

    st.markdown(html, unsafe_allow_html=True)