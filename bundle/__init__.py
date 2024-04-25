from flask import Flask, render_template 

app = Flask(__name__, template_folder='public')

def myapp():
    app.config['SECRET_KEY'] = 'nabil'

    from .views import views
    app.register_blueprint(views)
    return app