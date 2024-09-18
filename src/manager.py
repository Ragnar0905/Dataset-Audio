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
            
            try: 
                result = self.analyzer.run_model(record['medical_note'])
                results.append(result)
            except Exception as e:
                print(f"Error processing record {i}: {str(e)}")
                results.append(f"Error in record {i}")
                
        return results

