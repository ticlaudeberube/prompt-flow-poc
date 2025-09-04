import os
import requests
import json
from dotenv import load_dotenv
from promptflow.core import tool
from foundry_local import FoundryLocalManager

# Load environment variables
load_dotenv()


@tool
def chat(
    question: str, 
    chat_history: list = None, 
    temperature: float = None,
    max_tokens: int = None,
    model: str = None,
    top_p: float = 1.0,
    stop: list = None
) -> str:
    """
    Custom tool to call Foundry Local API directly without authentication
    
    Args:
        question: The user's question or prompt
        chat_history: Previous conversation messages
        temperature: Controls randomness in generation (0.0 to 2.0)
        max_tokens: Maximum number of tokens to generate
        model: The model name to use for generation
        top_p: Controls diversity via nucleus sampling (0.0 to 1.0)
        stop: List of strings where generation should stop
    """
    
    # Use environment variables for defaults
    if temperature is None:
        temperature = float(os.getenv('FOUNDRY_LOCAL_DEFAULT_TEMPERATURE', '0.7'))
    if max_tokens is None:
        max_tokens = int(os.getenv('FOUNDRY_LOCAL_DEFAULT_MAX_TOKENS', '256'))
    if model is None:
        model = os.getenv('FOUNDRY_LOCAL_DEFAULT_MODEL', 'Phi-3.5-mini-instruct-cuda-gpu')
    
    # Prepare messages
    messages = []
    
    # Add chat history if provided
    if chat_history:
        messages.extend(chat_history)
    
    # Add current question
    messages.append({"role": "user", "content": question})
    
    # Prepare the request payload
    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p
    }
    
    # Add stop sequences if provided
    if stop and len(stop) > 0:
        payload["stop"] = stop
    
    # Get endpoint from FoundryLocalManager or environment variable
    endpoint = None
    
    # Try to use FoundryLocalManager first
    try:
        manager = FoundryLocalManager()
        if manager.is_running():
            endpoint = manager.get_endpoint()
    except Exception:
        pass
    
    # Fall back to environment variable if auto-detection fails
    if not endpoint:
        endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT', 'http://127.0.0.1:58307')
    
    # Make the API call to Foundry Local
    try:
        response = requests.post(
            f"{endpoint}/v1/chat/completions",
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        
        result = response.json()
        return result["choices"][0]["message"]["content"]
        
    except requests.exceptions.RequestException as e:
        return f"Error calling Foundry Local: {str(e)}"
    except (KeyError, IndexError) as e:
        return f"Error parsing response: {str(e)}"


if __name__ == "__main__":
    # Test the function when run directly
    print("Testing Foundry Chat function...")
    test_response = chat(
        question="What is the golden ratio? Please be concise.",
        temperature=0.7,
        max_tokens=150
    )
    print("Test Response:")
    print(test_response)