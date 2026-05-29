from flask import Flask, request

app = Flask(__name__)


@app.route("/read")
def read_file():

    filename = request.args.get("file")

    # ⚠️ Path Traversal
    with open(f"files/{filename}", "r") as f:
        return f.read()
