from flask import Flask
from config import Config
from extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so Alembic can detect them
    from models import User

    @app.route("/")
    def home():
        return "Flask + PostgreSQL + Migrate working!"

    return app

# Expose app for Flask CLI
app = create_app()

# Run the server when executing: python app.py
if __name__ == "__main__":
    app.run(debug=True)

    #updated app file 
    