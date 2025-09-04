# Prompt Flow POC

This project is a Proof of Concept (POC) for experimenting with Prompt Flow tools and workflows using Model Context Protocol (MCP) servers.

## Features

- **🏠 Local Development Environment**: Complete Python setup with UV package manager
- **🤖 Foundry Local Integration**: Direct integration with local AI models via automatic endpoint detection
- **☁️ Azure Cloud Integration**: Structured Azure OpenAI and AI Foundry workflow organization
- **📊 Model Detection**: Lists all loaded models with display names and metadata
- **🛡️ Error Handling**: Comprehensive error handling with helpful diagnostic messages
- **📡 API Testing**: Tests both model listing and chat completion endpoints
- **⏱️ Timeout Management**: Configurable timeouts for reliable testing
- **🔗 Smart Detection**: Uses FoundryLocalManager for automatic endpoint detection
- **📈 Status Reporting**: Clear success/failure indicators with emoji feedback
- **📦 Modern Dependency Management**: Single `pyproject.toml` configuration  
- **🔧 Multiple MCP Servers**: Enhanced AI capabilities with 7 configured MCP servers
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

### 🔧 **Foundry Local Port Configuration**

**IMPORTANT**: Configure Foundry Local to use a fixed port for consistent connectivity.

#### **One-Time Setup (Recommended)**

Set Foundry Local to always use port 58307:

```bash
# Set the service port (one-time configuration)
foundry service set --port 58307 --show

# Verify the service is running on the correct port
foundry service status
curl http://127.0.0.1:58307/v1/models
```

#### **Configuration Persistence**

The port configuration is **persistent** - you only need to set it once:
- ✅ **Survives application restarts**
- ✅ **Survives system reboots** 
- ✅ **Applies to all future Foundry Local sessions**
- ✅ **Stored in Foundry Local's configuration files**

#### **Verification Commands**

```bash
# Check current service status and port
foundry service status

# View current configuration
foundry service set --show

# Test connectivity
curl http://127.0.0.1:58307/v1/models

# Restart service if needed (keeps same port)
foundry service restart
```

#### **Alternative Ports**

If port 58307 is in use, you can choose alternatives:

```bash
# Use port 11434 (Ollama standard)
foundry service set --port 11434

# Use port 8080 (common web service port)
foundry service set --port 8080

# Use port 5000 (development standard)
foundry service set --port 5000
```

#### **Troubleshooting Port Issues**

```bash
# Check what's using a port
netstat -an | findstr :58307

# Check Foundry Local processes
Get-Process | Where-Object {$_.ProcessName -like "*foundry*"}

# Reset to defaults if needed
foundry service set --defaults --show
```

### 🚀 **Auto-Start Foundry Local Service on System Startup**

Configure Foundry Local to start automatically when your computer boots up.

#### **Method 1: Windows Startup Folder (Simplest - Recommended)**

Create a batch file that automatically starts Foundry Local:

**Step 1: Open Startup Folder**
```powershell
# Open Windows Startup folder
Start-Process shell:startup
```

**Step 2: Create Batch File**
In the Startup folder that opens:
1. **Right-click** → **New** → **Text Document**
2. **Rename** to: `foundry-autostart.bat` (change extension from .txt to .bat)
3. **Right-click** the file → **Edit**
4. **Add this content:**

```batch
@echo off
REM Wait 10 seconds for system to fully boot
timeout /t 10 /nobreak >nul

REM Start Foundry Local service
foundry service start

REM Optional: Show confirmation (remove if you don't want popup)
echo Foundry Local started successfully!
timeout /t 3 /nobreak >nul
```

5. **Save and close**

**Step 3: Test the Batch File**
```powershell
# Test by double-clicking the batch file
# Or run from PowerShell:
& "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\foundry-autostart.bat"
```

#### **Alternative: Minimal Batch File**

For a simpler version without delays or messages:

```batch
@echo off
foundry service start
```

#### **Method 2: Windows Settings UI**

If Foundry Local appears in Windows Settings:

```powershell
# Open Startup Apps settings
Start-Process ms-settings:startupapps

# Look for "Foundry Local" or "Microsoft Foundry Local"
# Toggle it ON if found
```

#### **Method 3: Windows Task Scheduler (Advanced)**

Create a scheduled task for more control:

```powershell
# Open Task Scheduler (taskschd.msc)
# Or use PowerShell to create the task:

$Action = New-ScheduledTaskAction -Execute "foundry" -Argument "service start"
$Trigger = New-ScheduledTaskTrigger -AtStartup
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
$Task = New-ScheduledTask -Action $Action -Trigger $Trigger -Settings $Settings

# Register the task
Register-ScheduledTask -TaskName "FoundryLocalAutoStart" -InputObject $Task -User $env:USERNAME
```

#### **Method 3: Windows Service (Advanced)**

