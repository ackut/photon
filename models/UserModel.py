import time
from werkzeug.security import generate_password_hash
from sqlalchemy import Column, Integer, String
from ._database import _Base, _db


class UserModel(_Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(16), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    status = Column(Integer, nullable=False, default=0)
    created_at = Column(Integer, nullable=False)


def create(email: str, name: str, password: str) -> UserModel:
    User: UserModel = UserModel(
        email=generate_password_hash(email),
        name=name,
        password=generate_password_hash(password),
        created_at=time.time()
    )
    _db.add(User)
    _db.commit()

    return User


def get(id: int) -> UserModel:
    User: UserModel = _db.query(UserModel).get(id)
    return User if User else None


def get_by_email(email: str) -> UserModel:
    User: UserModel = _db.query(UserModel).filter_by(email=email).first()
    return User if User else None


def get_all(limit: int = 100) -> list[UserModel]:
    Users = _db.query(UserModel).limit(limit).all()
    return Users if Users else []


def edit(id: int, email: str, name: str, password: str, status: int) -> UserModel:
    User: UserModel = _db.query(UserModel).get(id)
    
    User.name = name
    User.email = generate_password_hash(email)
    User.password = generate_password_hash(password)
    User.status = status

    _db.add(User)
    _db.commit()

    return User if User else None


def delete(id: int) -> UserModel:
    User: UserModel = _db.query(UserModel).get(id)

    _db.delete(User)
    _db.commit()

    return User if User else None
