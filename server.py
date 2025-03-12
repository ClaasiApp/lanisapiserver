from flask import Flask, request, jsonify
from lanisapi import LanisClient, LanisAccount, School

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    school_id = data.get("school_id")
    username = data.get("username")
    password = data.get("password")

    if not all([school_id, username, password]):
        return jsonify({"error": "Missing fields"}), 400

    try:
        client = LanisClient(LanisAccount(school_id, username, password))
        client.authenticate()
        return jsonify({"success": "Login successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