If you want Foundry Local to run as a true Windows service:

```powershell
# Install NSSM (Non-Sucking Service Manager)
# Download from: https://nssm.cc/download

# Create service using NSSM
nssm install FoundryLocal "foundry"
nssm set FoundryLocal AppParameters "service start"
nssm set FoundryLocal DisplayName "Foundry Local AI Service"
nssm set FoundryLocal Description "Local AI model inference service"
nssm set FoundryLocal Start SERVICE_AUTO_START

# Start the service
nssm start FoundryLocal
```

#### **Method 4: PowerShell Profile Auto-Start**

Add to your PowerShell profile for automatic start when opening PowerShell:

```powershell
# Edit your PowerShell profile
notepad $PROFILE

# Add this line to auto-start Foundry Local
if (!(Get-Process foundry -ErrorAction SilentlyContinue)) {
    Start-Process -FilePath "foundry" -ArgumentList "service", "start" -NoNewWindow
}
```

#### **Method 5: Registry Startup Entry**

Add Foundry Local to Windows Registry startup entries:

```powershell
# Add registry entry for auto-start
$RegPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
$AppName = "FoundryLocal"
$AppPath = "foundry service start"

Set-ItemProperty -Path $RegPath -Name $AppName -Value $AppPath
```

#### **Verification Commands**

Check if auto-start is working:

```bash
# Check if Foundry Local is running
foundry service status

# Check system startup programs
Get-CimInstance -ClassName Win32_StartupCommand | Where-Object {$_.Name -like "*foundry*"}

# Check scheduled tasks
Get-ScheduledTask | Where-Object {$_.TaskName -like "*foundry*"}

# Check Windows services
Get-Service | Where-Object {$_.Name -like "*foundry*"}
```

#### **Recommended Approach**

For most users, **Method 2 (Task Scheduler)** is recommended because:
- ✅ Runs with proper user permissions
- ✅ Handles startup delays gracefully
- ✅ Easy to modify or disable
- ✅ Reliable across Windows updates
- ✅ Built into Windows (no additional software needed)

### Azure Settings

Configure Azure services for cloud-based AI workflows:

```bash
# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY=your-azure-openai-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name

# Azure AI Foundry Configuration  
AZURE_AI_FOUNDRY_PROJECT_ID=your-project-id
AZURE_AI_FOUNDRY_ENDPOINT=https://your-endpoint.cognitiveservices.azure.com/
```

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

### **local/ - Local AI Development**

The `src/local/` directory contains Prompt Flow configurations for **local AI development** using Foundry Local.

#### **Purpose:**
- 🏠 **Local Development**: Complete local AI setup without cloud dependencies
- 🔗 **Foundry Local Integration**: Direct integration with local Foundry Local service
- ⚙️ **Configuration Management**: Environment-based configuration for local development
- 💬 **Chat Capabilities**: Multi-turn conversations with local AI models

#### **Key Features:**
- **🚀 Zero Cloud Dependencies**: Everything runs locally
- **🎛️ Full Parameter Control**: Temperature, max_tokens, top_p, stop sequences
- **💬 Chat History Support**: Multi-turn conversations with context preservation
- **� Model Switching**: Easy switching between available Foundry Local models
- **🛡️ Error Handling**: Graceful error handling with informative messages
- **⚡ High Performance**: Direct HTTP calls for optimal response times

#### **Usage:**
```bash
# Test the local flow
cd src/local
python -m promptflow._cli._pf.entry flow test --flow . --inputs question="What is AI?"

# Validate flow configuration
python -m promptflow._cli._pf.entry flow validate --source .
```

#### **Local Development Workflow:**
1. **Start Foundry Local**: Launch the Foundry Local application
2. **Load a Model**: Download and load a model (e.g., Phi-3.5-mini)
3. **Configure Environment**: Set up your `.env` file with local settings
4. **Test Flow**: Use the commands above to test your local AI setup
5. **Develop**: Build and test your AI workflows locally before cloud deployment

### **azure/ - Azure Hosted Remote Flows**

The `src/azure/` directory contains Prompt Flow configurations for **Azure hosted remote AI services**.

#### **Purpose:**
- ☁️ **Cloud Development**: Azure-hosted AI model integration  
- 🔐 **Authentication**: Azure AD and API key management
- 🏗️ **Enterprise Scale**: Production-ready cloud workflows
- 🔄 **Remote Execution**: Flows that run on Azure infrastructure

#### **Structure:**
```
azure/
├── openai/              # Azure OpenAI flows
├── ai-foundry/          # Azure AI Foundry flows
├── shared/              # Common Azure configurations
└── README.md           # Azure documentation
```

