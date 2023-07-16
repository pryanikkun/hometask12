from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint

UPLOAD_PATH = 'uploads/images'

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route('/uploads/images/<path:path>')
def static_dir(path):
    return send_from_directory(UPLOAD_PATH, path)
