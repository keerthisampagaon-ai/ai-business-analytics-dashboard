import pandas as pd

def ask_data(question, df):

    question = question.lower()

    # Revenue question
    if "revenue" in question and "total" in question:
        return f"Total revenue is ${df['revenue'].sum():,.0f}"

    # Best region
    if "region" in question and "highest" in question:
        region = df.groupby("region")["revenue"].sum().idxmax()
        return f"{region} region generates the highest revenue."

    # Top products
    if "top" in question and "product" in question:
        top = df.groupby("product")["revenue"].sum().sort_values(ascending=False).head(5)
        return f"Top products are: {', '.join(top.index)}"

    # Cancellation rate
    if "cancel" in question:
        cancel = df["order_status"].value_counts(normalize=True).get("Cancelled",0)*100
        return f"Cancellation rate is {cancel:.1f}%"

    # Payment method
    if "payment" in question:
        pay = df["payment_method"].value_counts().idxmax()
        return f"Most used payment method is {pay}"

    return "Sorry, I couldn't understand the question. Try asking about revenue, regions, products, or payments."