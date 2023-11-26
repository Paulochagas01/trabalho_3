import os
import hashlib
import sys

def get_password_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def hash_password(password):
  hashed_password = hashlib.sha256(password.encode()).hexdigest()
  return hashed_password

def check_password(user_password, stored_hashed_password):
  hashed_user_password = hash_password(user_password)
  return hashed_user_password == stored_hashed_password
    

if __name__ == "__main__":
    #Obtém o diretório do script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    #Caminhos dos arquivos de senha
    password_file = os.path.join(script_directory, "../passwords/password.txt")
    hashed_password_file = os.path.join(script_directory, "../passwords/encryptedPassword.txt")

    #Leia a senha armazenada e a senha criptografada do arquivo
    stored_password = get_password_from_file(password_file)
    stored_hashed_password = get_password_from_file(hashed_password_file)

    
    #Input da senha pelo usuario
    input_password = 'senha123' # Senha Correta
    # input_password = 'senha'    # Senha Incorreta

    #Conferindo as senhas obtidas
    # print(f"Senha contida no arquivo password.txt: {stored_password}")
    # print(f"Senha contida no arquivo encryptedPassword.txt: {stored_hashed_password}")
    print("Check de senha")
    print(f"Senha inputada pelo usuario: {input_password}")

    #Conferindo a senha fornecida pelo usuario e a contida no arquivo txt
    if check_password(input_password,stored_hashed_password):
      print("Senha Correta!")
    else:
      print("Senha Incorreta!")
      sys.exit(1)


