# Azure AI Foundry Flows

This folder contains Prompt Flow configurations for **Azure AI Foundry**.

## What is Azure AI Foundry Inference?

Azure AI Foundry inference is designed for **enterprise-scale custom AI model deployment**:

### 🎯 **Primary Use Cases:**
- **Custom Model Deployment**: Deploy your own fine-tuned models
- **Enterprise MLOps**: Production-ready model serving with versioning
- **Multi-Model Management**: Deploy and manage multiple AI models
- **Advanced AI Workflows**: Combine models in complex pipelines

### 🆚 **vs. Other Services:**
| Service | Purpose |
|---------|---------|
| **Azure OpenAI** | Pre-built models (GPT-4, Claude, etc.) |
| **Azure AI Foundry** | Custom/fine-tuned models, MLOps |
| **Foundry Local** | Local development/testing |

### 💡 **When to Use:**
- You have custom-trained AI models
- Need enterprise-scale model deployment
- Require model versioning and A/B testing
- Want centralized ML model governance

## Features

- **🏭 Model Management**: Deploy and manage AI models at scale
- **🔧 Fine-tuning**: Custom model training and fine-tuning workflows
- **📊 Monitoring**: Model performance tracking and analytics
- **🚀 MLOps**: End-to-end machine learning operations

## Environment Variables

Required environment variables for Azure AI Foundry:

```bash
AZURE_AI_FOUNDRY_PROJECT_ID=your-project-id
AZURE_AI_FOUNDRY_ENDPOINT=https://your-workspace.workspaces.api.azureml.ms
AZURE_SUBSCRIPTION_ID=your-subscription-id
AZURE_TENANT_ID=your-tenant-id
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
```

## Getting Started

1. Create an Azure AI Foundry workspace
2. Set up a project in the workspace
3. Configure authentication credentials
4. Deploy flows to Azure AI Foundry

## Starter Template

This folder includes a basic Azure AI Foundry inference flow:

- `flow.dag.yaml` - Main flow definition
- `foundry_inference.py` - Python inference function (**starter template**)
- `requirements.txt` - Python dependencies

### 📝 **Implementation Notes:**
The `foundry_inference.py` is a **starter template** that provides:
- ✅ Azure ML client setup and authentication
- ✅ Error handling structure
- ⚠️ **Needs custom implementation** of actual model inference logic

### 🔧 **To Complete Implementation:**
```python
# Add to foundry_inference.py:
endpoint = ml_client.online_endpoints.get(name=model_name)
response = ml_client.online_endpoints.invoke(
    endpoint_name=model_name,
    request_file=input_data,
    deployment_name="default"
)
```

### Running the Flow

```bash
# Install dependencies
pip install -r requirements.txt

# Run the flow
pf flow test --flow . --inputs model_name="gpt-35-turbo" input_data="Hello AI Foundry!"
```