#### **Key Features:**
- **🤖 Azure OpenAI Integration**: GPT models, embeddings, and completions
- **🏭 AI Foundry Support**: Model deployment and management workflows
- **🔐 Enterprise Security**: Azure AD authentication and role-based access
- **📊 Monitoring & Analytics**: Built-in performance tracking
- **🚀 Scalable Deployment**: Auto-scaling cloud infrastructure
- **🔄 MLOps Integration**: End-to-end machine learning operations

#### **Environment Configuration:**
Azure flows require additional environment variables:
```bash
# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY=your-azure-openai-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview

# Azure AI Foundry Configuration
AZURE_AI_FOUNDRY_PROJECT_ID=your-project-id
AZURE_AI_FOUNDRY_ENDPOINT=https://your-endpoint.cognitiveservices.azure.com/
```

#### **Usage:**
```bash
# Navigate to Azure OpenAI flows
cd src/azure/openai

# Navigate to Azure AI Foundry flows
cd src/azure/ai-foundry

# Test Azure connectivity (when flows are added)
python -m promptflow._cli._pf.entry flow test --flow . --inputs question="Hello from Azure!"
```

#### **Getting Started with Azure:**
1. **Create Azure Resources**: Set up Azure OpenAI or AI Foundry resources
2. **Configure Authentication**: Set up service principals and API keys
3. **Deploy Models**: Deploy your preferred models (GPT-4, custom models)
4. **Test Connectivity**: Validate connections before building flows
5. **Deploy Flows**: Deploy to Azure for production use

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
src/local/
├── test_local_foundry.py  # Standalone connectivity test and chat completion script
├── demo-chat-flow/        # ✅ Working Prompt Flow implementation
│   ├── flow.dag.yaml      # Flow configuration and parameters
│   ├── foundry_chat.py    # Custom Python tool for Foundry Local API
│   ├── chat.jinja2        # Chat template with history support
│   └── README.md          # Flow-specific documentation
└── README.md             # Local development documentation
```

**Note:** Dependencies are managed through the main `pyproject.toml` file at the project root.

#### **Usage:**

**Quick Connectivity Test:**
```bash
# Navigate to local directory
cd src/local

# Run connectivity test
python test_local_foundry.py

# Test Prompt Flow implementation
cd demo-chat-flow
python -m promptflow._cli._pf.entry flow test --flow . --inputs question="What is AI?"

# Test with custom parameters
python -m promptflow._cli._pf.entry flow test --flow . --inputs question="Tell me about the golden ratio" temperature=0.9 max_tokens=100
```

**VS Code Extension:**
1. Open the `demo-chat-flow` folder in VS Code
2. Install the Prompt Flow extension
3. Click "Test Flow" in the extension

**Current Status:**
- ✅ `test_local_foundry.py`: Fully functional connectivity test with chat completion
- ✅ `demo-chat-flow/`: Working Prompt Flow implementation with Foundry Local integration
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

### **2. Configure Foundry Local Port (One-Time Setup)**
```bash
# Set fixed port for Foundry Local (only needs to be done once)
foundry service set --port 58307 --show

# Verify configuration
foundry service status
curl http://127.0.0.1:58307/v1/models
```

### **3. Start Foundry Local**
```bash
# Start Foundry Local application (if not already running)
# Should now show: 🟢 Service is already running on http://127.0.0.1:58307/

# OPTIONAL: Set up auto-start on system boot (see Auto-Start section below)
# Recommended: Use Task Scheduler method for automatic startup
```

### **4. Test Basic Connectivity**
```bash
# Test Foundry Local connection
python src/app.py
```

### **5. Test Prompt Flow**
```bash
# Test the local chat flow
cd src/local
python -m promptflow._cli._pf.entry flow test --flow . --inputs question="Hello!"

# Or explore Azure flows (when configured)
cd src/azure/openai  # or ai-foundry
```

### **6. Use in VS Code**
```bash
# Open local flow in VS Code with Prompt Flow extension
code src/local

# Or open Azure flows
code src/azure/openai
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

# Validate local flow configuration  
cd src/local
python -m promptflow._cli._pf.entry flow validate --source .

# Test local flow with parameters
python -m promptflow._cli._pf.entry flow test --flow . --inputs \
  question="Your question" \
  temperature=0.8 \
  max_tokens=300

# Test Azure flows (when configured)
cd src/azure/openai
python -m promptflow._cli._pf.entry flow validate --source .
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
├── src/                # Source code and flows
│   ├── app.py          # Main connectivity test script
│   ├── local/          # Local AI development (Foundry Local)
│   └── azure/          # Azure hosted remote flows
│       ├── openai/     # Azure OpenAI flows
│       ├── ai-foundry/ # Azure AI Foundry flows
│       └── shared/     # Common Azure configurations
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

### ✅ **Local Flow - Foundry Local Integration**

The `local` flow has been successfully configured to work with Foundry Local. Here's what was debugged and resolved:

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
cd src/local
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
cd src/local
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