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
    # criando variaveis de variação
    titulo= "Silk Song"
    ano= 2025
    categoria= "Metroid vania"
    
    jogadores = ['Eduardo', 'Ana', 'Guilherme', 'Vitor', 'Antonio', 'Brenon', 'Kaio com k']
    return render_template('games.html',
                           titulo=titulo,
                           ano=ano,
                           categoria=categoria,
                           jogadores=jogadores)

@app.route('/console')
def console():
    consoles = ['Eduardo', 'mintendo', 'xbox', 'play station']
    return render_template('console.html',
                           consoles=consoles)



#servidor web
if __name__ == '__main__':
    app.run(debug=True)
    #o app.fy for o arquivo principal ele inici o server