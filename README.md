# 🚀 Chatbot with HTML Structured Formatted (Flask + Bootstrap)

A full-stack, production-grade Question Answering Chatbot built using **Gemini API**, **Python Flask**, and **Bootstrap**. This app mimics the **ChatGPT-style UI** by rendering structured Markdown responses from Gemini, including code blocks, headers, and lists.

---

## 📸 Demo Preview

<img width="1349" height="712" alt="Image" src="https://github.com/user-attachments/assets/b6fd463b-5b21-4751-a64d-788feb55c6d8" />

---

## 🔧 Tech Stack

| Layer              | Technology                                    |
| ------------------ | --------------------------------------------- |
| Frontend           | HTML, CSS, Bootstrap 5, Vanilla JS            |
| Backend            | Python, Flask                                 |
| AI/LLM             | Google Gemini Pro (via `google-generativeai`) |
| API Key Mgmt       | `python-dotenv`                               |
| Markdown Rendering | `markdown` Python library                     |

---

## ⚙️ Features

* ✅ ChatGPT-style **Markdown rendering** (code blocks, headings, lists)
* ✅ Gemini-powered accurate responses using `gemini-pro`
* ✅ Clean Bootstrap UI with responsive design
* ✅ JavaScript-powered asynchronous chat (no page reload)
* ✅ Error-handling for broken requests
* ✅ Easily extensible to include login, memory, tools, etc.

---

## 📁 Project Structure

```
gemini_chatbot/
├── app.py                     # Flask backend
├── .env                       # API keys (not shared)
├── requirements.txt           # Dependencies
├── templates/
│   └── index.html             # Frontend UI
├── static/
│   └── style.css              # Optional custom styles
```

---

## 🔑 Environment Setup

### 1. Clone the Repo

```bash
git clone https://github.com/<your-username>/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Create `.env` File

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> 🔐 Keep this file private and **never share your API key** publicly.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, manually install:

```bash
pip install flask google-generativeai markdown python-dotenv
```

---

## 🚀 Run the Application

```bash
python app.py
```

Then visit: `http://127.0.0.1:5000`

---

## 💡 Example Prompts

| Prompt                             | Response Style          |
| ---------------------------------- | ----------------------- |
| `Give for loop code in Python`     | Code + explanation      |
| `What is a dictionary in Python?`  | Bullet points + example |
| `Write HTML code for a login form` | Rendered code block     |
| `Explain AI in 3 bullet points`    | Structured Markdown     |

---

## 🛠️ Customization Ideas (Next-Level)

You can easily extend this app into:

* 🔐 User authentication system
* 💬 Persistent chat history (local DB / SQLite)
* 🧠 LangChain or Agentic AI integration
* 🧾 Export conversation to PDF or Markdown
* 🌐 Deploy on Render, Vercel, or Railway
* 📲 Mobile-responsive design

---

## 📦 Deployment Suggestions

| Platform        | Status                       |
| --------------- | ---------------------------- |
| Render.com      | ✅ Easy Flask deploy          |
| Railway.app     | ✅ One-click deploy           |
| Heroku (legacy) | ⚠️ Deprecated                |
| Docker          | ✅ Production-ready container |

---

## 📄 License

This project is licensed under the **MIT License**.
Feel free to fork, modify, and use in commercial or educational projects. ⭐

---

## 🤝 Contact

> 🔗 Developed by **[Md Emon Hasan](https://www.linkedin.com/in/md-emon-hasan-695483237/)**
> 📧 Email: [iconicemon01@gmail.com](mailto:iconicemon01@gmail.com)
> 💼 GitHub: [Md-Emon-Hasan](https://github.com/Md-Emon-Hasan)
> 📱 WhatsApp: [+8801834363533](https://wa.me/8801834363533)

---
