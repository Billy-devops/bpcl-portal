from flask import Flask, request, jsonify
import mysql.connector
import time

app = Flask(__name__)

# wait for DB (important)
time.sleep(10)

conn = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="bpcl"
)

cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS complaints (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dealer VARCHAR(255),
    message TEXT
)
""")

@app.route("/complaints", methods=["POST"])
def create_complaint():
    data = request.json
    dealer = data.get("dealer")
    message = data.get("message")

    cursor.execute(
        "INSERT INTO complaints (dealer, message) VALUES (%s, %s)",
        (dealer, message)
    )
    conn.commit()

    return jsonify({"message": "Complaint saved in DB"})

@app.route("/complaints", methods=["GET"])
def get_complaints():
    cursor.execute("SELECT * FROM complaints")
    rows = cursor.fetchall()

    result = []
    for r in rows:
        result.append({
            "id": r[0],
            "dealer": r[1],
            "message": r[2]
        })

    return jsonify(result)

app.run(host="0.0.0.0", port=5000)
