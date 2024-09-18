from crewai import Agent
from src.tasks import AnalysisTask
import subprocess
# import os
# os.environ["OPENAI_API_KEY"] = "NA"

class MedicalNoteAnalyzer:
    def __init__(self):
        try:
            result = subprocess.run(['ollama', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                print('Ollama model initialized')
            else:
                print('Ollama is not running or not installed')
        except Exception as e:
            print(f"Error initializing Ollama model: {e}")
            print("Attempting to pull the model...")
            self.model = self.pull_model()
        
        # Configuración del agente 
        self.agent = Agent(
            role='Medical Note Analyzer',
            goal='Analyze medical notes for semantic, syntactic, and lexical consistency',
            backstory="You're an expert in medical terminology and natural language processing, specializing in auditing medical documentation, you only give answers in spanish.",
            verbose=True 
            )
        
    def pull_model(self):
        try:
            # Llamamos a ollama para asegurarnos de que el modelo está disponible
            result = subprocess.run(['ollama', 'pull', 'llama3.1'], check=True, capture_output=True, text=True, encoding='utf-8')
            print("Successfully pulled llama3.1 model")
            return 'llama3.1'
        except subprocess.CalledProcessError as e:
            print(f"Error pulling the model: {e.stderr}")
            print("Please make sure Ollama is installed and running.")
            return None
        
    def run_model(self, prompt):
        try:
            task = AnalysisTask.create_task(
                medical_note=prompt,
                agent = self.agent
                )
            
            command = ['ollama', 'run', 'llama3.1', task.description]
            print(f"Running command: {command}")
            result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')

            if result.returncode == 0:
                return result.stdout
            else:
                return f"Error: {result.stderr}, Command: {command}, Return code: {result.returncode}"
        except Exception as e:
            print(f"Error running the model: {e}")
            return f"Error during analysis: {e}"