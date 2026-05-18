# importando o flask na aplicação
from flask import Flask, render_template
from controllers import routes
import pymysql
from models.database import db, Game

#carregando o flask em uma variavel
app = Flask(__name__, template_folder='views')
#a__name__ e uma variavel do python que tem o nome do bjeto atual


DB_NAME = 'thegames'

app.config['DATABASE_NAME'] = DB_NAME

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

from controllers import routes
#enviando a variavel app (flask) para as rotas

routes.init_app(app)

#servidor web
if __name__ == '__main__':
    
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print("O banco de dados foi criado com sucesso")
    except Exception as error:
        print(f"Erro ao criar o banco: {error}")
    finally:
        connection.close()
        db.init_app(app = app)
        with app.test_request_context():
            db.create_all()
        
        

   
     
        app.run(debug=True)
    #o app.fy for o arquivo principal ele inici o server