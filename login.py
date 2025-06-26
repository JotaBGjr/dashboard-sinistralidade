import streamlit as st
import streamlit_authenticator as stauth
import os
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
        return base64.b64encode(data).decode()

# CSS
    st.markdown(f"""
        <style>
            html, body, .stApp {{
                background-color: black !important;
            }}

            #MainMenu, header, footer {{visibility: hidden;}}

            .logo-img {{
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 700px;
                margin-top: 1px;
                margin-bottom: 3px;
            }}

            .login-box {{
                background-color: rgba(0, 0, 0, 0.6);
                padding: 3rem;
                border-radius: 1rem;
                text-align: center;
                color: white;
                max-width: 400px;
                margin: auto;
            }}

            input {{
                color: black !important;
            }}
        </style>
    """, unsafe_allow_html=True)

    # Imagem
    st.markdown(
        f'<img class="logo-img" src="data:image/png;base64,{image_base64}">',
        unsafe_allow_html=True
    )






def tela_login():
    # Configuração de hash e imagem
    hashed_password = '$2b$12$T5NFaY4UIFtb03wtXKryNu6wFlun6pQt4L/aKxa2eidzixAaQ1tLi'
    image_path = os.path.join(os.getcwd(), "pages", "imagens", "imagem_aggrega.png")
    image_base64 = get_base64_of_bin_file(image_path)

    

    # Configuração do authenticator
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

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    login_result = authenticator.login("Login", "main")

    if login_result is not None:
        name, auth_status, username = login_result

        if auth_status:
            st.success(f"Bem-vindo(a), {name}!")
        elif auth_status is False:
            st.error("Usuário ou senha incorretos.")
        else:
            st.info("Por favor, faça login.")
        
        return name, auth_status, username
    else:
        st.info("Por favor, faça login.")
        return None, None, None
