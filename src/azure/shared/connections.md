# Azure Connection Configurations

This folder contains shared connection configurations for Azure services.

## Connection Files

### azure_openai_connection.yaml
Azure OpenAI service connection configuration.

### azure_ml_connection.yaml  
Azure Machine Learning workspace connection configuration.

## Usage

These connection files can be referenced by flows in the parent directories:

```yaml
# In flow.dag.yaml
nodes:
- name: my_node
  connection: azure_openai_connection  # References shared/azure_openai_connection.yaml
```

## Environment Variables

Make sure these environment variables are set in your `.env` file:

```bash
# Azure OpenAI
AZURE_OPENAI_API_KEY=your-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

# Azure ML / AI Foundry
AZURE_SUBSCRIPTION_ID=your-subscription-id
AZURE_RESOURCE_GROUP=your-resource-group
AZURE_WORKSPACE_NAME=your-workspace-name
```
