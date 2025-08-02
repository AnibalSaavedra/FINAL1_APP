
import streamlit as st
from fpdf import FPDF
from io import BytesIO

def generar_pdf(titulo, respuestas):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=titulo, ln=True, align="C")
    pdf.ln(10)
    for pregunta, respuesta in respuestas.items():
        pdf.multi_cell(0, 10, txt=f"{pregunta}: {respuesta}")
    # Guardar el PDF localmente
    pdf.output("informe_mbi360.pdf")
    # También permitir descarga directa desde interfaz
    pdf_buffer = BytesIO()
    pdf.output(pdf_buffer)
    st.download_button(
        label="📄 Descargar informe PDF",
        data=pdf_buffer.getvalue(),
        file_name="informe_mbi360.pdf",
        mime="application/pdf"
    )
