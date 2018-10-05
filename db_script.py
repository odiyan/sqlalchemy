from sqlalchemy import MetaData, create_engine
import os
import csv
import glob
import re

engine = create_engine('mysql+pymysql://root:demimondaine@localhost/mtm_mapped')
conn = engine.connect()

tablemeta = MetaData(bind=engine, reflect=True)

# with open('/home/shyam/project/code/practice/mtm-data/Sea-Trial-Data.csv', \
#          newline='') as csv_file:
#    csv_data = csv.reader(csv_file, delimiter=',')
#    for row in csv_data:
#        # conn.execute(table_sea_trial.insert().values(row))
#        print(row)
# table_sea_trial = Table('SEATRIAL', tablemeta, autoload=True, autoload_with=engine)


csv_dict = {}
table_dict = {}
table_dict_lower = {}
csv_dict_lower = {}

for csvfile in glob.glob(os.path.join('../database/mtm-data', '*.csv')):
    with open(csvfile, encoding="latin-1") as f:
        csv_data = csv.reader(f, delimiter=',')
        regx_pat = '\s'
        row1_with_space = next(csv_data)
        row1 = [re.sub(regx_pat, '_', row) for row in row1_with_space]
        # print('\n', csvfile)
        # print(row1)
        
        # pattern = re.compile('\.\/mtm\-data[\S]*\.csv')
        pattern1 = '\.\.\/database\/mtm\-data\/'
        pattern2 = '\.csv'
        stripped_first = re.sub(pattern1, '', csvfile)
        stripped_file_name = re.sub(pattern2, '', stripped_first)
        # pattern.match(csvfile).group()
        csv_dict[stripped_file_name] = [row.lower() for row in row1]
        csv_dict_lower[stripped_file_name.lower()] = [row.lower() for
                                                      row in row1]

# print(csv_dict)

# for t in tablemeta.sorted_tables:
    # print('*'*10, '\n', t.name, '\n', '*'*10)
    # for c in t.c:
    #     print('\n', c)

for t in tablemeta.sorted_tables:
    # print(t, type(t))
    col_names = [str(col).lower() for col in t.c.keys()]
    # print(str(t.name), col_names)
    table_name = str(t.name)
    table_name_lower = table_name.lower()
    table_dict[table_name] = col_names
    table_dict_lower[table_name_lower] = col_names

    # print(t.select(), '***', type(t.select()))
    # table_dict[t.name] = [dict(row) for row in engine.execute(t.select())]
#    statement = text("describe ")
#    conn.execute(statement)
# print(table_dict)

# for file_name in csv_dict_lower.keys():
#    if file_name not in table_dict_lower.keys():
#        print(file_name)
#    else:
#        extra_columns_in_csv = set(csv_dict_lower[file_name]).difference(
#            table_dict_lower[file_name])
#        print(file_name, extra_columns_in_csv)

for file_name in csv_dict.keys():  # map(lambda x: x.lower(), csv_dict.keys()):
    if file_name.lower() not in map(lambda x: x.lower(), table_dict.keys()):
        print(file_name)
    else:
        extra_columns_in_csv = set(csv_col.lower() for csv_col in
                                   csv_dict[file_name]).difference(
            tab_col_name.lower() for tab_col_name in
                                       table_dict_lower[file_name.lower()])
        print(file_name, extra_columns_in_csv)

# import sys, os
# sys.path.append(os.path.join(os.path.dirname(__file__), '.., alembic, versions'))
# from test import col_dict
# 
# print('*'*8, set(col_dict.keys()).difference(csv_dict_lower['vesseldetail']))
