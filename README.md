# Простое приложение с rest api

Сборка  
docker-compose build

Запуск  
docker-compose up

Остановка  
docker-compose down

### Работа с api:
### Регистрация
<a name="sign">[POST] /rest-auth/registration/</a>
--------
Регистрация и получение авторизационного токена
Request:
- username: Логин
- password1: Пароль
- password2: Пароль

Ответ:
```javascript
{"details": "Registered"}
```
>

### Авторизация
<a name="login">[POST] /rest-auth/login/</a>
--------
Авторизация и получение авторизационного токена

Request:
- username: Логин
- password: Пароль

Ответ:
```javascript
{"key": "2d500db1e51153318e300860064e52c061e72016"}
```
>

### Получить одну запись
<a name="getBlog">[GET] /api/v1/blogs/3</a>
--------
Request:
- "Authorization: Token 2d500db1e51153318e300860064e52c061e72016"

Ответ:
```javascript
{"author": "USERNAME4", "description": "text", "title": "BLog1"}
```
>

### Создать запись
<a name="createBlog">[POST] /api/v1/blogs/</a>
--------
Request:
- "Authorization: Token 2d500db1e51153318e300860064e52c061e72016"
- title="Too simple" 
- description="About this app"

Ответ:
```javascript
{"author": "USERNAME4", "description": "About this app", "title": "Too simple"}
```
>

### Обновить запись
<a name="updateBlog">[PUT] /api/v1/blogs/3</a>
--------
Request:
- "Authorization: Token 2d500db1e51153318e300860064e52c061e72016"
- title="New title" 
- description="New text"

Ответ:
```javascript
{"author": "USERNAME4", "description": "New text", "title": "New title"}
```
>

### Удалить запись
<a name="deleteBlog">[DELETE] /api/v1/blogs/3</a>
--------
Request:
- "Authorization: Token 2d500db1e51153318e300860064e52c061e72016"

>
