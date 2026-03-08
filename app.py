import streamlit as st
import pandas as pd
import plotly.io as pio

from cleaner import clean_data
from charts import *
from insights import recommendations
from pdf_export import export_dashboard
from kpi_cards import kpi_card

st.set_page_config(layout="wide")

st.title("AI Business Analytics Dashboard")

st.sidebar.title("Sections")

page = st.sidebar.radio(
"Navigate",
[
"Executive Summary",
"Trends",
"Product Performance",
"Geography/Customers",
"Operations"
])

# EXECUTIVE SUMMARY

if page=="Executive Summary":

    file = st.file_uploader("Upload CSV",type="csv")

    if file:

        df = clean_data(pd.read_csv(file))

        revenue = df["revenue"].sum()
        orders = df["order_id"].count()
        aov = revenue/orders
        rating = df["rating"].mean()

        c1,c2,c3,c4 = st.columns(4)

        with c1:
            kpi_card("Revenue",f"${revenue:,.0f}")

        with c2:
            kpi_card("Orders",orders)

        with c3:
            kpi_card("AOV",f"${aov:.2f}")

        with c4:
            kpi_card("Rating",f"{rating:.2f}")

        rec = recommendations(df)

        st.subheader("AI Recommendations")

        for r in rec:
            st.info(r)

        # EXPORT BUTTON
        if st.button("Export Executive Report"):

            kpis = {
                "Revenue": revenue,
                "Orders": orders,
                "AOV": aov,
                "Rating": rating
            }

            charts=[]

            file = export_dashboard(kpis,charts,rec)

            with open(file,"rb") as f:

                st.download_button(
                "Download PDF",
                f,
                file_name="executive_report.pdf"
                )

# TRENDS

if page=="Trends":

    file = st.file_uploader("Upload CSV",type="csv")

    if file:

        df = clean_data(pd.read_csv(file))

        fig = sales_trend(df)

        st.plotly_chart(fig,use_container_width=True)

        rec = recommendations(df)

        for r in rec:
            st.info(r)

        if st.button("Export Trends Report"):

            fig.write_image("trend_chart.png")

            kpis={}

            charts=["trend_chart.png"]

            file = export_dashboard(kpis,charts,rec)

            with open(file,"rb") as f:

                st.download_button(
                "Download PDF",
                f,
                file_name="trend_report.pdf"
                )

# PRODUCT PERFORMANCE

if page=="Product Performance":

    file = st.file_uploader("Upload CSV",type="csv")

    if file:

        df = clean_data(pd.read_csv(file))

        fig1 = top_products(df)
        fig2 = bottom_products(df)

        st.plotly_chart(fig1)
        st.plotly_chart(fig2)

        rec = recommendations(df)

        for r in rec:
            st.info(r)

        if st.button("Export Product Report"):

            fig1.write_image("top_products.png")
            fig2.write_image("bottom_products.png")

            charts=["top_products.png","bottom_products.png"]

            file = export_dashboard({},charts,rec)

            with open(file,"rb") as f:

                st.download_button(
                "Download PDF",
                f,
                file_name="product_report.pdf"
                )

# GEOGRAPHY

if page=="Geography/Customers":

    file = st.file_uploader("Upload CSV",type="csv")

    if file:

        df = clean_data(pd.read_csv(file))

        fig = region_sales(df)

        st.plotly_chart(fig)

        rec = recommendations(df)

        for r in rec:
            st.info(r)

        if st.button("Export Region Report"):

            fig.write_image("region_chart.png")

            charts=["region_chart.png"]

            file = export_dashboard({},charts,rec)

            with open(file,"rb") as f:

                st.download_button(
                "Download PDF",
                f,
                file_name="region_report.pdf"
                )

# OPERATIONS

if page=="Operations":

    file = st.file_uploader("Upload CSV",type="csv")

    if file:

        df = clean_data(pd.read_csv(file))

        fig1 = payment_methods(df)
        fig2 = order_status(df)

        st.plotly_chart(fig1)
        st.plotly_chart(fig2)

        rec = recommendations(df)

        for r in rec:
            st.info(r)

        if st.button("Export Operations Report"):

            fig1.write_image("payment_chart.png")
            fig2.write_image("status_chart.png")

            charts=["payment_chart.png","status_chart.png"]

            file = export_dashboard({},charts,rec)

            with open(file,"rb") as f:

                st.download_button(
                "Download PDF",
                f,
                file_name="operations_report.pdf"
                )