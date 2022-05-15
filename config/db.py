from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Mariobrosx2021@localhost:3306/sakila")

meta = MetaData()

conn = engine.connect()