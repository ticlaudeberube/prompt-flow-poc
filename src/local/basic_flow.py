from promptflow import tool
from foundry_local_sdk import FoundryLocalClient

@tool
def foundry_chat(question: str) -> str:
    """Use Foundry Local for chat completion in Prompt Flow"""
    
    client = FoundryLocalClient()
    
    if not client.is_service_running():
        return "Error: Foundry Local is not running"
    
    models = client.list_models()
    if not models:
        return "Error: No models available in Foundry Local"
    
    model_name = models[0].name
    
    response = client.chat_completion(
        model=model_name,
        messages=[{"role": "user", "content": question}]
    )
    
    return response.choices[0].message.content