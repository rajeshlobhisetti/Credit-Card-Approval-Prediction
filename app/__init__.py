import os
from flask import Flask
from flask_login import LoginManager
from config.database import init_db
from database.models import User

def create_app():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(base_dir, 'templates')
    static_dir = os.path.join(base_dir, 'static')
    
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'creditpulse-ai-secret-key-prod-2026')
    
    # Initialize database
    init_db()
    
    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'warning'
    
    @login_manager.user_loader
    def load_user(user_id):
        from config.database import SessionLocal
        db = SessionLocal()
        try:
            return db.query(User).filter(User.UserID == int(user_id)).first()
        finally:
            db.close()
    
    # Register blueprints
    from app.routes import main_bp
    from app.auth import auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    
    return app
