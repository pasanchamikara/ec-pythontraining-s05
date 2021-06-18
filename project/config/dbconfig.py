from sqlalchemy import create_engine

# engine = create_engine("mysql+mysqldb://root@23.92.23.113/mydb", echo=True, pool_size=6, max_overflow=10, encoding='latin1')
engine = create_engine("mysql+pymysql://root@localhost/ectest")

engine.connect()