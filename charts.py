import plotly.express as px

# Global color theme
TEMPLATE = "plotly_white"

# Color palettes
BAR_COLORS = px.colors.qualitative.Bold
PIE_COLORS = px.colors.qualitative.Set3
LINE_COLORS = px.colors.qualitative.Plotly


# ---------------------------
# SALES TREND
# ---------------------------

def sales_trend(df):

    trend = df.groupby(df['order_date'].dt.to_period("M"))['revenue'].sum().reset_index()
    trend['order_date'] = trend['order_date'].astype(str)

    fig = px.line(
        trend,
        x="order_date",
        y="revenue",
        title="Sales Trend",
        markers=True,
        color_discrete_sequence=LINE_COLORS
    )

    fig.update_traces(line=dict(width=4))

    fig.update_layout(template=TEMPLATE)

    # save image for pdf
    fig.write_image("trend_chart.png", scale=3)

    return fig


# ---------------------------
# TOP PRODUCTS
# ---------------------------

def top_products(df):

    top = df.groupby("product")["revenue"].sum().sort_values(ascending=False).head(10).reset_index()

    fig = px.bar(
        top,
        x="product",
        y="revenue",
        title="Top 10 Products",
        color="product",
        color_discrete_sequence=BAR_COLORS
    )

    fig.update_layout(template=TEMPLATE)

    fig.write_image("top_products.png", scale=3)

    return fig


# ---------------------------
# BOTTOM PRODUCTS
# ---------------------------

def bottom_products(df):

    bottom = df.groupby("product")["revenue"].sum().sort_values().head(5).reset_index()

    fig = px.bar(
        bottom,
        x="product",
        y="revenue",
        title="Bottom 5 Products",
        color="product",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    fig.update_layout(template=TEMPLATE)

    fig.write_image("bottom_products.png", scale=3)

    return fig


# ---------------------------
# REGION SALES
# ---------------------------

def region_sales(df):

    region = df.groupby("region")["revenue"].sum().reset_index()

    fig = px.bar(
        region,
        x="revenue",
        y="region",
        orientation="h",
        title="Sales by Region",
        color="region",
        color_discrete_sequence=BAR_COLORS
    )

    fig.update_layout(template=TEMPLATE)

    fig.write_image("region_sales.png", scale=3)

    return fig


# ---------------------------
# PAYMENT METHODS
# ---------------------------

def payment_methods(df):

    pay = df["payment_method"].value_counts().reset_index()
    pay.columns = ["method", "count"]

    fig = px.pie(
        pay,
        values="count",
        names="method",
        title="Payment Methods",
        color_discrete_sequence=PIE_COLORS
    )

    fig.update_layout(template=TEMPLATE)

    fig.write_image("payment_methods.png", scale=3)

    return fig


# ---------------------------
# ORDER STATUS
# ---------------------------

def order_status(df):

    status = df["order_status"].value_counts().reset_index()
    status.columns = ["status", "count"]

    fig = px.pie(
        status,
        values="count",
        names="status",
        title="Order Status",
        color_discrete_sequence=px.colors.qualitative.Safe
    )

    fig.update_layout(template=TEMPLATE)

    fig.write_image("order_status.png", scale=3)

    return fig