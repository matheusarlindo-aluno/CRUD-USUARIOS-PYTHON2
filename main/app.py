from flask import Flask, jsonify, request
app = Flask(__name__)

usuarios_lista = []


# 1- Criar Usuarios
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')
    cpf = dados.get('CPF')

    if not nome or not email or not senha or not cpf:
        return jsonify({'erro': 'Todos os campos são obrigatórios!'})

    usuario = {
        'nome': nome,
        'email': email,
        'senha': senha,
        'CPF': cpf
    }
    usuarios_lista.append(usuario)
    return jsonify(usuario)

#2- Listar todos os Usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios_lista)

#3- Listar um Usuario
@app.route('/usuarios/<string:CPF>', methods=['GET'])
def listarUmUsario(CPF):
    for usuario in usuarios_lista:
        try:
            if usuario["CPF"] == CPF:
                return jsonify(usuario)
        except KeyError:
            continue
    return jsonify({"mensagem": "Nenhum Usuário Encontrado"})

#4- Deletar um Usuario
@app.route('/usuarios/<string:CPF>', methods=['DELETE'])
def deletarUsuario(CPF):
    for usuario in usuarios_lista:
        try:
            if usuario["CPF"] == CPF:
                usuarios_lista.remove(usuario)
                return jsonify({"mensagem": "Usuario Deletado com Sucesso"})
        except KeyError:
            continue
    return jsonify({"mensagem": "Nenhum Usuário Encontrado"})
