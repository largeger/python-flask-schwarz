from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'quiz-master-secret-42'

    # Blueprints registrieren
    from blueprints.auth import auth_bp
    from blueprints.quiz import quiz_bp
    from blueprints.results import results_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(quiz_bp, url_prefix='/quiz')
    app.register_blueprint(results_bp, url_prefix='/results')

    @app.route('/')
    def index():
        from flask import redirect, url_for
        return redirect(url_for('auth.login'))

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5010)
