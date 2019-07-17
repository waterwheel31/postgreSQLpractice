# this shows the most popular article authors 

import psycopg2 as pg

DBNAME = 'news'
SQL_view = 'create view r_articles as select replace(path, \'/article/\',\'\') as path from log;'
SQL_auth = 'create view n_authors as select author, count(author) as num from r_articles left join articles on r_articles.path = articles.slug group by author order by count(author) desc;'
SQL_name = 'create view name_authors as select name, num from n_authors left join authors on n_authors.author = authors.id;' 
SQL      = 'select * from name_authors;'


db = pg.connect(dbname=DBNAME)
conn  = db.cursor()
conn.execute(SQL_view)
conn.execute(SQL_auth)
conn.execute(SQL_name)
conn.execute(SQL)
result = conn.fetchall()
db.close()

print('\nTop Authors:\n')

for author in result:
    if author[0] is not None: 
        print(author[0] + '\t ('+ str(author[1]) + ') ')
