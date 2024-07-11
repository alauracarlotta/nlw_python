from flask import jsonify, Blueprint # jsonify => para transformar as nossas respostas para o usuário / Blueprint => Ajuda a dar nomes bacanas para as nossas rotas e o que ela é.

trips_routes_bp = Blueprint("trip_routes", __name__) # bp de 'blueprint'

@trips_routes_bp.route('/trips', methods=["POST"]) # tem uma única função de POST
def create_trip(): # criar viagem
    return jsonify({ "ola": "mundo" }), 200