import requests


def explain_code_quality(
    code,
    prediction,
    features
):

    prompt = f"""
You are an AI code reviewer.

Code Quality Prediction: {prediction}

Code Metrics:
{features}

Analyze this code and explain:

1. Why the quality was predicted this way
2. Main issues in the code
3. Suggestions for improvement

Code:
{code}
"""

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()

        print(result)

        if "response" in result:
            return result["response"]

        elif "error" in result:
            return f"Ollama Error: {result['error']}"

        else:
            return "Unexpected response from Ollama."

    except Exception as e:
        return f"Connection Error: {str(e)}"