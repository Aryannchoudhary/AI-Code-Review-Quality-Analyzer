from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    repo_url,
    prediction_label,
    health_score,
    explanation,
    avg_metrics,
    file_df
):

    pdf_file = "AI_Code_Review_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    
    # TITLE
    content.append(
        Paragraph(
            "AI Code Review & Quality Analyzer",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

   
    # SUMMARY
    content.append(
        Paragraph(
            "Repository Summary",
            styles["Heading1"]
        )
    )

    summary_data = [
        ["Repository URL", repo_url],
        ["Quality", prediction_label],
        ["Health Score", f"{health_score}/100"]
    ]

    summary_table = Table(
        summary_data,
        colWidths=[150, 300]
    )

    summary_table.setStyle(
        TableStyle([
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('BACKGROUND', (0,0), (0,-1), colors.lightgrey)
        ])
    )

    content.append(summary_table)

    content.append(
        Spacer(1, 20)
    )

  
    # METRICS
    content.append(
        Paragraph(
            "Repository Metrics",
            styles["Heading1"]
        )
    )

    metric_data = [["Metric", "Value"]]

    for metric, value in avg_metrics.items():

        metric_data.append([
            metric,
            str(round(value, 2))
        ])

    metric_table = Table(metric_data)

    metric_table.setStyle(
        TableStyle([
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('BACKGROUND', (0,0), (-1,0), colors.lightblue)
        ])
    )

    content.append(metric_table)

    content.append(
        Spacer(1, 20)
    )


    # FILE ANALYSIS
    content.append(
        Paragraph(
            "File-wise Analysis",
            styles["Heading1"]
        )
    )

    file_data = [
        [
            "File",
            "Quality",
            "Maintainability",
            "Complexity"
        ]
    ]

    for _, row in file_df.iterrows():

        file_data.append([
            str(row["File"]),
            str(row["Quality"]),
            str(row["Maintainability"]),
            str(row["Complexity"])
        ])

    file_table = Table(file_data)

    file_table.setStyle(
        TableStyle([
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('BACKGROUND', (0,0), (-1,0), colors.lightgreen)
        ])
    )

    content.append(file_table)

    content.append(
        Spacer(1, 20)
    )


    # AI REVIEW
    content.append(
        Paragraph(
            "AI Repository Review",
            styles["Heading1"]
        )
    )


    content.append(
        Paragraph(
            explanation[:2000],
            styles["BodyText"]
        )
    )

    doc.build(content)

    return pdf_file