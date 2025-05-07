from flask import Flask, jsonify, request
main = Flask(__name__)

usuarios_lista = []


# 1- Criar Usuarios
@main.route('/usuarios', methods=['POST'])
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
@main.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios_lista)

#3- Listar um Usuario
@main.route('/usuarios/<string:CPF>', methods=['GET'])
def listarUmUsario(cpf):
    for usuario in usuarios_lista:
        try:
            if usuario["CPF"] == cpf:
                return jsonify(usuario)
        except KeyError:
            continue
    return jsonify({"Nenhum Usuário Encontrado"})

#4- Deletar um Usuario
@main.route('/usuarios/<string:CPF>', methods=['DELETE'])
def deletarUsuario(cpf):
    for usuario in usuarios_lista:
        try:
            if usuario["CPF"] == cpf:
                usuarios_lista.remove(usuario)
                return jsonify({"Usuario Deletado com Sucesso"})
        except KeyError:
            continue
    return jsonify({"Nenhum Usuário Encontrado"})
