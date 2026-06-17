from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    
    # Konfiguration (z.B. für Flash-Messages)
    app.config['SECRET_KEY'] = 'dev-key-123'

    # Blueprints importieren
    from blueprints.main import main_bp
    from blueprints.blog import blog_bp

    # Blueprints registrieren
    app.register_blueprint(main_bp)
    app.register_blueprint(blog_bp, url_prefix='/blog')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5004)
