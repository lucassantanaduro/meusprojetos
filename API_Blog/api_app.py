from flask import Flask, jsonify, request,make_response
from estrutura_flask_sql_alchemy import Autor,Postagem,app,db
from datetime import datetime,timedelta
import jwt
from functools import wraps

def token_obrigatorio(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        #verificar se o token foi enviado na requisição
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'mensagem':'Token não incluido'},401)
        #validando token consultando DB
        try:
            resultado = jwt.decode(token,app.config['SECRET_KEY'],algorithms=['HS256'])            
            autor = Autor.query.filter_by(id_autor=resultado['id_autor']).first()
        except:
            return jsonify({'mensagem':'Token é invalido!'},401)
        return f(autor,*args,**kwargs)
    return decorated

@app.route('/login')
def login():
    auth = request.authorization #pega as info de login atraves da requisição
    if not auth or not auth.username or not auth.password:
        #informando para o usurio que o login esta invalido, e redirecionando para fazer login
        return make_response('Login invalido',401,{'www-authenticate':'Basic realm="Login obrigatório"'})
    usuario = Autor.query.filter_by(nome=auth.username).first()
    if not usuario:
        return make_response('Login invalido',401,{'www-authenticate':'Basic realm="Login obrigatório"'})
    if auth.password == usuario.senha:
        token = jwt.encode({'id_autor':usuario.id_autor,'exp': datetime.utcnow()+timedelta(minutes=30)}
                           ,app.config['SECRET_KEY'])
        return jsonify({'token':token})
    return make_response('Login invalido',401,{'www-authenticate':'Basic realm="Login obrigatório"'})


############################Tabela Postagem############################
@app.route('/postagens')
@token_obrigatorio
def obter_postagens(autor):
    postagens = Postagem.query.all()#Retorna todas as propiedades da classe/tabela Postagem/autor
    lista_de_postagens = []
    for postagem in postagens:
        postagem_atual = {
            "id_postagem":postagem.id_postagem,
            "titulo":postagem.titulo,
            "id_autor":postagem.id_autor,
        }
        lista_de_postagens.append(postagem_atual)

    return jsonify(lista_de_postagens)

#GET com id
@app.route('/postagens/<int:id_postagem>', methods= ['GET'])
@token_obrigatorio
def obter_postagem_por_id(autor,id_postagem):
    postagem = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not postagem:
        return jsonify({"mensagem":'Postagem nao encontrada!'})
    postagem_atual = {
        'id_postagem': postagem.id_postagem,
        'titulo': postagem.titulo,
        'id_autor': postagem.id_autor
    }

    return jsonify(postagem_atual)

#Criar um POST - POST ://lhttpsocalhost:5000/data/
@app.route('/postagens', methods= ['POST'])
@token_obrigatorio
def adicionar_postagem(autor):
    nova_postagem = request.get_json()    
    postagem = Postagem()
    try:
        postagem.titulo = nova_postagem['titulo']
    except:
        pass
    try:
        postagem.id_autor = nova_postagem['id_autor']
    except:
        pass
    db.session.add(postagem)#adicionando o autor
    db.session.commit()
    return jsonify ({'mensagem':'Postagem adicionada com sucesso!','postagem':nova_postagem}),200
    
    return jsonify ({'mensagem':'nao foi possivel'})
    #salvando no db

#Alterando postagem - PUT https://localhost:5000/data/1
@app.route('/postagens/<int:id_postagem>', methods= ['PUT'])
@token_obrigatorio
def alterar_postagem(autor,id_postagem):
    auteracao_post = request.get_json()
    post = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not post:
        return jsonify({'mensagem':'Post nao encontrado!'})
    #verificando se existe titulo na alteração
    try:
         post.titulo = auteracao_post['titulo']
    except:
        pass
    #verificando se existe id_autor na alteração
    try:
        post.id_autor = auteracao_post['id_autor']
    except:
        pass
    #verificando se existe senha na alteração
    
    db.session.commit()
    return jsonify({'Mensagem':'Alteração adicionada com sucesso!'},200)
    
