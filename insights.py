import pandas as pd

def generate_insights(df):

    insights = []

    # --------------------
    # Revenue Insight
    # --------------------

    total_revenue = df["revenue"].sum()

    insights.append(
        f"Total revenue generated is ${total_revenue:,.0f}, showing the overall business performance."
    )

    # --------------------
    # Region Insight
    # --------------------

    if "region" in df.columns:

        region_sales = df.groupby("region")["revenue"].sum()

        best_region = region_sales.idxmax()
        worst_region = region_sales.idxmin()

        insights.append(
            f"The highest revenue comes from the {best_region} region, while {worst_region} generates the lowest revenue."
        )

    # --------------------
    # Product Insight
    # --------------------

    if "product" in df.columns:

        product_sales = df.groupby("product")["revenue"].sum()

        top_product = product_sales.idxmax()

        insights.append(
            f"The best selling product is {top_product}, contributing significantly to total revenue."
        )

    # --------------------
    # Payment Insight
    # --------------------

    if "payment_method" in df.columns:

        payment = df["payment_method"].value_counts()

        popular_method = payment.idxmax()

        insights.append(
            f"Most customers prefer paying via {popular_method}."
        )

    # --------------------
    # Order Status Insight
    # --------------------

    if "order_status" in df.columns:

        status = df["order_status"].value_counts(normalize=True)

        cancel_rate = status.get("Cancelled",0) * 100

        insights.append(
            f"The cancellation rate is {cancel_rate:.1f}% of total orders."
        )

    # --------------------
    # Sales Trend Insight
    # --------------------

    if "order_date" in df.columns:

        df["order_date"] = pd.to_datetime(df["order_date"])

        monthly = df.groupby(df["order_date"].dt.to_period("M"))["revenue"].sum()

        trend = "increasing" if monthly.iloc[-1] > monthly.iloc[0] else "declining"

        insights.append(
            f"Sales trend over time appears to be {trend} based on monthly revenue analysis."
        )

    return insights