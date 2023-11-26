from ..scripts.senha import check_password, hash_password

# Define uma função de teste chamada test_verificar_senha
def test_verificar_senha():
    # Cria uma variável chamada stored_password e atribui um valor fictício a ela
    stored_hashed_password='55a5e9e78207b4df8699d60886fa070079463547b095d1a05bc719bb4e6cd251'
    correct_user_password = "senha123"
    incorrect_user_password= "senha"
    
    # Testa se a função check_password retorna True para a senha correta
    assert check_password(correct_user_password, stored_hashed_password) is True, "A senha correta deveria ser validada"
    
    # Testa se a função check_password retorna False para uma senha incorreta
    assert check_password(incorrect_user_password, stored_hashed_password) is False, "A senha incorreta deveria falhar"