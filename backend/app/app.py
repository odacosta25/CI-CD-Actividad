from flask import Flask, jsonify
import os
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "¡Bienvenido a la API Flask!"

@app.route('/data')
def get_data():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST')
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM data;")
    result = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)