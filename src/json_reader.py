import json
from typing import List, Dict

class JSONReader:
    @staticmethod
    def read_json(file_path: str) -> List[Dict[str, str]]:
        try: 
            with open(file_path, 'r', encoding='utf-8') as jsonfile:
                data = json.load(jsonfile)
                return[
                    {
                        'medical_note': record['medical_note'],
                    }
                    for record in data
                ]
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return[]
        except json.JSONDecodeError as e:
            print(f"Error reading JSON file: {e}")
            return[]