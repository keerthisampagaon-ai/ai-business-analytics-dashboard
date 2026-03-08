import streamlit as st
import pandas as pd

from cleaner import clean_data
from charts import *
from insights import generate_insights
from pdf_export import export_dashboard
from kpi_cards import kpi_card

st.set_page_config(layout="wide")

st.title("AI Business Analytics Dashboard")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Sections",
    [
        "Executive Summary",
        "Trends",
        "Product Performance",
        "Geography/Customers",
        "Operations"
    ]
)

# SINGLE DATASET FOR WHOLE DASHBOARD
st.sidebar.subheader("Upload Dataset")

file = st.sidebar.file_uploader("Upload CSV", type="csv")

if file:

    df = clean_data(pd.read_csv(file))

    # KPIs
    revenue = df["revenue"].sum()
    orders = df["order_id"].count()
    aov = revenue / orders
    rating = df["rating"].mean()

    # AI INSIGHTS
    insights = generate_insights(df)

    # -------------------------
    # EXECUTIVE SUMMARY
    # -------------------------

    if page == "Executive Summary":

        st.header("Executive Summary")

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            kpi_card("Revenue", f"${revenue:,.0f}")

        with c2:
            kpi_card("Orders", orders)

        with c3:
            kpi_card("Average Order Value", f"${aov:.2f}")

        with c4:
            kpi_card("Customer Rating", f"{rating:.2f}")

        st.subheader("AI Business Insights")

        for i in insights:
            st.info(i)

    # -------------------------
    # TRENDS
    # -------------------------

    if page == "Trends":

        st.header("Sales Trends")

        fig = sales_trend(df)

        st.plotly_chart(fig, use_container_width=True)

    # -------------------------
    # PRODUCT PERFORMANCE
    # -------------------------

    if page == "Product Performance":

        st.header("Product Performance")

        fig1 = top_products(df)
        fig2 = bottom_products(df)

        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)

    # -------------------------
    # GEOGRAPHY
    # -------------------------

    if page == "Geography/Customers":

        st.header("Regional Sales")

        fig = region_sales(df)

        st.plotly_chart(fig, use_container_width=True)

    # -------------------------
    # OPERATIONS
    # -------------------------

    if page == "Operations":

        st.header("Operations Overview")

        fig1 = payment_methods(df)
        fig2 = order_status(df)

        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)

    # -------------------------
    # SAVE CHARTS FOR PDF
    # -------------------------

    sales_trend(df).write_image("trend_chart.png", scale=3)
    top_products(df).write_image("top_products.png", scale=3)
    bottom_products(df).write_image("bottom_products.png", scale=3)
    region_sales(df).write_image("region_sales.png", scale=3)
    payment_methods(df).write_image("payment_methods.png", scale=3)
    order_status(df).write_image("order_status.png", scale=3)

    # -------------------------
    # FULL DASHBOARD EXPORT
    # -------------------------

    st.sidebar.divider()

    if st.sidebar.button("Export Full Dashboard Report"):

        kpis = {
            "Total Revenue": f"${revenue:,.0f}",
            "Total Orders": orders,
            "Average Order Value": f"${aov:.2f}",
            "Customer Rating": f"{rating:.2f}"
        }

        report = export_dashboard(kpis, insights)

        with open(report, "rb") as f:

            st.sidebar.download_button(
                label="Download PDF Report",
                data=f,
                file_name="Business_Dashboard_Report.pdf",
                mime="application/pdf"
            )