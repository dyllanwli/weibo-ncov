#!/bin/sh


# do not run this script
exit 0;

# install mysql by docker compose

# load modify configuration file from /Docker/mysqld.cnf to your compose

# grant the access for weibospider database
docker exec mysql bash
mysql -u root -p
grant all on *.* to weibospider@'%' identified by '123456';
# refresh the mysql and restart it 
flush privileges;
# restart in container
/etc/init.d/mysql restart
