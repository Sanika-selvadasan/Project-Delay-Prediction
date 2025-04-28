import os
import requests
from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-70b-8192"

# Function to call Groq API
def get_mitigation_strategy(features, prediction):
    prompt = f"""
    A project task has the following characteristics:
    - Risk Level: {features['Risk']}
    - Priority: {features['Priority']}
    - Planned Hours: {features['Hours']}
    - Delay: {features['Delay']} (Note: A negative delay value indicates the number of days left before the task's deadline; a positive delay means the task is overdue.)
    - Root Cause: {features['RootCause']}
    - Predicted Overdue: {"Yes" if prediction else "No"}

    Considering these factors, suggest a single, actionable mitigation strategy to prevent or minimize the potential delay. Focus on how we should adjust one or more of the task's characteristics or introduce a specific action. Explain your reasoning briefly.

    """

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful project management assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 500
    }

    response = requests.post(GROQ_URL, headers=headers, json=payload)
    response.raise_for_status()
    result = response.json()

    return result['choices'][0]['message']['content']
