# /usr/bin/env python
# -*- coding:utf-8 -*-

#账号Cookie
cookie = {
    '1060887552@qq.com':'Cookie: account=1*********%40qq.com; _ga=GA1.2.434193837.1520823086; JSESSIONID=571BC28468DC60B837DCACA7137A0105; _gid=GA1.2.261475438.1521256117; btcValue=0.00000000; usdValue=0.0000000000; u_id=5196d0a24eabe5c8426b6f9db3e07569'
}

#测试币种列表
test_coin_name = ('TRX_BTC',)

#测试参数配置
test_config = {
    'TRX_BTC' : {
        #BTC
        'marketId':'a3551348feb411e7a6d000163e0205ba',
        #TRX
        'vcoinId':'0a4c27167b6e4275975e2b63307bd39b',

        'price_number':('one_same_price_same_number',),

        #单账号，价格相同，数量相同
        'one_same_price_same_number':{
            'desc':'单账号，价格相同，数量相同',
            #abs配置
            'one_buy_abs_n':'1',
            'one_buy_abs_c':'1',
            'one_sell_abs_n':'1',
            'one_sell_abs_c':'1',
            'batch_buy_abs_n':'1000',
            'batch_buy_abs_c':'100',
            'batch_sell_abs_n':'1000',
            'batch_sell_abs_c':'100',
            #交易参数
            'buy_account':('1060887552@qq.com',),
            'sell_account':('1060887552@qq.com',),
            'buy_price':'0.00600001',
            'sell_price':'0.00600001',
            'buy_number':'0.02',
            'sell_number':'0.02'
        },

        #单账号，价格相同，数量不同
        'one_same_price_diff_number':{
            'desc':'单账号，价格相同，数量不同',
            #abs配置
            'one_buy_abs_n':'1',
            'one_buy_abs_c':'1',
            'one_sell_abs_n':'1',
            'one_sell_abs_c':'1',
            'batch_buy_abs_n':'10',
            'batch_buy_abs_c':'1',
            'batch_sell_abs_n':'10',
            'batch_sell_abs_c':'1',
            #交易参数
            'buy_account':('1060887552@qq.com',),
            'sell_account':('1060887552@qq.com',),
            'buy_price':'0.00600001',
            'sell_price':'0.00600001',
            'buy_number':'0.02',
            'sell_number':'0.01'
        },

        #多账号，价格相同，数量相同
        'many_same_price_diff_number':{
            'desc':'多账号，价格相同，数量相同',
            #abs配置
            'one_buy_abs_n':'1',
            'one_buy_abs_c':'1',
            'one_sell_abs_n':'1',
            'one_sell_abs_c':'1',
            'batch_buy_abs_n':'10',
            'batch_buy_abs_c':'1',
            'batch_sell_abs_n':'10',
            'batch_sell_abs_c':'1',
            #交易参数
            'buy_account':('1060887552@qq.com',),
            'sell_account':('1060887552@qq.com',),
            'buy_price':'0.00600001',
            'sell_price':'0.00600001',
            'buy_number':'0.02',
            'sell_number':'0.01'
        },

        #多账号，价格相同，数量不同
        'many_same_price_diff_number':{
            'desc':'多账号，价格相同，数量不同',
            #abs配置
            'one_buy_abs_n':'1',
            'one_buy_abs_c':'1',
            'one_sell_abs_n':'1',
            'one_sell_abs_c':'1',
            'batch_buy_abs_n':'10',
            'batch_buy_abs_c':'1',
            'batch_sell_abs_n':'10',
            'batch_sell_abs_c':'1', 
            #交易参数
            'buy_account':('1060887552@qq.com',),
            'sell_account':('1060887552@qq.com',),
            'buy_price':'0.00600001',
            'sell_price':'0.00600001',
            'buy_number':'0.02',
            'sell_number':'0.01'
        }

    }
}