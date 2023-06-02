from . import UserModel, _database


_database._Base.metadata.create_all(_database._Engine)
