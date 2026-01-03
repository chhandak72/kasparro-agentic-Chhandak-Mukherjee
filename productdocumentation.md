## 🧠 System Design Overview

This project is designed as a **true multi-agent system** following an **agentic architecture**, rather than a static or sequential workflow.

The system consists of multiple **independent, autonomous agents** that collaborate to generate structured product content. Agents do not call one another directly. Instead, they interact indirectly through a **shared memory ** and are coordinated by an **orchestrator** that enables dynamic execution.

The core design goals are:

- Clear separation of agent responsibilities  
- Agent autonomy  
- Dynamic coordination without hard-coded control flow  

---

## 🏗️ Architectural Components

### 2.1 Agents

Each agent is a self-contained unit with a **single, clearly defined responsibility**. Agents inspect shared system state and decide independently whether to act.

| Agent | Responsibility |
|------|----------------|
| DataParserAgent | Converts raw product input into an internal product model |
| QuestionGeneratorAgent | Generates and categorizes user questions |
| ContentBlockAgent | Creates reusable content logic blocks |
| PageBuilderAgent | Assembles final pages using templates and shared data |

**Agent Characteristics:**

- Agents do not depend on each other directly  
- Agents do not assume a fixed execution order  
- Agents can be added or removed without modifying other agents  

---

### 2.2 Shared Memory

A shared memory component acts as the **central coordination medium** for the system.

Agents:
- Read from shared memory to determine whether they should act  
- Write their outputs back to shared memory  
- Communicate indirectly through state changes  

This design ensures **loose coupling** and allows agent interactions to emerge dynamically at runtime.

---

### 2.3 Orchestrator

The orchestrator is responsible **only for coordination**, not control logic.

It repeatedly cycles through all registered agents and allows each agent to execute if its internal conditions are met. The orchestrator does **not** enforce:

- A fixed execution order  
- A predefined workflow  
- Explicit agent dependencies  

As a result, overall system behavior emerges from **agent decisions** rather than static sequencing.

---

### 2.4 Content Generation Pipeline

Although the system produces outputs in a logical sequence, this sequence is **not hard-coded**. Instead, the effective pipeline emerges dynamically:

1. Product data is parsed into an internal representation  
2. Questions are generated once product data becomes available  
3. Reusable content blocks are created independently  
4. Templates are applied to assemble final content pages  

Each step occurs **only when the required state becomes available** in shared memory, preserving agent autonomy and dynamic coordination.

---
