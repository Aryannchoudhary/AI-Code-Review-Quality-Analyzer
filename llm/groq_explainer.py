import requests
import streamlit as st


GROQ_API_KEY = st.secrets("GROQ_API_KEY")

def explain_code_quality(code, prediction, features):

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You are a senior code reviewer."},
            {"role": "user", "content": f"""
Code: {code}
Prediction: {prediction}
Features: {features}

Explain issues and improvements.
"""}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    # SAFE HANDLING (IMPORTANT)
    if "choices" not in result:
        return f"LLM Error: {result}"

    return result["choices"][0]["message"]["content"]