from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, template_folder='public', static_folder='static', static_url_path='')

def myapp():
    app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
    app.config['DATABASE_URI'] = os.getenv('DATABASE_URI')

    from .views import views
    app.register_blueprint(views)
    return app
