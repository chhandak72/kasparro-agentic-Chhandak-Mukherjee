# llm/client.py
import json

class LLMClient:
    """
    Mock LLM client for offline / quota-free execution.
    This preserves agentic architecture while avoiding external API calls.
    """

    def __init__(self, mock=True):
        self.mock = mock

    def generate(self, prompt: str) -> str:
        return self._mock_response(prompt)

    def _mock_response(self, prompt: str) -> str:
        # Question generation agent
        if "Generate at least 15 user questions" in prompt:
            return json.dumps({
                "Informational": [
                    "What is GlowBoost Vitamin C Serum?",
                    "What does 10% Vitamin C mean?",
                    "Who is this serum suitable for?"
                ],
                "Safety": [
                    "Is GlowBoost safe for sensitive skin?",
                    "Are there any side effects?"
                ],
                "Usage": [
                    "How should GlowBoost be applied?",
                    "When should it be used?",
                    "Can it be used daily?"
                ],
                "Purchase": [
                    "What is the price of GlowBoost?",
                    "Is GlowBoost worth the price?"
                ],
                "Comparison": [
                    "How does GlowBoost compare to other Vitamin C serums?",
                    "How is GlowBoost different from Product B?"
                ]
            }, indent=2)

        # Content blocks agent
        if "Create reusable content logic blocks" in prompt:
            return json.dumps({
                "description_block": "GlowBoost is a 10% Vitamin C serum designed for oily and combination skin.",
                "benefits_block": [
                    "Brightens skin tone",
                    "Fades dark spots"
                ],
                "usage_block": "Apply 2–3 drops in the morning before sunscreen.",
                "safety_block": "Mild tingling may occur for sensitive skin.",
                "pricing_block": "₹699"
            }, indent=2)

        # Page builder agent
        if "Generate STRICT JSON for" in prompt:
            return json.dumps({
                "faq.json": {
                    "faqs": [
                        {
                            "question": "What is GlowBoost Vitamin C Serum?",
                            "answer": "GlowBoost is a 10% Vitamin C serum formulated for oily and combination skin."
                        },
                        {
                            "question": "How do I use GlowBoost?",
                            "answer": "Apply 2–3 drops in the morning before sunscreen."
                        },
                        {
                            "question": "Is it safe for sensitive skin?",
                            "answer": "Mild tingling may occur for sensitive skin."
                        },
                        {
                            "question": "What are the benefits?",
                            "answer": "It brightens skin and helps fade dark spots."
                        },
                        {
                            "question": "What is the price?",
                            "answer": "GlowBoost is priced at ₹699."
                        }
                    ]
                },
                "product_page.json": {
                    "title": "GlowBoost Vitamin C Serum",
                    "description": "A 10% Vitamin C serum designed for oily and combination skin.",
                    "benefits": [
                        "Brightening",
                        "Fades dark spots"
                    ],
                    "usage": "Apply 2–3 drops in the morning before sunscreen.",
                    "price": "₹699"
                },
                "comparison_page.json": {
                    "product_a": {
                        "name": "GlowBoost Vitamin C Serum",
                        "price": "₹699"
                    },
                    "product_b": {
                        "name": "RadianceX Serum",
                        "ingredients": ["Vitamin C"],
                        "benefits": ["Glow enhancement"],
                        "price": "₹799"
                    },
                    "comparison": "GlowBoost is more affordable and includes Hyaluronic Acid for hydration."
                }
            }, indent=2)

        return "{}"
