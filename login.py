import hashlib

usuarios = {
    "jorge": hashlib.sha256("1234".encode()).hexdigest(),
    "admin": hashlib.sha256("admin".encode()).hexdigest()
}

def tela_login():
    st.title(" Tela de Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    if st.button("Entrar"):
        if usuario in usuarios and usuarios[usuario] == senha_hash:
            st.session_state.login_realizado = True
            st.session_state.usuario = usuario
            st.success("Login realizado com sucesso!")
            st.experimental_rerun()
        else:
            st.error("Usuário ou senha incorretos.")
