from flask import Flask, jsonify, request
from model.post import Post

posts = []

app = Flask(__name__)


@app.route('/ping')
def index():
    return jsonify({'response': 'pong'})


# Вспомогательная функция для сериализации поста
def serialize_post(post):
    return {
        'id': post.id,
        'body': post.body,
        'author': post.author
    }


# Функция для получения следующего ID
def get_next_id():
    if not posts:
        return 1
    return max(post.id for post in posts) + 1


# Создание поста
@app.route('/create_post', methods=['POST'])
def create_post():
    '''{"body": "text", "author": "@aqaguy"}'''
    try:
        post_json = request.get_json()
        if not post_json or 'body' not in post_json or 'author' not in post_json:
            return jsonify({'error': 'Missing body or author'}), 400

        # Создаем пост с ID - передаем все три аргумента
        next_id = get_next_id()
        post = Post(post_json['body'], post_json['author'], next_id)
        posts.append(post)

        return jsonify({
            'status': 'success',
            'post': serialize_post(post)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Чтение постов
@app.route('/read_posts', methods=['GET'])
def read_posts():
    posts_data = [serialize_post(post) for post in posts]
    return jsonify({'posts': posts_data, 'count': len(posts_data)})


# Чтение конкретного поста по ID
@app.route('/read_post/<int:post_id>', methods=['GET'])
def read_post(post_id):
    # Ищем пост по ID
    for post in posts:
        if post.id == post_id:
            return jsonify({'post': serialize_post(post)})
    return jsonify({'error': 'Post not found'}), 404


# Обновление поста по ID
@app.route('/update_post/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    # Ищем пост по ID
    for post in posts:
        if post.id == post_id:
            try:
                post_json = request.get_json()

                if 'body' in post_json:
                    post.body = post_json['body']
                if 'author' in post_json:
                    post.author = post_json['author']

                return jsonify({
                    'status': 'success',
                    'post': serialize_post(post)
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'Post not found'}), 404


# Удаление поста по ID
@app.route('/delete_post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    # Ищем пост по ID
    for i, post in enumerate(posts):
        if post.id == post_id:
            try:
                deleted_post = posts.pop(i)
                return jsonify({
                    'status': 'success',
                    'deleted_post': serialize_post(deleted_post)
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'Post not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)