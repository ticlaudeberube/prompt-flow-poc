# Prompt Flow POC

This project is a Proof of Concept (POC) for experimenting with Prompt Flow tools and workflows using Model Context Protocol (MCP) servers.

## Features

- **🏠 Local Development Environment**: Complete Python setup with UV package manager
- **🤖 Foundry Local Integration**: Direct integration with local AI models via automatic endpoint detection
- **📊 Model Detection**: Lists all loaded models with display names and metadata
- **🛡️ Error Handling**: Comprehensive error handling with helpful diagnostic messages
- **📡 API Testing**: Tests both model listing and chat completion endpoints
- **⏱️ Timeout Management**: Configurable timeouts for reliable testing
- **🔗 Smart Detection**: Uses FoundryLocalManager for automatic endpoint detection
- **📈 Status Reporting**: Clear success/failure indicators with emoji feedback
- **📦 Modern Dependency Management**: Single `pyproject.toml` configuration  
- **🔧 Multiple MCP Servers**: Enhanced AI capabilities with 7 configured MCP servers
- **☁️ Azure AI Foundry Integration**: Cloud AI model deployment and management
- **🐙 GitHub Integration**: Repository management and collaboration tools
- **🧪 Testing & Debugging Tools**: Simple connectivity testing and validation scripts
- **📊 Prompt Flow Examples**: Production-ready conversational AI workflows

## MCP Server Configuration

This project uses multiple Model Context Protocol (MCP) servers to provide enhanced AI capabilities:

### 🖥️ **Filesystem Server**
- **Purpose**: File system access and manipulation
- **Package**: `@modelcontextprotocol/server-filesystem`
- **Scope**: Workspace file operations

### 🔄 **Git Server**
- **Purpose**: Git repository operations and version control
- **Package**: `@modelcontextprotocol/server-git`
- **Scope**: Repository management and Git operations

### ☁️ **Azure MCP Server**
- **Purpose**: Azure cloud services integration
- **Package**: `@azure/mcp`
- **Requirements**: Azure credentials (see Environment Setup)

### 🗄️ **SQLite Server**
- **Purpose**: Local database operations
- **Package**: `@modelcontextprotocol/server-sqlite`
- **Database**: `./data` directory

### 🧠 **Memory Server**
- **Purpose**: Persistent memory and context management
- **Package**: `@modelcontextprotocol/server-memory`

### 🐙 **GitHub Server**
- **Purpose**: GitHub API integration and repository management
- **Package**: `@modelcontextprotocol/server-github`
- **Requirements**: GitHub Personal Access Token (see Environment Setup)

### 🤖 **Azure AI Foundry Server**
- **Purpose**: Azure AI model deployment and management
- **Source**: `git+https://github.com/azure-ai-foundry/mcp-foundry.git`
- **Requirements**: Azure AI credentials (see Environment Setup)

## Environment Setup

Create a `.env` file in the project root with the following variables:

```bash
# Azure Configuration
# Get these from Azure Portal > Azure Active Directory > App registrations
AZURE_SUBSCRIPTION_ID=your-subscription-id-here
AZURE_TENANT_ID=your-tenant-id-here
AZURE_CLIENT_ID=your-client-id-here
AZURE_CLIENT_SECRET=your-client-secret-here

# Additional Azure AI Foundry settings (if needed)
# AZURE_AI_FOUNDRY_PROJECT_ID=your-project-id
# AZURE_AI_FOUNDRY_ENDPOINT=https://your-endpoint.cognitiveservices.azure.com/

# GitHub Configuration
# Generate at: GitHub Settings > Developer settings > Personal access tokens
GITHUB_PERSONAL_ACCESS_TOKEN=your-github-token-here
```

### 🔑 **Getting Azure Credentials**
1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to Azure Active Directory > App registrations
3. Create a new application or use existing one
4. Copy the Application (client) ID, Directory (tenant) ID
5. Generate a client secret under "Certificates & secrets"
6. Note your subscription ID from the Azure portal

### 🔑 **Getting GitHub Token**
1. Go to GitHub Settings > Developer settings > Personal access tokens
2. Generate new token (classic)
3. Select appropriate scopes for your needs
4. Copy the generated token

## Python Interpreter Setup

