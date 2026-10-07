# Agent Lab

A hands-on workspace for exploring and building AI agents, tool use, and conversational systems.

## Project Structure

```text
agent-lab/
├── chat/
│   ├── chat.py           # Basic interactive chatbot with DeepSeek API
│   └── chat_memory.py    # Multi-turn chat with persistent JSON memory and token tracking
├── .env.example          # Template for required environment variables
├── .gitignore            # Git ignore configuration
├── requirements.txt      # Python dependencies
└── README.md
```

## Getting Started

### 1. Environment Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Configuration

Copy the sample environment file and add your API key:

```bash
cp .env.example .env
```

Edit `.env` and set your DeepSeek API key:

```env
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

### 3. Running the Scripts

- **Basic Chat**:
  ```bash
  python chat/chat.py
  ```

- **Persistent Chat Memory**:
  ```bash
  python chat/chat_memory.py
  ```
  *(Supports commands: `quit` to exit, `clear` to reset memory)*
