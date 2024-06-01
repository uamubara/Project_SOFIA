# Import statements
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from openai import OpenAI
import assemblyai as aai

from config import Config

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Accessing variables
aws_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
OpenAI(api_key=os.getenv('your_openai_api_key'))
aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')
api_key = os.getenv('Weather_API_KEY')

# Initialize database support
db = SQLAlchemy()

# Initialize migration engine
migrate = Migrate()


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Bind SQLAlchemy and Migrate to the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register the Blueprint from the factory
    from .routes import main
    app.register_blueprint(main)

    return app
