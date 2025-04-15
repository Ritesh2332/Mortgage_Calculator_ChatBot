import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment!")

# Configure
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

def get_mortgage_advice(principal, rate, years):
    prompt = (
        f"I am taking a home loan of ₹{principal} for {years} years at an interest rate of {rate}%. "
        "Please provide some brief financial advice or insight for this mortgage plan."
    )

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Could not get AI advice: {e}"
