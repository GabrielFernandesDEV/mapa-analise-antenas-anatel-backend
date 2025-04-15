import psycopg2
import os

def get_mvt_tile(z, x, y, schema_name, table_name):
    """
    Função para chamar a função gov.get_vector_tile no banco de dados,
    que gera o tile MVT a partir de z, x, y, schema_name e table_name.
    """
    conn = psycopg2.connect(
        host=os.getenv("DATABASE_HOST"),
        dbname=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        port=os.getenv("DATABASE_PORT"),
        password=os.getenv("DATABASE_PASSWORD")
    )
    
    query = """
        SELECT gov.get_vector_tile(
            z => %s,
            x => %s,
            y => %s,
            schema_name => %s,
            table_name => %s
        );
    """
    
    try:
        cur = conn.cursor()
        cur.execute(query, (z, x, y, schema_name, table_name))
        result = cur.fetchone()
        tile_data = result[0] if result and result[0] is not None else None
        cur.close()
        conn.close()
        return tile_data
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        return None
