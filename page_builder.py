from agents.base import BaseAgent

class PageBuilderAgent(BaseAgent):
    def act(self, memory):
        if (
            memory.exists("questions")
            and memory.exists("content_blocks")
            and not memory.exists("pages")
        ):
            prompt = f"""
            Using:
            Questions: {memory.get("questions")}
            Content Blocks: {memory.get("content_blocks")}

            Generate STRICT JSON for:
            1. faq.json (minimum 5 Q&A)
            2. product_page.json
            3. comparison_page.json

            Comparison must include fictional Product B
            (name, ingredients, benefits, price).

            Return JSON in this structure:
            {{
              "faq.json": {{ ... }},
              "product_page.json": {{ ... }},
              "comparison_page.json": {{ ... }}
            }}
            """
            pages = self.llm.generate(prompt)
            memory.set("pages", pages)
            memory.post_message(self.name, "All pages generated as JSON")
