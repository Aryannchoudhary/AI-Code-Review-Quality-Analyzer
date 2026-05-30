from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    repo_url,
    prediction_label,
    health_score,
    explanation
):

    pdf_file = "AI_Code_Review_Report.pdf"

    doc = SimpleDocTemplate(
        pdf_file
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Code Review Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"Repository: {repo_url}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Repository Quality: {prediction_label}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Health Score: {health_score}/100",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "AI Review",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            explanation,
            styles["BodyText"]
        )
    )

    doc.build(content)

    return pdf_file