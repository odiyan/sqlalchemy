from sqlalchemy import engine, MetaData, select, Table, create_engine
import os
import csv
import glob
import re

engine = create_engine('mysql+pymysql://root:demimondaine@localhost/mtm_mapped')
conn = engine.connect()

tablemeta = MetaData(bind=engine, reflect=True)

#with open('/home/shyam/project/code/practice/mtm-data/Sea-Trial-Data.csv', \
#          newline='') as csv_file:
#    csv_data = csv.reader(csv_file, delimiter=',')
#    for row in csv_data:
#        # conn.execute(table_sea_trial.insert().values(row))
#        print(row)
#table_sea_trial = Table('SEATRIAL', tablemeta, autoload=True, autoload_with=engine)

csv_dict = {}
table_dict = {}
for csvfile in glob.glob(os.path.join('./mtm-data', '*.csv')):
    with open(csvfile) as f:
        csv_data = csv.reader(f, delimiter=',')
        row1 = next(csv_data)
        #print('\n', csvfile)
        #print(row1)
        
        #pattern = re.compile('\.\/mtm\-data[\S]*\.csv')
        pattern1 = '\.\/mtm\-data\/'
        pattern2 = '\.csv'
        stripped_first = re.sub(pattern1, '', csvfile)
        stripped_file_name = re.sub(pattern2, '', stripped_first)
        #pattern.match(csvfile).group()
        csv_dict[stripped_file_name.lower()] = [row.lower() for row in row1]

print(csv_dict)

for t in tablemeta.sorted_tables:
    print('*'*10, '\n', t.name, '\n', '*'*10)
    for c in t.c:
        print('\n', c)
