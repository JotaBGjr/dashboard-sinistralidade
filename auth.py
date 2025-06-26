import streamlit_authenticator as stauth

users = ["Gestao", "admin"]
hashed_passwords = [
  '$2b$12$PtUOGRTIuWmnXGPA2xYZPO/kd.5Of4EMdphz6O6NtLBRXMXlRBQe6',  # 1234
  '$2b$12$SnU9rK3yyvQJwVtTkZJv/uSDsD3DYiMki3zUck/t5rR.rqIm7b0fW'   # admin

]

authenticator = stauth.Authenticate(
  names=users,
  usernames=users,
  passwords=hashed_passwords,
  cookie_name="app_login",
  key="minhocauhaha"
  cookie_expiry_days=1,
)
