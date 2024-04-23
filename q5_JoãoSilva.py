from flask import Flask, request, jsonify
import hashlib
import mysql.connector

# Inicialização do Flask
app = Flask(__name__)

# Conexão com o banco de dados
def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="seu_usuario",
            passwd="sua_senha",
            database="seu_banco_de_dados"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: '{err}'")
        return None

# Função para executar a query SQL e retornar os resultados
def execute_sql_query(query, args=None, query_type="fetch"):
    connection = create_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, args)
        if query_type == "fetch":
            result = cursor.fetchall()
            connection.close()
            return result
        else:
            connection.commit()
            connection.close()
            return cursor.lastrowid
    except mysql.connector.Error as err:
        print(f"Error: '{err}'")
        connection.close()
        return None

# Função de hash para senhas
hash_password = lambda password: hashlib.sha256(password.encode()).hexdigest()

# Rota de registro de usuário
@app.route('/register', methods=['POST'])
def register_user():
    name = request.json.get('name')
    country = request.json.get('country')
    id_console = request.json.get('id_console')
    password = request.json.get('password')

    hashed_password = hash_password(password)  # Criptografa a senha antes de armazenar
    insert_query = "INSERT INTO USERS (name, country, id_console, password) VALUES (%s, %s, %s, %s)"
    user_id = execute_sql_query(insert_query, (name, country, id_console, hashed_password), "insert")

    return jsonify({"user_id": user_id}), 201

# Rota de autenticação de usuário
@app.route('/login', methods=['POST'])
def authenticate_user():
    name = request.json.get('name')
    password = request.json.get('password')
    hashed_password = hash_password(password)

    select_query = "SELECT id, password FROM USERS WHERE name = %s"
    user = execute_sql_query(select_query, (name,), "fetch")

    if user and user[0]['password'] == hashed_password:
        return jsonify({"message": "Authentication successful", "user_id": user[0]['id']}), 200
    else:
        return jsonify({"message": "Authentication failed"}), 401

if __name__ == '__main__':
    app.run(debug=True)
