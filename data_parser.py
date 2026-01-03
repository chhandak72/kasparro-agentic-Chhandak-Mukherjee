from agents.base import BaseAgent

class DataParserAgent(BaseAgent):
    def act(self, memory):
        if not memory.exists("product"):
            product = {
                "name": "GlowBoost Vitamin C Serum",
                "concentration": "10%",
                "skin_type": ["Oily", "Combination"],
                "ingredients": ["Vitamin C", "Hyaluronic Acid"],
                "benefits": ["Brightening", "Fades dark spots"],
                "usage": "Apply 2–3 drops in the morning before sunscreen",
                "side_effects": "Mild tingling for sensitive skin",
                "price": "₹699"
            }
            memory.set("product", product)
            memory.post_message(self.name, "Product data parsed into internal model")
