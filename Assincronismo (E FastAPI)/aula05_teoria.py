from flask import Flask
from time import sleep

# a teoria fala sobre Assincronismo no FastAPI, nesse script com flask é o caso sincrono

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    sleep(20)
    return { 'olá': 'mundo!' }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 8000, threaded=False) # o threaded faz um trabalho sincrono "simulando" um trabalho assincrono
