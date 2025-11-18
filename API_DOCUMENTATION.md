Blog API Documentation
Базовый URL

http://localhost:5000
Эндпоинты
1. Проверка работоспособности
GET /ping
Проверяет, что API работает.
Ответ:

json
{
  "response": "pong"
}
2. Создание поста
POST /create_post
Создает новый пост в блоге.
Тело запроса:

json
{
  "body": "Текст поста",
  "author": "@username"
}
Ответ:

json
{
  "status": "success",
  "post": {
    "id": 1,
    "body": "Текст поста",
    "author": "@username"
  }
}
3. Получение всех постов
GET /read_posts
Возвращает список всех постов.
Ответ:

json
{
  "posts": [
    {
      "id": 1,
      "body": "Текст поста 1",
      "author": "@user1"
    },
    {
      "id": 2,
      "body": "Текст поста 2", 
      "author": "@user2"
    }
  ],
  "count": 2
}
4. Получение конкретного поста
GET /read_post/{id}
Возвращает пост по указанному ID.
Параметры:

id - ID поста (целое число, начиная с 1)

Ответ (успех):

json
{
  "post": {
    "id": 1,
    "body": "Текст поста",
    "author": "@username"
  }
}
Ответ (ошибка):

json
{
  "error": "Post not found"
}
5. Обновление поста
PUT /update_post/{id}
Обновляет существующий пост.
Параметры:

id - ID поста для обновления

Тело запроса (можно передавать только изменяемые поля):

json
{
  "body": "Новый текст поста",
  "author": "@new_username"
}
Ответ:

json
{
  "status": "success",
  "post": {
    "id": 1,
    "body": "Новый текст поста",
    "author": "@new_username"
  }
}
6. Удаление поста
DELETE /delete_post/{id}
Удаляет пост по указанному ID.
Параметры:

id - ID поста для удаления

Ответ:

json
{
  "status": "success",
  "deleted_post": {
    "id": 1,
    "body": "Текст поста",
    "author": "@username"
  }
}
Коды статусов HTTP
200 - Успешный запрос

400 - Неверные данные запроса

404 - Пост не найден

500 - Внутренняя ошибка сервера

Примеры использования
Создание поста
bash
curl -X POST http://localhost:5000/create_post \
  -H "Content-Type: application/json" \
  -d '{"body": "Мой первый пост", "author": "@ivanov"}'
Получение всех постов
bash
curl http://localhost:5000/read_posts
Обновление поста
bash
curl -X PUT http://localhost:5000/update_post/1 \
  -H "Content-Type: application/json" \
  -d '{"body": "Обновленный текст"}'
Удаление поста
bash
curl -X DELETE http://localhost:5000/delete_post/1