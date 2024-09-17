import csv
from typing import List, Dict

class CSVReader:
    @staticmethod
    def read_csv_to_records(file_path: str) -> List[Dict[str, str]]:
        try:
            with open(file_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
                reader = csv.DictReader(csvfile)
                return [
                    {
                        'medical_note': row['medical_note'],
                        'diagnose': row['diagnose']
                    }
                    for row in reader
                ]
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return []
        except csv.Error as e:
            print(f"Error reading CSV file: {e}")
            return []