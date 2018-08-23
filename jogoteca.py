from flask import Flask, render_template, request, redirect
app = Flask(__name__)

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

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 