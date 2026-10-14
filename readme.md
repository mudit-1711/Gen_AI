# Gen AI

A hands-on repository for exploring Generative AI, LangChain integrations, cloud inference providers (Groq, Hugging Face), and local offline LLM execution.

---

## 🚀 Quick Start

### 1. Activate Virtual Environment
Use the following command in PowerShell to activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

> **Note:** If you encounter execution policy restrictions in PowerShell, you can temporarily allow scripts with:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> ```

### 2. Install Dependencies
Install all required libraries specified in [requirements.txt](file:///d:/Gen%20AI/requirements.txt):

```powershell
pip install -r requirements.txt
```

### 3. Environment Variables Setup
Create a `.env` file in the root directory and add the required API keys for cloud providers:

```env
GROQ_API_KEY=your_groq_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

---

## 📁 Repository Structure

```text
Gen AI/
├── chatmodels/
│   ├── chat.py           # Groq cloud model integration (e.g. gpt-oss-120b)
│   ├── huggingface.py    # Hugging Face Hub Endpoint (e.g. DeepSeek-R1)
│   └── localmodel.py     # Local offline LLM execution (TinyLlama-1.1B)
├── LLMS/                 # Local directory for cached model weights (git-ignored)
├── requirements.txt      # Project dependencies
├── test.py               # Basic environment verification script
└── readme.md             # Project documentation
```

---

## 🛠️ Features & Usage

### 🦙 Run Local LLM (TinyLlama)
Runs `TinyLlama/TinyLlama-1.1B-Chat-v1.0` locally using Hugging Face pipelines with weights cached under `LLMS/Tiny Lamma/`.

```powershell
python chatmodels/localmodel.py
```

### ⚡ Chat with Groq
Interactive chat model powered by Groq using LangChain's unified `init_chat_model`:

```powershell
python chatmodels/chat.py
```

### 🤗 Hugging Face Endpoint
Connect to hosted models on Hugging Face Inference Endpoints:

```powershell
python chatmodels/huggingface.py
```

### 🧪 Verify Installation
Verify LangChain installation:

```powershell
python test.py
```