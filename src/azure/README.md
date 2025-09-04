# Azure Hosted Remote Flows

This folder contains Prompt Flow configurations for **Azure hosted remote AI services**.

## Structure

```
azure/
├── openai/              # Azure OpenAI flows
├── ai-foundry/          # Azure AI Foundry flows
├── shared/              # Common Azure configurations
└── README.md           # This documentation
```

## Purpose

- **☁️ Cloud Development**: Azure-hosted AI model integration
- **🔐 Authentication**: Azure AD and API key management
- **🏗️ Enterprise Scale**: Production-ready cloud workflows
- **🔄 Remote Execution**: Flows that run on Azure infrastructure

## Environment Configuration

Configure your Azure settings in the project's `.env` file:

```bash
# Azure Configuration
AZURE_SUBSCRIPTION_ID=your-subscription-id-here
AZURE_TENANT_ID=your-tenant-id-here
AZURE_CLIENT_ID=your-client-id-here
AZURE_CLIENT_SECRET=your-client-secret-here

# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY=your-azure-openai-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview

# Azure AI Foundry Configuration
AZURE_AI_FOUNDRY_PROJECT_ID=your-project-id
AZURE_AI_FOUNDRY_ENDPOINT=https://your-workspace.workspaces.api.azureml.ms
```

## Folders

### 🤖 **openai/**
Azure OpenAI Service integrations for GPT models, embeddings, and completions.

### 🏭 **ai-foundry/**
Azure AI Foundry workflows for model deployment, fine-tuning, and management.

### 🔧 **shared/**
Common Azure configurations, connections, and utilities shared across flows.

## Getting Started

1. **Configure Azure Credentials**: Set up your `.env` file with Azure credentials
2. **Choose Your Service**: Navigate to the appropriate subfolder (openai, ai-foundry)
3. **Test Connectivity**: Use the provided test scripts to validate connections
4. **Deploy Flows**: Deploy flows to Azure for production use

## Authentication

This folder requires Azure authentication. See the main project README for detailed setup instructions for:
- Azure Portal configuration
- Service Principal creation
- API key generation
