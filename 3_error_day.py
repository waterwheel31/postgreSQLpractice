#!/usr/bin/env python3
# this shows the days that have more than 1% of the requrests were errors 

import psycopg2 as pg

DBNAME    = 'news'
SQL_count_all   = 'create view n_error_all as select date(time) as date, count(status) as count from log group by date(time) ;'
SQL_count_err = 'create view n_error_err as select date(time) as date, count(status) as count from log where status like \'4%\'group by date(time)  ;'
SQL_joint     = 'create view n_joint as select n_error_all.date as date, n_error_err.count as err, n_error_all.count as al from n_error_err left join n_error_all on n_error_all.date = n_error_err.date ;'
SQL           = 'select date, cast(err as float)/cast( al as float) as err_rate from n_joint'

db = pg.connect(dbname=DBNAME)
conn  = db.cursor()

conn.execute(SQL_count_all)
conn.execute(SQL_count_err)
conn.execute(SQL_joint)
conn.execute(SQL)
result = conn.fetchall()
db.close()

print('\nDays with error rate >1%:\n')

threshold = 0.01

for item in result:
    if item[1]> threshold:
        print(str(item[0]) + ' error rate:' + str(item[1]))