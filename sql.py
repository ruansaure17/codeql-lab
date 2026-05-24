import sqlite3

def buscar_usuario_vulneravel(user_id):

    conn = sqlite3.connect('banco.db')

    cursor = conn.cursor()

    # ⚠️ SQL INJECTION: nunca faça isso em produção!
    cursor.execute(f"SELECT * FROM users WHERE id={user_id}")

    return cursor.fetchone()