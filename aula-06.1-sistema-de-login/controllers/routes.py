from flask import render_template, request, redirect, url_for

from models.database import Game, db, Console, Usuario
from werkzeug.security import generate_password_hash


# Criando a função para receber o Flask (app)

def init_app(app):
    # Simulando um Banco de Dados
    listaGames = [{"titulo": "CS-GO", "ano": 2012, "genero": "FPS"}]

    # Criando a rota principal do site
    @app.route('/')
    # def serve para criar funções no Python
    def home():
        return render_template('index.html')


    @app.route('/games')
    def games():
        # Criando variáveis para passar as informações de um jogo
        titulo = "Silk Song"
        ano = 2025
        genero = "Metroidvania"
        # variavel = chaves do obj = valores do obj
        # chave + valor = item
        
        # Criando um obj Python (dicionário) para representar as propriedades de um jogo
        game = {
            "Título" : "Minecraft",
            "Ano" : 2012,
            "Categoria" : "Sandbox"
        }
        
        # Criando Vetor (Lista)
        jogadores = ['Eduardo','Carlinhos','Breno','Marcele']
        
        return render_template('games.html',
                            titulo=titulo,
                            ano=ano,
                            genero=genero,
                            jogadores=jogadores,
                            game=game)
    # {{ nome da variável }} -> Jinja2 permite exibir variáveis Python no HTML (um pacote do Flask)

    @app.route('/consoles')
    def consoles():
        consoles = ['Playstation 4','Playstation 3','Xbox 360','Xbox One','Nintendo Switch']
        return render_template('consoles.html',
                            consoles=consoles)
    
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            listaGames.append({'titulo': request.form.get('titulo'),
                               'ano': request.form.get('ano'),
                               'genero': request.form.get('genero')})
            # o metodo append adiciona valores a lista
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               listaGames=listaGames)
        
    @app.route("/estoque_jogos", methods=['GET', 'POST'])
    #criando um parametro para excluir
    @app.route("/estoque-jogo/delete/<int:id>")
    def estoque_jogos(id=None):
        #verificando se o usuario está tentando enviar o id para a rota
        if id:
            game = Game.query.get(id)
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque_jogos'))
        
        if request.method == 'POST':
            dados_form = request.form.to_dict()
            
            newGame = Game(
                dados_form['titulo'],
                dados_form['ano'],
                dados_form['categoria'],
                dados_form['plataforma'],
                dados_form['preco'],
                dados_form['quantidade']
            )
            
            db.session.add(newGame)
            db.session.commit()
            return redirect(url_for('estoque_jogos'))
        #selecionando todos os jogos do banco
        games = Game.query.all()
        return render_template('estoque-jogos.html', games = games)
    
    @app.route('/editar-jogos/<int:id>', methods=['GET', 'POST'])
    def editar_jogos(id):
        # buscar o jogo no banco
        game = Game.query.get(id)
        # e post?
        if request.method == 'POST': 
            dados_form = request.form.to_dict()
            game.titulo = dados_form['titulo']
            game.ano = dados_form['ano']
            game.categoria = dados_form['categoria']
            game.plataforma = dados_form['plataforma']
            game.preco = dados_form['preco']
            game.quantidade = dados_form['quantidade']
            db.session.commit()
            return redirect(url_for('estoque'))
        return render_template('editar-jogos.html', game=game)
    
    
    

    @app.route("/estoque_console", methods=['GET', 'POST'])
    @app.route("/estoque-console/delete/<int:id>")
    def estoque_console(id=None):
        #verificando se o usuario está tentando enviar o id para a rota
        if id:
            console = Console.query.get(id)
            db.session.delete(console)
            db.session.commit()
            return redirect(url_for('estoque_console'))
        
        if request.method == 'POST':
            dados_form = request.form.to_dict()
            
            newConsole = Console(
                dados_form['nome'],
                dados_form['ano'],
                dados_form['fabricante'],
                dados_form['plataforma'],
                dados_form['preco'],
                dados_form['quantidade']
            )
            
            db.session.add(newConsole)
            db.session.commit()
            return redirect(url_for('estoque_console'))
        #selecionando todos os consoles do banco
        consoles = Console.query.all()
        return render_template('estoque-console.html', consoles = consoles)
    
    
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        if request.method == "POST":
            email = request.form['email']
            senha = request.form['senha']
            senha_criptografada = generate_password_hash(senha, method='scrypt')
            novo_usuario = Usuario(email=email, senha=senha_criptografada)
            db.session.add(novo_usuario)
            db.session.commit() 
            return redirect(url_for('login'))       
        return render_template('cadastro.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        return "bem-vindo a página de login!"
