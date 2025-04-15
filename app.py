from flask import Flask
from flask_cors import CORS
from controllers.tile_controller import tile_blueprint
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)
CORS(app)

# Registra o Blueprint que contém as rotas do tile
app.register_blueprint(tile_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
