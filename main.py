from manager import AnalysisManager
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Dynamics data from the frontend
@app.route('/analyze', methods=['POST'])
def analyze_note():
    # Receive information from the frontend
    data = request.get_json()
    
    # Verify medical note
    if not data or 'medical_note' not in data:
        return jsonify({"error": "No medical note provided"}), 400
    
    if not data['medical_note'].strip():
        return jsonify({'error': 'Medical note is empty'}), 400
    
    #Tiempo de procesamiento
    start_time = time.time()
    
    # Process medical note
    manager = AnalysisManager()
    medical_records = [{'medical_note': data['medical_note']}]
    
    try:
        results = manager.analyze_records(medical_records)
        end_time = time.time()
        processing_time= end_time - start_time #Tiempo que se demora
        if not results or results == 'Invalid error':
            return jsonify({'error':'Analysis failed or invalid record', 'processing Time': f'{processing_time:.2f} seconds'}), 500
        
        return jsonify({'results': results, 'processing Time: ': f'{processing_time:.2f} seconds'}), 200
    except Exception as e:
        return jsonify({"error":str(e)}), 500

if __name__ == '__main__':
    #Debug mode
    app.run(debug=True, host='0.0.0.0', port=5000)

