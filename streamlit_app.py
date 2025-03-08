import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# HTML con CSS y JavaScript
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .stApp {
            background-color: #f0f0f0;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            padding: 15px 32px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div style="text-align: center;">
        <h1 style="color: blue;">Mi Aplicación Streamlit</h1>
        <p style="font-size: 20px;">Sube tu foto y toma una nueva</p>
        <button class="stButton">Botón</button>
    </div>
    <script>
        document.querySelector('.stButton button').addEventListener('click', function() {
            alert('¡Hola, Streamlit!');
        });
    </script>
</body>
</html>
"""

# Insertar HTML en la aplicación
st.html(html_code, unsafe_allow_html=True)


st.form('my_form')
st.text_input("enter name")
st.text_input("enter email")