This project requires **Python 3.10 or higher**. Here's how to set up your Python environment:

### 📦 **Installing UV Package Manager**

This project uses [uv](https://github.com/astral-sh/uv) for Python version and package management:

**Windows (PowerShell):**
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Windows (Command Prompt/Git Bash):**
```bash
# Download and run installer
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add to PATH manually
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**macOS:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add to PATH (if not automatically added)
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### 🐍 **Setup Python with UV**

```bash
# Install Python 3.10 and create virtual environment
uv python install 3.10
uv venv --python 3.10
```

### ✅ **Verify Installation**

```bash
# Check UV installation
uv --version

# Check available Python versions with UV
uv python list
```

**If UV is not recognized:**

**Windows:**
```bash
# Add UV to PATH manually
$env:PATH += ";$env:USERPROFILE\.cargo\bin"

# Or restart your terminal and try:
%USERPROFILE%\.cargo\bin\uv --version
```

**macOS:**
```bash
# Add to current session
export PATH="$HOME/.cargo/bin:$PATH"

# Or use full path
~/.cargo/bin/uv --version
```

### 🔧 **IDE Configuration**

**VS Code:**
1. Install Python extension
2. Open project folder
3. Press `Ctrl+Shift+P` → "Python: Select Interpreter"
4. Choose the Python 3.10+ interpreter or `.venv/Scripts/python.exe` after creating virtual environment

**PyCharm:**
1. File → Settings → Project → Python Interpreter
2. Add new interpreter → Existing environment
3. Select Python 3.10+ executable

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/ticlaudeberube/prompt-flow-poc.git
   cd prompt-flow-poc
   ```

2. **Set up Python environment**
   ```bash
   # Ensure Python 3.10+ is installed
   uv venv
   source .venv/bin/activate  # On macOS/Linux
   # or .venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   uv sync
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your actual credentials
   ```

5. **Test MCP servers**
   ```bash
   # Test Azure AI Foundry MCP server
   uvx --prerelease=allow --no-cache --from git+https://github.com/azure-ai-foundry/mcp-foundry.git run-azure-ai-foundry-mcp --help
   
   # Test GitHub token
   source .env && curl -H "Authorization: token $GITHUB_PERSONAL_ACCESS_TOKEN" https://api.github.com/user
   ```

## Installation

You can install dependencies using [uv](https://github.com/astral-sh/uv):

```bash
# Install all dependencies
uv sync

# Add a new package (example: promptflow-tools)
uv add promptflow-tools

# Install MCP servers globally (optional)
npm install -g @modelcontextprotocol/server-filesystem
npm install -g @modelcontextprotocol/server-git
npm install -g @azure/mcp
npm install -g @modelcontextprotocol/server-sqlite
npm install -g @modelcontextprotocol/server-memory
npm install -g @modelcontextprotocol/server-github
```

## Environment Configuration

The project uses environment variables for configuration. Copy the example file and customize:

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with your settings
```

### Foundry Local Settings

Configure your local AI service endpoint and default model settings:

```bash
# Foundry Local endpoint (automatically detected if running)
FOUNDRY_LOCAL_ENDPOINT=http://127.0.0.1:58307

# Default model settings for Prompt Flow
FOUNDRY_LOCAL_DEFAULT_MODEL=Phi-3.5-mini-instruct-cuda-gpu
FOUNDRY_LOCAL_DEFAULT_TEMPERATURE=0.7
FOUNDRY_LOCAL_DEFAULT_MAX_TOKENS=256
```

**Note**: The application will automatically detect Foundry Local using `FoundryLocalManager`. Environment variables serve as fallback configuration when auto-detection fails.

## Usage Examples

### 🤖 **AI-Powered Development**
With the MCP servers configured, you can:

- **Code Generation**: Use Azure AI models to generate code based on your repository context
- **Documentation**: Automatically generate documentation from your codebase
- **Code Review**: Get AI-powered code reviews and suggestions
- **Prompt Engineering**: Test and refine prompts with real-time feedback

### 📊 **Data Operations**
- **Database Queries**: Use SQLite server for local data analysis
- **File Processing**: Batch process files in your workspace
- **Git Operations**: Automate version control workflows
- **Repository Analysis**: Analyze code patterns and dependencies

### ☁️ **Azure Integration**
- **Model Deployment**: Deploy AI models to Azure AI Foundry
- **Resource Management**: Manage Azure resources programmatically
- **Monitoring**: Track model performance and usage
- **Scaling**: Auto-scale AI workloads based on demand

## 🧪 **Testing & Development Scripts**

### **app.py - Foundry Local Test Script**

The `src/app.py` script is a comprehensive testing tool for validating Foundry Local connectivity and functionality.

#### **Purpose:**
- ✅ Test Foundry Local service connectivity
- ✅ List available models and their status
- ✅ Perform chat completion tests
- ✅ Validate API endpoint functionality
- ✅ Debug connection issues

#### **Prerequisites:**
1. **Foundry Local Application** must be running
2. **At least one model** must be loaded in Foundry Local
3. **Python environment** must be activated

#### **Usage:**

```bash
# Navigate to project root
cd prompt-flow-poc

# Activate virtual environment
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # macOS/Linux

# Run the test script
python src/app.py
```

#### **Expected Output:**

```bash
🔍 Testing Foundry Local connectivity...
✅ Foundry Local service is running
🔗 Service endpoint: http://127.0.0.1:58307
✅ Available models:
   - Phi-3-mini-4k-instruct-cuda-gpu (Phi-3 Mini 4K Instruct (GPU))
   - Phi-3.5-mini-instruct-cuda-gpu (None)

🚀 Testing chat completion with model: Phi-3-mini-4k-instruct-cuda-gpu

💬 Chat Response:
--------------------------------------------------
The golden ratio, often denoted by the Greek letter phi (Φ), is an irrational 
number approximately equal to 1.6180339887498...
--------------------------------------------------
✅ Test completed successfully!
```

#### **Features:**
- ** Model Detection**: Lists all loaded models with display names and metadata
- **🛡️ Error Handling**: Comprehensive error handling with helpful diagnostic messages
- **📡 API Testing**: Tests both model listing and chat completion endpoints
- **⏱️ Timeout Management**: Configurable timeouts for reliable testing
- **🔗 Fixed Endpoint**: Uses configured endpoint http://127.0.0.1:58307
- **📈 Status Reporting**: Clear success/failure indicators with emoji feedback

#### **Troubleshooting:**

**❌ "Foundry Local is not running"**
```bash
# Solution: Start Foundry Local application
# Ensure it shows: 🟢 Service is already running on http://127.0.0.1:XXXX/
```

**❌ "No models available"**
```bash
# Solution: Load a model in Foundry Local
# 1. Open Foundry Local app
# 2. Download a model (e.g., Phi-3.5-mini)
# 3. Click "Load" to activate the model
```

**❌ "Could not connect to Foundry Local"**
```bash
# Solution: Check port and firewall
# 1. Verify Foundry Local is running
# 2. Check Windows Firewall settings
# 3. Try different ports: 1234, 58307
```

**❌ "Error making chat completion request"**
```bash
# Solution: Model issues
# 1. Ensure model is fully loaded (not just downloaded)
# 2. Check model has sufficient memory
# 3. Restart Foundry Local if needed
```

#### **Development Notes:**
- Uses `FoundryLocalManager` for automatic service detection
- Falls back to `FOUNDRY_LOCAL_ENDPOINT` environment variable if auto-detection fails
- Makes direct HTTP requests to detected endpoint
- Designed for debugging and validation workflows
- All configuration externalized to `.env` file for easy customization

### **new-chat-flow - Prompt Flow Integration**

The `src/new-chat-flow/` directory contains a complete Prompt Flow that integrates with Foundry Local for conversational AI workflows.

#### **Purpose:**
- 🔄 Provide conversational AI through Prompt Flow
- 🔗 Integrate with Foundry Local without authentication
- ⚙️ Configurable LLM parameters (temperature, max_tokens, etc.)
- 💬 Support chat history for multi-turn conversations
- 🎛️ VS Code extension compatibility

#### **Key Features:**
- **🚀 Zero-Config Setup**: No API keys or authentication required
- **🎛️ Full Parameter Control**: Temperature, max_tokens, top_p, stop sequences
- **💬 Chat History Support**: Multi-turn conversations with context preservation
- **🔄 Model Switching**: Easy switching between available Foundry Local models
- **🏗️ Custom Architecture**: Direct API integration bypassing standard LLM limitations
- **📊 Real-time Validation**: Built-in flow validation and error reporting
- **🖥️ IDE Integration**: Seamless VS Code Prompt Flow extension support
- **⚡ High Performance**: Direct HTTP calls for optimal response times

#### **Key Files:**
```
src/new-chat-flow/
├── flow.dag.yaml          # Flow configuration and parameters
├── foundry_chat.py        # Custom Python tool for Foundry Local API
├── chat.jinja2           # Original chat template (not used)
├── README.md             # Flow-specific documentation
├── azure_openai.yaml     # Original Azure connection (not used)
└── openai.yaml           # Original OpenAI connection (not used)
```

**Note:** Dependencies are managed through the main `pyproject.toml` file at the project root.

#### **Usage:**

**Command Line Testing:**
```bash
# Navigate to flow directory
cd src/new-chat-flow

# Test with default inputs
python -m promptflow._cli._pf.entry flow test --flow .

# Test with custom inputs
python -m promptflow._cli._pf.entry flow test --flow . --inputs \
  question="Tell me about AI" \
  temperature=0.9 \
  max_tokens=200

# Test with different model
python -m promptflow._cli._pf.entry flow test --flow . --inputs \
  question="Hello!" \
  model="Phi-3-mini-4k-instruct-cuda-gpu"
```

**VS Code Extension:**
1. Open the `new-chat-flow` folder in VS Code
2. Install the Prompt Flow extension
3. Click "Test Flow" in the extension
4. Adjust parameters in the UI as needed

#### **Configurable Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `question` | string | "Hello! How can you help me today?" | User input/question |
| `chat_history` | list | `[]` | Previous conversation messages |
| `temperature` | double | `0.7` | Controls creativity (0.0-2.0) |
| `max_tokens` | int | `256` | Maximum response length |
| `model` | string | `"Phi-3.5-mini-instruct-cuda-gpu"` | Model to use |
| `top_p` | double | `1.0` | Nucleus sampling (0.0-1.0) |
| `stop` | list | `[]` | Stop sequences |

#### **Custom Integration:**
The flow uses a custom Python tool (`foundry_chat.py`) that:
- Makes direct HTTP calls to Foundry Local API
- Bypasses authentication requirements
- Provides full parameter control
- Handles errors gracefully
- Supports chat history formatting
- Uses project-wide dependencies from `pyproject.toml` (no separate requirements.txt needed)

#### **Example Response:**
```json
{
    "answer": "Hello! I'm Phi, an AI language model, and I'm here to assist you with a wide range of tasks. I can help with answering questions, writing, analysis, coding, and much more. What would you like to work on today?"
}
```

## 🚀 **Quick Start Guide**

### **1. Setup Environment**
```bash
# Clone and setup
git clone <your-repo>
cd prompt-flow-poc

# Install dependencies
uv sync

# Activate environment
.venv\Scripts\activate  # Windows
```

### **2. Start Foundry Local**
```bash
# Start Foundry Local application
# Ensure you see: 🟢 Service is already running on http://127.0.0.1:XXXX/
```

### **3. Test Basic Connectivity**
```bash
# Test Foundry Local connection
python src/app.py
```

### **4. Test Prompt Flow**
```bash
# Test the chat flow
cd src/new-chat-flow
python -m promptflow._cli._pf.entry flow test --flow . --inputs question="Hello!"
```

### **5. Use in VS Code**
```bash
# Open flow in VS Code with Prompt Flow extension
code src/new-chat-flow
```

## 📋 **Common Commands**

### **Environment Management**
```bash
# Sync dependencies
uv sync

# Add new package
uv add package-name

# Check environment
uv pip list
```

### **Testing Scripts**
```bash
# Test Foundry Local connectivity
python src/app.py

# Validate flow configuration  
cd src/new-chat-flow
python -m promptflow._cli._pf.entry flow validate --source .

# Test flow with parameters
python -m promptflow._cli._pf.entry flow test --flow . --inputs \
  question="Your question" \
  temperature=0.8 \
  max_tokens=300
```

### **Debugging**
```bash
# Check Foundry Local status
curl http://127.0.0.1:58307/v1/models

# Check if service is running
curl http://127.0.0.1:58307/health  # if available

# List available connections (if any)
python -m promptflow._cli._pf.entry connection list
```

## Project Structure

```
prompt-flow-poc/
├── .env                    # Environment variables (create from .env.example)
├── .env.example           # Template for environment variables
├── .vscode/
│   └── mcp.json          # MCP server configuration
├── data/                 # SQLite database directory
├── main.py              # Main application entry point
├── pyproject.toml       # Python dependencies and project config
├── uv.lock             # Locked dependency versions
└── README.md           # This file
```

## Troubleshooting

### **MCP Server Issues**
```bash
# Check if MCP servers are accessible
npx @modelcontextprotocol/server-filesystem --help
npx @azure/mcp --help

# Verify Azure AI Foundry server
uvx --from git+https://github.com/azure-ai-foundry/mcp-foundry.git run-azure-ai-foundry-mcp --help
```

### **Authentication Issues**
```bash
# Test Azure authentication
az login
az account show

# Test GitHub authentication
source .env && curl -H "Authorization: token $GITHUB_PERSONAL_ACCESS_TOKEN" https://api.github.com/user
```

### **Environment Issues**
```bash
# Reload environment variables
source .env

# Check Python environment
uv python --version
uv pip list
```

## Debugging Guide

### ✅ **New Chat Flow - Foundry Local Integration**

The `new-chat-flow` has been successfully configured to work with Foundry Local. Here's what was debugged and resolved:

#### **Issues Resolved:**
1. **Connection Authentication**: Replaced built-in LLM node with custom Python node to bypass authentication requirements
2. **API Endpoint**: Configured to use correct Foundry Local port (58307) instead of default (1234)
3. **Model Names**: Updated to use correct model ID: `Phi-3.5-mini-instruct-cuda-gpu`
4. **Input Validation**: Added default values for required inputs to work with VS Code extension

#### **Current Configuration:**
- **Custom Python Tool**: `foundry_chat.py` - Direct API calls to Foundry Local
- **API Endpoint**: `http://127.0.0.1:58307/v1/chat/completions`
- **Model**: `Phi-3.5-mini-instruct-cuda-gpu`
- **No Authentication Required**: Foundry Local doesn't require API keys

#### **Testing the Flow:**
```bash
# Command line test
cd src/new-chat-flow
..\..\.venv\Scripts\python.exe -m promptflow._cli._pf.entry flow test --flow . --inputs question="Hello!"

# Validate flow configuration
..\..\.venv\Scripts\python.exe -m promptflow._cli._pf.entry flow validate --source .
```

#### **Prerequisites:**
1. **Foundry Local must be running** on port 58307
2. **Model loaded**: Ensure `Phi-3.5-mini-instruct-cuda-gpu` model is loaded in Foundry Local
3. **Test connectivity**: `curl http://127.0.0.1:58307/v1/models`

### 🔧 **Common Debugging Steps**

#### **Foundry Local Issues**
```bash
# Check if Foundry Local is running
curl http://127.0.0.1:58307/v1/models

# Check service status
curl http://127.0.0.1:58307/health  # if available

# Restart Foundry Local if needed
# Close and reopen Foundry Local application
```

#### **Prompt Flow Issues**
```bash
# Validate flow configuration
cd src/new-chat-flow
..\..\.venv\Scripts\python.exe -m promptflow._cli._pf.entry flow validate --source .

# Test flow with inputs
..\..\.venv\Scripts\python.exe -m promptflow._cli._pf.entry flow test --flow . --inputs question="test"

# Check flow connections (if using any)
..\..\.venv\Scripts\python.exe -m promptflow._cli._pf.entry connection list
```

#### **Python Environment Issues**
```bash
# Check Python environment
uv python --version
.venv\Scripts\python.exe --version

# Reinstall dependencies
uv sync

# Check required packages
.venv\Scripts\pip.exe list | findstr "requests\|promptflow"
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with MCP servers
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [Azure AI Foundry](https://docs.microsoft.com/en-us/azure/ai-foundry/)
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [UV Package Manager](https://github.com/astral-sh/uv)