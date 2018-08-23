from flask import Flask
app = Flask(__name__)

@app.route('/inicio/')
def ola():
    return 'teste'

app.run()
