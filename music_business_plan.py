import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io

# Title
st.title("Music Business Plan Generator")

# Introduction
st.write("Create a business plan for your music career. Fill out the sections below and download your plan as a PDF.")

# Business Plan Sections (based on punchlist categories)
business_plan = {
    "Executive Summary": "Provide an overview of your music career goals, target audience, and unique selling points.",
    "Writing": "Detail your process for creating songs, including inspiration sources, lyric writing, and melody development.",
    "Recording": "Outline your recording setup, equipment, and approach to capturing high-quality audio.",
    "Editing": "Describe your editing workflow, tools used, and techniques for refining tracks.",
    "Mixing": "Explain your mixing process, including balancing tracks and applying effects.",
    "Mastering": "Define your mastering strategy to ensure professional sound quality.",
    "Copywriting": "Plan your promotional content, such as bios, press releases, and social media captions.",
    "Publishing": "Detail your approach to copyright, PRO registration, and metadata management.",
    "Uploading": "Specify platforms for distribution and steps for uploading your music.",
    "Sharing": "Outline your strategy for sharing music with fans, curators, and media.",
    "Calling": "List key contacts (producers, venues, etc.) and your outreach plan.",
    "Scheduling": "Provide a timeline for recording, releases, and marketing campaigns.",
    "Music Marketing": "Describe your marketing tactics, including ads, social media, and fan engagement.",
    "Music Sales": "Plan your pricing, merch offerings, and sales tracking methods.",
    "Touring": "Detail your touring strategy, including venue booking and promotion."
}

# User Inputs
st.write("Fill out each section of your business plan:")
plan_data = {}
for section, description in business_plan.items():
    st.subheader(section)
    st.write(description)
    plan_data[section] = st.text_area(f"Enter details for {section}", height=150)

# PDF Generation Function
def generate_pdf(plan_data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph("Music Business Plan", styles['Title']))
    story.append(Spacer(1, 12))

    # Add each section
    for section, content in plan_data.items():
        story.append(Paragraph(section, styles['Heading1']))
        story.append(Spacer(1, 6))
        story.append(Paragraph(content, styles['BodyText']))
        story.append(Spacer(1, 12))

    doc.build(story)
    buffer.seek(0)
    return buffer

# Download Button
if st.button("Generate and Download PDF"):
    if all(plan_data.values()):  # Ensure all fields are filled
        pdf_buffer = generate_pdf(plan_data)
        st.download_button(
            label="Download Business Plan PDF",
            data=pdf_buffer,
            file_name="Music_Business_Plan.pdf",
            mime="application/pdf"
        )
    else:
        st.error("Please fill out all sections before generating the PDF.")

# Footer
st.write("Complete the fields above to create a tailored business plan for your music career!")
