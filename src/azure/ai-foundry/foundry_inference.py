from promptflow import tool
import os
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

@tool
def foundry_inference(model_name: str, input_data: str) -> str:
    """
    Basic Azure AI Foundry model inference
    """
    try:
        # Initialize Azure ML client
        credential = DefaultAzureCredential()
        
        subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
        resource_group = os.getenv("AZURE_RESOURCE_GROUP")
        workspace_name = os.getenv("AZURE_WORKSPACE_NAME")
        
        ml_client = MLClient(
            credential=credential,
            subscription_id=subscription_id,
            resource_group_name=resource_group,
            workspace_name=workspace_name
        )
        
        # This is a starter template - implement your model inference logic here
        result = f"Azure AI Foundry inference with model '{model_name}' for input: '{input_data}'"
        
        return result
        
    except Exception as e:
        return f"Error in Azure AI Foundry inference: {str(e)}"
