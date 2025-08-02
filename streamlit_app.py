
import streamlit as st
from fpdf import FPDF
from datetime import datetime

def ejecutar_test_disociacion():
    st.header("🧠 Módulo 1: Test de disociación o trauma")
    preguntas = [
        ("Me desconecto fácilmente de lo que estoy sintiendo en situaciones difíciles.", "explicación 1"),
        ("A veces actúo como si estuviera en piloto automático y luego no recuerdo bien lo que hice.", "explicación 2"),
        ("Me cuesta identificar lo que siento o ponerlo en palabras.", "explicación 3"),
    ]
    respuestas = []
    for pregunta, explicacion in preguntas:
        with st.expander(pregunta):
            st.markdown(f"🛈 {explicacion}")
            respuesta = st.slider("Selecciona un nivel:", 1, 5, 3, key=pregunta)
            respuestas.append(respuesta)
    if st.button("Generar informe - Test Disociación"):
        puntaje = sum(respuestas)
        st.success(f"Puntaje total: {puntaje}")
        generar_pdf("Test de disociación", respuestas)

def ejecutar_test_epigenetico():
    st.header("🧬 Módulo 2: Estado epigenético emocional")
    preguntas = [
        ("Mi madre vivió situaciones traumáticas antes de que yo naciera.", "Herencia emocional materna"),
        ("Mi padre fue emocionalmente ausente o rígido.", "Herencia emocional paterna"),
        ("Siento que repito patrones familiares aunque no quiera.", "Epigenética transgeneracional"),
    ]
    respuestas = []
    for pregunta, explicacion in preguntas:
        with st.expander(pregunta):
            st.markdown(f"🛈 {explicacion}")
            respuesta = st.slider("Selecciona un nivel:", 1, 5, 3, key=pregunta)
            respuestas.append(respuesta)
    if st.button("Generar informe - Estado epigenético"):
        puntaje = sum(respuestas)
        st.success(f"Puntaje total: {puntaje}")
        generar_pdf("Estado epigenético emocional", respuestas)

def ejecutar_test_condiciones_clinicas():
    st.header("🩺 Módulo 3: Condiciones clínicas")
    categorias = {
        "Metabolismo": ["Fatiga después de comer", "Aumento de peso sin causa aparente"],
        "Digestión": ["Distensión abdominal", "Dificultad para digerir ciertos alimentos"],
        "Inflamación": ["Dolores articulares recurrentes", "Sensación de cuerpo inflamado"],
    }
    respuestas = {}
    for categoria, items in categorias.items():
        st.subheader(f"🔹 {categoria}")
        for item in items:
            valor = st.radio(item, ["1 (Nunca)", "2 (A veces)", "3 (Frecuente)"], key=item)
            respuestas[item] = valor
    if st.button("Generar informe - Condiciones clínicas"):
        generar_pdf("Condiciones clínicas", list(respuestas.values()))

def generar_pdf(titulo, respuestas):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Informe MBI 360°", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Módulo: {titulo}", ln=2, align="C")
    pdf.ln(10)
    for i, r in enumerate(respuestas, 1):
        pdf.cell(200, 10, txt=f"Ítem {i}: {r}", ln=1)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Fecha de generación: {fecha}", ln=1)
    pdf.output("/mnt/data/informe_mbi360.pdf")
    st.success("✅ Informe generado con éxito.")
    st.download_button("Descargar informe", data=open("/mnt/data/informe_mbi360.pdf", "rb"), file_name="informe_mbi360.pdf")

# Interfaz principal
st.title("🌐 MBI 360° – Evaluación Integral del Ser")
st.markdown("Bienvenido al sistema **MBI 360°**, una herramienta para conocer en profundidad tu estado emocional, epigenético, físico y energético.")
modulos = {
    "Test de disociación o trauma": ejecutar_test_disociacion,
    "Estado epigenético emocional": ejecutar_test_epigenetico,
    "Condiciones clínicas (metabolismo, digestión, inflamación)": ejecutar_test_condiciones_clinicas,
}
seleccionados = st.multiselect("Selecciona los módulos que deseas realizar:", list(modulos.keys()))
for modulo in seleccionados:
    modulos[modulo]()
