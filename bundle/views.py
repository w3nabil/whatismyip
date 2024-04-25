from flask import Blueprint, render_template, request
import requests, os 
from dotenv import load_dotenv
load_dotenv()

views = Blueprint('views', __name__, template_folder='public')

@views.route('/')
def index():
    userip = request.headers.get('X-forwarded-for', request.remote_addr)
    callapi = requests.get(f'https://ipinfo.io/{userip}/json?{os.getenv('token')}')
    ip = callapi.json()
    return render_template('index.html', ip=ip)