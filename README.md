<div align="center">

# 🎓 GATE CS ChatBot

### AI-Powered Question Answering System for GATE Computer Science Exam Preparation

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.0-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![Google AI](https://img.shields.io/badge/Google%20Gemini-AI-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev)

**An intelligent chatbot designed to help students prepare for GATE CS exams by answering questions, explaining concepts, and recommending study materials.**

</div>

---

## 📸 Screenshots

<div align="center">

### 🏠 Home Page
<!-- Add your screenshot here -->
<img src="https://github.com/purbashabarik/chatBot_QA_GATE_CS/blob/main/assets/home.png" alt="Home Page" width="800"/>
<p><em>Landing page with login/signup options</em></p>

---
### 🔐 Sign-Up Page
<!-- Add your screenshot here -->
<img src="https://github.com/purbashabarik/chatBot_QA_GATE_CS/blob/main/assets/sign_up.png" alt="Sign-Up Page" width="800"/>
<p><em>User Registration Interface</em></p>


### 🔐 Login Page
<!-- Add your screenshot here -->
<img src="https://github.com/purbashabarik/chatBot_QA_GATE_CS/blob/main/assets/login.png" alt="Login Page" width="800"/>
<p><em>User authentication interface</em></p>

---

### 💬 Chat Interface - PYQ Mode
<!-- Add your screenshot here -->
<img src="https://github.com/purbashabarik/chatBot_QA_GATE_CS/blob/main/assets/pyq_chat.png" alt="PYQ Chat" width="800"/>
<p><em>Ask questions about Previous Year GATE Questions</em></p>

---

### 📚 Chat Interface - Books Mode
<!-- Add your screenshot here -->
<img src="https://github.com/purbashabarik/chatBot_QA_GATE_CS/blob/main/assets/book_chat.png" alt="Books Chat" width="800"/>
<p><em>Get explanations from Computer Science textbooks</em></p>

</div>

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔐 User Authentication
- Secure login & signup system
- Session management
- Protected chat routes

### 💬 Intelligent Chat Interface
- Natural language processing
- Real-time responses
- ChatGPT-like UI with markdown support

</td>
<td width="50%">

### 📝 Previous Year Questions (PYQs)
- Access GATE CS previous year papers
- Get detailed solutions & explanations
- Topic-wise question filtering

### 📚 Book-Based Learning
- Query from CS textbooks
- Concept explanations
- Study material recommendations

</td>
</tr>
</table>

### 🚀 Key Highlights

| Feature | Description |
|---------|-------------|
| 🤖 **AI-Powered** | Google Gemini 2.5 Flash for intelligent responses |
| 🔍 **Semantic Search** | FAISS vector database for relevant content retrieval |
| 📊 **Markdown Support** | Formatted responses with code blocks, lists, tables |
| 🎨 **Modern UI** | Responsive design with Tailwind CSS |
| ⚡ **Fast Responses** | Optimized embeddings for quick answers |

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technologies |
|----------|-------------|
| **Backend** | ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) |
| **AI/ML** | ![Google AI](https://img.shields.io/badge/Gemini%20AI-4285F4?style=flat-square&logo=google) ![LangChain](https://img.shields.io/badge/LangChain-121212?style=flat-square) |
| **Database** | ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite) ![FAISS](https://img.shields.io/badge/FAISS-00599C?style=flat-square) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![TailwindCSS](https://img.shields.io/badge/Tailwind-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) |

</div>

---

## 📦 Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

### Step-by-Step Setup

### 1️⃣ Clone the repository
git clone https://github.com/purbashabarik/chatBot_QA_GATE_CS.git

### 2️⃣ Navigate to project directory
cd chatBot_QA_GATE_CS

### 3️⃣ Create virtual environment
python -m venv venv

### 4️⃣ Activate virtual environment
#### On macOS/Linux:
source venv/bin/activate
#### On Windows:
venv\Scripts\activate

### 5️⃣ Install dependencies
pip install -r requirements.txt

### 6️⃣ Run database migrations
python manage.py migrate

### 7️⃣ Start the development server
python manage.py runserver### 🔑 API Key Setup

> **Note:** The Google API key is already integrated in the project. No additional setup required!

If you want to use your own API key:
1. Get a key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Update the key in `room/views.py`

---

## 🚀 Usage

### 1️⃣ Access the Application
Open your browser and navigate to: http://127.0.0.1:8000/

### 2️⃣ Create an Account / Login
- Click **Sign Up** to create a new account
- Or **Log In** with existing credentials

### 3️⃣ Choose Your Mode

| Mode | URL | Description |
|------|-----|-------------|
| **PYQ Chat** | `/rooms/pyq` | Ask about GATE previous year questions |
| **Books Chat** | `/rooms/room_books/` | Query from CS textbooks |

### 4️⃣ Start Asking Questions!

**Example queries:**
- *"Explain binary search trees"*
- *"Show me GATE 2020 questions on Operating Systems"*
- *"What is the time complexity of quicksort?"*
- *"Explain page replacement algorithms"*


---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

## 👩‍💻 Author

<div align="center">

**Purbasha Barik**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/purbashabarik)

</div>

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

Made with ❤️ for GATE aspirants

</div>





