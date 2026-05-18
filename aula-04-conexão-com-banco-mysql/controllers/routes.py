#importar o render_template
#motor para renderizar as paginas

from flask import render_template

#função para receber flask (app)

def init_app(app):
   # a partir daqui virão as rotas

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
        
        #criaddo um objeto python para representar as propriedades de um jogo
        game= {
            "Título": "minecraft",
            "Ano": 2012,
            "Categoria" :"sandbox"
        }
        
        
        
        jogadores = ['Eduardo', 'Ana', 'Guilherme Briggs', 'Vitor', 'Antonio', 'Brenon', 'Kaio com k']
        return render_template('games.html',
                            titulo=titulo,
                            ano=ano,
                            categoria=categoria,
                            jogadores=jogadores,
                            game=game)

    @app.route('/consoles')
    def console():
        consoles = ['Play station 1', 'Nintendo 3DS', 'Xbox', 'Play station 2', 'Play station 3']
        return render_template('consoles.html',
                            consoles=consoles)

   