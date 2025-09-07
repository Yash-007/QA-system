import os
from google import generativeai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')
generativeai.configure(api_key=api_key)

model = generativeai.GenerativeModel(
    'gemini-1.5-flash-002',
    )

def ask_query(query: str):
    try:
        response = model.generate_content(query)
        return response.text

    except Exception as e:
        print("error is:", e)
        return e