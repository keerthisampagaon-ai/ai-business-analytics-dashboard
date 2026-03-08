from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def export_dashboard(kpis, charts, insights):

    file="dashboard_report.pdf"

    styles = getSampleStyleSheet()

    elements=[]

    elements.append(Paragraph("Business Dashboard Report", styles['Title']))
    elements.append(Spacer(1,20))

    for k,v in kpis.items():
        elements.append(Paragraph(f"{k}: {v}", styles['BodyText']))

    elements.append(Spacer(1,20))

    for img in charts:
        elements.append(Image(img, width=400, height=250))
        elements.append(Spacer(1,20))

    elements.append(Paragraph("Recommendations", styles['Heading2']))

    for ins in insights:
        elements.append(Paragraph(ins, styles['BodyText']))

    pdf=SimpleDocTemplate(file)
    pdf.build(elements)

    return file