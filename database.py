from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = postgres://wurnbgfr:Mu4LsxImrzT_dBV-Reu5rvXOT4MeV5BD@rosie.db.elephantsql.com/wurnbgfr'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


# MYSQL Series
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:test1234!@127.0.0.1:3306/todoapp"



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
