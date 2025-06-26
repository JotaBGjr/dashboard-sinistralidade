import streamlit as st
import streamlit_authenticator as stauth
import os
import base64

def get_base64_of_bin_file(bin_file_path):
    """Converte arquivo binário em string base64."""
    with open(bin_file_path, 'rb') as f:
        return base64.b64encode(f.read()).decode()

def load_image_base64(image_filename):
    """Carrega imagem e retorna como base64."""
    image_path = os.path.join(os.getcwd(), "pages", "imagens", image_filename)
    return get_base64_of_bin_file(image_path)

def apply_custom_styles():
    """Aplica CSS customizado à interface do Streamlit."""
    st.markdown("""
        <style>
            html, body, .stApp {
                background-color: black !important;
            }

            #MainMenu, header, footer {visibility: hidden;}

            .logo-img {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 700px;
                margin-top: 1px;
                margin-bottom: 3px;
            }

            .login-box {
                background-color: rgba(0, 0, 0, 0.6);
                padding: 3rem;
                border-radius: 1rem;
                text-align: center;
                color: white;
                max-width: 400px;
                margin: auto;
            }

            input {
                color: black !important;
            }
        </style>
    """, unsafe_allow_html=True)

def configurar_autenticacao():
    """Cria e retorna objeto de autenticação."""
    hashed_password = '$2b$12$T5NFaY4UIFtb03wtXKryNu6wFlun6pQt4L/aKxa2eidzixAaQ1tLi'
    config = {
        'credentials': {
            'usernames': {
                'usuario1': {
                    'name': 'Usuário 1',
                    'password': hashed_password
                }
            }
        },
        'cookie': {
            'name': 'teste_cookie',
            'key': 'super_chave_teste',
            'expiry_days': 1
        },
        'preauthorized': {
            'emails': []
        }
    }
    return stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

def tela_login():
    """Renderiza tela de login e retorna estado de autenticação."""
    image_base64 = load_image_base64("imagem_aggrega.png")
    apply_custom_styles()

    st.markdown(
        f'<img class="logo-img" src="data:image/png;base64,{image_base64}">',
        unsafe_allow_html=True
    )

    authenticator = configurar_autenticacao()
    login_result = authenticator.login("Login", location="sidebar")

    if login_result is not None:
        name, auth_status, username = login_result

        if auth_status:
            st.success(f"Bem-vindo(a), {name}!")
        elif auth_status is False:
            st.error("Usuário ou senha incorretos.")
        else:
            st.info("Por favor, faça login.")

        return name, auth_status, username

    st.info("Por favor, faça login.")
    return None, None, None