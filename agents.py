import subprocess
from crewai import Agent
import time

class MedicalNoteAnalyzer(Agent):
    def __init__(self):
        super().__init__(
            role='Medical Note Analyzer',
            goal = "Analyze medical notes for semantic, syntactic, and lexical consistency.",
            backstory="You're an expert in medical terminology and natural language processing, specializing in auditing medical documentation, you only give answers in Spanish.",
            max_iter=1, #Reduce el tiempo de  iteraciones
            max_execution_time=1, # Limita el tiempo de ejecucion para acelerar el procesamiento
            verbose= True, # Habilitar logs para entender el proceso
            memory =True,
            max_retry_limit= 2,
            respect_context_window=True
            )
        self.max_iter = 10  # Configura el número máximo de iteraciones
        self.max_execution_time = 30  # Tiempo máximo para la ejecución
        self.verbose = True  #Detalles de en la ejecución 
        
        self.pull_model()
        
    def pull_model(self):
        try:
            # Llamamos a ollama para asegurarnos de que el modelo está disponible
            subprocess.run(['ollama', 'pull', 'medllama2'], check=True, capture_output=True, text=True, encoding='utf-8')
            print("Model medllama2 initialized and ready")
        except subprocess.CalledProcessError as e:
            print(f"Error pulling the model: {e.stderr}")
            raise RuntimeError("Ollama Model initialization failed")
        
    def run_model(self, medical_note):
        
        try:
            start_time = time.time()
            prompt = f"Analiza esta nota médica y encuentra posibles errores gramaticales: \"{medical_note}\""
            print(f"Analizando la nota médica: {prompt}")
            command = [
                'ollama', 'run', 'medllama2',
                prompt]
            result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
            
            end_time = time.time()
            print(f"Time taken for model analysis: {end_time - start_time:.2f} seconds")
            
            if result.returncode == 0:
                return result.stdout
            else:
                print(f'Error en el analisis {result.stderr}')
                return 'Analisis de la nota medica erroneo'
            
        except Exception as e:
            print(f"Error running the model: {e}")
            return "Medical note analysis failed"