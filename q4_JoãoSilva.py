# Função para gerar código SQL para INNER JOIN
generate_inner_join_sql = lambda tables, join_condition: f"INNER JOIN ".join(tables) + f" ON {join_condition}"

# Função para gerar comando SELECT com os atributos fornecidos
generate_select_sql = lambda select_fields, table, additional_clauses="": f"SELECT {', '.join(select_fields)} FROM {table} {additional_clauses}".strip()

# Exemplo de uso das funções acima para gerar uma consulta SQL

# Digamos que queremos unir as tabelas GAMES, VIDEOGAMES e COMPANY onde as condições se aplicam
tables_to_join = ["GAMES", "VIDEOGAMES", "COMPANY"]
join_condition = "GAMES.id_console = VIDEOGAMES.id_console AND VIDEOGAMES.id_company = COMPANY.id_company"

# Atributos que desejamos selecionar
attributes_to_select = ["GAMES.title", "GAMES.genre", "COMPANY.name"]

# Gerar a consulta INNER JOIN
inner_join_query = generate_inner_join_sql(tables_to_join, join_condition)

# Gerar a consulta SELECT final, incluindo a parte INNER JOIN
final_select_query = generate_select_sql(attributes_to_select, inner_join_query)

print(final_select_query)  # Isto imprimirá a consulta SQL final que pode ser usada para executar no banco de dados.


# Gerar a condição INNER JOIN para nossa consulta específica
specific_join_condition = "GAMES.id_console = VIDEOGAMES.id_console AND VIDEOGAMES.id_company = COMPANY.id_company"

# Atributos que desejamos selecionar para essa consulta específica
specific_attributes_to_select = ["GAMES.title", "COUNT(COMPANY.name)"]

# Usamos uma cláusula adicional para contar os jogos por empresa e agrupá-los
additional_clauses = "GROUP BY GAMES.title HAVING COUNT(COMPANY.name) > 1"

# Gerar a consulta INNER JOIN específica
specific_inner_join_query = generate_inner_join_sql(tables_to_join, specific_join_condition)

# Gerar a consulta SELECT final específica
specific_final_select_query = generate_select_sql(specific_attributes_to_select, specific_inner_join_query, additional_clauses)

print(specific_final_select_query)  # Imprime a consulta SQL final específica.
