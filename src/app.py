"""
Foundry Local Test Script

Usage:
1. Start Foundry Local Windows app
2. Load a model (e.g., phi-3.5-mini) in the app
3. Run: python src/app.py

Purpose:
- Test Foundry Local connectivity
- Verify model availability
- Quick testing and debugging

For Prompt Flow integration, use flows/basic_flow.py instead
"""

import os
import requests
from dotenv import load_dotenv
from foundry_local import FoundryLocalManager

# Load environment variables from .env file
load_dotenv()

def main():
    print("🔍 Testing Foundry Local connectivity...")
    
    endpoint = None
    
    # Try to use FoundryLocalManager first
    try:
        manager = FoundryLocalManager()
        
        # Check if service is running
        if manager.is_service_running():
            endpoint = manager.endpoint
            # Remove /v1 suffix if present to avoid double /v1
            if endpoint.endswith('/v1'):
                endpoint = endpoint[:-3]
            print("✅ Foundry Local service is running")
            print(f"🔗 Service endpoint (auto-detected): {endpoint}")
        else:
            print("⚠️ FoundryLocalManager couldn't detect running service")
            
    except Exception as e:
        print(f"⚠️ FoundryLocalManager error: {e}")
    
    # Fallback to environment variable if auto-detection failed
    if not endpoint:
        endpoint = os.getenv('FOUNDRY_LOCAL_ENDPOINT')
        if endpoint:
            print(f"🔗 Using endpoint from .env file: {endpoint}")
        else:
            print("❌ No endpoint found. Please start Foundry Local or configure FOUNDRY_LOCAL_ENDPOINT in .env")
            print("💡 Make sure Foundry Local is running or set FOUNDRY_LOCAL_ENDPOINT=http://127.0.0.1:58307 in .env")
            return False

    # List available models via HTTP API
    try:
        response = requests.get(f"{endpoint}/v1/models", timeout=10)
        response.raise_for_status()
        
        models_data = response.json()
        models = models_data.get("data", [])
        
        if not models:
            print("❌ No models available. Please load a model in Foundry Local.")
            return False
            
        print(f"✅ Available models:")
        for model in models:
            print(f"   - {model.get('id', 'Unknown')} ({model.get('display_name', 'No display name')})")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error listing models: {e}")
        return False
    except Exception as e:
        print(f"❌ Error parsing models response: {e}")
        return False

    # Use the first available model for testing
    model_id = models[0]["id"]
    print(f"\n� Testing chat completion with model: {model_id}")
    
    # Make a chat completion request
    try:
        chat_response = requests.post(
            f"{endpoint}/v1/chat/completions",
            headers={"Content-Type": "application/json"},
            json={
                "model": model_id,
                "messages": [{"role": "user", "content": "What is the golden ratio? Please be concise."}],
                "max_tokens": 150,
                "temperature": 0.7
            },
            timeout=30
        )
        
        chat_response.raise_for_status()
        result = chat_response.json()
        
        print("\n💬 Chat Response:")
        print("-" * 50)
        print(result["choices"][0]["message"]["content"])
        print("-" * 50)
        print("✅ Test completed successfully!")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error making chat completion request: {e}")
        return False
    except (KeyError, IndexError) as e:
        print(f"❌ Error parsing chat response: {e}")
        print(f"Response: {result if 'result' in locals() else 'No response'}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)