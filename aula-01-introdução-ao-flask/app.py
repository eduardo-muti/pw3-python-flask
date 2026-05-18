# importando o flask na aplicação
from flask import Flask, render_template

#carregando o flask em uma variavel
app = Flask(__name__, template_folder='views')
#a__name__ e uma variavel do python que tem o nome do bjeto atual

#crindo a rota principal do site
@app.route('/')
# def  cria funções no python
def home():
    return render_template('index.html')



@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/console')
def console():
    return render_template('console.html')



#servidor web
if __name__ == '__main__':
    app.run()
    #o app.fy for o arquivo principal ele inici o server