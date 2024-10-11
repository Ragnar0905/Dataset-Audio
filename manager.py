from agents import MedicalNoteAnalyzer
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor

class AnalysisManager:  
    def __init__(self):
        self.analyzer = MedicalNoteAnalyzer()
        
    def analyze_records(self, records: List[Dict[str, str]]) -> List[str]:
        results = []
        
        with ThreadPoolExecutor() as excecutor:
            futures = [excecutor.submit(self.analyze_record, record) for record in records]
            
            for future in futures:
                result = future.result()
                results.append(result)
    
    def analyze_record(self, record):
        
    #Verificar que sea un registro valido y tiene "medical_note"
        if not isinstance(record, dict) or 'medical_note' not in record:
            print(f"Error: 'record' is not a valid dictionary or 'medical_note' key is missing.")
            return 'Invalid error'
        
        medical_note = record['medical_note']
        # Ejecuta el analisis en Ollama
        result = self.analyzer.run_model(medical_note) #Realiza el analisis en Ollama
        
        if not result:
            print('El resultado del análisis esta vacío o es nulo')
            
        return result

