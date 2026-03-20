from flask import Flask, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)

@app.route('/pacientes', methods=['GET'])
def get_pacientes():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pacientes;")
        rows = cursor.fetchall()

        pacientes = []
        for row in rows:
            pacientes.append({
                "id": row[0],
                "nombre": row[1],
                "edad": row[2]
            })

        cursor.close()
        conn.close()

        return jsonify({
            "ok": True,
            "data": pacientes
        }), 200

    except Exception as e:
        return jsonify({
            "ok": False,
            "error": str(e)
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)