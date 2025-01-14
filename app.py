import streamlit as st
import requests

def agregar_fuente_a_n8n(url):
    """
    Envía una URL al webhook de n8n.
    """
    webhook_url = "https://n8n.andycruzh.com/webhook-test/fb713243-ebcf-49ca-9c1c-a41576b90954"
    try:
        response = requests.post(webhook_url, json={"url": url})
        
        if response.status_code == 200:
            return response.json().get("message", "Scrapeo realizado con éxito")
        else:
            return "Error al procesar en n8n"
        
    except Exception as e:
        print(f"Error al enviar datos a n8n: {e}")
        return False
    

# Título de la página
st.title("Gestión de Fuentes de Datos y Prompts")


st.subheader("Agregar Nueva Fuente")
# Formulario para URL
url = st.text_area("Escribe un mensaje:")
if st.button("Agregar"):
    mensaje = agregar_fuente_a_n8n(url)
    st.success(mensaje)

    st.subheader("Datos Extraídos")
    # Simula datos extraídos
    #data = [{"URL": "https://docs.google.com/spreadsheets/d/1malv5wVoc8qEu9vhQTKXlgtxPsnYqNOyKzkbBpYKt_A/edit?gid=0#gid=0", "Extracto": "Texto de ejemplo"}]
    url = "https://docs.google.com/spreadsheets/d/1malv5wVoc8qEu9vhQTKXlgtxPsnYqNOyKzkbBpYKt_A/edit?gid=0#gid=0"

    # Botón estilo HTML
    st.markdown(
        f"""
        <a href="{url}" target="_blank" style="display: inline-block; padding: 10px 20px; 
        font-size: 16px; color: white; background-color: #007432; text-decoration: none; 
        border-radius: 5px;">
        Ver datos
        </a>
        """,
        unsafe_allow_html=True,
    )
        