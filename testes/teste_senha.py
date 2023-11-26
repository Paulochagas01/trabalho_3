from ..scripts.senha import check_password, hash_password

# Define uma função de teste chamada test_verificar_senha
def test_verificar_senha():
    # Cria uma variável chamada stored_password e atribui um valor fictício a ela
    stored_hashed_password='50b1214339543e1b2846826a2c1495a4c279ce177f859a4db3d3b86024e0a519'
    correct_user_password = "senha_aleatoria"
    incorrect_user_password= "senha_errada"
    
    # Testa se a função check_password retorna True para a senha correta
    assert check_password(correct_user_password, stored_hashed_password) is True, "A senha correta deveria ser validada"
    
    # Testa se a função check_password retorna False para uma senha incorreta
    assert check_password(incorrect_user_password, stored_hashed_password) is False, "A senha incorreta deveria falhar"