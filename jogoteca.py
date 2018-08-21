from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/inicio/')
def ola():
    jogo1 = Jogo('Super Mário', 'Ação', 'Super Nitendo')
    jogo2 = Jogo('Pokemon Gold', 'RPG', 'GameBoy')
    lista = [jogo1, jogo2]
    return render_template('lista.html', titulo= 'Jogos')


#app.run(host='localhost', port=8080) -> Rodar em uma porta e ip diferente
app.run()