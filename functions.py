import json

POST_PATH = 'posts.json'


def load_posts():
    with open(POST_PATH, 'r', encoding='utf-8') as f:
        posts = json.load(f)
        return posts


def uploads_posts(post):
    posts = load_posts()
    posts.append(post)

    with open(POST_PATH, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)


