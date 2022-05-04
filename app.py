import socket
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    output = f"Hostname: {socket.gethostname()}<br/>"
    for k, v in request.headers:
        output += f"{k}: {v}<br/>"
    return output

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)