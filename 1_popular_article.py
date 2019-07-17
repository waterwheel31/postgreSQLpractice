# This code extracts the most popular articles 

import psycopg2 as pg

DBNAME = 'news'
SQL    = 'select path, count(path) from log group by path order by count(path) desc limit 10;'

db = pg.connect(dbname=DBNAME)
conn  = db.cursor()
conn.execute(SQL)
result = conn.fetchall()
db.close()

print('\nTop Articles:\n')

for article in result:
    
    if article[0].startswith('/article/'):
        print(article[0].replace('/article/','') + '\t ('+ str(article[1]) + ') ')
