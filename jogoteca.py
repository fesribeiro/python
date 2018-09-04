from flask import Flask, render_template, request, redirect, session, flash, url_for
from dao import JogoDao, UsuarioDao
from models import Jogo, Usuario
import pymysql
import os

app = Flask(__name__)
app.secret_key = 'Felipe'
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/upload'
db = pymysql.connect(user='root',passwd='', host='localhost', port=3306)

jogo_dao = JogoDao(db)
usuario_dao =  UsuarioDao(db)


cursor = db.cursor()
'''
cursor.execute('select * from jogoteca.jogo')
for jogo in cursor.fetchall():
    print(jogo[1])
'''


@app.route('/')
def index():
    lista = jogo_dao.listar()
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo/')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect( url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect( url_for('login', proxima=url_for('editar')))
    jogo = jogo_dao.busca_por_id(id)
    return render_template('editar.html', titulo='Alterar jogo', jogo=jogo)

@app.route('/deletar/<int:id>')
def deletar(id):
    jogo_dao.deletar(id)
    flash("Jogo excluido com sucesso !")
    return redirect(url_for('index'))


@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console)
    jogo = jogo_dao.salvar(jogo)
    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    arquivo.save('upload/' + arquivo.filename)
    return redirect(url_for('index'))

@app.route('/atualizar', methods=['POST',])
def atualizar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome,categoria, console, id=request.form['id'])
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(request.form['usuario'] + ' logou com sucesso !!')
            proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuário ' + request.form['usuario'] + ' não logou !')
        return redirect(url_for('login'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html',proxima=proxima)

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('login'))


if __name__ == '__main__':
  app.run(host='192.168.1.3', port=8000, debug=True)
 