from main import app
from models import UserModel


@app.get('/users/')
def get_users(limit: int = 100):
    return UserModel.get_all(limit)


@app.post('/user/')
def create_user(email: str, name: str, password: str):
    if UserModel.get_by_email(email):
        return {
            'message': 'Пользователь с таким email уже существует.'
        }

    User = UserModel.create(email, name, password)
    return {
        'id': User.id,
        'name': User.name,
        'email': User.email,
        'password': User.password,
        'created_at': User.created_at
    }


@app.get('/user/{id}')
def get_user(id: int):
    User = UserModel.get(id)

    return {
        'id': User.id,
        'name': User.name,
        'email': User.email,
        'password': User.password,
        'created_at': User.created_at
    } if User else {
        'message': 'Пользователя не существует.'
    }


@app.put('/user/')
def edit_user(id: int, email: str, name: str, password: str, status: int):
    User = UserModel.edit(id, email, name, password, status)

    return {
        'id': User.id,
        'name': User.name,
        'email': User.email,
        'password': User.password,
        'created_at': User.created_at
    }


@app.delete('/user/')
def get_user(id: int):
    if not UserModel.get(id):
        return {'message': 'Пользователя не существует'}

    User = UserModel.delete(id)

    return {
        'message': 'Пользователь удалён.',
        'user': {
            'id': User.id,
            'email': User.email,
            'password': User.password,
            'created_at': User.created_at
        }
    }
