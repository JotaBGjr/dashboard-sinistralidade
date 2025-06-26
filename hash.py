import bcrypt

senha = input("Digite a senha que deseja hashear: ").encode('utf-8')
hashed = bcrypt.hashpw(senha, bcrypt.gensalt())
print(hashed.decode())