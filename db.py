from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")