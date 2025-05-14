from main.app import app
import pytest
import unittest


#Teste Criar Usuario
def testCriarUsuario():
    app.testing = True
    client = app.test_client()
    response = client.post("/usuarios", json={
        'nome': 'Beatriz',
        'email': 'beatriz@teste.com',
        'senha': '123456',
        'CPF': '12345678900'
    })
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data == {'nome': 'Beatriz', 'email': 'beatriz@teste.com', 'senha': '123456', 'CPF': '12345678900'}

#Teste Listar todos os usuarios
def testListarUsuarios():
    app.testing = True
    client = app.test_client()
    response = client.get("/usuarios" )
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data == [{'nome': 'Beatriz', 'email': 'beatriz@teste.com', 'senha': '123456', 'CPF': '12345678900'}]

#Teste Listar um usuario
def testListarUmUsuario():
    app.testing = True
    client = app.test_client()
    response = client.get("/usuarios", json={
        'CPF': '12345678900'
    })
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data == [{'nome': 'Beatriz', 'email': 'beatriz@teste.com', 'senha': '123456', 'CPF': '12345678900'}]

#Teste Listar um usuario inexistente
def testListarUmUsuarioInexistente():
    app.testing = True
    client = app.test_client()
    response = client.get("/usuarios/12345678999")
    json_data = response.get_json() 

    assert response.status_code == 200
    
    assert json_data['mensagem'] == 'Nenhum Usuário Encontrado'

#Teste Deletar um usuario
def testDeletarUsuario():
    app.testing = True
    client = app.test_client()
    response = client.delete("/usuarios/12345678900")
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data['mensagem'] == 'Usuario Deletado com Sucesso'

#Teste Deletar um usuario inexistente
def testDeletarUsuarioInexistente():
    app.testing = True
    client = app.test_client()
    response = client.delete("/usuarios/12345678999")
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data['mensagem'] == 'Nenhum Usuário Encontrado'
    

