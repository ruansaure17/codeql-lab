from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/user')
def buscar_usuario():

    user_id = request.args.get("id")

    conn = sqlite3.connect("banco.db")

    cursor = conn.cursor()

    cursor.execute(
        f"SELECT * FROM users WHERE id = {user_id}"
    )

    return str(cursor.fetchone())