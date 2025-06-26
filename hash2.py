import streamlit_authenticator as stauth

senha = "Aggrega@2025"
hash_gerada = stauth.Hasher([senha]).generate()
print("Hash:", hash_gerada[0])