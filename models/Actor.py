from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine

actors = Table("actor", meta, 
              Column("actor_id", SMALLINT, primary_key=True), 
              Column("first_name", String(45)),
              Column("last_name", String(45)),
              Column("last_update", TIMESTAMP))

meta.create_all(engine)