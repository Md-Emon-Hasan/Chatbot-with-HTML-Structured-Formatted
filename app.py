import markdown
import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from markupsafe import Markup

# Load .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-pro')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json["question"]
    try:
        response = model.generate_content(user_question)
        # Convert Markdown → HTML
        html_answer = Markup(markdown.markdown(response.text, extensions=['fenced_code']))
        return jsonify({"answer": html_answer})
    except Exception as e:
        return jsonify({"answer": f"<div class='alert alert-danger'>❌ Error: {str(e)}</div>"})

if __name__ == "__main__":
    app.run(debug=True)
