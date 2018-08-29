from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String),
)

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False)
)

#print(users.metadata)
metadata.create_all(engine)

ins = users.insert().values(name='jack', fullname='jack jones')

conn = engine.connect()
conn.execute(ins)

ins = users.insert()
conn.execute(ins, id=2, name='wendy', fullname='Wendy Williams')

conn.execute(addresses.insert(), [
    {'user_id' : 1, 'email_address' : 'jack@yahoo.com'},
    {'user_id' : 1, 'email_address' : 'jack@msn.com'},
    {'user_id' : 2, 'email_address' : 'www@sss.org'},
    {'user_id' : 2, 'email_address' : 'wendy@aol.com'},
])

from sqlalchemy.sql import select
s = select([users])
result = conn.execute(s)

for row in conn.execute(s):
    print("name:", row[users.c.name], "; fullname:", row[users.c.fullname])

s = select([users.c.name, users.c.fullname])
result = conn.execute(s)
for row in result:
    print(row)

s = select([users, addresses]).where(users.c.id == addresses.c.user_id)
for row in conn.execute(s):
    print(row)

from sqlalchemy.sql import and_, or_, not_
print(and_(
    users.c.name.like('j%'),
    users.c.id == addresses.c.user_id,
    or_(
        addresses.c.email_address == 'wendy@aol.com',
        addresses.c.email_address == 'jack@yahoo.com'
        ),
    not_(users.c.id > 5)
    )
)

result.close()

