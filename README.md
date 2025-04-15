🏠 Mortgage Calculator Chatbot with Gemini AI
Welcome to the Mortgage Calculator Chatbot, an AI-powered Streamlit web application that helps users estimate their monthly home loan payments and provides smart financial advice using Google's Gemini AI.

🔗[🚀 Try the Live App](https://mortgagecalculatorchatbot-ritesh2332.streamlit.app/)

📌 Features
✅ Monthly Mortgage Calculation based on principal, interest rate, and term

🤖 AI-Powered Financial Advice using Gemini 2.0 Flash

🌐 Streamlit Web Interface – no installation needed for end users

🔐 Secure API key management via .env (locally) and Streamlit secrets (online)

💡 Simple and clean user interface

🧰 Tech Stack

Tool / Library	Purpose
Python	Core programming language
Streamlit	Web app framework
Gemini API (Google)	AI-driven financial advice
python-dotenv	Environment variable management
Git + GitHub	Version control and code hosting

🚀 Live Demo
Click here to use the app instantly (no installation required):
👉 https://mortgagecalculatorchatbot-ritesh2332.streamlit.app/

🖥️ How to Run Locally
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Ritesh2332/Mortgage_Calculator_ChatBot.git
cd Mortgage_Calculator_ChatBot

2. Create .env file
Inside the project folder, create a .env file and add your Gemini API key:

ini
Copy
Edit
GEMINI_API_KEY="your_api_key_here"
🔐 Never share this key publicly

3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Run the App
bash
Copy
Edit
streamlit run app.py
📐 Mortgage Formula Used
𝑀=𝑃⋅(𝑟^(1+𝑟)^𝑛/(1+𝑟)^𝑛−1

Where:
M = monthly payment

P = loan principal

r = monthly interest rate

n = number of total payments

📚 References
Streamlit Docs

Gemini AI by Google

python-dotenv

Google AI Studio

