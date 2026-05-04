from flask import Flask, request, jsonify

app = Flask(__name__)

complaints = []

@app.route("/api/complaints", methods=["POST"])
def create_complaint():
    data = request.json
    complaints.append(data)
    return {"message": "Complaint registered"}

@app.route("/api/complaints", methods=["GET"])
def get_complaints():
    return jsonify(complaints)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
    