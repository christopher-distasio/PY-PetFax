# from flask import Flask
from petfax import create_app
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env
print("Database URL from .env:", os.getenv('DATABASE_URL'))

# def create_app():
#     app = Flask(__name__)

#     @app.route('/')
#     def hello():
#         return 'Hello, PetFax!'

#     # Set the SQLAlchemy database URI from the environment variable
#     # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
#     # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     return app

app = create_app()

if __name__ == '__main__':
    # Optional: Set default port from environment variable or use 5001
    port = int(os.getenv('PORT', 5001))
    print(f"Running on port: {port}")
    app.run(debug=True, port=port)
