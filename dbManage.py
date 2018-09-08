import pymysql
import config

class dbManage(object):

    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn=pymysql.connect(host=config.db_host,user=config.db_user,passwd=config.db_passwd,db=config.db_name,port=3306,charset='utf8')
        self.cur=self.conn.cursor()


    def insertfoods(self, foodname = ''):
        if foodname == '':
            return
        value = "insert into foods( foodname)  value(\"%s\") on duplicate key update foodname =values(foodname)" %foodname

        self.cur.execute(value)
        self.conn.commit()

    def insertmenu(self, menu, week, group=None):
        if group == None:
            group = -1
        value = "insert into menus(menu, `group`, `week`) value(\"%s\", %s)" %(menu, group, week)
        self.cur.execute(value)
        self.conn.commit()
      
    def insertfoodnum(self, food, week, group=None):
        if group == None:
            group = -1
        for foodname, foodnum in food.items():               
            value = "insert into foodnum(foodname, foodnum, `group`, `week`) value(\"%s\", %s, %s, %s)" %(foodname, foodnum, group, week)
            print(value)
            self.cur.execute(value)
            self.conn.commit()

    def insertfoodnumSingle_by_many(self, food, ename, menuid, week):
        for foodname, foodnum in food.items():
            value = "insert into foodnumSingle(foodname, foodnum, ename, menuid, `week`) value(\"%s\", %s, \"%s\", %s, %s)" %(foodname, foodnum, ename, menuid, week)
            print(value)
            self.cur.execute(value)
            self.conn.commit()

    def selectfoods(self, foodname):
        value = "select * from foods where foodname = \"%s \"" % foodname
        self.cur.execute(value)
        results = self.cur.fetchone()
        return results

    def selectfoodnum(self, foodnames, week, group=None):
        if group == None:
            group = -1

        result = dict()
        for foodname in foodnames:
            value = "select foodname, foodnum from foodnum where foodname=\"%s\" and `group`=%s and `week` = %s" %(foodname, group, week)
            self.cur.execute(value)
            r = self.cur.fetchone()
            if r:
                result[r[0]] = r[1]
        return result

    def selectfoodnumSingle(self, ename, menuid):
        value = "select foodname, foodnum, `week`, where ename=\"%s\" and menuid=%s" % (foodname, ename, menuid)
        self.cur.execute(value)
        r = self.cur.fetchall()
        return r
    
    def selectmenusBynew(self, week,  group=None):
        if group == None:
            group = -1
        value = "select menu from menus where `group` = %s and `week` = %s order by id desc limit 1" % (group, week)
        self.cur.execute(value)
        r = self.cur.fetchone()
        return r

    def close(self):
        self.cur.close()
        self.conn.close()


if __name__=="__main__":
    db = dbManage()
    db.connect()
    #db.insertfoods("ceshi")
    result = db.selectmenusBynew()
    print(result)
    # food = dict()
    # food["1"] = 2
    # food["22"] = 3
    # db.insertfoodnumSingel_by_many(food, "jim", 2)
    # result = db.selectfoods("ceshi")
    # print(result)
    # print(result[0])
    db.close()
