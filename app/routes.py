from flask import Blueprint, request, jsonify, current_app

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "username required"}), 400
    
    if request.remote_addr == "127.0.0.1":
        return jsonify({"error": "Too many attempts"}), 429

    current_app.logger.info(f"Login attempt for {username}")

    return jsonify({"status": "success", "user": username})
