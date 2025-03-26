from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_sqlalchemy.query import Query

#criando um API flask
app = Flask(__name__)
app.config['SECRET_KEY']= '654321'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' #url do banco de dados
#criando uma instancia de SQLAlchemy
db = SQLAlchemy(app)
db:SQLAlchemy #para "tipar" diretamente a variavel para o tipo SQLAlchemy
#Definir estrutura da tabela/classe postagem
class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    #autor
    id_autor = db.Column(db.Integer,db.ForeignKey('autor.id_autor'))
#Defenir estrutura da tabela/classe autor
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')#nesta função deve passar o nome da classe e nao o nome da tabela

def inicializar_banco():
    #criando o banco de dados
    with app.app_context():
        db.drop_all()#exclui qualquer estrutura previa -de banco de dados- que possa existir
        db.create_all()
        #criar usuarios administradores
        autor = Autor(nome='Lucas Santana',email='lucas@gmail.com',senha='123456',admin=True)
        db.session.add(autor)
        db.session.commit()    

#Só ira criar um novo banco de dados se rodar esse arquivo.py
if __name__ == "__main__":
    inicializar_banco()