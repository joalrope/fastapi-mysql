from sqlalchemy import create_engine, MetaData

engine = create_engine(
    "mysql+pymysql://root:Cheo.-2436@localhost:3306/crud_python")

meta = MetaData()

conn = engine.connect()
