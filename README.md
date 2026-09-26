# ✈️ AeroMind — LLM-Powered Aviation Simulation & RAG System

> **AeroMind** is an AI-powered aviation simulation and decision-support training system that combines a flight simulator, state analysis, Retrieval-Augmented Generation (RAG), vector search, and a local Large Language Model (LLM) to generate grounded situation reports.

⚠️ **Important:** AeroMind is a **simulation and educational project**. It does not use real aircraft data and is **not intended for real-world aviation operations**.

---

## 📌 Table of Contents

* [Overview](#-overview)
* [Project Objective](#-project-objective)
* [Key Features](#-key-features)
* [System Architecture](#-system-architecture)
* [Technologies](#-technologies)
* [Project Structure](#-project-structure)
* [How the System Works](#-how-the-system-works)
* [Flight Simulation](#-flight-simulation)
* [State Analysis](#-state-analysis)
* [RAG Pipeline](#-rag-pipeline)
* [Vector Search with FAISS](#-vector-search-with-faiss)
* [LLM Integration](#-llm-integration)
* [AI Situation Report](#-ai-situation-report)
* [Streamlit Dashboard](#-streamlit-dashboard)
* [Simulation Events](#-simulation-events)
* [Installation](#-installation)
* [Running the Project](#-running-the-project)
* [Testing](#-testing)
* [Example Workflow](#-example-workflow)
* [Why RAG?](#-why-rag)
* [Security and Safety](#-security-and-safety)
* [Limitations](#-limitations)
* [Future Improvements](#-future-improvements)
* [Skills Demonstrated](#-skills-demonstrated)
* [Interview Explanation](#-interview-explanation)
* [CV Description](#-cv-description)
* [License](#-license)

---

# 🧠 Overview

AeroMind is a **simulated aviation environment** designed to demonstrate how Artificial Intelligence, RAG, vector databases, and local LLMs can be combined with a simulation engine.

The system simulates an aircraft and continuously monitors its state:

* Altitude
* Speed
* Heading
* Fuel
* Weather
* Communication status
* Navigation status
* Latitude
* Longitude

During the simulation, different events are introduced automatically.

For example:

```text
Step 5  → Severe weather
Step 8  → Communication degraded
Step 10 → Navigation degraded
```

The system detects these changes, generates alerts, retrieves relevant simulated procedures from a knowledge base, and sends the retrieved information to a local LLM.

The LLM then generates a grounded **AI Situation Report**.

---

# 🎯 Project Objective

The main objective of AeroMind is to demonstrate an end-to-end AI pipeline:

```text
Simulation
     ↓
Aircraft State
     ↓
State Analysis
     ↓
Alert Detection
     ↓
RAG Query
     ↓
Semantic Search
     ↓
FAISS
     ↓
Relevant Knowledge
     ↓
Local LLM
     ↓
AI Situation Report
     ↓
Streamlit Dashboard
```

The project focuses on:

* AI Engineering
* Generative AI
* Retrieval-Augmented Generation
* Local LLMs
* Semantic Search
* Vector Search
* Simulation
* Python Software Engineering
* AI Safety / Grounding
* Interactive AI dashboards

---

# 🚀 Key Features

## ✈️ Flight Simulation

AeroMind contains a simulated aircraft with a dynamic state.

The simulator updates:

* Altitude
* Speed
* Fuel
* Position

It also introduces simulated system events.

---

## 🧠 AI State Analysis

The system analyzes the aircraft state and detects predefined conditions.

Example:

```text
Severe weather detected
Communication system degraded
Navigation system degraded
```

---

## 🔎 Retrieval-Augmented Generation

The detected situation is transformed into a search query.

Example:

```text
Severe weather detected Communication system degraded Navigation system degraded
```

The system then retrieves relevant documents from the simulated aviation knowledge base.

---

## 🗂️ Semantic Search

AeroMind uses:

* Sentence Transformers
* Embeddings
* FAISS

to find documents that are semantically relevant to the current situation.

---

## 🤖 Local LLM

AeroMind uses a local LLM through Ollama.

Current model:

```text
llama3.2:3b
```

The LLM receives:

* Aircraft state
* Detected alerts
* Retrieved knowledge

and generates a grounded situation report.

---

## 📊 Interactive Dashboard

The Streamlit dashboard displays:

* Aircraft state
* System status
* Simulation step
* Position
* Simulation history
* Flight trends
* AI alerts
* RAG query
* Retrieved knowledge
* AI situation report

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │   Flight Simulator  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Aircraft State    │
                         │                     │
                         │ Altitude            │
                         │ Speed               │
                         │ Fuel                │
                         │ Weather             │
                         │ Communication       │
                         │ Navigation          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   State Analyzer    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Alert Detection  │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │     RAG Query       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │     Sentence Transformers   │
                    │          Embeddings          │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                         ┌─────────────────────┐
                         │        FAISS        │
                         │   Vector Search     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Retrieved Knowledge │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Ollama / LLM     │
                         │    Llama 3.2 3B     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ AI Situation Report │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Streamlit Dashboard │
                         └─────────────────────┘
```

---

# 🛠️ Technologies

| Technology            | Role                                      |
| --------------------- | ----------------------------------------- |
| Python                | Main programming language                 |
| Pydantic              | Aircraft state validation                 |
| Streamlit             | Interactive dashboard                     |
| Pandas                | Simulation history and data visualization |
| Sentence Transformers | Text embeddings                           |
| FAISS                 | Vector similarity search                  |
| Ollama                | Local LLM runtime                         |
| Llama 3.2 3B          | Local language model                      |
| Pytest                | Testing                                   |
| Git / GitHub          | Version control                           |
| Docker                | Containerization / future deployment      |

---

# 📁 Project Structure

```text
AeroMind/
│
├── app/
│   ├── __init__.py
│   │
│   ├── simulator/
│   │   ├── __init__.py
│   │   ├── aircraft.py
│   │   ├── scenarios.py
│   │   ├── engine.py
│   │   ├── dashboard.py
│   │   └── state_analyzer.py
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   └── retriever.py
│   │
│   └── llm/
│       ├── __init__.py
│       └── client.py
│
├── data/
│   └── documents/
│       ├── weather_procedures.txt
│       ├── communication_procedures.txt
│       └── navigation_procedures.txt
│
├── tests/
│   ├── test_simulator.py
│   ├── test_analyzer.py
│   └── test_rag.py
│
├── requirements.txt
├── .gitignore
├── .env
├── docker-compose.yml
└── README.md
```

---

# ✈️ Flight Simulation

The aircraft is represented using a Pydantic model.

The state contains:

```text
Aircraft ID
Altitude
Speed
Heading
Fuel
Weather
Communication
Navigation
Latitude
Longitude
```

Example:

```python
AircraftState(
    aircraft_id="A12",
    altitude=18000,
    speed=420,
    heading=270,
    fuel=75,
    weather="Clear",
    communication="Normal",
    navigation="Normal",
    latitude=30.4200,
    longitude=-9.6000
)
```

Pydantic provides structured data validation for the simulated aircraft state.

---

# 🎮 Simulation Engine

The simulation engine is implemented in:

```text
app/simulator/engine.py
```

Every time the user runs a simulation step:

```text
Step +1
Fuel decreases
Altitude changes
Speed changes
Position changes
System events may occur
```

Example:

```text
Step 1
Altitude = 18100 ft
Speed = 418 kt
Fuel = 74.5%

Step 2
Altitude = 18200 ft
Speed = 416 kt
Fuel = 74.0%

...

Step 10
Altitude = 19000 ft
Speed = 400 kt
Fuel = 70.0%
```

The simulator is intentionally simplified because the objective is to demonstrate the AI architecture rather than reproduce a real aircraft physics model.

---

# ⚠️ Simulation Events

AeroMind contains predefined simulated events.

| Simulation Step | Event                  |
| --------------: | ---------------------- |
|               5 | Severe weather         |
|               8 | Communication degraded |
|              10 | Navigation degraded    |

Example:

```python
if self.step_count == 5:
    self.aircraft.weather = "Severe"

if self.step_count == 8:
    self.aircraft.communication = "Degraded"

if self.step_count == 10:
    self.aircraft.navigation = "Degraded"
```

These events allow the AI pipeline to react to changing simulated conditions.

---

# 🧠 State Analyzer

The state analyzer is responsible for detecting predefined conditions.

File:

```text
app/simulator/state_analyzer.py
```

Example:

```python
if state.weather == "Severe":
    alerts.append("Severe weather detected")

if state.communication == "Degraded":
    alerts.append("Communication system degraded")

if state.navigation == "Degraded":
    alerts.append("Navigation system degraded")
```

The analyzer converts the aircraft state into human-readable alerts.

Example:

```text
Aircraft State
      ↓
State Analyzer
      ↓
Detected Alerts
      ↓
Severe weather detected
Communication system degraded
Navigation system degraded
```

---

# 🔎 RAG Query Generation

After detecting the alerts, AeroMind generates a query for the RAG system.

Example:

```text
Severe weather detected
Communication system degraded
Navigation system degraded
```

The function:

```python
build_rag_query(state)
```

combines the detected alerts into a semantic search query.

Example output:

```text
Severe weather detected Communication system degraded Navigation system degraded
```

---

# 📚 RAG Pipeline

RAG stands for:

> **Retrieval-Augmented Generation**

Instead of asking the LLM to generate an answer using only its internal knowledge, AeroMind first retrieves relevant information from a controlled knowledge base.

The pipeline is:

```text
Aircraft State
      ↓
Detected Alerts
      ↓
RAG Query
      ↓
Text Embeddings
      ↓
FAISS Search
      ↓
Relevant Documents
      ↓
LLM
      ↓
Grounded Report
```

---

# 📄 Knowledge Base

The simulated knowledge base is stored in:

```text
data/documents/
```

Current documents:

```text
weather_procedures.txt
communication_procedures.txt
navigation_procedures.txt
```

These documents contain simulated procedures used only by the training environment.

Example:

```text
AVIATION SIMULATION - WEATHER PROCEDURES

Purpose:
This document contains simulated procedures for handling
severe weather conditions in the AeroMind training environment.
```

The documents are deliberately limited and controlled so that the LLM can be grounded in retrieved information.

---

# 🧩 Document Loader

File:

```text
app/rag/loader.py
```

The document loader:

1. Searches the documents directory.
2. Reads `.txt` files.
3. Loads their contents.
4. Returns structured documents.

Example:

```python
documents.append({
    "filename": file_path.name,
    "text": text
})
```

---

# 🔢 Text Embeddings

AeroMind uses:

```text
Sentence Transformers
```

with:

```text
all-MiniLM-L6-v2
```

The model converts text into numerical vectors called **embeddings**.

Conceptually:

```text
"Severe weather detected"
             ↓
     Sentence Transformer
             ↓
       [0.21, -0.08, ...]
```

Documents with similar meanings produce vectors that are closer together in the embedding space.

---

# 🗂️ FAISS Vector Search

AeroMind uses:

```text
FAISS
```

FAISS stands for:

> **Facebook AI Similarity Search**

It is used to efficiently search vectors.

The process is:

```text
Documents
    ↓
Embeddings
    ↓
FAISS Index
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Top-K Documents
```

The current implementation uses:

```python
faiss.IndexFlatL2()
```

which performs L2-distance based similarity search.

---

# 🔍 Retrieval Example

Suppose the current state generates:

```text
Severe weather detected
Communication system degraded
Navigation system degraded
```

The retriever searches the knowledge base.

Possible result:

```text
communication_procedures.txt
weather_procedures.txt
```

The retrieved documents are then passed to the LLM.

---

# 🤖 LLM Integration

AeroMind uses:

```text
Ollama
```

to run a local LLM.

Current model:

```text
llama3.2:3b
```

The Python application communicates with Ollama through the Python client.

Architecture:

```text
AeroMind
    ↓
Python Ollama Client
    ↓
Ollama
    ↓
Llama 3.2 3B
    ↓
Generated Report
```

---

# 🧠 Prompt Engineering

The LLM receives a structured prompt containing:

### 1. Aircraft State

```text
Altitude
Speed
Heading
Fuel
Weather
Communication
Navigation
```

### 2. Detected Alerts

Example:

```text
Severe weather detected
Communication system degraded
Navigation system degraded
```

### 3. Retrieved Knowledge

The documents returned by FAISS.

### 4. Generation Rules

The model is instructed to:

* Use only provided information.
* Avoid inventing procedures.
* Avoid inventing recommendations.
* Avoid using external knowledge.
* Clearly mention missing information.
* Treat the environment as a simulation.

---

# 📋 AI Situation Report

The generated report follows a fixed structure.

```text
1. Situation Summary

2. Detected Issues

3. Retrieved Simulated Procedures

4. Evidence from Retrieved Knowledge

5. Important Limitations
```

This structure makes the LLM output easier to read and evaluate.

---

# 🛡️ AI Grounding

One important aspect of AeroMind is **grounding**.

The system does not simply ask:

```text
"What should the aircraft do?"
```

Instead, it provides the LLM with:

```text
Current State
+
Detected Alerts
+
Retrieved Knowledge
```

The LLM is explicitly instructed to remain within the retrieved knowledge.

This reduces unsupported generated content and makes the project a practical demonstration of **grounded generative AI**.

---

# 📊 Streamlit Dashboard

The main interface is built with:

```text
Streamlit
```

Run:

```powershell
python -m streamlit run app/simulator/dashboard.py
```

The dashboard provides several sections.

---

## ✈️ Aircraft Metrics

The dashboard displays:

```text
Altitude
Speed
Fuel
Heading
```

Example:

```text
Altitude     18,000 ft
Speed        420 kt
Fuel         75%
Heading      270°
```

---

## 🛰️ Aircraft Systems

The dashboard monitors:

```text
Weather
Communication
Navigation
```

Normal conditions are displayed differently from degraded conditions.

---

## 📍 Simulated Position

The aircraft position is displayed using:

```text
Latitude
Longitude
```

The position is simulated and does not represent real aircraft tracking.

---

# 📈 Simulation History

Every simulation step can be stored in Streamlit session state.

The history contains:

```text
Step
Altitude
Speed
Fuel
Heading
Weather
Communication
Navigation
```

This allows the dashboard to display the evolution of the simulation.

---

# 📉 Flight Trends

The dashboard visualizes:

### Altitude

```text
Altitude vs Simulation Step
```

### Speed

```text
Speed vs Simulation Step
```

### Fuel

```text
Fuel vs Simulation Step
```

These charts help visualize how the simulated aircraft state changes over time.

---

# 🧠 AI State Analysis Dashboard

The dashboard displays the alerts generated by:

```python
analyze_state(state)
```

Example:

```text
⚠️ Severe weather detected
⚠️ Communication system degraded
⚠️ Navigation system degraded
```

---

# 🔎 RAG Query Dashboard

The generated RAG query is displayed directly in the dashboard.

Example:

```text
Severe weather detected Communication system degraded Navigation system degraded
```

This makes the RAG process transparent and easier to understand.

---

# 📚 Retrieved Knowledge Dashboard

The retrieved documents are displayed using expandable sections.

Example:

```text
📄 communication_procedures.txt

📄 weather_procedures.txt
```

Users can inspect the exact knowledge provided to the LLM.

---

# 🤖 AI Situation Report Dashboard

Finally, the dashboard displays the generated report.

```text
Aircraft State
      ↓
AI Analysis
      ↓
RAG Retrieval
      ↓
LLM
      ↓
AI Situation Report
```

This represents the final output of the complete AeroMind pipeline.

---

# 🔄 Complete End-to-End Workflow

The complete process can be summarized as:

```text
1. Start Simulation
        ↓
2. Initialize Aircraft
        ↓
3. Update Aircraft State
        ↓
4. Detect Simulation Events
        ↓
5. Analyze Aircraft State
        ↓
6. Generate Alerts
        ↓
7. Build RAG Query
        ↓
8. Generate Query Embedding
        ↓
9. Search FAISS Index
        ↓
10. Retrieve Relevant Documents
        ↓
11. Build LLM Prompt
        ↓
12. Send Prompt to Local LLM
        ↓
13. Generate Grounded AI Report
        ↓
14. Display Results in Streamlit
```

---

# 🧪 Testing

AeroMind contains several test scripts.

## Test Simulator

```powershell
python -m tests.test_simulator
```

This verifies that the simulation engine correctly updates the aircraft state.

---

## Test Analyzer

```powershell
python -m tests.test_analyzer
```

This verifies that alerts are correctly detected.

---

## Test RAG + LLM

```powershell
python -m tests.test_rag
```

This tests the complete:

```text
State
→ Alerts
→ RAG Query
→ FAISS
→ Retrieved Knowledge
→ LLM
→ AI Report
```

---

# 💻 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/zakariyaerrahma/AeroMind.git
```

```bash
cd AeroMind
```

---

## 2. Create Virtual Environment

Windows PowerShell:

```powershell
python -m venv .venv
```

Activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

# 🤖 Install Ollama

AeroMind uses Ollama to run the local LLM.

After installing Ollama, download the model:

```powershell
ollama pull llama3.2:3b
```

Test the model:

```powershell
ollama run llama3.2:3b
```

---

# ▶️ Running AeroMind

Open a terminal and activate the environment:

```powershell
cd C:\Users\zakar\Desktop\AeroMind
```

```powershell
.\.venv\Scripts\Activate.ps1
```

Start Ollama:

```powershell
ollama run llama3.2:3b
```

Then open another terminal and run:

```powershell
cd C:\Users\zakar\Desktop\AeroMind
```

```powershell
.\.venv\Scripts\Activate.ps1
```

Start Streamlit:

```powershell
python -m streamlit run app/simulator/dashboard.py
```

The application will open in the browser.

---

# ⚙️ Requirements

Example dependencies:

```text
streamlit
pandas
pydantic
sentence-transformers
faiss-cpu
ollama
python-dotenv
pytest
fastapi
uvicorn
```

Install them with:

```powershell
pip install -r requirements.txt
```

---

# 🐳 Docker

Docker support is included as part of the project architecture.

The application can be containerized using:

```text
Docker
Docker Compose
```

However, Ollama is a separate local LLM runtime and may require additional configuration depending on the deployment environment.

For local development, running Ollama directly on the host system is the simplest configuration.

---

# 🔐 Security and Safety Considerations

AeroMind is designed as a controlled simulation.

Important principles:

### 1. No Real Aircraft Data

The aircraft state is generated by the simulator.

### 2. No Real-Time Flight Data

The application does not connect to aircraft systems or live aviation networks.

### 3. Controlled Knowledge Base

The RAG system uses local simulated documents.

### 4. Local LLM

The LLM can run locally through Ollama.

### 5. Grounded Generation

The prompt explicitly limits the LLM to the supplied information.

### 6. Simulation-Only Procedures

The documents are educational and simulated.

---

# ⚠️ Limitations

AeroMind is a research and educational prototype.

It does **not** provide:

* Real flight control
* Real aircraft navigation
* Real-time aircraft telemetry
* Certified aviation procedures
* Real-world operational recommendations
* Safety-critical decision making

The simulation model is intentionally simplified.

The AI report is also not a certified aviation system.

---

# 🚧 Future Improvements

Possible future versions could include:

## 🧠 Advanced RAG

Replace the simple document retrieval system with:

* Document chunking
* Metadata filtering
* Hybrid search
* Reranking
* Better retrieval evaluation

---

## 🤖 Advanced LLM Support

Support multiple local models:

```text
Llama
Mistral
Qwen
Gemma
```

---

## 🧩 Better Knowledge Management

Add:

```text
PDF documents
Markdown documents
Structured JSON
Metadata
Document versioning
```

---

## 📊 Advanced Dashboard

Possible improvements:

* Interactive timeline
* Event timeline
* System health indicators
* More advanced charts
* Simulation replay
* Scenario selection
* AI report history

---

## 🧪 Automated Evaluation

Add evaluation metrics for:

* Retrieval accuracy
* Relevant document selection
* Grounding
* Hallucination rate
* Response consistency

---

## ☁️ Cloud Deployment

Possible deployment architecture:

```text
Streamlit
     ↓
FastAPI
     ↓
RAG Service
     ↓
Vector Database
     ↓
LLM Service
```

This could later be deployed using:

```text
Docker
AWS
Azure
Google Cloud
```

---

# 🧑‍💻 Skills Demonstrated

AeroMind demonstrates practical skills in:

### Artificial Intelligence

* Machine Learning concepts
* Generative AI
* LLM integration
* Prompt engineering
* AI grounding

### RAG

* Embeddings
* Semantic search
* Vector databases
* FAISS
* Knowledge retrieval

### Software Engineering

* Modular Python architecture
* Object-oriented programming
* Pydantic models
* Testing
* Git
* GitHub

### Data Engineering

* Text processing
* Embeddings
* Vector representations
* Data visualization

### Cloud / DevOps

* Docker
* Docker Compose
* Local AI infrastructure
* Service architecture

### AI Systems

* Simulation
* State monitoring
* Event detection
* AI-assisted reporting
* Human-readable dashboards

---

# 💼 Why This Project Is Interesting

AeroMind combines several modern AI technologies in one project:

```text
Simulation
+
Artificial Intelligence
+
RAG
+
Vector Search
+
LLM
+
Dashboard
+
Software Engineering
```

Instead of building only a chatbot, the project demonstrates a complete AI system that:

```text
Receives structured state
        ↓
Analyzes the state
        ↓
Detects events
        ↓
Retrieves relevant knowledge
        ↓
Uses an LLM
        ↓
Generates a grounded report
        ↓
Displays the result
```

---

# 🎤 Interview Explanation

A simple way to explain the project during an interview:

> **AeroMind is a simulated aviation environment that combines a flight simulator with an AI-powered RAG pipeline. The simulator generates an aircraft state and predefined events such as severe weather or degraded communication. A state analyzer detects these events and converts them into a semantic query. Sentence Transformers generate embeddings and FAISS retrieves the most relevant documents from a local knowledge base. The retrieved information is then provided to a local Llama 3.2 model through Ollama, which generates a grounded situation report. The entire process is visualized through a Streamlit dashboard.**

---

# 🧩 Main Concepts to Understand

If you present this project during an interview, you should be comfortable explaining:

### What is RAG?

Retrieval-Augmented Generation combines information retrieval with generative AI.

```text
Retrieve information
        +
Generate response
```

---

### What is an Embedding?

An embedding is a numerical representation of text that captures semantic information.

Example:

```text
"Severe weather"
       ↓
Numerical vector
```

---

### What is FAISS?

FAISS is a library designed for efficient similarity search over vector representations.

---

### Why Sentence Transformers?

Sentence Transformers convert sentences and documents into embeddings that can be compared semantically.

---

### Why Ollama?

Ollama provides a simple way to run LLMs locally.

---

### Why a Local LLM?

A local model allows the project to demonstrate LLM capabilities without requiring a cloud API for inference.

---

### Why Streamlit?

Streamlit provides a simple way to build an interactive Python-based dashboard.

---

### Why Pydantic?

Pydantic provides structured models and data validation for the aircraft state.

---

# 📌 Project Summary

AeroMind demonstrates an end-to-end architecture for a grounded AI system:

```text
                AEROMIND

       ┌─────────────────────┐
       │  Simulated Aircraft │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │   State Analyzer    │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │     RAG Query       │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ Sentence Transformer│
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │        FAISS        │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ Retrieved Knowledge  │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │  Llama 3.2 3B LLM   │
       │       Ollama         │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ AI Situation Report │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ Streamlit Dashboard │
       └─────────────────────┘
```

---

# 👨‍💻 Author

**Zakariya Errahma**

Master's Student — AI Embedded / Edge AI

Interests:

* Artificial Intelligence
* Embedded AI
* Edge AI
* Cybersecurity
* Computer Vision
* Cloud & DevOps
* Generative AI
* RAG Systems
* AI Systems

GitHub:

**zakariyaerrahma**

---

# 📄 License

This project is intended for educational and research purposes.

The AeroMind simulation and its documents are not intended for real-world aviation operations.

---

# ⭐ Final Note

AeroMind is a portfolio project designed to demonstrate how modern AI components can be integrated into a complete software system.

The project combines:

```text
Python
    +
Simulation
    +
State Analysis
    +
RAG
    +
Embeddings
    +
FAISS
    +
Local LLM
    +
Ollama
    +
Streamlit
```

The main focus is not to reproduce a real aircraft system, but to demonstrate the architecture and engineering principles behind a **grounded AI decision-support simulation**.
