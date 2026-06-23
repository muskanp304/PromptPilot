from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from reportlab.pdfgen import canvas
from flask import send_file
import io
from werkzeug.security import check_password_hash, generate_password_hash
from pypdf import PdfReader
from prompts.qa_prompts import QA_PROMPTS
from prompts.summary_prompts import SUMMARY_PROMPTS
from prompts.content_prompts import CONTENT_PROMPTS
from services.ai_service import generate_response
from database.db import (
    initialize_database,
    save_feedback,
    get_feedback,
    save_chat,
    get_chat_history,
    save_prompt_history,
    get_prompt_history,
    get_total_chats,
    get_total_feedback,
    get_positive_feedback,
    get_total_prompts,
    get_most_used_feature,
    get_recent_activities,
    get_feature_usage,
    get_feedback_stats,
    get_daily_usage,
    save_user,
    get_user_by_username,
)

app = Flask(__name__)
app.secret_key = "promptpilot"
# Create database tables
initialize_database()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if "user_id" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if not username or not password or not confirm_password:
            flash("Please fill in all fields.", "danger")
            return redirect(url_for("register"))

        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return redirect(url_for("register"))

        if get_user_by_username(username):
            flash("Username already exists. Please choose another.", "danger")
            return redirect(url_for("register"))

        save_user(username, generate_password_hash(password))
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        user = get_user_by_username(username)

        if not user or not check_password_hash(user[2], password):
            flash("Invalid username or password.", "danger")
            return redirect(url_for("login"))

        session["user_id"] = user[0]
        session["username"] = user[1]
        flash("Welcome back, {}!".format(user[1]), "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))


@app.route("/qa", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        question = request.form["question"]
        mode = request.form["mode"]

        selected_prompt = QA_PROMPTS[mode]

        final_prompt = f"""
        {selected_prompt}

        Question:
        {question}
        """

        response = generate_response(
            final_prompt
        )

        save_prompt_history(
            "Question Answering",
            selected_prompt,
            question
        )
        save_chat("Question Answering", question, response)

        return {
            "prompt": selected_prompt,
            "user_input": question,
            "response": response,
            "feature": "Question Answering"
        }

    return render_template(
        "qa.html"
    )


@app.route("/summary", methods=["GET", "POST"])
def summary():

    if request.method == "POST":

        notes = request.form.get("notes", "").strip()
        pdf_file = request.files.get("pdf_file")
        summary_type = request.form["summary_type"]

        if pdf_file and pdf_file.filename.endswith(".pdf"):
            try:
                reader = PdfReader(pdf_file)
                pdf_text = "\n".join(
                    page.extract_text() or ""
                    for page in reader.pages
                )
                notes = notes + "\n" + pdf_text if notes else pdf_text
            except Exception:
                flash("Unable to extract text from the uploaded PDF.", "danger")
                return redirect(url_for("summary"))

        if not notes:
            flash("Please enter notes or upload a PDF to summarize.", "danger")
            return redirect(url_for("summary"))

        selected_prompt = SUMMARY_PROMPTS[
            summary_type
        ]

        final_prompt = f"""
        {selected_prompt}

        Text:
        {notes}
        """

        response = generate_response(
            final_prompt
        )

        save_prompt_history(
            "Summarizer",
            selected_prompt,
            notes
        )
        save_chat("Summarizer", notes, response)

        return {
            "prompt": selected_prompt,
            "user_input": notes[:100],
            "response": response,
            "feature": "Summarizer"
        }

    return render_template(
        "summary.html"
    )

@app.route("/content", methods=["GET", "POST"])
def content():

    if request.method == "POST":

        topic = request.form["topic"]

        content_type = request.form[
            "content_type"
        ]

        selected_prompt = CONTENT_PROMPTS[
            content_type
        ]

        final_prompt = f"""
        {selected_prompt}

        Topic:
        {topic}
        """

        response = generate_response(
            final_prompt
        )

        save_prompt_history(
            "Content Generator",
            selected_prompt,
            topic
        )
        save_chat("Content Generator", topic, response)

        return {
            "prompt": selected_prompt,
            "user_input": topic,
            "response": response,
            "feature": "Content Generator"
        }

    return render_template(
        "content.html"
    )


@app.route("/planner", methods=["GET", "POST"])
def planner():

    if request.method == "POST":

        subject = request.form["subject"]
        days = request.form["days"]

        final_prompt = f"""
        Create a {days}-day study plan for {subject}.

        Make it day-wise and easy for a college student.
        """

        response = generate_response(
            final_prompt
        )

        save_prompt_history(
            "Study Planner",
            final_prompt,
            subject
        )
        save_chat("Study Planner", subject, response)

        return {
            "prompt": final_prompt,
            "user_input": subject,
            "response": response,
            "feature": "Study Planner"
        }

    return render_template(
        "planner.html"
    )


@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    if request.method == "POST":

        topic = request.form["topic"]

        final_prompt = f"""
        Generate 5 multiple-choice questions
        on {topic}.

        Provide answers at the end.
        """

        response = generate_response(
            final_prompt
        )

        save_prompt_history(
            "Quiz Generator",
            final_prompt,
            topic
        )
        save_chat("Quiz Generator", topic, response)

        return {
            "prompt": final_prompt,
            "user_input": topic,
            "response": response,
            "feature": "Quiz Generator"
        }

    return render_template(
        "quiz.html"
    )


@app.route("/analyzer", methods=["GET", "POST"])
def analyzer():

    if request.method == "POST":

        topic = request.form["topic"]

        beginner_prompt = (
            "Explain in simple language."
        )

        technical_prompt = (
            "Explain using technical terminology."
        )

        exam_prompt = (
            "Provide a university exam answer."
        )

        # Save prompt history

        save_prompt_history(
            "Prompt Analyzer",
            beginner_prompt,
            topic
        )

        save_prompt_history(
            "Prompt Analyzer",
            technical_prompt,
            topic
        )

        save_prompt_history(
            "Prompt Analyzer",
            exam_prompt,
            topic
        )

        beginner_response = (
            f"{topic} explained in simple language "
            f"for beginners."
        )

        technical_response = (
            f"{topic} explained with technical details "
            f"and concepts."
        )

        exam_response = (
            f"{topic} explained in an exam-oriented "
            f"answer format."
        )

        save_chat("Prompt Analyzer", topic, beginner_response)

        return render_template(
            "analyzer_result.html",

            beginner_prompt=beginner_prompt,
            beginner_response=beginner_response,

            technical_prompt=technical_prompt,
            technical_response=technical_response,

            exam_prompt=exam_prompt,
            exam_response=exam_response
        )

    return render_template("analyzer.html")

@app.route("/history")
def history():

    records = get_prompt_history()

    return render_template(
        "history.html",
        records=records
    )

@app.route("/feedback", methods=["POST"])
def feedback():

    feature = request.form["feature"]
    user_feedback = request.form["feedback"]

    save_feedback(
        feature,
        user_feedback
    )

    flash(
        "Feedback saved successfully!",
        "success"
    )

    return redirect(
        request.referrer
    )

@app.route("/download")
def download():

    response_text = request.args.get(
        "response"
    )

    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)

    y = 800

    for line in response_text.split("\n"):
        p.drawString(
            50,
            y,
            line
        )
        y -= 20

    p.save()

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="response.pdf",
        mimetype="application/pdf"
    )


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    total_chats = get_total_chats()
    total_feedback = get_total_feedback()
    total_prompts = get_total_prompts()

    positive = get_positive_feedback()

    if total_feedback > 0:
        positive_percentage = round(
            (positive / total_feedback) * 100,
            2
        )
    else:
        positive_percentage = 0

    most_used = get_most_used_feature()
    activities = get_recent_activities()
    feature_usage = get_feature_usage()
    feedback_stats = get_feedback_stats()
    daily_usage = get_daily_usage()

    return render_template(
        "dashboard.html",
        total_chats=total_chats,
        total_feedback=total_feedback,
        total_prompts=total_prompts,
        positive_percentage=positive_percentage,
        most_used=most_used,
        activities=activities,
        feature_labels=[row[0] for row in feature_usage],
        feature_values=[row[1] for row in feature_usage],
        feedback_labels=[row[0] for row in feedback_stats],
        feedback_values=[row[1] for row in feedback_stats],
        daily_labels=[row[0] for row in daily_usage],
        daily_values=[row[1] for row in daily_usage],
    )

if __name__ == "__main__":
    app.run(debug=True)