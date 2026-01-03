from agents.base import BaseAgent

class ContentBlockAgent(BaseAgent):
    def act(self, memory):
        if memory.exists("product") and not memory.exists("content_blocks"):
            prompt = f"""
            Using ONLY this product data:
            {memory.get("product")}

            Create reusable content logic blocks as JSON:
            - description_block
            - benefits_block
            - usage_block
            - safety_block
            - pricing_block

            These blocks must be reusable across pages.
            """
            blocks = self.llm.generate(prompt)
            memory.set("content_blocks", blocks)
            memory.post_message(self.name, "Reusable content logic blocks created")
