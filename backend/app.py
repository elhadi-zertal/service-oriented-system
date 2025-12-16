import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host = os.getenv('DB_HOST', 'postgres'),
        database = os.getenv('DB_NAME', 'postgres'),
        user = os.getenv('DB_USER', 'postgres'),
        password = os.getenv('DB_PASSWORD', 'postgres')
    )


@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

@app.route('/logs', methods=['GET'])
def get_logs():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, service_name, log_message, created_at
        FROM system_logs
        ORDER BY created_at DESC
    """)

    logs = []
    for row in cur.fetchall():
        logs.append(
            {
            'id': row[0],
            'service': row[1],
            'message': row[2],
            'timestamp': row[3].isoformat()
            }
        )

    cur.close()
    conn.close()
    return jsonify({'logs': logs, 'count': len(logs)})

