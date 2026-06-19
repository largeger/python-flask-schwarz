from flask import Blueprint, render_template, session, redirect, url_for

results_bp = Blueprint('results', __name__)

@results_bp.route('/summary')
def summary():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    
    score = session.get('score', 0)
    username = session.get('username', 'Unbekannt')
    # Fragen-Anzahl (hier hardcoded für Demo, in Realität aus Datenquelle)
    total = 3 
    percentage = round((score / total) * 100) if total > 0 else 0

    return render_template('results/final.html', username=username, score=score, total=total, percentage=percentage)
