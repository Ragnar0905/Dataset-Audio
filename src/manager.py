# from crewai import Crew
from src.agents import MedicalNoteAnalyzer
from src.tasks import AnalysisTask
from typing import List, Dict

class AnalysisManager:  
    def __init__(self):
        self.analyzer = MedicalNoteAnalyzer()
        
    def analyze_records(self, records: List[Dict[str, str]]) -> List[str]:
        results = []
        for i, record in enumerate(records, 1):
            print(f"Analyzing record {i} of {len(records)}...")
            
            if not isinstance(record, dict) or 'medical_note' not in record:
                print(f"Error: 'record' is not a valid dictionary or 'medical_note' key is missing.")
                continue
            task = AnalysisTask.create_task(
                medical_note=record['medical_note'],
                diagnose='',
                agent=self.analyzer.agent
            )
            
            result = self.analyzer.run_model(task)
            results.append(result)
        return results

