from llm.client import LLMClient
from core.memory import SharedMemory
from core.orchestrator import Orchestrator

from agents.data_parser import DataParserAgent
from agents.question_generator import QuestionGeneratorAgent
from agents.content_block_agent import ContentBlockAgent
from agents.page_builder import PageBuilderAgent

llm = LLMClient(mock=True)

memory = SharedMemory()

agents = [
    DataParserAgent("DataParserAgent", llm),
    QuestionGeneratorAgent("QuestionGeneratorAgent", llm),
    ContentBlockAgent("ContentBlockAgent", llm),
    PageBuilderAgent("PageBuilderAgent", llm)
]

orchestrator = Orchestrator(agents)
orchestrator.run(memory)

print("\nFINAL GENERATED PAGES:\n")
pages = memory.get("pages")


print("\nAGENT EXECUTION LOG:\n")
for msg in memory.messages:
    print(msg)


import json
import os

os.makedirs("outputs", exist_ok=True)

pages = json.loads(memory.get("pages"))


with open("outputs/faq.json", "w", encoding="utf-8") as f:
    json.dump(pages["faq.json"], f, indent=2, ensure_ascii=False)

with open("outputs/product_page.json", "w", encoding="utf-8") as f:
    json.dump(pages["product_page.json"], f, indent=2, ensure_ascii=False)

with open("outputs/comparison_page.json", "w", encoding="utf-8") as f:
    json.dump(pages["comparison_page.json"], f, indent=2, ensure_ascii=False)

print("\nJSON files written to /outputs folder")
