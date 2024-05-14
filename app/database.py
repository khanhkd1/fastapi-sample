from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


mysql_user = os.environ.get('MYSQL_USER')
mysql_password = os.environ.get('MYSQL_PASSWORD')
mysql_host = os.environ.get('MYSQL_HOST')
mysql_db = os.environ.get('MYSQL_DATABASE')
mysql_port = os.environ.get('MYSQL_PORT')

engine = create_engine(
    f"postgresql+psycopg2://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
