# /usr/bin/env python
# -*- coding:utf-8 -*-

import os
from log import logger,log_dumps
import trade_config

_ABS_CMD_ = 'D:/dev_tool/Apache24/bin/abs'

def buy(coin_name, price_number_config, buy_n, buy_c, buy_account):
    test_config=trade_config.test_config[coin_name]
    buy_cookie = trade_config.cookie[buy_account]
    cur_path = os.path.abspath('.')
    buy_post_file = os.path.join(cur_path, '%s_one_user_same_price_same_number_buy.data' % coin_name)
    #print(buy_post_file)
    
    with open(buy_post_file, 'w') as bf:
        content = 'marketId=%s&vcoinId=%s&tradeType=1&tradePrice=%s&tradeNumber=%s' %(test_config['marketId'], test_config['vcoinId'], test_config[price_number_config]['buy_price'], test_config[price_number_config]['buy_number'])
        bf.write(content)

    #买入
    buy_cmd = '%s -n %s -c %s -H "%s" -p %s -T application/x-www-form-urlencoded "https://www.mexc.io/member/trans/entrustTrade"' % (_ABS_CMD_, buy_n, buy_c, buy_cookie, buy_post_file)
    buy_result = os.popen(buy_cmd)
    #print(buy_result.read())

    log_content = os.linesep
    log_content += '#################################################' + os.linesep
    log_content += 'buy' + os.linesep
    log_content += coin_name + os.linesep
    log_content += log_dumps(test_config[price_number_config]) + os.linesep
    log_content += buy_result.read() + os.linesep
    log_content += '#################################################' + os.linesep
    logger().debug(log_content)

def sell(coin_name, price_number_config, sell_n, sell_c, sell_account):
    test_config=trade_config.test_config[coin_name]
    sell_cookie = trade_config.cookie[sell_account]
    cur_path = os.path.abspath('.')
    sell_post_file = os.path.join(cur_path, '%s_one_user_same_price_same_number_sell.data' % coin_name)
    #print(buy_post_file)
    #print(sell_post_file)
    
    test_config=trade_config.test_config[coin_name]
    with open(sell_post_file, 'w') as sf:
        content = 'marketId=%s&vcoinId=%s&tradeType=1&tradePrice=%s&tradeNumber=%s' %(test_config['marketId'], test_config['vcoinId'], test_config[price_number_config]['sell_price'], test_config[price_number_config]['sell_number'])
        sf.write(content)

    #卖出
    sell_cmd = '%s -n %s -c %s -H "%s" -p %s -T application/x-www-form-urlencoded "https://www.mexc.io/member/trans/entrustTrade"' % (_ABS_CMD_, sell_n, sell_c, sell_cookie, sell_post_file)
    sell_result = os.popen(sell_cmd)
    #print(sell_result.read())

    log_content = os.linesep
    log_content += '#################################################' + os.linesep
    log_content += 'sell' + os.linesep
    log_content += coin_name + os.linesep
    log_content += log_dumps(test_config[price_number_config]) + os.linesep
    log_content += sell_result.read() + os.linesep
    log_content += '#################################################' + os.linesep
    logger().debug(log_content)