from sqlalchemy import create_engine, MetaData, Table, select
#from sqlalchemy.orm import sessionmaker 
from pandas import DataFrame

engine = create_engine('mysql+pymysql://root:demimondaine@localhost/mtm_db')
conn = engine.connect()

tablemeta = MetaData(bind=engine, reflect=True)

# table_temp = Table('temp', tablemeta, autoload=True)
#Session = sessionmaker()
#Session.configure(bind=engine)
#
#session = Session()

# print(conn.execute(select([table_temp]).where(table_temp.c.RPM==0)).fetchone())

#result = session.query(table_temp).all()
#print(table_temp.c.SootLanded)
#print(result)

#for c in table_temp.c.RPM:
#    print(c)


#stmt = select([table_temp]).where(table_temp.c.RPM==0)
#
#result = conn.execute(stmt).fetchall()
#
#for res in result:
#    print(res)

def querydb(query):
    """
    Function to execute query and return dataframe
    """
    
    df = DataFrame(query.all())
    #df.columns = 

    
# table_test = Table('NOONDATA', tablemeta, autoload=True)
for t in tablemeta.sorted_tables:
    print(t.name)
