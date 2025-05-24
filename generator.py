import requests
from config import HUGGINGFACE_API_KEY, LLM_MODEL

def generate_response(prompt):
    headers = {
        "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
        "Content-Type": "application/json"
    }

    url = f"https://router.huggingface.co/novita/v3/openai/chat/completions"
    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt
                }
            ],
        "model": f"{LLM_MODEL}"
    }

    response = requests.post(url, headers=headers, json=payload)

    print("Status code:", response.status_code)
    print("Response content:", response.text)

    if response.status_code == 200:
        try:
            result = response.json()
            if isinstance(result, dict) and "choices" in result:
                return result["choices"][0]["message"]["content"]
            else:
                print("⚠️ Unexpected response structure:", result)
                return "Sorry, I couldn't generate a response."
        except Exception as e:
            print("❌ JSON parsing error:", e)
            return "Error: Failed to parse API response."
    elif response.status_code == 503:
        # Model is loading or unavailable
        return "The model is loading, please try again shortly."
    elif response.status_code == 429:
        return "Rate limit exceeded, please wait before retrying."
    elif response.status_code in (401, 403):
        return "Authentication failed. Check your API key and permissions."
    else:
        return f"API error {response.status_code}: {response.text}"
