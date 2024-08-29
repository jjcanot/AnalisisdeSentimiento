import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from PIL import Image

# Configuración de la página
st.title('Análisis de Sentimiento')
st.subheader("Hola, por favor escribe el texto o la frase que deseas analizar")

# Barra lateral con información sobre polaridad y subjetividad
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write("""
        Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
        Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
        
        Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
        (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

# Expander para analizar polaridad y subjetividad
with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:
        # Traducir texto a inglés
        translator = Translator()
        translation = translator.translate(text1, src="es", dest="en")
        trans_text = translation.text
        
        # Analizar sentimiento con TextBlob
        blob = TextBlob(trans_text)
        
        # Mostrar resultados
        st.write('Polarity: ', round(blob.sentiment.polarity, 2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))
        
        # Abrir imagen según la polaridad
        x = round(blob.sentiment.polarity, 2)
        if x >= 0.5:
            st.write('Estás feliz')
            img = Image.open('Feliz.jpg')
            st.image(img)
        elif x <= -0.5:
            st.write('Es un sentimiento Negativo')
        else:
            st.write('Es un sentimiento Neutral')
