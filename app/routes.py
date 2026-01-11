from flask import Blueprint, request, jsonify, current_app

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "username missing"}), 400
    
    if request.remote_addr == "127.0.0.1":
        return jsonify({"error": "Too many attempts"}), 429

    current_app.logger.info(
    f"Login attempt | user={username} | ip={request.remote_addr}"
)
    return jsonify({"status": "success", "user": username})

@auth.route("/loginrebase")
def login_rebase_demo():
    current_app.logger.debug("Login rebase demo endpoint hit")
    return "login demo"

