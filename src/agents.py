from crewai import Agent, Task
from langchain_community.chat_models import ollama
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL
import subprocess
import os
os.environ["OPENAI_API_KEY"] = "NA"

class MedicalNoteAnalyzer:
    def __init__(self):
        try:
            #self.model = ollama(model='llama3.1', base_url="http://localhost:11434")
            print('Ollama model initialized')
        except Exception as e:
            print(f"Error initializing Ollama model: {e}")
            print("Attempting to pull the model...")
            self.model = self.pull_model()
            
        self.agent = Agent(
            role='Medical Note Analyzer',
            goal='Analyze medical notes for semantic, syntactic, and lexical consistency',
            backstory="You're an expert in medical terminology and natural language processing, specializing in auditing medical documentation, you only give answers in spanish.",
            verbose=True,
            model_config={
            "model_name": "ollama",
            "model_path": "llama3.1",
            "base_url": "http://localhost:11434",
            }, # Use the appropriate Ollama model here
            )
        
    def pull_model(self):
        try:
            # Llamamos a ollama para asegurarnos de que el modelo está disponible
            result = subprocess.run(['ollama', 'pull', 'llama3.1'], check=True, capture_output=True, text=True, encoding='utf-8')
            print("Successfully pulled llama3 model")
            return 'llama3'
        except subprocess.CalledProcessError as e:
            print(f"Error pulling the model: {e.stderr}")
            print("Please make sure Ollama is installed and running.")
            return None
        
    def run_model(self, prompt):
        try:
            if isinstance(prompt, Task):
            # Extraemos el texto del atributo 'description'
                prompt_str = prompt.description
            elif isinstance(prompt, str):
                prompt_str = prompt
            else:
                raise ValueError(f"Expected a string or Task for the prompt, but got {type(prompt)}")
        
            command = ['ollama', 'run', 'llama3.1', prompt_str]
            print(f"Running command: {command}")
            result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')

            if result.returncode != 0:
                return result.stdout
            else:
                return f"Error: {result.stderr}, Command: {command}, Return code: {result.returncode}"
        except Exception as e:
            print(f"Error running the model: {e}")
            return f"Error during analysis: {e}"