from flask import Flask, render_template, request, jsonify, redirect, url_for
from chatbot import get_bot_response
from database import (
    init_db, insert_default_data, save_chat,
    get_total_faqs, add_faq, delete_faq,
    get_faq_by_id, update_faq, search_faqs,
    get_chat_history, get_total_chats, get_total_categories
)

app = Flask(__name__)

# Initialize DB
init_db()
insert_default_data()


@app.route("/")
def home():
    return render_template("index2.html")


@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    bot_response = get_bot_response(user_message)
    save_chat(user_message, bot_response)
    return jsonify({"response": bot_response})


@app.route("/admin")
def admin():
    search = request.args.get("search", "")
    category = request.args.get("category", "")

    # Show only latest 5 FAQs in panel
    faqs = search_faqs(search, category, limit=5)
    chats = get_chat_history()

    return render_template(
        "admin.html",
        faqs=faqs,
        chats=chats,
        total_faqs=get_total_faqs(),
        total_chats=get_total_chats(),
        total_categories=get_total_categories(),
        search=search,
        category=category
    )


@app.route("/add", methods=["POST"])
def add():
    question = request.form["question"]
    answer = request.form["answer"]
    category = request.form["category"]
    add_faq(question, answer, category)
    return redirect(url_for("admin"))


@app.route("/delete/<int:id>")
def delete(id):
    delete_faq(id)
    return redirect(url_for("admin"))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        update_faq(
            id,
            request.form["question"],
            request.form["answer"],
            request.form["category"]
        )
        return redirect(url_for("admin"))

    return render_template("edit_faq.html", faq=get_faq_by_id(id))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
