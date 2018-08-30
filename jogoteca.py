from flask import Flask, render_template, request, redirect, session, flash, url_for
from dao import JogoDao
from models import Jogo, Usuario
import pymysql
app = Flask(__name__)
app.secret_key = 'Felipe'
#host = "0.0.0.0"
#user = "root"
#passwd = ""
#db = 'jogoteca'
#port = 3306

db = pymysql.connect(user='root',passwd='', host='localhost', port=3306)

jogo_dao = JogoDao(db)

Usuario1 = Usuario('felipe', 'felipe', '123456')
Usuario2 = Usuario('victor', 'victor', '654321')

usuarios = {Usuario1.id: Usuario1,Usuario2.id: Usuario2}

Jogo1 = Jogo('Super Mario', 'Ação', 'Nitendo')
Jogo2 = Jogo('GTA', 'Ação', 'Xbox')
Jogo3 = Jogo('Mortal Combat', 'Luta', 'Nitendo')
lista = [Jogo1, Jogo2, Jogo3]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo/')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect( url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console)
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(request.form['usuario'] + ' logou com sucesso !!')
            proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuário ' + request.form['usuario'] + 'não logou !')
        return redirect(url_for('login'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html',proxima=proxima)

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))


if __name__ == '__main__':
  app.run(host='localhost', port=8000, debug=True)
 