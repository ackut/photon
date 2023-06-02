from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# _Engine = create_engine('mysql+pymysql://user:password@host/db_name')
_Engine = create_engine('sqlite+pysqlite:///database.db')
_Session = sessionmaker(bind=_Engine)
_Base = declarative_base()
_db = _Session()
