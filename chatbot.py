import sqlite3
from difflib import SequenceMatcher

DB_NAME = "college_chatbot.db"


def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def get_bot_response(user_input):
    user_input_clean = user_input.strip().lower()

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM faqs")
    faqs = cursor.fetchall()
    conn.close()

    if not faqs:
        return "No FAQs are added yet. Please add questions from the admin panel first."

    best_match = None
    best_score = 0

    # Similarity matching
    for question, answer in faqs:
        score = similarity(user_input_clean, question.lower())
        if score > best_score:
            best_score = score
            best_match = answer

    # Keyword fallback
    if best_score < 0.45:
        for question, answer in faqs:
            q_words = question.lower().split()
            user_words = user_input_clean.split()
            common_words = set(q_words) & set(user_words)

            if len(common_words) >= 2:
                return answer

    if best_score > 0.45:
        return best_match
    else:
        return "Sorry, I couldn't understand that clearly. Please ask about admissions, fees, courses, hostel, scholarship, exams, placements, or campus facilities."
