
# 🎓 College Chatbot (Flask + AI)

A simple AI-powered College Chatbot built using Flask, SQLite, and basic NLP.
It helps students get information about admissions, fees, courses, hostel, exams, and more.

---

## 🚀 Features

* 🤖 AI Chatbot (FAQ-based response system)
* 🧠 Smart similarity matching (difflib)
* 💬 Chat history storage
* 🛠️ Admin panel to:

  * Add FAQs
  * Edit FAQs
  * Delete FAQs
  * Search & filter FAQs
* 📊 Dashboard stats (FAQs, chats, categories)
* 🎨 Modern UI (HTML + CSS + JS)

---

## 📁 Project Structure

```
college_chatbot_project/
│
├── app2.py
├── chatbot.py
├── database.py
├── college_chatbot.db
│
├── templates/
│   ├── index2.html
│   ├── admin.html
│   ├── edit_faq.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│       └── gehu-bg.jpg
```

---

## ⚙️ Installation

### 1. Clone or Download Project

```
git clone <your-repo-link>
cd college_chatbot_project
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```
python app2.py
```

Then open browser:

```
http://127.0.0.1:5000/
```

---

## 🔑 Main Routes

* `/` → Homepage (Chatbot UI)
* `/admin` → Admin Panel
* `/get_response` → Chatbot API

---

## 🧠 How Chatbot Works

* Uses **SequenceMatcher** for similarity matching
* If match score > 0.45 → returns best answer
* Otherwise → fallback keyword matching
* If no match → default response

---

## 🗄️ Database

SQLite database (`college_chatbot.db`) with tables:

* `faqs` → Stores questions & answers
* `chat_history` → Stores user chats

---

## 🛠️ Technologies Used

* Python (Flask)
* SQLite
* HTML, CSS, JavaScript
* Basic NLP (difflib)

---

## 📌 Future Improvements

* Add login authentication for admin
* Use ML/NLP models instead of rule-based matching
* Deploy on cloud (Render / Railway / AWS)
* Add voice chatbot support

---

## 👨‍💻 Author

Developed as a mini project for college chatbot system.
=======
# chatbot

