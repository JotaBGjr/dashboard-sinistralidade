# login.py

import streamlit_authenticator as stauth

def configurar_autenticador():
    nomes = ["Jorge"]
    usernames = ["jorge"]
    senhas = ["Aggrega@2025"]  # senha em texto

    hashed_senhas = sauth.Hasher(senhas).generate()

    authenticator = sauth.Authenticate(
        nomes,
        usernames,
        hashed_senhas,
        "meu_dashboard",        # nome do cookie
        "chave_ultra_secreta",  # segredo do cookie
        cookie_expiry_days=1
    )

    return authenticator
