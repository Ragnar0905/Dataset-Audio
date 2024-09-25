from src.agents import MedicalNoteAnalyzer
from typing import List, Dict

class AnalysisManager:  
    def __init__(self):
        self.analyzer = MedicalNoteAnalyzer()
        
    def analyze_records(self, records: List[Dict[str, str]]) -> List[str]:
        results = []
        
        #Iterar sobre los resigtros y procesar cada nota medica
        for i, record in enumerate(records, 1):
            print(f"Analyzing record {i} of {len(records)}...")
            
            #Verificar que sea un registro valido y tiene "medical_note"
            if not isinstance(record, dict) or 'medical_note' not in record:
                print(f"Error: 'record' is not a valid dictionary or 'medical_note' key is missing.")
                continue
            
            medical_note = record['medical_note']
            # Ejecuta el analisis en Ollama
            result = self.analyzer.run_model(medical_note)
            results.append(result)
                
        return results

