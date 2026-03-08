def recommendations(df):

    rec = []

    if "order_status" in df.columns:

        cancel = df["order_status"].value_counts(normalize=True).get("Cancelled",0)

        if cancel > 0.15:
            rec.append("High cancellation rate detected. Improve logistics.")

    if "product" in df.columns:

        slow = df.groupby("product")["revenue"].sum().sort_values().head(3)

        rec.append(f"Slow moving products: {', '.join(slow.index)}")

    if "region" in df.columns:

        best = df.groupby("region")["revenue"].sum().idxmax()

        rec.append(f"Highest revenue from {best}. Increase marketing here.")

    return rec