#Excluindo postagem - DELETE https://localhost:5000/data/1
@app.route('/postagens/<int:id_postagem>', methods= ['DELETE'])
@token_obrigatorio
def excluir_postagem(autor,id_postagem):
    postagem = Postagem.query.filter_by(id_postagem=id_postagem).first()
    if not postagem:
        jsonify({'mensagem':'Postagem inexistente!'})
    db.session.delete(postagem)
    db.session.commit()
    return jsonify({'mensagem':'Postagem excluida com sucesso!'},200)

############################Tabela Autor############################
#Rota padrao - GET https://localhost:5000
@app.route('/autores')
@token_obrigatorio
def obter_autores(autor):
    autores = Autor.query.all()#Retorna todas as propiedades da classe/tabela Autor/autor
    lista_de_autores = []
    for autor in autores:
        autor_atual = {}
        autor_atual['id_autor'] = autor.id_autor
        autor_atual['nome'] = autor.nome
        autor_atual['email'] = autor.email
        autor_atual['admin'] = autor.admin
        lista_de_autores.append(autor_atual)

    return jsonify(lista_de_autores)

#GET com id - GET https://localhost:5000/data/1
@app.route('/autores/<int:id_autor>', methods= ['GET'])
@token_obrigatorio
def obter_autor_por_id(autor,id_autor):
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify(f'Autor nao encontrado!')
    autor_atual = {
        'id_autor': autor.id_autor,
        'nome': autor.nome,
        'email': autor.email,
        'admin': autor.admin
    }

    return jsonify(autor_atual)

#Criar um POST - POST https://localhost:5000/data/
@app.route('/autores', methods= ['POST'])
@token_obrigatorio
def adicionar_autor():
    novo_autor = request.get_json()    
    autor = Autor()    
    try:
         autor.nome = novo_autor['nome']
    except:
        pass
    #verificando se existe email na alteração
    try:
        autor.email = novo_autor['email']
    except:
        pass
    #verificando se existe senha na alteração
    try:
        autor.senha = novo_autor['senha']
    except:
        pass
    #verificando se existe admin na alteração
    try:
        autor.admin = novo_autor['admin']
    except:
        pass
    if not autor.nome:
        return jsonify ({'mensagem':'Propiedade nome vazia'})
    db.session.add(autor)#adicionando o autor
    db.session.commit()#salvando no db

    return jsonify ({'mensagem':'Autor adicionado com sucesso!','autor':novo_autor}),200
    
#Alterando autor - PUT https://localhost:5000/data/1
@app.route('/autores/<int:id_autor>', methods= ['PUT'])
@token_obrigatorio
def alterar_autor(autor,id_autor):
    auteracao_autor = request.get_json()
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        return jsonify({f'Autor nao encontrado!'})
    #verificando se existe nome na alteração
    try:
         autor.nome = auteracao_autor['nome']
    except:
        pass
    #verificando se existe email na alteração
    try:
        autor.email = auteracao_autor['email']
    except:
        pass
    #verificando se existe senha na alteração
    try:
        autor.senha = auteracao_autor['senha']
    except:
        pass
    #verificando se existe admin na alteração
    try:
        autor.admin = auteracao_autor['admin']
    except:
        pass

    db.session.commit()
    return jsonify({'Mensagem':'Alteração adicionada com sucesso!'},200)
        
#Excluindo dado - DELETE https://localhost:5000/data/1
@app.route('/autores/<int:id_autor>', methods= ['DELETE'])
@token_obrigatorio
def excluir_autor(autor,id_autor):
    autor = Autor.query.filter_by(id_autor=id_autor).first()
    if not autor:
        jsonify({'mensagem':'Autor inexistente!'})
    db.session.delete(autor)
    db.session.commit()
    return jsonify({'mensagem':'Autor excluido com sucesso!'},200)

app.run(port=8080,host='localhost',debug=True)


