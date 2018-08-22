from flask import Flask, render_template
app = Flask(__name__)

class Jogo:

    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/')
def index():
    Jogo1 = Jogo('Super Mario', 'Ação', 'Nitendo')
    Jogo2 = Jogo('GTA', 'Ação', 'Xbox')
    Jogo3 = Jogo('Mortal Combat', 'Luta', 'Nitendo')
    lista = [Jogo1, Jogo2, Jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 