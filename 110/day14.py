from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from dayba import bank_addUser
from dayba import bank_savemoney
from dayba import bank_drawmoney
from dayba import bank_zhuanmoney
from dayba import bank_queryaccount

add = [
    ["12345678", "旺财", 123456, "中国", "北京", "回龙观", "S001", "200", "2021-08-06"]
]
sav = [
    ["12345678"]
]
dra = [
    ["87654321",123456,"100"]
]
zhuan = [
    ["87654321","12345678",123456,"400"]
]
que = [
    ["12345678",123456]
]

@ddt  # 注解，注释这个类是参数化类
class TestCalc(TestCase):
    # 测试开户
    @data(*add)  # 引入数据源
    @unpack
    def testAdd(self, account, username, password, country, province, street, gate, money, regiaterDate):
        # 2.调用被测方法
        test_addUser = bank_addUser().bank_addUser(account, username, password, country, province, street, gate, money,
                                                   regiaterDate)

        # 3.断言
        self.assertEqual(test_addUser, 1)


 # 测试存钱
@data(*sav)  # 引入数据源
@unpack
def testsav(self, account):
    # 2.调用被测方法
    test_sav = bank_savemoney().bank.savemoeny(account)

    # 3.断言
    self.assertEqual(test_sav, 0)

# 测试取钱
@data(*dra)  # 引入数据源
@unpack
def testdra(self, account, password, cash):
    # 2.调用被测方法
    test_dra = bank_drawmoney().bank_drawmoney(account, password, cash)

    # 3.断言
    self.assertEqual(test_dra, 0)

# 测试转账
@data(*zhuan)  # 引入数据源
@unpack
def testzhuan(self, cardNum, collection, in_password, amount):
    # 2.调用被测方法
    test_zhuan = bank_zhuanmoney().bank_zhuanmoney(cardNum, collection, in_password, amount)

     # 3.断言
    self.assertEqual(test_zhuan, 0)

#测试查询
@data(*que)  # 引入数据源
@unpack
def testque(self, account, password):
    # 2.调用被测方法
     test_que = bank_queryaccount().bank_queryaccount(account, password)

     # 3.断言
     self.assertEqual(test_que, 0)

