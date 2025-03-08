import streamlit as st 
import pandas as pd 
#vaidacion dsimple de usuario y clave  con un archivo csv

def validarUsuario(usuario,clave):
    """ permite la validacion de usuario
    
    Args:
        usuario (str):
        usuario a validar
        clave (str): clave del usaurio
        retutn bool
        true usuaurio valido, dalse usuario invalido
        
    """
defusuario = pd.read_csv('usuario.csv')

if len(defusuario[(defusuario['usuario']==usuario) & defusuario['clave']==clave])>0:
    return True
else:
    return False

def generarMenu(usuario):
    """generar el menu dependienfo del usuario
    
    Args:
       usuario (str): usuario utilizido para general el menu
       
    """

with st.sidebar:
    #cargar la tabla de usuario
    defusuario = pd.read_csv('usuario.csv')
    #filtramos la tabla de usuario
    defUsuario =[(defusuario['usuario']==usuario)]
    #Mostramos el nombre del usuario
    st.write(f " hola :blue-background[{nombre}]** ")
    #mostramos los enlaces de paginas
    st.pages_link("inicio.py", label=Inicio, icon=":material/home:")
    st.subheader("Tableros")
    st.pages_link("pages/pagina1.py") label='ventas', icon=":material/sell:"
    st.pages_link("pages/pagina2") label='ventas', icon=":material/shoping_cart:"
    st.pages_link("pages/pagina3") label='personal', icon=":material/group:"
    #boton para cerrar la session
    btnSalir = st.button("salir")
    if  btnSalir:
        st.session_state.clear()
         #luego de borrar sessio_state reiniciamos la app para mostrar la opcion de usuario y clave
           st.rerun()

            
def generarLogin():
    """ genera la ventana del login o muestra el menu si el login es valido """ 
    #validemos si el usaurio ya fue ingresado
    if 'usuario' in session_state:
        generarMenu(st.session_state['usuario']) # si hay usuario usario carguemos el menu
    else:
        #carguemos el formulario de login
        
        
    with st.form(frmLogin):
        
        parUsuario = st.text_input('usuario')
        parPassword = st.text_input('password', type='password')
        btnLogin = st.form_submit_button('ingresar', type='primary')
        if btnLogin:
            if validarUsuario(parUsuario, parPassword):
                st.session_state['usuario']== parUsuario
                #si el usuario es correcto reiniciamos la app para que se cargue el menu
                st.rerun()
            else:
                #si el usuaro es einvalido mostramos el mensaje de error
                st.error('usuario o clave invalidos', icon=":material/gpp_maybe:")    
        
        
        
