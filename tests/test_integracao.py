from main.app import app
import pytest
import unittest


class TestUsuario(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    #Teste Criar Usuario
    def testCriarUsuario(self):
        response = self.client.post("/usuarios", json={
            'nome': 'Beatriz',
            'email': 'beatriz@teste.com',
            'senha': '123456',
            'CPF': '12345678900'
        })
        json_data = response.get_json()
        self.assertEqual (response.status_code, 200)
        self.assertEqual (json_data, {'nome': 'Beatriz', 
                                      'email': 'beatriz@teste.com', 
                                      'senha': '123456', 
                                      'CPF': '12345678900'
                                        })  

    #Teste Listar todos os usuarios
    def testListarUsuarios(self):
        # Cria o usuário primeiro
        self.client.post("/usuarios", json={
            'nome': 'Beatriz',
            'email': 'beatriz@teste.com',
            'senha': '123456',
            'CPF': '12345678900'
            })

        response = self.client.get("/usuarios" )
        json_data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual (json_data, [{'nome': 'Beatriz', 'email': 'beatriz@teste.com', 'senha': '123456', 'CPF': '12345678900'}])

    #Teste Listar um usuario
    def testListarUmUsuario(self):
        # Cria o usuário primeiro
        self.client.post("/usuarios", json={
            'nome': 'Beatriz',
            'email': 'beatriz@teste.com',
            'senha': '123456',
            'CPF': '12345678900'
            })

        response = self.client.get("/usuarios/12345678900")
        json_data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_data, {'nome': 'Beatriz', 'email': 'beatriz@teste.com', 'senha': '123456', 'CPF': '12345678900'})

    #Teste Listar um usuario inexistente
    def testListarUmUsuarioInexistente(self):
        response = self.client.get("/usuarios/12345678999")
        json_data = response.get_json() 

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_data['mensagem'], 'Nenhum Usuário Encontrado')

    #Teste Deletar um usuario
    def testDeletarUsuario(self):
        response = self.client.delete("/usuarios/12345678900")
        json_data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual (json_data['mensagem'], 'Usuario Deletado com Sucesso')

    #Teste Deletar um usuario inexistente
    def testDeletarUsuarioInexistente(self):
        response = self.client.delete("/usuarios/12345678999")
        json_data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_data['mensagem'], 'Nenhum Usuário Encontrado')
    
if __name__ == '__main__':
    unittest.main()
