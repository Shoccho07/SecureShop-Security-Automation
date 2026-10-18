"""SecureShop sample application for DevSecOps training."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Reject request bodies larger than 16 KiB.
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.post("/greet")
def greet():
    if not request.is_json:
        return jsonify({
            "error": "Content-Type must be application/json"
        }), 415

    payload = request.get_json(silent=True)

    if not isinstance(payload, dict):
        return jsonify({
            "error": "Request body must be a JSON object"
        }), 400

    name = payload.get("name")

    if not isinstance(name, str):
        return jsonify({
            "error": "'name' must be a string"
        }), 400

    name = name.strip()

    if not name or len(name) > 80:
        return jsonify({
            "error": "'name' must contain 1 to 80 characters"
        }), 400

    return jsonify({"message": f"Hello, {name}!"}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
