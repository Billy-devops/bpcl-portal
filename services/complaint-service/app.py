from flask import Flask, request, jsonify
import mysql.connector
import time

app = Flask(__name__)

# DB CONNECTION (RETRY LOGIC)
def get_db_connection():
    retries = 15
    while retries > 0:
        try:
            conn = mysql.connector.connect(
                host="bpcl-mysql",
                user="root",
                password="root",
                database="bpcl"
            )
            print("DB connected ✔")
            return conn
        except Exception as e:
            print("DB not ready:", e)
            time.sleep(3)
            retries -= 1

    raise Exception("Database connection failed")


# AUTO TABLE CREATE
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            message TEXT
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

init_db()


# CREATE COMPLAINT
@app.route('/complaints', methods=['POST'])
def create_complaint():
    data = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO complaints (name, email, message) VALUES (%s, %s, %s)",
        (data["name"], data["email"], data["message"])
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Saved ✔"})


# GET COMPLAINTS
@app.route('/complaints', methods=['GET'])
def get_complaints():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM complaints")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(rows)


# HEALTH CHECK (IMPORTANT)
@app.route('/health', methods=['GET'])
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"status": "UP ✔ DB Connected"})
    except:
        return jsonify({"status": "DOWN ❌ DB Issue"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    