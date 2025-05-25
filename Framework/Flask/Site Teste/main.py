from flask import Flask

app = Flask(__name__)

from routes import *

if __name__ == '__main__': # para evitar problemas futuros
    app.run(debug=True) # vai executar o código, o debug é para aparecer as mudanças do site em tempo real
