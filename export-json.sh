# !/bin/bash


# run below command at your server which host mongodb 
mongoexport --host="127.0.0.1:27017" --collection=weibo --db=weibo --out weibo1.json --jsonArray --authenticationDatabase admin -u admin -p password --forceTableScan