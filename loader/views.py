from flask import Blueprint, request, render_template
from functions import uploads_posts
from json import JSONDecodeError
import logging

logging.basicConfig(level=logging.INFO, encoding='utf-8')
loader_blueprint = Blueprint('loader_blueprint', __name__,
                             url_prefix='/post', template_folder='templates',
                             static_folder='static')


@loader_blueprint.route('/form')
def page_form():
    return render_template('post_form.html')


@loader_blueprint.route('/upload', methods=['POST'])
def page_upload():
    file = request.files.get('picture')
    filename = file.filename
    content = request.values.get('content')

    if filename.split('.')[-1] not in ['png', 'jpg', 'jpeg']:
        logging.error('Формат загруженного файла не тот')
        return '<h1>Не наш формат файла</h1> <br> <a href="/post/form" class="link">Назад</a>'

    post = {'pic': f'/uploads/images/{filename}', 'content': content}
    try:
        uploads_posts(post)
    except FileNotFoundError:
        logging.info('Файл posts.json потерялся')
        return '<h1>Файл не найден</h1>'
    except JSONDecodeError:
        logging.info('Файл posts.json не читается')
        return '<h1>JSON-файл не JSON</h1>'
    else:
        file.save(f'./uploads/images/{filename}')

    return render_template('post_uploaded.html', post=post)
