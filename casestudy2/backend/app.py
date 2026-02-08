from flask import Flask, request, jsonify

app = Flask(__name__)

patients = []
patient_id = 1

@app.route('/api/patients', methods=['GET'])
def get_patients():
    return jsonify(patients), 200

@app.route('/api/patients', methods=['POST'])
def add_patient():
    global patient_id
    data = request.json

    if not data.get("name") or not data.get("age"):
        return jsonify({"error": "Invalid data"}), 400

    patient = {
        "id": patient_id,
        "name": data["name"],
        "age": data["age"],
        "gender": data["gender"],
        "contact": data["contact"],
        "disease": data["disease"],
        "doctor": data["doctor"]
    }
    patients.append(patient)
    patient_id += 1

    return jsonify(patient), 201

@app.route('/api/patients/<int:pid>', methods=['GET'])
def get_patient(pid):
    for p in patients:
        if p["id"] == pid:
            return jsonify(p), 200
    return jsonify({"error": "Patient not found"}), 404

@app.route('/api/patients/<int:pid>', methods=['PUT'])
def update_patient(pid):
    data = request.json
    for p in patients:
        if p["id"] == pid:
            p.update(data)
            return jsonify(p), 200
    return jsonify({"error": "Patient not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
