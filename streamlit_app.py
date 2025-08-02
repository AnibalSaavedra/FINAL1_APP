# -*- coding: utf-8 -*-
# SISTEMA UNIFICADO: MBI 360° - RITUAL (app.py)
# Autor: Aníbal Saavedra

# ---- MODULO: Disociación o Trauma ----


# ---- MODULO: Epigenético Emocional ----


# ---- MODULO: Condiciones Clínicas ----

import streamlit as st

def ejecutar_test_condiciones_clinicas():
    st.title("🧬 MBI 360° – Módulo 3: Condiciones Clínicas Opcionales")
    st.markdown("Evalúa tu estado físico a través de síntomas relacionados con metabolismo, digestión, inflamación, hormonas, inmunidad y salud neuropsicológica.")
    st.markdown("Responde cada afirmación del 1 (nada) al 3 (mucho). Puedes presionar ❓ para entender mejor cada afirmación.")

    afirmaciones = {
        "Metabolismo": [
            ("Siento cansancio excesivo incluso después de dormir.", "Podrías tener un metabolismo lento o desequilibrio energético celular."),
            ("Mi peso varía fácilmente sin causa aparente.", "El metabolismo alterado influye en la regulación de peso corporal."),
            ("Me cuesta mantenerme activo o motivado físicamente.", "Una baja eficiencia metabólica puede reducir tu energía.")
        ],
        "Digestión": [
            ("Frecuentemente tengo hinchazón o gases después de comer.", "Puede deberse a una mala digestión o disbiosis intestinal."),
            ("Sufro de estreñimiento o diarrea de forma regular.", "Puede ser por estrés o alimentos inflamatorios."),
            ("Siento pesadez o lentitud mental luego de las comidas.", "Tu cuerpo puede estar sobrecargado procesando alimentos.")
        ],
        "Inflamación": [
            ("Siento dolor muscular o articular sin haberme exigido físicamente.", "Puede indicar inflamación crónica en tejidos blandos."),
            ("Mi piel suele enrojecerse, picar o tener brotes.", "Las inflamaciones internas a menudo se manifiestan en la piel."),
            ("Retengo líquidos o me hincho con facilidad.", "Un sistema inflamado tiende a acumular líquidos.")
        ],
        "Salud Hormonal": [
            ("Mis cambios de humor son intensos o impredecibles.", "Las hormonas influyen directamente en el equilibrio emocional."),
            ("Siento disminución del deseo sexual sin causa aparente.", "Puede estar relacionado con un desequilibrio hormonal."),
            ("Mis ciclos menstruales o patrones hormonales son irregulares.", "Puede ser señal de desregulación endocrina.")
        ],
        "Inmunidad": [
            ("Me enfermo con frecuencia (resfríos, virus, etc.).", "Tu sistema inmune podría estar debilitado."),
            ("Tardo más tiempo del habitual en recuperarme de enfermedades.", "Una inmunidad baja puede dificultar la recuperación."),
            ("Siento fatiga inmune (como si estuviera siempre en modo alerta).", "Tu sistema inmune puede estar hiperactivo.")
        ],
        "Neuropsicológicos": [
            ("Tengo problemas de memoria o concentración frecuentes.", "Tu sistema nervioso puede estar afectado por estrés o inflamación."),
            ("Siento ansiedad o nerviosismo constante.", "Refleja desregulación del sistema nervioso autónomo."),
            ("Me cuesta mantener el ánimo estable durante el día.", "Puede haber desequilibrio entre neurotransmisores y hormonas.")
        ]
    }

    resultados = {}
    for categoria, items in afirmaciones.items():
        st.subheader(f"🔹 {categoria}")
        for idx, (texto, explicacion) in enumerate(items):
            col1, col2 = st.columns([4, 1])
            with col1:
                seleccion = st.radio(texto, [1, 2, 3], key=f"{categoria}_{idx}")
                resultados[f"{categoria}_{idx}"] = seleccion
            with col2:
                with st.expander("❓"):
                    st.caption(explicacion)

    if st.button("✅ Finalizar evaluación"):
        st.success("Tus respuestas han sido registradas. Pronto podrás descargar el informe personalizado.")


# ---- APP PRINCIPAL ----

import streamlit as st
from modulo_disociacion import ejecutar_test_disociacion
from modulo_epigenetico import ejecutar_test_epigenetico
from modulo_condiciones import ejecutar_test_condiciones_clinicas

st.set_page_config(page_title="MBI 360°", page_icon="🌀", layout="centered")

st.title("🌀 MBI 360° – Evaluación Integral del Ser")

st.markdown("""
Bienvenido al sistema **MBI 360°**, una herramienta única para conocer en profundidad tu estado emocional, epigenético, físico y energético.

**Marca:** RITUAL  
**Creador:** Aníbal Saavedra – Biotecnólogo MIB
""")

st.markdown("### Selecciona uno o varios módulos que deseas realizar:")

modulos = [
    "Test de disociación o trauma",
    "Estado epigenético emocional (líneas materna/paterna)",
    "Condiciones clínicas opcionales"
]

modulos_seleccionados = st.multiselect("", modulos)

if not modulos_seleccionados:
    st.warning("Selecciona al menos un módulo para continuar.")
else:
    if "Test de disociación o trauma" in modulos_seleccionados:
        ejecutar_test_disociacion()
    if "Estado epigenético emocional (líneas materna/paterna)" in modulos_seleccionados:
        ejecutar_test_epigenetico()
    if "Condiciones clínicas opcionales" in modulos_seleccionados:
        ejecutar_test_condiciones_clinicas()

st.markdown("---")
st.markdown("📲 ¿Necesitas ayuda o una consulta personalizada? [Contáctame por WhatsApp](https://wa.me/56967010107)")

