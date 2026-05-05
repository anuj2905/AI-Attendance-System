# 🤖 AI Attendance System

🚀 **Built by Anuj Patil**

🌐 **Live Demo:**
👉 https://patil-anuj-ai-attendance.streamlit.app/

---

## ✨ Overview

An intelligent attendance system powered by **AI, Face Recognition, and Voice Authentication**.
This system automates attendance tracking, eliminating manual errors and improving efficiency using modern computer vision techniques ([DEV Community][1]).

---

## 🔥 Features

* 🎯 Real-time Face Recognition
* 🎤 Voice-based Attendance (AI powered)
* 👨‍🏫 Teacher Dashboard
* 👨‍🎓 Student Dashboard
* 📊 Attendance Tracking System
* 🔐 Secure Login with Encryption
* ☁️ Supabase Cloud Database
* ⚡ Fast & Interactive UI (Streamlit)

---

## 🧠 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **AI/ML:** OpenCV, Face Recognition
* **Voice AI:** Resemblyzer
* **Database:** Supabase
* **Security:** bcrypt

---

## 🚀 How to Run Locally

```bash
# Clone repo
git clone https://github.com/anuj2905/AI-Attendance-System.git

# Open folder
cd AI-Attendance-System

# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
python -m streamlit run app.py
```

---

## 🔑 Environment Variables

Create file:

```
.streamlit/secrets.toml
```

Add:

```toml
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_key"
```

---

## 🎯 How It Works

1. Register face & voice
2. Start attendance system
3. Camera detects face
4. AI verifies identity
5. Attendance marked automatically

👉 This eliminates manual attendance and improves accuracy.

---

## 🚀 Future Improvements

* 📱 Mobile-friendly UI
* 📊 Advanced analytics dashboard
* 🔗 QR-based attendance system
* 🌐 Multi-user role management
* ☁️ Cloud scalability

---

## 🙌 Author

**Anuj Patil**
🚀 AI Developer | Builder

---

## ⭐ Support

If you like this project:

👉 Star ⭐ this repo
👉 Share with others

---

[1]: https://dev.to/anurag_panda/face-attendance-maker-using-streamlit-and-opencv-3fh0?utm_source=chatgpt.com "🧑‍💼 Face Attendance Maker using Streamlit and OpenCV 😎"
