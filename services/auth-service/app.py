from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/auth", methods=["POST"])
def login():
    email = request.json.get("email")

    if email.endswith("@bharatpetroleum.in"):
        return {"status": "allowed"}
    else:
        return {"status": "denied"}

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
    