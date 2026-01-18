import os
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def chatgpt_career_guidance(skills):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are an AI career guidance expert."
            },
            {
                "role": "user",
                "content": f"Suggest career paths and next skills for someone with skills: {skills}"
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]
