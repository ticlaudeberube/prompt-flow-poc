# Prompt Flow POC

This project is a Proof of Concept (POC) for experimenting with Prompt Flow tools and workflows using Model Context Protocol (MCP) servers.

## Features

- Local development environment setup
- Integration with `promptflow-tools`
- Multiple MCP servers for enhanced AI capabilities
- Azure AI Foundry integration
- GitHub integration for repository management
- Example flows and usage instructions

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