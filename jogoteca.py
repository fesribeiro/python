from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'Felipe'

class Jogo:

    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


Jogo1 = Jogo('Super Mario', 'Ação', 'Nitendo')
Jogo2 = Jogo('GTA', 'Ação', 'Xbox')
Jogo3 = Jogo('Mortal Combat', 'Luta', 'Nitendo')
lista = [Jogo1, Jogo2, Jogo3]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo/')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request. form['nome']
    categoria = request. form['categoria']
    console = request. form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/autenticar/', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + 'Logou com sucesso !')
        return redirect('/')
    else:
        flash('Usuário ' + request.form['usuario'] + 'não logou !')
        return redirect('/login')

@app.route('/login', methods=['POST',])
def login():
    return render_template('login.html')


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 