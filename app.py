import csv  
from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai 
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.0-flash")

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    question = ""
    response = ""

    if request.method == 'POST':
        question = request.form['question']
        try:
            response = model.generate_content(question).text
        except Exception as e:
            response = f"Erro ao processar a pergunta: {e}"

    return render_template('chat.html', question=question, response=response)

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)