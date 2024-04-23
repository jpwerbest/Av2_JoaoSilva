import mysql.connector

# Conexão com o banco de dados
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except mysql.connector.Error as err:
        print(f"Error: '{err}'")

    return connection

# Executar uma query no banco de dados
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except mysql.connector.Error as err:
        print(f"Error: '{err}'")

# Código para criar as tabelas (exemplo para a tabela USERS)
create_users_table = """
CREATE TABLE IF NOT EXISTS USERS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    country VARCHAR(50),
    id_console INT
);
"""

# Estabeleça a conexão usando suas credenciais reais
connection = create_server_connection("localhost", "seu_usuario", "sua_senha")

# Crie a tabela USERS (repita para as outras tabelas)
execute_query(connection, create_users_table)

# Funções para inserir, remover e consultar registros seriam implementadas de forma semelhante
