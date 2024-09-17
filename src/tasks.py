from crewai import Task, Agent

class AnalysisTask:
    @staticmethod
    def create_task(medical_note: str, diagnose: str, agent: Agent) -> Task:
        return Task(
            description=f"""Analyze the following medical note and diagnosis for inconsistencies in terminology, grammar, and vocabulary. Generate a concise report highlighting any issues found.

Medical Note: {medical_note}

Focus on:
1. Semantic consistency
2. Syntactic correctness
3. Lexical appropriateness
4. Terminology accuracy
5. Grammar and punctuation
6. Vocabulary suitability""",
            agent=agent,
            expected_output="A concise report of semantic, syntactic, lexical, terminology, grammar, and vocabulary inconsistencies found."
        )