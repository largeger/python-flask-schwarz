from flask import Blueprint, render_template, request, redirect, url_for, session, flash

quiz_bp = Blueprint('quiz', __name__)

QUESTIONS = [
    {
        "id": 0,
        "text": "Was ist Flask?",
        "options": ["Ein Micro-Framework", "Eine Kaffeemaschine", "Ein Datenbanksystem"],
        "correct": "Ein Micro-Framework"
    },
    {
        "id": 1,
        "text": "Wie heißt die Template-Engine von Flask?",
        "options": ["Mustache", "Jinja2", "Pug"],
        "correct": "Jinja2"
    },
    {
        "id": 2,
        "text": "Welche HTTP-Methode wird standardmäßig für Formulare genutzt, die Daten speichern?",
        "options": ["GET", "POST", "PUT"],
        "correct": "POST"
    }
]

@quiz_bp.route('/start')
def start_quiz():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    session['score'] = 0
    session['current_question'] = 0
    return redirect(url_for('quiz.show_question'))

@quiz_bp.route('/frage', methods=['GET', 'POST'])
def show_question():
    if 'username' not in session:
        return redirect(url_for('auth.login'))

    idx = session.get('current_question', 0)
    if idx >= len(QUESTIONS):
        return redirect(url_for('results.summary'))

    question = QUESTIONS[idx]

    if request.method == 'POST':
        user_answer = request.form.get('answer')
        if not user_answer:
            flash("Bitte wähle eine Antwort aus!", "warning")
        else:
            if user_answer == question['correct']:
                session['score'] += 1
                flash("Richtig! 🎉", "success")
            else:
                flash(f"Falsch! Die richtige Antwort war: {question['correct']} ❌", "danger")
            
            session['current_question'] += 1
            return redirect(url_for('quiz.show_question'))

    return render_template('quiz/question.html', question=question, total=len(QUESTIONS), current=idx+1)
