import configparser
appConfig = configparser.ConfigParser()
appConfig.read("app.ini")
DBMS = appConfig.get("CoreContext", "dbms")
USER = appConfig.get("CoreContext", "user")
PWD = appConfig.get("CoreContext", "password")
HOST = appConfig.get("CoreContext", "host")
DB = appConfig.get("CoreContext", "database")

db_connect = DBMS + USER + PWD + HOST + DB

import sys # print to stdout for some testing

"""
HIDE CONNECTION DETAILS

https://gist.github.com/derzorngottes/3b57edc1f996dddcab25
https://stackoverflow.com/questions/26127655/can-i-use-a-config-file-to-hold-connection-string-parameters

print(">>>>> TESTING CONFIG FILE <<<<<")
print(db_connect)
print(">>>>> connection string <<<<<")

"""
