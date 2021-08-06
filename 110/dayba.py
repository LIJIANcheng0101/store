'''
    中国工商银行账户管理系统：
        ICBC:
'''
import time
import random
import pymysql
import itertools
con = pymysql.connect(host="localhost", user="root", password="", database="icbc")
cursor = con.cursor()
# 1.准备一个数据库 和 银行名称
bank = {}  # 空的数据库
'''
    中国工商银行账户管理系统：
        ICBC:
'''
import pymysql
import itertools
import time
import random

con = pymysql.connect(host="localhost", user="root", password="", database="icbc")
cursor = con.cursor()
# 1.准备一个数据库 和 银行名称

'''
    {
        "张三":{
            account:s001,
            country:"中国"
        }，
        "李四":{
        }
    }
'''
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的


# 2.入口程序
def welcome():
    print("*************************************")
    print("*      中国工商银行昌平支行           *")
    print("*************************************")
    print("*  1.开户                            *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money, regiaterDate):
    # 1.判断数据库是否已满
    sql = "select count(*) from person"
    cursor.execute(sql)
    data = cursor.fetchone()
    if data[0] >= 100:
        return 3
    # 3.正常开户
    sql1 = "insert into person values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = [account, username, password, country, province, street, gate, money, regiaterDate, bank_name]
    cursor.execute(sql1, param)
    return 1

def bank_drawmoney(account,password,dmoney):
    sql = "select * from person where account = %s"
    param = [account]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if not data:
        return 1
    sql = "select * from person where account = %s and password = %s"
    param = [account, password]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if not data:
        return 2
    sql = "select money from person where account = %s"
    param = [account]
    cursor.execute(sql, param)
    data = cursor.fetchone()
    if dmoney > data[0]:
        return 3
    return 4

def drawmoney():
    account = int(input("请输入您的账号:"))
    password = input("请输入您的账号密码:")
    dmoney = int(input("请输入您要取的金额:"))

    status1 = bank_drawmoney(account,password,dmoney)

    if status1 == 1:
        print("对不起，您输入的账号不存在！")
    elif status1 == 2:
        print("对不起，您输入的密码或账号错误！")
    elif status1 == 3:
        print("穷鬼！你账户没那么多钱！")
    elif status1 == 4:
        sql = "update person set money = money - %s where account = %s"
        param = [dmoney, account]
        cursor.execute(sql,param)
        sql = "select money from person where account = %s"
        param = [account]
        cursor.execute(sql, param)
        data = cursor.fetchone()
        print("取钱成功，请拿好您的小票", )
        info = '''
        ---------取款信息---------
        账号：%s
        取款金额:%s
        账户余额：$s
        '''
        print(info % (account, dmoney, data[0]))




def bank_savemoney(accout):
    sql = "select * from person where account = %s"
    param = [accout]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if not data:
        return 1
    return 2

def savemoney():
    account = int(input("请输入您的账号:"))
    smoney = int(input("请输入您要存入的金额："))

    status3 = bank_savemoney(account)
    if status3 == 1:
        print("对不起，您输入的账户不存在!")
    elif status3 == 2:
        sql = "update bank set money = money + %s where account = %s"
        param = [smoney, account]
        cursor.execute(sql, param)
        sql = "select money from person where account= %s "
        param = [account]
        cursor.execute(sql, param)
        data = cursor.fetchone()
        print("存钱成功！该账户现余额为:", data[0])




# 用户的开户的操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    password = input("请输入您的开户密码：")
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = int(input("请输入您的开户初始余额："))  # 将输入金额转换成int类型
    regiaterData = time.strftime('%y-%m-%d', time.localtime(time.time()))
    # 随机产生8为数字
    account = random.randint(10000000, 99999999)

    status = bank_addUser(account, username, password, country, province, street, gate, money, regiaterData)

    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")

    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
            ----------个人信息------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            余额：%s
            开户行地址：%s
            ------------------------
        '''
        print(info % (username, password, account, country, province, street, gate, money, bank_name))

def bank_queryaccount(account,password):
    sql = "select * from person where account = %s"
    param = [account]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if not data:
        return 1
    sql = "select * from person where account = %s and password = %s"
    param = [account, password]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if not data:
        return 2
    return 0

def queryaccount():
    account = int(input("请输入您的账号:"))
    password = input("请输入您的账号密码:")
    status2 = bank_queryaccount(account,password)
    if status2 == 1:
        print("对不起，您输入的账号不存在！")
    elif status2 == 2:
        print("对不起，您输入的密码或账号错误！")
    elif status2 == 0:
        sql = "select * from person where account = %s"
        param = [account]
        cursor.execute(sql, param)
        data1 = cursor.fetchall()
        data = list(data1)
        print("查询成功！以下是您的个人账户信息：")
        info1 = '''
                    ----------账户信息------
                    当前账号：%s
                    密码：%s
                    余额：%s
                    地址信息:
                        国家：%s
                        省份：%s
                        街道：%s
                        门牌号: %s
                    开户行地址：%s
                    ------------------------
                '''
        print(info1 % (data[0][1], data[0][0], data[0][3], data[0][4], data[0][5], data[0][6], data[0][7], data[0][9]))

def bank_zhuanmoney(account1,account2,password,zmoney):
    sql = "select * from person where account = %s"
    param = [account1]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if not data:
        return 1
    sql = "select * from person where account = %s"
    param = [account2]
    cursor.execute(sql, param)
    data1 = cursor.fetchall()
    if not data1:
        return 1
    if account1 == account2:
        return 4
    sql = "select * from person where account = %s and password = %s"
    param = [account1,password]
    cursor.execute(sql, param)
    data = cursor.fetchall()
    if not data:
        return 2
    sql = "select money from person where account = %s"
    param = [account1]
    cursor.execute(sql, param)
    data = cursor.fetchone()
    if zmoney > data[0]:
        return 3
    return 0

def zhuanmoney():
    account1 = int(input("请输入您的账号:"))
    account2 = int(input("请输入要转入的账号:"))
    password = input("请输入账号密码:")
    zmoney = int(input("请输入您要转的金额："))
    status4 = bank_zhuanmoney(account1,account2,password,zmoney)
    if status4 == 4:
        print("对不起，转账失败")
    elif status4 == 3:
        print("对不起，转账失败！")
    elif status4 == 2:
        print("密码有误")
    elif status4 == 1:
        print("没有此账号")
    elif status4 == 0:
        sql = "update person set money = money - %s where account = %s"
        param = [zmoney, account1]
        cursor.execute(sql, param)
        sql = "update person set money = money + %s where account = %s"
        param = [zmoney, account2]
        cursor.execute(sql, param)

        sql = "select money from person where account = %s"
        param = [account1]
        cursor.execute(sql, param)
        data = cursor.fetchone()
        print("转账成功！以下是您的转账信息：")
        info1 = '''
                            ----------个人信息------
                            转出账号：%s
                            转入账号：%s
                            转出金额：%s
                            您的账号余额：%s
                            ------------------------
                        '''
        print(info1 % (account1, account2, zmoney, data[0]))


        bank[account1]["money"] = bank[account1]["money"] - zmoney
        bank[account2]["money"] = bank[account2]["money"] + zmoney
        print("转账成功！当前账户余额为：",bank[account1]["money"])
        print("转入的账号",account2,"的余额为：",bank[account2]["money"])

while True:
    # 打印欢迎程序
    welcome()
    chose = input("请输入您的业务：")
    if chose == "1":
        addUser()
        con.commit()
    elif chose == "2":
        savemoney()
        con.commit()
    elif chose == "3":
        drawmoney()
        con.commit()
    elif chose == "4":
        zhuanmoney()
        con.commit()
    elif chose == "5":
        queryaccount()
        con.commit()
    elif chose == "6":
        print("欢迎下次光临！")
        cursor.close()
        con.close()
        break
    else:
        print("输入错误！请重新输入！")

