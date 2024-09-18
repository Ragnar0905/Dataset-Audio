from crewai import Task, Agent

class AnalysisTask:
    @staticmethod
    def create_task(medical_note: str, agent: Agent) -> Task:
        return Task(
            description=f"""Analyze the following medical note and diagnosis for inconsistencies in terminology, grammar, and vocabulary. 
                            Generate a concise report highlighting any issues found.
                            Medical Note: {medical_note}""",
                        agent=agent,
                        expected_output="A concise report of semantic, syntactic, lexical, terminology, grammar, and vocabulary inconsistencies found."
        )