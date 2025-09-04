# Azure OpenAI Flows

This folder contains Prompt Flow configurations for **Azure OpenAI Service**.

## What is Azure OpenAI?

Azure OpenAI provides access to **OpenAI's pre-built models** hosted on Azure infrastructure:

### 🎯 **Primary Use Cases:**
- **Enterprise GPT Access**: Use GPT-4, GPT-3.5-turbo with enterprise security
- **Text Generation**: Advanced text completion and content creation
- **Conversational AI**: Build chatbots and virtual assistants
- **Content Analysis**: Text summarization, sentiment analysis, extraction

### 🆚 **vs. Other Services:**
| Service | Purpose |
|---------|---------|
| **Azure OpenAI** | Pre-built models (GPT-4, GPT-3.5, etc.) |
| **Azure AI Foundry** | Custom/fine-tuned models, MLOps |
| **Foundry Local** | Local development/testing |

### 💡 **When to Use:**
- Need access to latest GPT models
- Require enterprise-grade security and compliance
- Want Azure integration (networking, authentication)
- Building production conversational AI applications

## Features

- **🤖 GPT Models**: Integration with GPT-3.5, GPT-4, and other Azure OpenAI models
- **📝 Text Generation**: Advanced text completion and generation workflows
- **🔍 Embeddings**: Text embedding generation for search and similarity
- **💬 Chat Completion**: Conversational AI with Azure OpenAI

## Environment Variables

Required environment variables for Azure OpenAI:

```bash
AZURE_OPENAI_API_KEY=your-azure-openai-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
```

## Getting Started

1. Create an Azure OpenAI resource in Azure Portal
2. Deploy a model (e.g., GPT-3.5-turbo, GPT-4)
3. Configure environment variables
4. Test the flows in this folder

## Starter Template

This folder includes a basic Azure OpenAI chat completion flow:

- `flow.dag.yaml` - Main flow definition with LLM node
- `chat_completion.jinja2` - Chat prompt template (**ready to use**)
- `requirements.txt` - Python dependencies

### 📝 **Implementation Notes:**
The Azure OpenAI flow is **production-ready** and provides:
- ✅ Complete chat completion workflow
- ✅ Configurable temperature and max tokens
- ✅ Jinja2 prompt templating
- ✅ Azure OpenAI connection integration

### 🔧 **Ready to Use:**
```yaml
# The flow uses standard Azure OpenAI API:
- type: llm
  api: chat
  connection: azure_openai_connection
  inputs:
    temperature: 0.7
    max_tokens: 800
```

### Running the Flow

```bash
# Install dependencies
pip install -r requirements.txt

# Run the flow
pf flow test --flow . --inputs question="What can you help me with?"
```
