from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    # Khởi tạo các module
    db.init_app(app)
    login_manager.init_app(app)

    # Cấu hình LoginManager
    login_manager.login_view = 'auth.login'  # Đảm bảo có route login
    login_manager.login_message = "Vui lòng đăng nhập để truy cập."

    # Đăng ký các route hoặc blueprint (nếu có)
    from .routes import main
    app.register_blueprint(main)

    return app
