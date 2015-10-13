mysql -u root -p 
use base;
FLUSH TABLE WHIT READ LOCK;
SHOW MASTER STATUS;
quit

mysqldump -u root -p base>/a/donde/mandarlo/archivo.sql

mysql -u root -p 
UNLOCK TABLE;

ESCLAVO=

mysql 
create database base;
mysql -u root -p base < base.sql 

my.cnf 
[mysql]
server -id=4
master -host=ip del master
master - user=usuario_esclavo
master - password = secret
master - connect - retry=60
replicate-do-db=conexion
