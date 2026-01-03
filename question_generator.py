from agents.base import BaseAgent

class QuestionGeneratorAgent(BaseAgent):
    def act(self, memory):
        if memory.exists("product") and not memory.exists("questions"):
            prompt = f"""
            Using ONLY the following product data:
            {memory.get("product")}

            Generate at least 15 user questions grouped into categories:
            - Informational
            - Safety
            - Usage
            - Purchase
            - Comparison

            Return STRICT JSON:
            {{
              "Informational": [...],
              "Safety": [...],
              "Usage": [...],
              "Purchase": [...],
              "Comparison": [...]
            }}
            """
            questions = self.llm.generate(prompt)
            memory.set("questions", questions)
            memory.post_message(self.name, "Categorized user questions generated")
