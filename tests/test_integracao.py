from app import main
import pytest


#Teste Criar um usuario
def testCriarUsuario():
    main.testing = True
    client = main.test_client()
    response = client.get("/usuarios?nome=Beatriz&email=beatriz@teste.com&senha=123456&CPF=12345678900")
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data == {'nome': 'Beatriz', 'email': 'beatriz@teste.com', 'senha': '123456', 'CPF': '12345678900'}

#Teste Listar todos os usuarios
def testListarUsuarios():
    main.testing = True
    client = main.test_client()
    response = client.get("/usuarios")
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data == {'nome': 'Beatriz', 'email': 'beatriz@teste.com', 'senha': '123456', 'CPF': '12345678900'}

#Teste Listar um usuario
def testListarUmUsuario():
    main.testing = True
    client = main.test_client()
    response = client.get("/usuarios/12345678900")
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data == {'nome': 'Beatriz', 'email': 'beatriz@teste.com', 'senha': '123456', 'CPF': '12345678900'}

#Teste Listar um usuario inexistente
def testListarUmUsuarioInexistente():
    main.testing = True
    client = main.test_client()
    response = client.get("/usuarios/12345678899")
    json_data = response.get_json()

    assert response.status_code == 404
    assert json_data == {'Nenhum Usuário Encontrado'}

#Teste Deletar um usuario
def testDeletarUsuario():
    main.testing = True
    client = main.test_client()
    response = client.delete("/usuarios/12345678944")
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data == {'Usuario Deletado com Sucesso'}

#Teste Deletar um usuario inexistente
def testDeletarUsuarioInexistente():
    main.testing = True
    client = main.test_client()
    response = client.delete("/usuarios/12345678944")
    json_data = response.get_json()

    assert response.status_code == 404
    assert json_data == {'Nenhum Usuário Encontrado'}
