from flask import Flask, request
import os
import subprocess

app = Flask(__name__)

@app.route('/ping')
def ping():
    host = request.args.get('host')

    

    subprocess.run(
    ["ping", "-c", "1", host],
    check=True
)

    return "Ping executado"

if __name__ == '__main__':
    app.run(debug=True)