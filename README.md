# Multi-Agent Content Generation System

This project implements a **true multi-agent architecture** for automated product content generation using an agentic design pattern.

Independent agents collaborate via shared memory and are dynamically coordinated through an orchestration layer to generate structured, machine-readable content pages from limited product data. The system avoids static control flow and demonstrates agent autonomy, modularity, and extensibility.

---

##  System Workflow 

1. Product data is parsed into an internal representation  
2. User questions are generated and categorized  
3. Reusable content blocks are created  
4. Templates are applied to assemble content pages  
5. Final outputs are produced as structured JSON  

All steps are executed by autonomous agents that decide when to act based on shared system state.

---

## 📁 Repository Structure
agentic-content-generation-system/
- ├── agents/
- │   ├── base.py
- │   ├── data_parser.py
- │   ├── question_generator.py
- │   ├── content_block_agent.py
- │   └── page_builder.py
- ├── core/
- │   ├── memory.py
- │   └── orchestrator.py
- ├── llm/
- │   └── client.py
- ├── templates/
- │   ├── faq_template.py
- │   ├── product_template.py
- │   └── comparison_template.py
- ├── docs/
- │   └── projectdocumentation.md
- ├── outputs/
- │   ├── faq.json
- │   ├── product_page.json
- │   └── comparison_page.json
- ├── main.py
- ├── requirements.txt
- └── README.md

> Detailed system architecture is given in productdocumentation.md.

> The project runs in **mock LLM mode by default**, so no API keys or paid services are required.

---

## 🖥 System Requirements

- Python 3.9 or later  
- Windows / macOS / Linux  
- Minimal memory requirements  
- Internet connection not required (mock mode)

Optional:
- OpenAI / Gemini API access (for real LLM mode)

---

## ▶️ How to Run

```bash
python main.py
