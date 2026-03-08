from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


def export_dashboard(kpis, insights):

    file = "dashboard_report.pdf"

    styles = getSampleStyleSheet()

    elements = []

    # -------------------
    # TITLE PAGE
    # -------------------

    elements.append(Paragraph("Business Analytics Dashboard Report", styles['Title']))
    elements.append(Spacer(1,40))
    elements.append(Paragraph("Automated report generated from Streamlit dashboard.", styles['BodyText']))
    elements.append(PageBreak())


    # -------------------
    # EXECUTIVE SUMMARY
    # -------------------

    elements.append(Paragraph("Executive Summary", styles['Heading1']))
    elements.append(Spacer(1,20))

    for k,v in kpis.items():
        elements.append(Paragraph(f"<b>{k}</b>: {v}", styles['BodyText']))

    elements.append(PageBreak())


    # -------------------
    # SALES TREND
    # -------------------

    elements.append(Paragraph("Sales Trend", styles['Heading1']))
    elements.append(Spacer(1,20))
    elements.append(Image("trend_chart.png", width=450, height=250))
    elements.append(PageBreak())


    # -------------------
    # PRODUCT PERFORMANCE
    # -------------------

    elements.append(Paragraph("Top Products", styles['Heading1']))
    elements.append(Spacer(1,20))
    elements.append(Image("top_products.png", width=450, height=250))
    elements.append(Spacer(1,30))

    elements.append(Paragraph("Bottom Products", styles['Heading1']))
    elements.append(Spacer(1,20))
    elements.append(Image("bottom_products.png", width=450, height=250))

    elements.append(PageBreak())


    # -------------------
    # GEOGRAPHY
    # -------------------

    elements.append(Paragraph("Sales by Region", styles['Heading1']))
    elements.append(Spacer(1,20))
    elements.append(Image("region_sales.png", width=450, height=250))

    elements.append(PageBreak())


    # -------------------
    # OPERATIONS
    # -------------------

    elements.append(Paragraph("Payment Methods", styles['Heading1']))
    elements.append(Spacer(1,20))
    elements.append(Image("payment_methods.png", width=450, height=250))

    elements.append(Spacer(1,40))

    elements.append(Paragraph("Order Status", styles['Heading1']))
    elements.append(Spacer(1,20))
    elements.append(Image("order_status.png", width=450, height=250))

    elements.append(PageBreak())


    # -------------------
    # AI INSIGHTS
    # -------------------

    elements.append(Paragraph("AI Recommendations", styles['Heading1']))
    elements.append(Spacer(1,20))

    for ins in insights:
        elements.append(Paragraph(ins, styles['BodyText']))
        elements.append(Spacer(1,10))


    pdf = SimpleDocTemplate(file, pagesize=A4)

    pdf.build(elements)

    return file