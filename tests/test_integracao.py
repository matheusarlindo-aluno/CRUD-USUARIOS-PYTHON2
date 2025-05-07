from main.app import app
import pytest


#Teste Criar um usuario
def testCriarUsuario(usuarios):
    app.testing = True
    client = app.test_client()
    response = client.get("/usuarios?nome=Beatriz&email=beatriz@teste.com&senha=123456&CPF=12345678900")
    json_data = response.get_json(usuarios)

    assert response.status_code == 200
    assert json_data == [{'nome': 'Beatriz', 'email': 'beatriz@teste.com', 'senha': '123456', 'CPF': '12345678900'}]

#Teste Listar todos os usuarios
def testListarUsuarios(usuarios):
    app.testing = True
    client = app.test_client()
    response = client.get("/usuarios")
    json_data = response.get_json(usuarios)

    assert response.status_code == 200
    assert json_data == [{'nome': 'Beatriz', 'email': 'beatriz@teste.com', 'senha': '123456', 'CPF': '12345678900'}]

#Teste Listar um usuario
def testListarUmUsuario(cpf):
    app.testing = True
    client = app.test_client()
    response = client.get("/usuarios/12345678900")
    json_data = response.get_json(cpf)

    assert response.status_code == 200
    assert json_data == [{'nome': 'Beatriz', 'email': 'beatriz@teste.com', 'senha': '123456', 'CPF': '12345678900'}]

#Teste Listar um usuario inexistente
def testListarUmUsuarioInexistente(cpf):
    app.testing = False
    client = app.test_client()
    response = client.get("/usuarios/12345678899")
    json_data = response.get_json(cpf)

    assert response.status_code == 404
    assert json_data == {'Nenhum Usuário Encontrado'}

#Teste Deletar um usuario
def testDeletarUsuario(cpf):
    app.testing = True
    client = app.test_client()
    response = client.delete("/usuarios/12345678944")
    json_data = response.get_json(cpf)

    assert response.status_code == 200
    assert json_data == {'Usuario Deletado com Sucesso'}

#Teste Deletar um usuario inexistente
def testDeletarUsuarioInexistente(cpf):
    app.testing = True
    client = app.test_client()
    response = client.delete("/usuarios/12345678944")
    json_data = response.get_json(cpf)

    assert response.status_code == 200
    assert json_data == {'Nenhum Usuário Encontrado'}
