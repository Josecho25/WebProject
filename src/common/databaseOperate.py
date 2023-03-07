import pymysql

from src.common.readData import Data


class DatabaseOperate:
    def sql_statement_execute(self, sqlStatement):
        # 1) 先获取到oa的mysql数据库的连接信息
        dbDict = Data().read_config_data('db.csv')
        # 2) 使用pymysql去连接mysql数据库；获取数据库的连接对象
        dbObject = pymysql.connect(host=dbDict['host'], user=dbDict['user'], password=dbDict['passwd'],
                        database=dbDict['database'], port=int(dbDict['port']), charset='utf8')
        # 3) 获取数据库的游标
        dbCursor = dbObject.cursor()
        # 4) 在数据库的游标中来执行sql语句（可以是select，可以是update，可以是insert，可以是delete等等）
        dbCursor.execute(sqlStatement)
        # 5) 如果是DML语句，那么必须要提交数据库的事务。
        dbObject.commit()
        # 6) 如果是DQL语句；那么就必须要从游标中获取查询结果；
        data = dbCursor.fetchall()
        # 7) 关闭数据库游标
        dbCursor.close()
        # 8) 关闭数据库连接
        dbObject.close()
        # 9) 返回获取到的查询结果
        return data
