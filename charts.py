import plotly.express as px

def sales_trend(df):

    trend = df.groupby(df['order_date'].dt.to_period("M"))['revenue'].sum().reset_index()
    trend['order_date'] = trend['order_date'].astype(str)

    fig = px.line(trend,x="order_date",y="revenue",title="Sales Trend")

    return fig


def top_products(df):

    top = df.groupby("product")["revenue"].sum().sort_values(ascending=False).head(10)

    fig = px.bar(top,title="Top 10 Products")

    return fig


def bottom_products(df):

    bottom = df.groupby("product")["revenue"].sum().sort_values().head(5)

    fig = px.bar(bottom,title="Bottom Products")

    return fig


def region_sales(df):

    region = df.groupby("region")["revenue"].sum()

    fig = px.bar(region,orientation="h",title="Sales by Region")

    return fig


def payment_methods(df):

    pay = df["payment_method"].value_counts()

    fig = px.pie(values=pay.values,names=pay.index,title="Payment Methods")

    return fig


def order_status(df):

    status = df["order_status"].value_counts()

    fig = px.pie(values=status.values,names=status.index,title="Order Status")

    return fig