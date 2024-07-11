from flask import Flask
from src.main.routes.trips_routes import trips_routes_bp # cadastrando no nosso servidor a nossa rota criada de trip

app = Flask(__name__) # ainda não criamos as rotas

app.register_blueprint(trips_routes_bp)
