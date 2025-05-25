from main import app
from flask import render_template  # procura a pasta templates do meu html

# rotas (ex: o que vai aparecer na rota homepage)
# o arquivo também pode se chamar views.py
# route -> siteteste.com/ <-
# funções -> O que você quer exibir naquela página


@app.route("/")  # rota da homepage, o app é o nome da variavel app criada no main.py
def homepage():  # o nome da função pode ser oq vc quiser
    return render_template("site_teste_homepage.html") # você retorna oq quer exibir

@app.route('/pagina2')
def pagina2():
    return render_template('site_teste_pagina2.html')
