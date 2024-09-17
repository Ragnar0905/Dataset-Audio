import json
from src.manager import AnalysisManager
from typing import List, Dict

class OutputHandler:
    @staticmethod
    def save_results_json(results:List[Dict[str,str]], output_path: str):
        """
        Save the results in JSON path

        results --> List of results generate for AnalysisManager
        output_path --> Where de information is save
        """
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(results,file,ensure_ascii= False, ident=4)
        print(f'Results saved to {output_path}')

    @staticmethod
    def analyze_and_save_json(records: List[Dict[str,str]], output_path:str):
        manager = AnalysisManager()
        results = manager.analyze_records(records)
        OutputHandler.save_results_json(results, output_path)