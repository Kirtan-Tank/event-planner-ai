# 🎭 Batman-Themed Event Planner Agent

An AI-powered **event planning assistant** built with Hugging Face's **smolagents** framework, enhanced with a modular design and superhero flair. This agent can brainstorm event themes, suggest menus, recommend catering services, create playlists, and more — all wrapped in a **Batman-inspired workflow**.

Made by following the guide from [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit2/smolagents/code_agents)
---

## ✨ Features
- 🦇 **Batman/Superhero Theme** maintained for fun demonstrations.
- 🤖 **Agentic Architecture** using smolagents' `CodeAgent` for expressive tool use.
- 🔧 **Modular Codebase** with separate files for configuration, tools, and utilities.
- ⚡ **Groq-powered LLMs** (`llama-3.1-8b-instant`) for faster responses.
- 📊 **Monitoring Ready** with Langfuse, OTel, and other observability integrations.
- 🌐 **Tools Available:**
  - Web search
  - Webpage visits
  - Custom event tools (menu, catering, superhero themes)

---

## 📂 Project Structure
```
event-planner-ai/
├─ event_planner/
│  ├─ __init__.py
│  ├─ agent.py          # Core agent setup
│  ├─ config.py         # Configuration and constants
│  ├─ tools.py          # Custom tools for events
│  └─ utils.py          # Helper functions
├─ examples/
│  └─ run_demo.py       # Demo script
├─ .gitignore
├─ requirements.txt
└─ README.md
```

---

## 🚀 Quickstart

### 1. Clone the Repository
```bash
git clone https://github.com/Kirtan-Tank/event-planner-ai.git
cd event-planner-ai
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv event-planner-venv
source event-planner-venv/bin/activate   # Mac/Linux
# OR
./event-planner-venv/Scripts/activate    # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables
Create a `.env` file:
```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the Demo
```bash
python -m examples.run_demo
```

---

## 🛠️ Tech Stack
- [Python](https://www.python.org/)
- [smolagents](https://huggingface.co/docs/smolagents)
- [Langfuse](https://langfuse.com/) for monitoring
- [OpenTelemetry](https://opentelemetry.io/) for tracing
- [Groq](https://groq.com/) for fast LLM inference

---

## 📈 Monitoring Setup
Enable observability with Langfuse + OTel by exporting:
```env
LANGFUSE_SECRET_KEY=your_secret
LANGFUSE_PUBLIC_KEY=your_public
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

---

## 🤝 Support
If you like it please star the repo.

---
 