from flask import Flask, jsonify, request

app = Flask(__name__)

# 🔥 Sample data (baad me DB se connect karenge)
dealers = [
    {"code": "120344", "name": "MEENAKSHI ENTERPRISES", "location": "Bathinda"},
    {"code": "120345", "name": "NARSHI RAM AGGARWAL", "location": "Rampuraphul"},
    {"code": "120346", "name": "SITA RAM AGGARWAL", "location": "Bathinda"},
]

@app.route("/api/dealers", methods=["GET"])
def get_dealers():
    search = request.args.get("search", "")
    filtered = [d for d in dealers if search.lower() in d["name"].lower()]
    return jsonify(filtered)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)