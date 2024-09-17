from src.json_reader import JSONReader
from src.save_results import OutputHandler
from src.manager import AnalysisManager
from src.config import RAW_DATA_PATH
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dynamics data from the frontend
@app.route('/analyze', methods=['POST'])
def analyze_note():
    # Receive information from the frontend
    data = request.get_json()
    
    # Verify medical note
    if not data or 'medical_note' not in data:
        return jsonify({"error": "No medical note provided"}), 400
    
    # Process medical note
    manager = AnalysisManager()
    medical_records = [{'medical_note': data['medical_note']}]
    results = manager.analyze_records(medical_records)
    
    # Return the results
    return jsonify(results), 200

if __name__ == '__main__':
    #Debug mode
    app.run(debug=True, host='0.0.0.0', port=5000)

