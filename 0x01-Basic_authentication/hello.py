from flask import Flask, jsonify
from os import getenv

app = Flask(__name__)

auth = None
AUTH_TYPE = getenv("AUTH_TYPE")

if AUTH_TYPE == auth:
    from api.v1.auth.auth import Auth
    auth = Auth()
elif AUTH_TYPE == basic_auth:
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth


@app.route('/')
def hello():
    return "<p>Hello, World!</p>"


@app.errorhandler(401)
def unauthorized(error) -> str:
    return jsonify({"error": "Unauthorized"})


if __name__ == "__main__":
    app.run()
