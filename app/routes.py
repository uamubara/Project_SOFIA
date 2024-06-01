from flask import Blueprint, render_template

from app.sofia_speak import open_ai

# Create a Blueprint for separation of concerns
main = Blueprint('main', __name__)


@main.route('/')
def chat():
    """Render the chat page."""
    return render_template('chat.html')


