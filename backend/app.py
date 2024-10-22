from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Connect to the PostgreSQL database
def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="mydatabase",
        user="myuser",
        password="mypassword"
    )
    return conn

@app.route('/api', methods=['GET'])
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    version = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({"PostgreSQL Version": version})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
