from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
SQLALCHEMY_DATABASE_URL = 'postgresql://neondb_owner:npg_IXljiOVMcm15@ep-tiny-surf-a1g3vj5h-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:ishan@127.0.0.1:3306/TodoApplicationDatabase'

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()