# Local Development

This folder contains local development workflows using Foundry Local.

## Structure

- `test_local_foundry.py` - Standalone connectivity test and chat completion script
- `demo-chat-flow/` - ✅ Working Prompt Flow implementation
- `README.md` - This documentation file

## Setup and Usage

### Quick Test with test_local_foundry.py

1. **Start Foundry Local**
   ```bash
   # Launch the Foundry Local Windows application
   # Load a model (e.g., phi-3.5-mini) in the app
   ```

2. **Configure Environment**
   ```bash
   # Ensure .env file is configured with:
   FOUNDRY_LOCAL_ENDPOINT=http://127.0.0.1:58307
   DEFAULT_MODEL=Phi-3-mini-4k-instruct-cuda-gpu
   ```

3. **Run Connectivity Test**
   ```bash
   # From src/local directory:
   python test_local_foundry.py
   ```

### Demo Chat Flow

The `demo-chat-flow/` directory contains a **working Prompt Flow implementation**:
- ✅ `foundry_chat.py` - Fully functional Prompt Flow tool for Foundry Local integration
- ✅ `flow.dag.yaml` - Complete flow configuration
- ✅ `chat.jinja2` - Chat template with history support
- ✅ Flow validation passing

#### **Usage:**
```bash
# Navigate to demo-chat-flow directory
cd demo-chat-flow

# Test the flow
python -m promptflow._cli._pf.entry flow test --flow . --inputs question="What is AI?"

# Test with custom parameters
python -m promptflow._cli._pf.entry flow test --flow . --inputs question="Tell me about the golden ratio" temperature=0.9 max_tokens=100

# Validate flow configuration
python -m promptflow._cli._pf.entry flow validate --source .
```

## Features

The test_local_foundry.py script provides:
- ✅ Foundry Local connectivity testing
- ✅ Automatic endpoint detection with fallback
- ✅ Model availability verification
- ✅ Chat completion testing
- ✅ Environment variable support
- ✅ Error handling and status reporting

The demo-chat-flow provides:
- ✅ Full Prompt Flow integration with Foundry Local
- ✅ Chat history support for multi-turn conversations
- ✅ Configurable parameters (temperature, max_tokens, model, etc.)
- ✅ Template-based prompt engineering
- ✅ Environment variable configuration
- ✅ Error handling and validation

## Dependencies

All dependencies are managed in the main `pyproject.toml` file.
