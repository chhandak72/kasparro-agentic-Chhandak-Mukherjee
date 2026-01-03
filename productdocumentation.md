# Multi-Agent Content Generation System

This project implements a **true multi-agent architecture** for automated product content generation using an agentic design pattern.

Independent agents collaborate via shared memory and are dynamically coordinated through an orchestration layer to generate structured, machine-readable content pages from limited product data. The system avoids static control flow and demonstrates agent autonomy, modularity, and extensibility.

---

##  Key Features

- True multi-agent system (not a static pipeline)
- Autonomous agents with clearly separated responsibilities
- Dynamic orchestration without hard-coded execution order
- Shared memory (blackboard pattern) for indirect agent communication
- Reusable content logic blocks
- Template-based page generation
- Mock LLM mode for deterministic, quota-free execution
- Clean JSON outputs suitable for downstream systems

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

