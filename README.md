
## This is a practice of PostgreSQL

This tries to do following tasks regarding a database

1. show the most popular articles
2. show the most popular article authors 
3. show the days that have more than 1% of the requrests were errors 



## To run these codes:

*  Install PostgreSQL in the machine (or Vagrant or Docker) 
*  Download the data base from this link and place in the same directory
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
*  Load the data into PostgreSQL Database
*  Prepare Python3 
*  Install psycopg2 ('pip3 install psycopg2')


## Followings are the resutls for the three tasks mentioned above


#### Result of 1 

Top Articles (number of views)

candidate-is-jerk        (338647)
bears-love-berries       (253801)
bad-things-gone  (170098)
goats-eat-googles        (84906)
trouble-for-troubled     (84810)
balloon-goons-doomed     (84557)
so-many-bears    (84504)
media-obsessed-with-bears        (84383)


#### Result of 2 

Top Authors (number of views) 

Ursula La Multa  (507594)
Rudolf von Treppenwitz   (423457)
Anonymous Contributor    (170098)
Markoff Chaney   (84557)


##### Result of 3 

Days with error rate >1%:

2016-07-17 error rate:0.022626862468
