# /usr/bin/env python
# -*- coding:utf-8 -*-

'''
对于每种币
案例1：同一个账户，买卖，价格一样，数量一样
案例2：同一个账户，买卖，价格一样，数量不一样
案例3：多个账号，一个账号买，另一个账号卖，价格一样，数量一样
案例4：多个账号，一个账号买，另一个账号卖，价格一样，数量不一样
'''

from multiprocessing import Process
import os
from log import logger,log_dumps
import trade_config
import buy_sell

def batch_buy_process(name, price_number_config, coin_name, account):
    # logger().debug('Run batch_buy_process %s (%s)...' % (name, os.getpid()))
    test_config=trade_config.test_config[coin_name]
    buy_n = test_config[price_number_config]['batch_buy_abs_n']
    buy_c = test_config[price_number_config]['batch_buy_abs_c']
    buy_sell.buy(coin_name, price_number_config, buy_n, buy_c, account)

def batch_sell_process(name, price_number_config, coin_name, account):
    # logger().debug('Run batch_sell_process %s (%s)...' % (name, os.getpid()))
    test_config=trade_config.test_config[coin_name]
    sell_n = test_config[price_number_config]['batch_sell_abs_n']
    sell_c = test_config[price_number_config]['batch_sell_abs_c']
    buy_sell.sell(coin_name, price_number_config, sell_n, sell_c, account)

# 批量
def batch(price_number_config, coin_name):
    buy_processes = []
    sell_processes = []

    test_config=trade_config.test_config[coin_name]
    for account in test_config[price_number_config]['buy_account']:
        buy_process = Process(target=batch_buy_process, args=('batch_buy_process_%s' % account, price_number_config, coin_name, account))
        buy_processes.append(buy_process)

    for account in test_config[price_number_config]['sell_account']:
       sell_process = Process(target=batch_sell_process, args=('batch_sell_process_%s' % account, price_number_config, coin_name, account))
       sell_processes.append(sell_process)

    for p in buy_processes:
        p.start()
    for p in sell_processes:
        p.start()

    for p in buy_processes:
        p.join()

    for p in sell_processes:
        p.join()

# 单笔
def one(price_number_config, coin_name):
    test_config=trade_config.test_config[coin_name]
    buy_n = test_config[price_number_config]['one_buy_abs_n']
    buy_c = test_config[price_number_config]['one_buy_abs_c']
    for account in test_config[price_number_config]['buy_account']:
        buy_sell.buy(coin_name, price_number_config, buy_n, buy_c, account)

    sell_n = test_config[price_number_config]['one_sell_abs_n']
    sell_c = test_config[price_number_config]['one_sell_abs_c']
    for account in test_config[price_number_config]['sell_account']:
        buy_sell.sell(coin_name, price_number_config, sell_n, sell_c, account)

def test():
    #价格相同，数量相同
    #价格相同，数量不同
    for coin_name in trade_config.test_coin_name:
        for price_number in trade_config.test_config[coin_name]['price_number']:
            one(price_number, coin_name)
            batch(price_number, coin_name)
    print('test finish')

if __name__=='__main__':
    test()