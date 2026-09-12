# Indra Agent Setup & Configuration Guide
*Built by CodersbyChance for SIH-26*

Indra is a fully autonomous, offline, privacy-first AI agent swarm designed to run entirely locally. This version features custom branding, local configuration constraints, multi-agent delegation, and file-based RAG—without any cloud dependencies.

---

## 1. System Capabilities & Features

### Core Offline Tools (Fully Unlocked)
Indra operates seamlessly without internet access using built-in local tools:
- **Code Execution (`code_execution`)**: Writes, tests, and runs Python scripts locally.
- **Project Management (`kanban` & `todo`)**: Creates and manages markdown-based Kanban boards and task lists.
- **Background Automation (`cronjob`)**: Schedules local tasks, reminders, and scripts to run on a timer via the `indra gateway`.
- **Context & Vision (`session_search`, `clarify`, `vision`)**: Analyzes past session logs and processes images completely locally using Vision Language Models (VLMs).
- **Persistent Memory (`memory`)**: Automatically learns user preferences and stores them in a local SQLite database for cross-session recall.

### Advanced Capabilities
- **Swarm Delegation (Parallel Agents)**: Using the custom `/trick-delegate` skill, the agent can spawn autonomous parallel sub-agents to tackle multiple tasks at once.
- **Dynamic Routing**: Automatically maps tasks to the best local model. For example, `indra-auto` (Qwen) handles tool execution and logic, while `indra-writer` (Gemma) or `indra-hermes` handles creative generation.
- **Obsidian Vault Integration (Local RAG)**: Instead of a heavy vector database, Indra uses file-based retrieval. It natively navigates your `MyVault` folder, reads your markdown/PDF documents into its context window, and acts as a "Second Brain" to answer questions based strictly on your private data.

---

## 2. Prerequisites: Binaries & Model Files

Before installing, you must place the backend engine and local LLM weights into the correct directories.

### A. The Backend Engine (`bin`)
Download the Llama-Swap engine executable (`llama-swap.exe` for Windows) and place it in the backend binary folder:
`C:\Users\khatr\OneDrive\Desktop\indra\SIH-26\hermes-agent\backend\bin\`

### B. The LLM Models (`.gguf`)
Download your preferred models (in `.gguf` format) from HuggingFace. Recommended models:
- **Qwen (indra-auto)**: `qwen2.5-7b-instruct-q4_k_m.gguf` (Excellent at tool calling).
- **Hermes (indra-hermes)**: `hermes-3-llama-8b.gguf`
- **Gemma (indra-writer)**: `gemma-2-2b-it.gguf`

Place all `.gguf` files into the models folder:
`C:\Users\khatr\OneDrive\Desktop\indra\SIH-26\hermes-agent\backend\models\`

### C. Vision Language Models (VLMs)
If you want local image analysis (the `vision` tool), you must download the vision projector file for your model. For example, if using Qwen2-VL, download the `mmproj-model-f16.gguf` projector.
Place the projector file in the **exact same directory** as your models:
`C:\Users\khatr\OneDrive\Desktop\indra\SIH-26\hermes-agent\backend\models\`

---

## 3. Installation (Local Build)

You must install the CLI directly from source to apply our custom `SOUL.md` prompt injections and branding.

1. Open PowerShell as Administrator.
2. Navigate to the frontend project root:
   ```powershell
   cd C:\Users\khatr\OneDrive\Desktop\indra\SIH-26\hermes-agent
   ```
3. Install the package in editable mode:
   ```powershell
   pip install -e .
   ```

---

## 4. Easy Configuration

### Environment Variables
Open (or create) the `C:\Users\khatr\OneDrive\Desktop\indra\.env` file and set your API key and Vault path:
```env
WORKBENCH_API_KEY=wb_live_1234567890abcdef1234567890abcdef
TERMINAL_ENV=local
OBSIDIAN_VAULT_PATH=C:\Users\khatr\OneDrive\Desktop\indra\MyVault
```
*(Make sure an empty folder named `MyVault` actually exists in your `indra` directory!)*

### Start the Backend
From the main `indra` directory, run our custom startup script. This script automatically scans your `models/` directory, writes the `llama-swap.yaml` configuration, and boots both the AI Workbench and the Llama-Swap engine.
```powershell
.\start-indra.ps1
```

### Register Models
If the UI says "No models registered", open a new PowerShell tab, navigate to the backend, and inject the models into the local SQLite database:
```powershell
cd C:\Users\khatr\OneDrive\Desktop\indra\SIH-26\hermes-agent\backend
.\venv\Scripts\python.exe register_models.py
```

---

## 5. Usage & Commands

Once the backend is running, open a new terminal and launch the interactive agent:

```powershell
indra dashboard
```

### Useful CLI Commands:
- `/model indra-auto`: Switches the active model to Qwen (Highly recommended for tool execution and Vault operations).
- `/trick-delegate [instructions]`: Forces the model to use the `delegate_task` tool properly to spawn multiple parallel sub-agents.
- `indra gateway`: Run this in a separate terminal if you want your background `cronjob` timers to physically execute.

### Important URLs for Debugging:
- **Indra Web UI:** `http://127.0.0.1:9119`
- **AI Workbench Gateway:** `http://127.0.0.1:8000/ui`
- **Llama-Swap Engine:** `http://127.0.0.1:8100/ui/`
