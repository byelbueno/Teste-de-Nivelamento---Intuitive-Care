from flask import Flask, request, jsonify
from flask_cors import CORS 
import psycopg2

db_config = {
    'host': 'localhost',
    'port': '5433',
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '1234'
}

app = Flask(__name__)
CORS(app) 

@app.route('/buscar-operadoras', methods=['GET'])
def buscar_operadoras():
    termo = request.args.get('termo', '').strip()
    print(f"Recebido termo de busca: {termo}")
    if not termo:
        return jsonify({'error': 'O termo de busca não foi fornecido'}), 400
    
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        
        query = """
            SELECT razao_social, nome_fantasia, modalidade, cidade, uf 
            FROM operadoras_ans
            WHERE razao_social ILIKE %s OR nome_fantasia ILIKE %s
            LIMIT 10;
        """
        cursor.execute(query, (f'%{termo}%', f'%{termo}%'))
        resultados = cursor.fetchall()
        print(f"Resultados encontrados: {resultados}") 
        
        operadoras = [
            {
                'razao_social': row[0],
                'nome_fantasia': row[1],
                'modalidade': row[2],
                'cidade': row[3],
                'uf': row[4]
            }
            for row in resultados
        ]
        
        cursor.close()
        conn.close()
        
        return jsonify(operadoras)
    
    except Exception as e:
        print(f"Erro no servidor: {str(e)}") 
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
