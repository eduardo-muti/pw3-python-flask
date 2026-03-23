# importando o flask na aplicação
from flask import Flask, render_template

#carregando o flask em uma variavel
app = Flask(__name__, template_folder='views')
#a__name__ e uma variavel do python que tem o nome do bjeto atual

from controllers import routes
#enviando a variavel app (flask) para as rotas

routes.init_app(app)

#servidor web
if __name__ == '__main__':
    app.run(debug=True)
    #o app.fy for o arquivo principal ele inici o server