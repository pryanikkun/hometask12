import logging
from flask import Blueprint, request, render_template
from functions import load_posts
from json import JSONDecodeError

logging.basicConfig(level=logging.INFO, encoding='utf-8')

main_blueprint = Blueprint('main_blueprint', __name__,
                           template_folder='templates')


@main_blueprint.route('/')
def page_index():
    return render_template('index.html')


@main_blueprint.route('/search/')
def page_search():
    s = request.values['s']
    logging.info(f'Выполняется поиск по слову {s}')
    try:
        posts = [x for x in load_posts() if s.lower() in x['content'].lower()]
    except FileNotFoundError:
        return '<h1>Файл не найден</h1>'
    except JSONDecodeError:
        logging.info('Файл posts.json не читается')
        return '<h1>JSON-файл не JSON</h1>'
    else:
        return render_template('post_list.html', search_by=s, posts=posts)
