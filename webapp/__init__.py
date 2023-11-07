from flask import Flask

def app_sekolah():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "belumrahasia"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin123@localhost:5432/postgres'

    from .models import db
    db.init_app(app)
    
    with app.app_context():
        from .views import views
        from .auth import auth

        app.register_blueprint(views, url_prefix="/")
        app.register_blueprint(auth, url_prefix="/login")

    return app