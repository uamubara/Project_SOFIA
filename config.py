import os


class Config:
    # Secret key for encrypting cookies
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_hard_to_guess_string'
    # Database URL (PostgreSQL), adjust username, password, host, and database name as needed
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://username:password@localhost/databasename'
    # This option disables the signal for every database change, which can improve performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AWS Polly


AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
REGION_NAME = 'REGION_NAME'

# Assembly AI
ASSEMBLYAI_API_KEY = 'ASSEMBLYAI_API_KEY'

# OpenAI

your_openai_api_key = 'your_openai_api_key'
