from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"msg": "DevSecOps AI Lab running"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "admin":
        return jsonify({"msg": "login success"})
    return jsonify({"msg": "login failed"}), 401

@app.route("/data")
def data():
    return jsonify({"data": "some secure data"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

