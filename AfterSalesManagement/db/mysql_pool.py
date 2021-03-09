import mysql.connector.pooling
import json


with open("./static/config/config.json", "r", encoding="utf-8") as f:
    __config = json.load(f)


# __config={
#     "host":"localhost",
#     "port":3306,
#     "user":"root",
#     "password":"",
#     "database":"trillion"
# }

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="my_pool",
        **__config, # 数据库连接参数
        pool_size=10  # 最大允许连接数
    )
except Exception as e:
    pool = None