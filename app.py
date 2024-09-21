# app.py
from flask import Flask, request, jsonify
from simulator import simulate_material_property

app = Flask(__name__)

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    composition = data.get('composition')
    temperature = data.get('temperature')
    
    if not composition or not temperature:
        return jsonify({"error": "Missing composition or temperature"}), 400
    
    result = simulate_material_property(composition, temperature)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
