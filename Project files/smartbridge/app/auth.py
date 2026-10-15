from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from database.models import User
from config.database import SessionLocal

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.Email == email).first()
            
            if user and check_password_hash(user.Password, password):
                login_user(user)
                flash('Login successful!', 'success')
                next_page = request.args.get('next')
                return redirect(next_page or url_for('main.dashboard'))
            else:
                flash('Invalid email or password.', 'danger')
        finally:
            db.close()
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Registration page"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return render_template('register.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters.', 'danger')
            return render_template('register.html')
        
        db = SessionLocal()
        try:
            # Check if user already exists
            existing_user = db.query(User).filter(User.Email == email).first()
            if existing_user:
                flash('Email already registered.', 'danger')
                return render_template('register.html')
            
            # Create new user
            new_user = User(
                Name=name,
                Email=email,
                Password=generate_password_hash(password, method='pbkdf2:sha256'),
                Role='user'
            )
            
            db.add(new_user)
            db.commit()
            
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.rollback()
            flash(f'Registration failed: {str(e)}', 'danger')
        finally:
            db.close()
    
    return render_template('register.html')

@auth_bp.route('/logout')
@login_required
def logout():
    """Logout"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
