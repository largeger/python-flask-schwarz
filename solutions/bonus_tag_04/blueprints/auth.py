from flask import Blueprint, render_template, request, redirect, url_for, session, flash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if not username:
            flash("Bitte gib einen Namen ein!", "danger")
        else:
            session['username'] = username
            session['score'] = 0
            session['current_question'] = 0
            return redirect(url_for('quiz.start_quiz'))
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
