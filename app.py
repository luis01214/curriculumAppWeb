import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pandas as pd

st.title("Clasificador de Currículums con IA")
st.write("Sube tu currículum y compara con una vacante para saber si hay alta, media o baja coincidencia.")

# Entrada de usuario
cv_text = st.text_area("Pega el texto de tu currículum aquí:", height=200)
vacante_text = st.text_area("Escribe la descripción de la vacante:", height=150)

if st.button("Analizar coincidencia"):
    if not cv_text or not vacante_text:
        st.warning("Por favor, llena ambos campos.")
    else:
        # Datos simulados para entrenamiento
        ejemplos = [
            "Desarrollador de software con experiencia en Python y Django",
            "Analista de datos con manejo de SQL y Excel",
            "Diseñador gráfico con experiencia en Adobe Illustrator",
            "Desarrollador backend experto en Java y bases de datos",
            "Experiencia en ventas, atención al cliente y trabajo en equipo"
        ]
        etiquetas = ["alta", "media", "baja", "alta", "media"]  # etiquetas simuladas

        # Entrenar el modelo con datos de ejemplo
        modelo = make_pipeline(TfidfVectorizer(), MultinomialNB())
        modelo.fit(ejemplos, etiquetas)

        # Clasificar el currículum comparándolo con la vacante
        entrada = [cv_text + " " + vacante_text]
        resultado = modelo.predict(entrada)

        st.success(f"Resultado: Coincidencia **{resultado[0].upper()}** con la vacante.")
st.write(">>>Hecho por Luis Eduardo Garcia")