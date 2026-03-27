from flask import Flask, jsonify, request
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)
 
@app.route('/pacientes', methods=['GET'])
def get_pacientes():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        

        cursor.execute("SELECT id, nombre, edad FROM pacientes;")
        rows = cursor.fetchall()

        pacientes = []
        for row in rows:
            p_id = row[0]

            cursor.execute("SELECT id, fecha, motivo FROM citas WHERE paciente_id = ?", (p_id,))
            citas_rows = cursor.fetchall()
            
            citas = [{"id": c[0], "fecha": c[1], "motivo": c[2]} for c in citas_rows]

            pacientes.append({
                "id": p_id,
                "nombre": row[1],
                "edad": row[2],
                "citas": citas
            })

        cursor.close()
        conn.close()
        return jsonify({"ok": True, "data": pacientes}), 200
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

@app.route('/pacientes', methods=['POST'])
def create_paciente():
    try:
        data = request.json
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pacientes (nombre, edad) VALUES (?, ?)", (data['nombre'], data['edad']))
        conn.commit()
        conn.close()
        return jsonify({"ok": True, "msg": "Paciente creado"}), 201
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

@app.route('/pacientes/<int:id>', methods=['DELETE'])
def delete_paciente(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()


        cursor.execute("DELETE FROM citas WHERE paciente_id = ?", (id,))
        

        cursor.execute("DELETE FROM pacientes WHERE id = ?", (id,))
        
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"ok": True, "msg": "Paciente y sus citas eliminados"}), 200

    except Exception as e:

        print(f"Error en el servidor: {str(e)}")
        return jsonify({"ok": False, "error": str(e)}), 500

@app.route('/citas', methods=['POST'])
def create_cita():
    try:
        data = request.json
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO citas (paciente_id, fecha, motivo) VALUES (?, ?, ?)", 
                       (data['paciente_id'], data['fecha'], data['motivo']))
        conn.commit()
        conn.close()
        return jsonify({"ok": True, "msg": "Cita creada"}), 201
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

@app.route('/citas/<int:id>', methods=['DELETE'])
def delete_cita(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM citas WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return jsonify({"ok": True, "msg": "Cita eliminada"}), 200
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)