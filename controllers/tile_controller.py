from flask import Blueprint, send_file, request
from models.tile_model import get_mvt_tile
import io

# Cria um Blueprint para os endpoints de tile
tile_blueprint = Blueprint('tile', __name__)

@tile_blueprint.route('/tiles/<int:z>/<int:x>/<int:y>.mvt', methods=['GET'])
def serve_mvt_tile(z, x, y):
    """
    Controller para servir o tile MVT. Caso os parâmetros schema_name e table_name não sejam informados,
    usa os valores padrão 'anatel' e 'municipios_onde_tem_5g'.
    
    Exemplo de requisição:
      /tiles/1/2/1.mvt?schema_name=anatel&table_name=municipios_onde_tem_5g
    """
    schema_name = request.args.get("schema_name", "anatel")
    table_name = request.args.get("table_name", "municipios_onde_tem_5g")
    print(f"Request: z={z}, x={x}, y={y}, schema_name={schema_name}, table_name={table_name}")
    
    tile_data = get_mvt_tile(z, x, y, schema_name, table_name)
    
    if tile_data:
        # "View": Retorna o arquivo MVT para o cliente
        return send_file(
            io.BytesIO(tile_data),
            mimetype='application/x-protobuf',  # MIME para Mapbox Vector Tiles
            as_attachment=True,
            download_name=f"tile_{z}_{x}_{y}.mvt"
        )
    else:
        return "Tile não encontrado", 404
