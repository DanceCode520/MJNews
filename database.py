#!/usr/bin/python3

import pymysql
from Model.models import News
import json

# 打开数据库连接
db = pymysql.connect(host="127.0.0.1", user="root", password="your passwords", database="your database")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


# 根据表名(tableName)获取表中全部数据
def selectAllData(tableName):
    # SQL 查询语句
    sql = "select * FROM %s" % tableName
    jsonStr = ""
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        jsonArr = []
        for item in results:
            # 将元组的内容放入字典里
            dic = {}
            dic["id"] = item[0]
            dic["title"] = item[1]
            dic["content"] = item[2]
            dic["writer"] = item[3]
            dic["date"] = item[4]
            dic["type"] = getNewsType(item[5])
            dic["picurl"] = item[6]
            jsonArr.append(dic)
        print(jsonArr)
        # jsonStr=json.dumps(jsonArr,ensure_ascii=False)  #将jsonArr数组转化为json
    except:
        print("Error: select data wrong")

    # 关闭数据库连接
    # db.close()
    return jsonArr


# 插入新闻信息
def insertData(title, content, wirter, time, ntype, fileName):
    # 打开数据库连接
    # db = pymysql.connect("127.0.0.1", "root", "michael88", "myNewsDB")
    # # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    sql = "INSERT INTO news(n_title,n_content,n_writer,n_time,n_fk_code,n_picture) VALUES " \
          "('%s','%s','%s','%s','%s','%s')" % \
          (title, content, wirter, time, ntype, fileName)
    isSuccess = False
    try:
        cursor.execute(sql)
        db.commit()
        isSuccess = True
    except:
        print("can not insert data")
        db.rollback()
    # db.close()
    return isSuccess


# 获取新闻信息
def getDataById(id):
    # 打开数据库连接
    # db = pymysql.connect("127.0.0.1", "root", "michael520", "mjnews")
    # # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    # SQL 查询语句

    sql = "select * FROM news WHERE n_id=%s" % id
    news = News()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print(results)
        news.id = results[0][0]
        news.title = results[0][1]
        news.content = results[0][2]
        news.writer = results[0][3]
        news.time = results[0][4]
        news.ntype = results[0][5]
        news.picture = results[0][6]
        # jsonStr = json.dumps(dic, ensure_ascii=False)
    except:
        print("Error: select data wrong")

    # 关闭数据库连接
    # db.close()
    return news


# 获取新闻类别
def getNewsType(type):
    # 打开数据库连接
    # db = pymysql.connect("127.0.0.1", "root", "michael520", "mjnews")
    # # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    # SQL 查询语句
    sql = "select t_content FROM newstype WHERE t_code=%s" % type
    typeStr = ""
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        typeStr = results[0][0]
        print('newstype==', typeStr)
    except:
        print("Error: select data wrong")
    return typeStr


# 修改新闻信息
def changeNewsData(news):
    # 打开数据库连接
    # db = pymysql.connect("127.0.0.1", "root", "michael88", "myNewsDB")
    # # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    sql = "UPDATE news set n_title='%s',n_content='%s',n_writer='%s',n_time='%s',n_fk_code='%s'," \
          "n_picture='%s' where n_id='%s'" % (news.title, news.content, news.writer, news.time, news.ntype, news.picture, id)
    ischanged = False
    try:
        cursor.execute(sql)
        db.commit()
        ischanged = True
    except:
        print("can not change data")
        db.rollback()
    # db.close()
    return ischanged


# 删除新闻信息
def deleteNews(id):
    # 打开数据库连接
    # db = pymysql.connect("127.0.0.1", "root", "michael520", "mjnews")
    # # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    sql = "delete from news where n_id='%s'" % id
    sucess = "0"
    try:
        cursor.execute(sql)
        db.commit()
        sucess = "1"
    except:
        print("can not delete data")
        db.rollback()
    # db.close()
    return sucess


# 根据新闻类别查找该类所有新闻
def getAllnewsByType(typeCode):
    sql = "SELECT news.*,newstype.t_content FROM news " \
          "JOIN newstype " \
          "WHERE newstype.t_code=news.n_fk_code AND news.n_fk_code=%s" % typeCode
    jsonArr = []
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for item in results:
            # 将对象放入字典里
            news = News()
            news.id = item[0]
            news.title = item[1]
            news.content = item[2]
            news.writer = item[3]
            news.time = item[4]
            news.ntype = item[7]
            news.picture = item[6]
            jsonArr.append(news)
            print('typenews==', results)
    except:
        print("Error: select data wrong")
    return jsonArr


# 检查用户是否存在
def checkUser(name, pwd):
    # 打开数据库连接
    # db = pymysql.connect("127.0.0.1", "root", "michael520", "mjnews")
    # # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    # SQL 查询语句
    sql = "select * FROM user WHERE u_name='%s' and u_pwd='%s'" % (name, pwd)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        if len(results) != 0:
            return results
        else:
            return False
    except:
        print("Error: select data wrong")
    # 关闭数据库连接
    # db.close()
